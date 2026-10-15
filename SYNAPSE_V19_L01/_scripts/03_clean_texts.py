"""Extrae (pdftotext, orden de lectura) y limpia cada PDF unico -> clean/DOC.txt (cuerpo) y refs/DOC.txt (referencias)."""
import json, subprocess, re, os, sys, textwrap
ROOT="/home/user/TejidoEmpresarial"; BASE=f"{ROOT}/SYNAPSE_V19_L01/_fuente_analitica"; OUT=sys.argv[1]
os.makedirs(f"{OUT}/clean",exist_ok=True); os.makedirs(f"{OUT}/refs",exist_ok=True)
docs=json.load(open(f"{BASE}/inventario_maestro.json"))
REF=re.compile(r"^\s*(\d+\.?\s*)?(references|referencias|bibliography|bibliograf[ií]a|reference list|literature cited|referencias bibliogr[aá]ficas|works cited)\s*:?\s*$",re.I)
stats=[]
for d in docs:
    raw=subprocess.run(["pdftotext","-enc","UTF-8",os.path.join(ROOT,d["path"]),"-"],capture_output=True,text=True).stdout
    pages=raw.split("\x0c")
    raw="\n\n".join(f"[[p.{i+1}]]\n"+pg for i,pg in enumerate(pages) if pg.strip())
    lines=raw.split("\n")
    # ultimo encabezado de referencias en la segunda mitad
    idx=None
    for i,l in enumerate(lines):
        if REF.match(l) and i>len(lines)*0.35: idx=i
    body=lines[:idx] if idx else lines; refs=lines[idx:] if idx else []
    def para(ls):
        txt="\n".join(ls); txt=re.sub(r"-\n(?=[a-záéíóúñ])","",txt)
        blocks=re.split(r"\n\s*\n",txt); out=[]
        for b in blocks:
            b=re.sub(r"\s*\n\s*"," ",b).strip()
            if b: out.append(textwrap.fill(b,width=230))
        return "\n".join(out)
    cb,cr=para(body),para(refs)
    open(f"{OUT}/clean/{d['doc_id']}.txt","w").write(cb); open(f"{OUT}/refs/{d['doc_id']}.txt","w").write(cr)
    stats.append((d["doc_id"],len(cb.split()),len(cr.split()),idx is not None))
json.dump(stats,open(f"{OUT}/clean_stats.json","w"))
tot=sum(s[1] for s in stats); print("palabras cuerpo:",tot,"| sin refs detectadas:",[s[0] for s in stats if not s[3]])
