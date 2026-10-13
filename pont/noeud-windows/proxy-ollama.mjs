#!/usr/bin/env node
// ⭐ 2026-10-12 — PROXY DU NŒUD DE CALCUL : le Moteur IA du serveur appelle Ollama sur ce PC, PAR LE VPN SEULEMENT.
// Avis CYBERSECU du 2026-10-12 (VALIDÉ AVEC RÉSERVES, conditions O1 à O8) — CYBERSECU\MEMOIRE.md §9.
//
//   O1  écoute sur l'adresse VPN (10.8.0.3:11435) et RIEN d'autre — adresse absente : arrêt, jamais de repli ; cible FIXE 127.0.0.1:11434 ;
//       méthode + chemin EXACTS (POST /api/chat, POST /api/embed, GET /api/tags ; `?`, encodage, `..` → 404) ; `model` lu dans un JSON valide
//       et limité aux 2 modèles autorisés (403) ; corps compté sur les octets LUS (413) ; en-têtes vers Ollama RECONSTRUITS (Content-Type seul) ;
//       `Origin` → 403, aucun en-tête CORS ; IP source vérifiée ici AUSSI ; 2 requêtes simultanées au plus (503) ; délais bornés.
//   O2  jeton OLLAMA_CLE (32 octets) dans %USERPROFILE%\.pleiade\ollama-cle.txt (droits du seul compte), comparé à temps constant sur les
//       empreintes SHA-256 ; absent ou faux → 401 sans détail ; échecs répétés → blocage temporaire. Le jeton n'est JAMAIS affiché.
//   O5  journal sans corps, sans réponse, sans jeton : horodatage, IP, méthode, chemin, statut, durée.
//
// Lancement : node proxy-ollama.mjs [--sources=10.8.0.1] [--ecoute=10.8.0.3] [--port=11435]
//   --sources : IP autorisées (séparées par des virgules). À FIXER d'après le journal (« refusé : source ») après un premier appel du conteneur.
//   --essai   : autorise --ecoute=127.0.0.1 pour les essais locaux (jamais en service).
import http from "node:http";
import crypto from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { execFileSync } from "node:child_process";

const arg = (k, d) => { const a = process.argv.find((x) => x.startsWith(`--${k}=`)); return a ? a.slice(k.length + 3) : d; };
const ESSAI = process.argv.includes("--essai");
const ECOUTE = arg("ecoute", "10.8.0.3");
const PORT = Number(arg("port", "11435"));
const SOURCES = new Set(arg("sources", "10.8.0.1").split(",").map((s) => s.trim()).filter(Boolean));
const CIBLE = { host: "127.0.0.1", port: 11434 };   // FIXE
const ROUTES = new Set(["POST /api/chat", "POST /api/embed", "GET /api/tags"]);
const MODELES = new Set(["gemma4:26b-a4b-it-qat", "bge-m3:latest", "bge-m3"]);
const MAX_CORPS = 1024 * 1024;          // 1 Mo (invite la plus longue mesurée : ~60 Ko ; lot de 32 vecteurs : ~70 Ko)
const MAX_SIMULTANEES = 2;
const DELAI_GENERATION_MS = 180_000;
const DOSSIER = path.join(os.homedir(), ".pleiade");
const FICHIER_CLE = ESSAI && arg("cle", "") ? arg("cle", "") : path.join(DOSSIER, "ollama-cle.txt");   // --cle : essais seulement (jeton jetable)
const JOURNAL = ESSAI && arg("cle", "") ? path.join(path.dirname(FICHIER_CLE), "proxy-essai.log") : path.join(DOSSIER, "noeud-ia", "proxy.log");

// ⭐ 2026-10-13 (grappe de nœuds) : tout PC du parc écoute sur SA propre adresse VPN — une adresse 10.8.0.2 à 10.8.0.254, écrite en chiffres
// (10.8.0.1 est le serveur) ; 127.0.0.1 seulement en essai. Toute autre adresse : arrêt (O1 inchangé : jamais d'écoute hors VPN).
const m = /^10\.8\.0\.(\d{1,3})$/.exec(ECOUTE);
if (!(m && Number(m[1]) >= 2 && Number(m[1]) <= 254) && !(ESSAI && ECOUTE === "127.0.0.1")) { console.error(`Adresse d'écoute refusée (${ECOUTE}) : une adresse du VPN de l'exercice, 10.8.0.2 à 10.8.0.254 (127.0.0.1 avec --essai).`); process.exit(2); }
if (![...SOURCES].every((s) => /^\d{1,3}(\.\d{1,3}){3}$/.test(s))) { console.error("--sources : adresses IPv4 seulement."); process.exit(2); }

// ── O2 : jeton ──
fs.mkdirSync(path.dirname(JOURNAL), { recursive: true });
if (!fs.existsSync(FICHIER_CLE)) {
  fs.writeFileSync(FICHIER_CLE, crypto.randomBytes(32).toString("base64url") + "\n", { flag: "wx" });
  try { execFileSync("icacls", [FICHIER_CLE, "/inheritance:r", "/grant:r", `${os.userInfo().username}:F`], { stdio: "ignore" }); }
  catch { console.error("⚠ Droits du fichier du jeton non restreints (icacls) : à corriger à la main."); }
  console.log(`Jeton créé : ${FICHIER_CLE} (ouvrez ce fichier vous-même pour le recopier dans l'instance « Moteur IA », champ OLLAMA_CLE).`);
}
const EMPREINTE = crypto.createHash("sha256").update(fs.readFileSync(FICHIER_CLE, "utf8").trim()).digest();
const jetonValide = (h) => {
  const m = /^Bearer ([A-Za-z0-9_-]{20,200})$/.exec(String(h || ""));
  const e = crypto.createHash("sha256").update(m ? m[1] : "").digest();
  return crypto.timingSafeEqual(e, EMPREINTE) && !!m;
};

