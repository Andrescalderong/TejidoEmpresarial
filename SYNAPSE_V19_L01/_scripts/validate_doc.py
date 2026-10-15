"""Valida un/varios D###.yaml contra los minimos de la especificacion SYNAPSE V19 (FBA)."""
import sys, yaml, json, re, glob
BASE="/home/user/TejidoEmpresarial/SYNAPSE_V19_L01/_fuente_analitica"
inv={d["doc_id"]:d for d in json.load(open(f"{BASE}/inventario_maestro.json"))}
def wc(x):
    if x is None: return 0
    if isinstance(x,str): return len(x.split())
    if isinstance(x,(list,tuple)): return sum(wc(i) for i in x)
    if isinstance(x,dict): return sum(wc(v) for v in x.values())
    return 0
MIN_C2={"objetivo":80,"marco":100,"metodologia":150,"resultados":200,"discusion":100}
MIN_C3={"antitesis":100,"sintesis":100,"puntos_oscuros":150}
def check(path):
    d=yaml.safe_load(open(path)); did=d["doc_id"]; pg=inv[did]["pages"]; errs=[]
    for k in ["relevancia","cluster_tema","metodo_tipo","tipo_recurso","kw_inferidas","c2","c3","socratica","kpis","madurez","valle","falacias","recomendacion","bradford","causal","gaps","figuras","competidores","econ","vacios"]:
        if k not in d: errs.append(f"falta {k}")
    if errs: return did,errs,{}
    c2,c3=d["c2"],d["c3"]
    for k,m in MIN_C2.items():
        if wc(c2.get(k))<m: errs.append(f"c2.{k} {wc(c2.get(k))}<{m}")
    for k,m in MIN_C3.items():
        if wc(c3.get(k))<m: errs.append(f"c3.{k} {wc(c3.get(k))}<{m}")
    if len(c3["areas_grises"])<3: errs.append("areas_grises<3")
    if wc(c3["areas_grises"])<150: errs.append(f"areas_grises palabras {wc(c3['areas_grises'])}<150")
    if len(c3["ideas"])<2 or wc(c3["ideas"])<200: errs.append(f"ideas {len(c3['ideas'])}/{wc(c3['ideas'])}p <2/200")
    if len(c3["relaciones"])<2: errs.append("relaciones<2")
    if len(c3["robustez"])!=4: errs.append("robustez!=4")
    if wc(c3["valor"][1])<50: errs.append("valor<50 palabras")
    if not (3<=len(d["kpis"])): errs.append("kpis<3")
    for r in d["kpis"]:
        if len(r)!=8: errs.append(f"kpi malformado {r[:1]}")
    m=d["madurez"]
    for k in ["trl","mrl","brl","irl","drl"]:
        if k not in m: errs.append(f"madurez.{k}")
    n2=sum(wc(c2.get(k)) for k in ["objetivo","pregunta","marco","metodologia","resultados","discusion","limitaciones","futuro"])
    n3=sum(wc(c3.get(k)) for k in ["tesis","antitesis","sintesis","areas_grises","puntos_oscuros","ideas","relaciones"])+wc(c3["valor"][1])
    n1=60; n4=wc(d["falacias"])+wc(d["bradford"])+30
    tot=n1+n2+n3+n4; need=1500 if pg>=15 else 800
    if tot<need: errs.append(f"ficha {tot}<{need}")
    if n3/tot<0.40: errs.append(f"capa3 {n3/tot:.0%}<40%")
    return did,errs,dict(pg=pg,c2=n2,c3=n3,tot=tot,share=round(n3/tot,2),need=need,kpis=len(d["kpis"]))
if __name__=="__main__":
    files=sys.argv[1:] or sorted(glob.glob(f"{BASE}/docs/D*.yaml"))
    bad=0
    for f in files:
        try: did,errs,st=check(f)
        except Exception as e: print(f,"ERROR YAML/estructura:",e); bad+=1; continue
        print(did, "OK" if not errs else "REVISAR", st, errs if errs else "")
        bad+= bool(errs)
    sys.exit(1 if bad else 0)
