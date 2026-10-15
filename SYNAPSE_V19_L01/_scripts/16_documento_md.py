"""Versión Markdown del documento completo (mismos bloques que el DOCX)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from synlib import L
D = json.load(open(f"{L}/documento/bloques.json")); out = []
esc = lambda c: str(c).replace("|", "\\|").replace("\n", " ")
out += [f"# {D['meta']['titulo']}", "", "**Andrés Calderón**", "", "## Resumen", "", D["meta"]["resumen"], "", f"*Palabras clave:* {D['meta']['kw']}", ""]
tab = 0
for b in D["blocks"]:
    t = b["t"]
    if t == "h1": out += ["", f"# {b['x']}", ""]
    elif t == "h2": out += ["", f"## {b['x']}", ""]
    elif t == "h3": out += ["", f"### {b['x']}", ""]
    elif t.startswith("fh"): out += ["", "#" * (int(t[2]) + 1) + " " + b["x"], ""]
    elif t == "p": out += [b["x"], ""]
    elif t == "ul": out += [f"- {x}" for x in b["items"]] + [""]
    elif t == "ol": out += [f"{n}. {x}" for n, x in enumerate(b["items"], 1)] + [""]
    elif t == "ref": out += [b["x"], ""]
    elif t == "table":
        rows = b["rows"]; nc = max(len(r) for r in rows); rows = [r + [""] * (nc - len(r)) for r in rows]
        if not b.get("c"):
            tab += 1; cap = b.get("cap") or ("", ""); out += [f"**Tabla {tab}**", "", f"*{cap[0]}{': ' + cap[1] if cap[1] else ''}*", ""]
        out += ["| " + " | ".join(esc(c) for c in rows[0]) + " |", "|" + "---|" * nc] + ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows[1:]] + [""]
    elif t == "fig": out += [f"**Figura {b['num']}**", "", f"*{b['x']}*", "", f"![{b['x']}](../figuras/{b['f']})", "", b["n"], ""]
    elif t == "pb": out += ["", "---", ""]
open(f"{L}/documento/Informe_Lote_L01_SYNAPSE_APA7.md", "w").write("\n".join(out))
print("MD palabras:", len(" ".join(out).split()))
