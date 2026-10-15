"""Citación verificada por coincidencia de las primeras ocho palabras del título contra listas de referencias.
Salidas: _fuente_analitica/aristas_citacion_verificadas.json y d100_referencia_a_documento.json.
Entradas (carpeta de trabajo de la sesión): refs/D###.txt (listas de referencias recortadas) y txt/Scopus_-_Tejido_empresarial.txt (lista de D100)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(__file__))
from synlib import *
W="/tmp/claude-0/-home-user/9a736d69-a05b-5f2d-be75-7dffdbaa2f82/scratchpad"
inv={d["doc_id"]:d for d in load_inv()}
norm=lambda s: re.sub(r"[^a-z0-9 ]"," ",s.lower()).split()
key={i:" ".join(norm(inv[i]["meta"].get("titulo",""))[:8]) for i in inv if len(norm(inv[i]["meta"].get("titulo","")))>=5}
refs={i:" ".join(norm(open(f"{W}/refs/{i}.txt").read())) for i in inv if os.path.exists(f"{W}/refs/{i}.txt")}
raw=open(f"{W}/txt/Scopus_-_Tejido_empresarial.txt").read(); lst=raw[raw.index("References\n"):]
refs["D100"]=" ".join(norm(lst))
edges=[[a,b] for a in refs for b in key if a!=b and key[b] in refs[a]]
lst=re.sub(r"https://www\.scopus\.com/pages/ai\?[^\n]*Página \d+ de 16\nScopus - Scopus AI[^\n]*\n","",lst)
items=re.split(r"\n\s*\n(?=\d{1,3}\. )",lst); refmap={}
for it in items:
    m=re.match(r"(\d+)\. ",it)
    if m: refmap[int(m.group(1))]=[i for i,k in key.items() if k in " ".join(norm(it))]
json.dump(edges,open(f"{BASE}/aristas_citacion_verificadas.json","w")); json.dump(refmap,open(f"{BASE}/d100_referencia_a_documento.json","w"))
print(len(edges),"aristas;",sum(len(v) for v in refmap.values()),"coincidencias de la lista de D100 (la referencia 1 requiere asignación manual: D070)")
