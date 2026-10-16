"""Versión Markdown del documento completo (mismos bloques que el DOCX), con índice, lista de figuras y de tablas enlazados."""
import json, os, sys, re, collections
sys.path.insert(0, os.path.dirname(__file__))
from synlib import L
D = json.load(open(f"{L}/documento/bloques.json")); B = D["blocks"]
esc = lambda c: str(c).replace("|", "\\|").replace("\n", " ")
seen = collections.Counter()
def slug(t):  # ancla al estilo GitHub
    t = re.sub(r"[*`]", "", t).lower(); t = re.sub(r"[^\w\- ]", "", t, flags=re.U).replace(" ", "-"); n = seen[t]; seen[t] += 1
    return t if n == 0 else f"{t}-{n}"
# paso 1: encabezados, anclas y rótulos
toc, figs, tabs = [], [], []; pend = None; tn = 0
for i, b in enumerate(B):
    t = b["t"]; lvl = {"h1": 1, "h2": 2, "h3": 3}.get(t) or ({"fh1": 2, "fh2": 3, "fh3": 4, "fh4": 5}.get(t))
    if lvl: b["_a"] = slug(b["x"])
    if t == "h1":
        if re.fullmatch(r"Apéndice [A-Z]", b["x"]): pend = b
        elif pend: toc.append((0, pend["x"] + ". " + b["x"], pend["_a"])); pend = None
        else: toc.append((0, b["x"], b["_a"]))
    elif t == "h2": toc.append((1, b["x"], b["_a"]))
    elif t == "fh1": toc.append((1, b["x"], b["_a"]))
    elif t == "fig": figs.append(b)
    elif t == "table" and not b.get("c"): tn += 1; tabs.append((tn, (b.get("cap") or ("",))[0]))
out = [f"# {D['meta']['titulo']}", "", "**Andrés Calderón**", "", "## Resumen", "", D["meta"]["resumen"], "", f"*Palabras clave:* {D['meta']['kw']}", "",
       "---", "", "## Contenido", ""]
for lv, tx, a in toc: out.append(("  " * lv) + f"- [{tx}](#{a})")
out += ["", "## Lista de figuras", ""] + [f"- Figura {b['num']}. {b['x']}" for b in figs] + ["", "## Lista de tablas", ""] + [f"- Tabla {n}. {c}" for n, c in tabs] + ["", "---", ""]
tab = 0
for b in B:
    t = b["t"]
    if t == "h1": out += ["", f"# {b['x']}", ""]
    elif t == "h2": out += ["", f"## {b['x']}", ""]
    elif t == "h3": out += ["", f"### {b['x']}", ""]
    elif t.startswith("fh"): out += ["", "#" * (int(t[2]) + 1) + " " + b["x"], ""]
    elif t == "p": out += [b["x"], ""]
    elif t == "ul": out += [f"- {x}" for x in b["items"]] + [""]
    elif t == "ol": out += [f"{n}. {x}" for n, x in enumerate(b["items"], 1)] + [""]
    elif t == "ref": out += [b["x"], ""]
    elif t == "fig": out += [f"**Figura {b['num']}**", "", f"*{b['x']}*", "", f"![{b['x']}](../figuras/{b['f'].replace('.png','.svg')})", "", b["n"], ""]
    elif t == "table":
        rows = b["rows"]; nc = max(len(r) for r in rows); rows = [r + [""] * (nc - len(r)) for r in rows]
        if not b.get("c"):
            tab += 1; cap = b.get("cap") or ("", ""); out += [f"**Tabla {tab}**", "", f"*{cap[0]}{': ' + cap[1] if cap[1] else ''}*", ""]
        out += ["| " + " | ".join(esc(c) for c in rows[0]) + " |", "|" + "---|" * nc] + ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows[1:]] + [""]
    elif t == "pb": out += ["", "---", ""]
open(f"{L}/documento/Informe_Lote_L01_SYNAPSE_APA7.md", "w").write("\n".join(out))
print("MD palabras:", len(" ".join(out).split()), "entradas de índice:", len(toc))
