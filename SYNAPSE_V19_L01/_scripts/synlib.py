"""Biblioteca comun: carga de inventario/analisis, referencias APA 7, calculos de SRL y brechas."""
import json, re, yaml, math, glob, os
ROOT="/home/user/TejidoEmpresarial"; L=f"{ROOT}/SYNAPSE_V19_L01"; BASE=f"{L}/_fuente_analitica"
FECHA="2026-10-15"
def load_inv(): return json.load(open(f"{BASE}/inventario_maestro.json"))
def load_docs():
    out={}
    for f in sorted(glob.glob(f"{BASE}/docs/D*.yaml")):
        d=yaml.safe_load(open(f)); out[d["doc_id"]]=d
    return out
def _initials(given):
    parts=[]
    for tok in given.replace(".", " ").split():
        sub=[s for s in tok.split("-") if s]
        parts.append("-".join(s[0].upper()+"." for s in sub).replace(".-", ".-"))
    return " ".join(parts)
def _apa_names(meta, corpus):
    if corpus=="SCOPUS" or corpus=="WOS":
        full=meta.get("autores_completos")
        names=[]
        if full:
            for a in full.split(";"):
                a=re.sub(r"\s*\(\d+\)\s*$","",a.strip())
                if "," in a:
                    fam,giv=a.split(",",1); names.append(f"{fam.strip()}, {_initials(giv.strip())}")
                else: names.append(a)
        else:
            for a in meta.get("autores","").split(";"):
                a=a.strip()
                if not a: continue
                m=re.match(r"(.+?)\s+((?:[A-Z]\.?-?)+)$",a)
                names.append(f"{m.group(1)}, {' '.join(c+'.' for c in re.findall(r'[A-Z]',m.group(2)))}" if m else a)
    elif corpus=="SCIELO":
        toks=[t.strip() for t in meta.get("autores","").split(",")]
        names=[]
        for i in range(0,len(toks)-1,2): names.append(f"{toks[i]}, {_initials(toks[i+1])}")
    else: names=[]
    return names
def apa_authors(names):
    if not names: return ""
    if len(names)==1: return names[0]
    if len(names)<=20: return ", ".join(names[:-1])+", & "+names[-1]
    return ", ".join(names[:19])+", . . . "+names[-1]
def apa_ref(d):
    m=d["meta"]; c=d["corpus"]; yr=m.get("anio","s. f.")
    if c=="SINTESIS_BUSCADOR":
        who="Elsevier. " if "Scopus" in m["fuente"] else "Clarivate. "
        return f"{who}({yr}). *{m['titulo']}* [Síntesis generada por IA, archivo PDF]. {m['fuente']}."
    a=apa_authors(_apa_names(m,c)) or "Autor no identificado"
    t=m.get("titulo","").rstrip(".")
    src=m.get("fuente","")
    if c=="SCIELO":
        mm=re.match(r"(.+?);\s*(\d+)\((\d+)\);\s*(\d+)-(\d+)",src)
        rev,vol,num,p1,p2=mm.groups() if mm else (src,"","","","")
        link=m.get("link","")
        return f"{a} ({yr}). {t}. *{rev}*, *{vol}*({num}), {p1}-{p2}. {link}"
    vol=m.get("volumen",""); num=m.get("numero",""); art=m.get("art_no",""); p1=m.get("pag_ini",""); p2=m.get("pag_fin","")
    vi=""
    if vol: vi=f", *{vol}*"+(f"({num})" if num else "")
    pg=""
    if art: pg=f", Article {art}"
    elif p1 and p2: pg=f", {p1}-{p2}"
    doi=m.get("doi","")
    tail=f" https://doi.org/{doi}" if doi else (f" {m.get('link','')}" if m.get('link') else "")
    return f"{a} ({yr}). {t}. *{src}*{vi}{pg}.{tail}"
def srl_calc(sr):
    if not sr: return None
    comp=sr.get("componentes",[]); ifs=sr.get("interfaces",[])
    if not ifs: return None
    terms=[]
    for i,j,irl in ifs:
        terms.append(comp[i][1]*irl); terms.append(comp[j][1]*irl)
    raw=sum(terms)/len(terms)
    lvl=max(1.0,min(9.0,raw/9.0))
    return dict(raw=round(raw,2), nivel=round(lvl,2), formula=f"SRL=Σ(TRLi×IRLij)/{len(terms)} términos ordenados = {raw:.1f}; ÷9 → {raw/9:.2f}; nivel acotado a [1,9] = {lvl:.2f}")
def gaps(d):
    m=d["madurez"]; trl=m["trl"][0]; brl=m["brl"][0]
    mrl=m["mrl"][1] if m["mrl"][0] else None
    irl=m["irl"][1] if m["irl"][0] else None
    drl=m["drl"][1] if m["drl"][0] else None
    g={"TB": trl-brl if (trl is not None and brl is not None) else None,
       "TM": trl-mrl if mrl is not None and trl is not None else None,
       "TI": trl-irl if irl is not None and trl is not None else None,
       "BD": brl-drl if drl is not None and brl is not None else None}
    valid={k:v for k,v in g.items() if v is not None}
    crit=max(valid,key=lambda k:abs(valid[k])) if valid else None
    names={"TB":"Valle de la Muerte Comercial (TRL-BRL)","TM":"Valle de la Muerte de Producción (TRL-MRL)","TI":"Valle de la Muerte de Integración (TRL-IRL)","BD":"Brecha Oferta-Demanda (BRL-DRL)"}
    return g, (names[crit] if crit else "N/A"), (valid[crit] if crit else None)
VALLES={0:"Ninguno",1:"V1 Investigación sin aplicación",2:"V2 Prototipo sin escalamiento",3:"V3 Tecnología sin negocio",4:"V4 Componentes sin integración",5:"V5 Demanda sin solución"}
def esc(s): return str(s).replace("|","\\|").replace("\n"," ") if s is not None else ""
def slug(t):
    import unicodedata
    t=unicodedata.normalize("NFKD",t).encode("ascii","ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+","-",t).strip("-")[:60]
