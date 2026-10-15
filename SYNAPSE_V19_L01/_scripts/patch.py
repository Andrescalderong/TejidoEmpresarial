"""Uso: patch.py D###.yaml  <<< JSON [[anchor, replacement], ...]  (anchor tolerante a saltos de linea/espacios)"""
import sys, re, json
p=sys.argv[1]; s=open(p).read(); pairs=json.load(sys.stdin)
for a,b in pairs:
    rx=r"\s+".join(re.escape(t) for t in a.split())
    m=re.search(rx,s)
    if not m: print("NO ENCONTRADO:",a[:60]); sys.exit(1)
    s=s[:m.start()]+b+s[m.end():]
open(p,"w").write(s); print("ok",len(pairs))
