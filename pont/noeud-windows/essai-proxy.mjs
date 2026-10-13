// Essais de refus du proxy du nœud de calcul (avis CYBERSECU 2026-10-12, O8) — en LOCAL, jeton JETABLE, jamais le vrai.
// node essai-proxy.mjs <dossier-temporaire>
import { spawn } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const dir = process.argv[2]; fs.mkdirSync(dir, { recursive: true });
const cle = path.join(dir, "cle-essai.txt"); const jeton = crypto.randomBytes(32).toString("base64url"); fs.writeFileSync(cle, jeton);
const P = spawn(process.execPath, [path.join(import.meta.dirname, "proxy-ollama.mjs"), "--essai", "--ecoute=127.0.0.1", "--port=11499", `--cle=${cle}`], { stdio: ["ignore", "pipe", "pipe"] });
P.stderr.on("data", (d) => process.stderr.write(d));
await new Promise((r) => P.stdout.once("data", r));
const B = "http://127.0.0.1:11499", ok = { Authorization: `Bearer ${jeton}`, "Content-Type": "application/json" };
const cas = [
  ["sans jeton → 401", () => fetch(B + "/api/tags"), 401],
  ["mauvais jeton → 401", () => fetch(B + "/api/tags", { headers: { Authorization: "Bearer " + crypto.randomBytes(32).toString("base64url") } }), 401],
  ["/api/pull → 404", () => fetch(B + "/api/pull", { method: "POST", headers: ok, body: JSON.stringify({ model: "bge-m3" }) }), 404],
  ["/api/chat?x → 404", () => fetch(B + "/api/chat?x", { method: "POST", headers: ok, body: "{}" }), 404],
  ["chemin encodé → 404", () => fetch(B + "/api/%63hat", { method: "POST", headers: ok, body: "{}" }), 404],
  ["GET /api/chat → 404", () => fetch(B + "/api/chat", { headers: ok }), 404],
  ["autre modèle → 403", () => fetch(B + "/api/chat", { method: "POST", headers: ok, body: JSON.stringify({ model: "llama3.1:8b", messages: [] }) }), 403],
  ["JSON illisible → 400", () => fetch(B + "/api/embed", { method: "POST", headers: ok, body: "pas du json" }), 400],
  ["corps trop gros → 413", () => fetch(B + "/api/embed", { method: "POST", headers: ok, body: "x".repeat(1024 * 1024 + 10) }).catch(() => ({ status: 413 })), 413],
  ["en-tête Origin → 403", () => fetch(B + "/api/tags", { headers: { ...ok, Origin: "http://evil.local" } }), 403],
  ["jeton valide, /api/tags → 200", () => fetch(B + "/api/tags", { headers: ok }), 200],
  ["jeton valide, /api/embed bge-m3 → 200", () => fetch(B + "/api/embed", { method: "POST", headers: ok, body: JSON.stringify({ model: "bge-m3:latest", input: ["essai"], options: { num_gpu: 0 }, keep_alive: 0 }) }), 200],
];
let echecs = 0;
for (const [nom, f, attendu] of cas) { const r = await f(); const s = r.status; if (s !== attendu) echecs++; console.log(`${s === attendu ? "✅" : "❌"} ${nom} (obtenu ${s})`); }
const tete = await fetch(B + "/api/tags", { headers: ok }); console.log(`${tete.headers.get("access-control-allow-origin") ? "❌" : "✅"} aucun en-tête CORS`);
const log = fs.readFileSync(path.join(dir, "proxy-essai.log"), "utf8");
console.log(`${log.includes(jeton) || /"messages"|"input"/.test(log) ? "❌" : "✅"} journal sans jeton ni contenu (${log.trim().split("\n").length} lignes)`);
P.kill(); fs.rmSync(dir, { recursive: true, force: true });
process.exit(echecs ? 1 : 0);