// ── O5 : journal ──
const journal = (ip, methode, chemin, statut, ms, note = "") => {
  const l = `${new Date().toISOString()} ${ip} ${methode} ${String(chemin).slice(0, 80).replace(/[^\x20-\x7e]/g, "?")} ${statut} ${ms}ms${note ? ` ${note}` : ""}\n`;
  try { fs.appendFileSync(JOURNAL, l); } catch { /* disque plein : on sert quand même */ }
  if (statut >= 400) process.stdout.write(l);
};

// Échecs de jeton : 10 en 5 min → 15 min de blocage pour cette IP.
const echecs = new Map();
const bloque = (ip) => { const e = echecs.get(ip); return !!e && e.jusqu > Date.now(); };
const echec = (ip) => { const e = echecs.get(ip) || { n: 0, debut: Date.now(), jusqu: 0 }; if (Date.now() - e.debut > 300_000) { e.n = 0; e.debut = Date.now(); } e.n++; if (e.n >= 10) { e.jusqu = Date.now() + 900_000; e.n = 0; journal(ip, "-", "-", 429, 0, "bloqué 15 min après 10 jetons refusés"); } echecs.set(ip, e); };

let enCours = 0;
const repondre = (res, statut, corps = "") => { if (!res.headersSent) { res.writeHead(statut, { "Content-Type": "text/plain; charset=utf-8", "Cache-Control": "no-store" }); } res.end(corps); };

const serveur = http.createServer((req, res) => {
  const t0 = Date.now(), ip = (req.socket.remoteAddress || "").replace(/^::ffff:/, ""), cle = `${req.method} ${req.url}`;
  const fin = (statut, note) => { journal(ip, req.method, req.url, statut, Date.now() - t0, note); };
  if (!SOURCES.has(ip) && !(ESSAI && ip === "127.0.0.1")) { fin(403, "refusé : source"); req.destroy(); return; }
  if (bloque(ip)) { repondre(res, 429); fin(429, "bloqué"); return; }
  if (req.headers.origin !== undefined) { repondre(res, 403); fin(403, "Origin"); return; }
  if (!ROUTES.has(cle)) { repondre(res, 404); fin(404); return; }
  if (!jetonValide(req.headers.authorization)) { echec(ip); repondre(res, 401); fin(401); return; }
  if (enCours >= MAX_SIMULTANEES) { repondre(res, 503); fin(503, "occupé"); return; }
  enCours++;
  let libere = false; const liberer = () => { if (!libere) { libere = true; enCours--; } };
  res.on("close", liberer);

  const morceaux = []; let lus = 0, trop = false;
  req.on("data", (c) => { lus += c.length; if (lus > MAX_CORPS) { trop = true; req.pause(); repondre(res, 413); fin(413); req.destroy(); return; } morceaux.push(c); });
  req.on("end", () => {
    if (trop) return;
    const corps = Buffer.concat(morceaux);
    if (req.method === "POST") {
      let j; try { j = JSON.parse(corps.toString("utf8")); } catch { repondre(res, 400); fin(400, "JSON illisible"); return; }
      if (!j || typeof j !== "object" || !MODELES.has(j.model)) { repondre(res, 403); fin(403, "modèle refusé"); return; }
    }
    const amont = http.request({ ...CIBLE, method: req.method, path: req.url, headers: req.method === "POST" ? { "Content-Type": "application/json", "Content-Length": corps.length } : {}, timeout: DELAI_GENERATION_MS }, (r) => {
      res.writeHead(r.statusCode || 502, { "Content-Type": r.headers["content-type"] || "application/json", "Cache-Control": "no-store" });
      r.pipe(res);
      r.on("end", () => fin(r.statusCode || 502));
    });
    amont.on("timeout", () => { amont.destroy(new Error("délai")); });
    amont.on("error", (e) => { repondre(res, 502); fin(502, e.message === "délai" ? "délai Ollama" : "Ollama injoignable"); });
    if (req.method === "POST") amont.end(corps); else amont.end();
  });
  req.on("error", () => liberer());
});
serveur.headersTimeout = 10_000;
serveur.requestTimeout = DELAI_GENERATION_MS + 10_000;
serveur.keepAliveTimeout = 5_000;
serveur.on("error", (e) => { console.error(`Arrêt : impossible d'écouter sur ${ECOUTE}:${PORT} (${e.code || e.message}). VPN connecté ? Adresse ${ECOUTE} présente sur ce PC ?`); process.exit(1); });
serveur.listen(PORT, ECOUTE, () => console.log(`Proxy du nœud de calcul : ${ECOUTE}:${PORT} → Ollama 127.0.0.1:11434 · sources admises : ${[...SOURCES].join(", ")} · journal : ${JOURNAL}`));
