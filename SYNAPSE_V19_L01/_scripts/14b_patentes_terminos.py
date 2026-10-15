"""Frecuencias de términos del eje del corpus en las páginas de patentes leídas por OCR (patentes/_ocr_texto/). Salida: patentes/csv/terminos_crudo.json"""
import sys, os, re, glob, json
sys.path.insert(0, os.path.dirname(__file__))
from synlib import L
OUT = f"{L}/patentes"; os.makedirs(f"{OUT}/csv", exist_ok=True)
terms = {"digital twin": r"digital\s*twin", "earthquake/seismic": r"earthquake|seismic", "disaster": r"disaster|catastroph",
         "natural hazard (flood,hurricane,storm)": r"hurricane|flood|tsunami|typhoon|wildfire", "disruption": r"disrupt", "resilience": r"resilien", "recovery": r"recover",
         "IoT": r"internet of things|\bIoT\b|\bloT\b", "sensor": r"sensor", "machine learning": r"machine[- ]learn|machine-learned", "blockchain/smart contract": r"blockchain|smart contract", "pandemic": r"pandemic|covid"}
res = {}
for f in glob.glob(f"{OUT}/_ocr_texto/*.txt"):
    tag = re.sub(r"_p\d+\.txt$", "", os.path.basename(f)); t = re.sub(r"(\w)-\s+(\w)", r"\1\2", open(f).read())  # une palabras partidas por guion de fin de línea
    d = res.setdefault(tag, {"paginas": 0, "palabras": 0, **{k: 0 for k in terms}})
    d["paginas"] += 1; d["palabras"] += len(t.split())
    for k, r in terms.items(): d[k] += len(re.findall(r, t, flags=re.I))
json.dump(res, open(f"{OUT}/csv/terminos_crudo.json", "w"), ensure_ascii=False, indent=1)
for k, v in sorted(res.items()): print(k, v["paginas"], "páginas;", v["digital twin"], "gemelo digital")
