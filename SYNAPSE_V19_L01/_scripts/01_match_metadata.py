"""Empareja cada PDF del repositorio con su registro bibliografico (Scopus CSV, SciELO CSV/RIS, WOS CSV).
Salida: _fuente_analitica/inventario.json  (DOC_ID, ruta, paginas, palabras, metadatos, metodo de emparejamiento)
"""
import re, json, os, sys, hashlib, unicodedata, pandas as pd
from difflib import SequenceMatcher
ROOT = "/home/user/TejidoEmpresarial"
TXT = sys.argv[1]            # carpeta con txt extraidos
OUT = sys.argv[2]
def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii","ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]+"," ",s)
def toks(s): return set(w for w in norm(s).split() if len(w)>3)

scopus = pd.read_csv(f"{ROOT}/SCOPUS_Tejido empresarial/scopus.csv").fillna("")
scielo = pd.read_csv(f"{ROOT}/SciElo_tejido Empresarial/export_20261014.csv").fillna("")
wos = pd.read_csv(f"{ROOT}/WOS_Tejido Empresarial/literature_review_references.csv").fillna("")

inv = []
for line in open(os.path.join(os.path.dirname(OUT),"..","..","..", "inventory_raw.txt")) if False else open(sys.argv[3]):
    pg, wc, path = line.rstrip("\n").split("|",2)
    inv.append(dict(pages=int(pg), words=int(wc), path=path[2:]))
md5 = {}
for line in open(sys.argv[4]):
    h, p = line.rstrip("\n").split("  ",1); md5[p[2:]] = h
for d in inv: d["md5"] = md5[d["path"]]

def slug(path): return path.replace("/","__").replace(" ","_")[:-4]
for d in inv:
    d["txt"] = os.path.join(TXT, slug(d["path"])+".txt")
    t = open(d["txt"], errors="ignore").read()
    d["head"] = t[:7000]
    d["folder"] = d["path"].split("/")[0] if "/" in d["path"] else "RAIZ"

def best_scopus(head):
    hn = norm(head); ht = toks(head)
    best = (0, None, None)
    for i, r in scopus.iterrows():
        doi = r["DOI"].lower().strip()
        if doi and doi in head.lower().replace(" ","").replace("\n","") : return (1.0, i, "DOI")
        tt = toks(r["Title"])
        if not tt: continue
        sc = len(tt & ht)/len(tt)
        # bonus si el titulo aparece literal
        if norm(r["Title"])[:60] in hn: sc = max(sc, 0.99)
        if sc > best[0]: best = (sc, i, "titulo")
    return best

for d in inv:
    d["match"] = None
    if d["folder"] == "SCOPUS_Tejido empresarial" or d["folder"]=="WOS_Tejido Empresarial":
        sc, i, how = best_scopus(d["head"])
        d["match_score"] = round(sc,2); d["match_how"]=how; d["scopus_idx"] = int(i) if i is not None else None
    elif d["folder"] == "SciElo_tejido Empresarial":
        d["match_how"]="SciELO"
json.dump(inv, open(OUT,"w"), indent=1, ensure_ascii=False)
low = [(d["path"], d.get("match_score"), scopus.loc[d["scopus_idx"],"Title"][:70] if d.get("scopus_idx") is not None else None) for d in inv if d.get("match_score") is not None and d["match_score"]<0.9]
print(len(inv), "PDF;", "emparejamientos dudosos:", len(low))
for x in low: print(x)
used = set(d["scopus_idx"] for d in inv if d.get("scopus_idx") is not None and d.get("match_score",0)>=0.9)
print("registros Scopus sin PDF:", len(scopus)-len(used))
