"""Genera los CSV del lote a partir de los YAML analíticos, el inventario y las relaciones.
Producidos aquí: inventario, kpis, madurez_multinivel, brechas_madurez, valles_muerte, dialectica, falacias, gaps_oportunidades,
competidores, figuras, sintesis_interpretativa, variables_econometricas, vacios_detectados, protopreguntas, bibliografia, fichas_bibliograficas.
Producidos por 06_conexiones.py: analisis_relacional. Producidos por 08_triangulacion_patrones.py: triangulacion, patrones_tensiones."""
import sys, os, re, json, collections, glob
sys.path.insert(0, os.path.dirname(__file__))
from synlib import *
import pandas as pd
inv={d["doc_id"]:d for d in load_inv()}; A=load_docs(); OUT=f"{L}/csv"
W=lambda df,n: df.to_csv(f"{OUT}/{n}.csv",index=False,encoding="utf-8-sig")
S=lambda x:" ".join(str(x).split()) if x is not None else ""
ids=sorted(A)
rows=[]
for i in ids:
    m=inv[i]["meta"]; a=A[i]
    rows.append(dict(doc_id=i,corpus=inv[i]["corpus"],archivo=inv[i]["path"],titulo=m.get("titulo",""),autores=m.get("autores",""),anio=m.get("anio",""),fuente=m.get("fuente",""),doi=m.get("doi",""),tipo_documento=m.get("tipo_scopus",""),idioma=m.get("idioma",""),
        paginas=inv[i]["pages"],palabras=inv[i]["words"],citas_scopus=m.get("citas_scopus"),relevancia=a["relevancia"],cluster_tema=a["cluster_tema"],metodo_tipo=a["metodo_tipo"],tipo_recurso=a["tipo_recurso"],recomendacion=a["recomendacion"],md5=inv[i]["md5"]))
W(pd.DataFrame(rows),"inventario")
r=[]
for i in ids:
    for k in A[i]["kpis"]:
        r.append(dict(doc_id=i,kpi=k[0],valor=k[1],unidad=k[2],contexto=k[3],ubicacion=k[4],fuente_dato=k[5],confianza=k[6],limitacion=k[7]))
W(pd.DataFrame(r),"kpis")
mm=[];bg=[];vl=[]
for i in ids:
    m=A[i]["madurez"]; s=srl_calc(m.get("srl")); g,crit,cv=gaps(A[i])
    mm.append(dict(doc_id=i,relevancia=A[i]["relevancia"],TRL=m["trl"][0],TRL_evidencia=m["trl"][1],TRL_justificacion=m["trl"][2],
        MRL=m["mrl"][1] if m["mrl"][0] else None,BRL=m["brl"][0],BRL_evidencia=m["brl"][1],BRL_justificacion=m["brl"][2],
        IRL=m["irl"][1] if m["irl"][0] else None,IRL_evidencia=m["irl"][2] if m["irl"][0] else None,
        DRL=m["drl"][1] if m["drl"][0] else None,DRL_evidencia=m["drl"][2] if m["drl"][0] else None,
        SRL_nivel=s["nivel"] if s else None,SRL_formula=s["formula"] if s else None))
    bg.append(dict(doc_id=i,gap_TRL_BRL=g["TB"],gap_TRL_MRL=g["TM"],gap_TRL_IRL=g["TI"],gap_BRL_DRL=g["BD"],brecha_critica=crit,valor_brecha_critica=cv))
    v=A[i]["valle"]; vl.append(dict(doc_id=i,valle_id=v[0],valle=VALLES[v[0]],descripcion=S(v[1]),severidad=v[2],estrategia_salida=S(v[3])))
W(pd.DataFrame(mm),"madurez_multinivel"); W(pd.DataFrame(bg),"brechas_madurez"); W(pd.DataFrame(vl),"valles_muerte")
r=[]
for i in ids:
    c=A[i]["c3"]; rb=c["robustez"]; gr=round(0.3*rb[0]+0.3*rb[1]+0.25*rb[2]+0.15*rb[3],1)
    r.append(dict(doc_id=i,tesis=S(c["tesis"]),antitesis=S(c["antitesis"]),sintesis=S(c["sintesis"]),consistencia=rb[0],calidad_evidencia=rb[1],validez_causal=rb[2],generalizabilidad=rb[3],robustez_global=gr,valor_estrategico=c["valor"][0]))
W(pd.DataFrame(r),"dialectica")
W(pd.DataFrame([dict(doc_id=i,falacia=f[0],evidencia=f[1],impacto=f[2]) for i in ids for f in A[i]["falacias"]]),"falacias")
W(pd.DataFrame([dict(doc_id=i,tipo=g[0],descripcion=g[1],severidad=g[2],tractabilidad=g[3],prioridad_1_10=g[4]) for i in ids for g in A[i]["gaps"]]),"gaps_oportunidades")
W(pd.DataFrame([dict(doc_id=i,competidor=c[0],pais=c[1],tipo=c[2],propuesta=c[3],fortaleza=c[4],debilidad=c[5],tendencia=c[6]) for i in ids for c in A[i]["competidores"]]),"competidores")
W(pd.DataFrame([dict(doc_id=i,figura=f[0],titulo=f[1],tipo=f[2],mensaje=f[3],dato_clave=f[4],calidad_extraccion=f[5]) for i in ids for f in A[i]["figuras"]]),"figuras")
r=[]
for i in ids:
    c=A[i]["c3"]
    r.append(dict(doc_id=i,sintesis=S(c["sintesis"]),valor_estrategico=c["valor"][0],valor_texto=S(c["valor"][1]),areas_grises=" || ".join(S(x) for x in c["areas_grises"]),ideas_propositivas=" || ".join(S(x) for x in c["ideas"]),relaciones_poco_exploradas=" || ".join(S(x) for x in c["relaciones"])))
W(pd.DataFrame(r),"sintesis_interpretativa")
W(pd.DataFrame([dict(doc_id=i,**{k:S(v) for k,v in A[i]["econ"].items()}) for i in ids]),"variables_econometricas")
W(pd.DataFrame([dict(doc_id=i,vacio_id=f"V-{i[1:]}-{n+1:02d}",tipo=v[0],descripcion=S(v[1])) for i in ids for n,v in enumerate(A[i]["vacios"])]),"vacios_detectados")
r=[]
for i in ids:
    a=A[i]; so=a["socratica"]
    r.append(dict(doc_id=i,tipo="pregunta del documento",protopregunta=S(a["c2"]["pregunta"])))
    r.append(dict(doc_id=i,tipo="hipótesis rival (socrática P6)",protopregunta=S(so["p6"])))
    r.append(dict(doc_id=i,tipo="contraejemplo no examinado (socrática P5)",protopregunta=S(so["p5"])))
    for n,g in enumerate(a["c3"]["areas_grises"][:2]): r.append(dict(doc_id=i,tipo=f"zona gris {n+1}",protopregunta=S(g)))
    for n,x in enumerate(a["c3"]["ideas"]): r.append(dict(doc_id=i,tipo=f"idea propositiva {n+1}",protopregunta=S(x)))
W(pd.DataFrame(r),"protopreguntas")
def _apa(i):
    r=apa_ref(inv[i])
    return r.replace("*28*(3), 5-6.","*28*(3), 315-316.") if i=="D087" else r  # paginación impresa del PDF (315-316); la base SciELO indica 5-6
W(pd.DataFrame([dict(doc_id=i,referencia_apa7=_apa(i)) for i in ids]),"bibliografia")
vr=[]
for i in ids:
    f=glob.glob(f"{L}/fichas/{i}_*.md")[0]; t=open(f).read()
    mn=1500 if inv[i]["pages"]>=15 else 800
    vr.append(dict(doc_id=i,ficha=os.path.relpath(f,L),palabras_ficha=len(t.split()),paginas_pdf=inv[i]["pages"],minimo_exigido=mn,cumple_extension=len(t.split())>=mn,n_areas_grises=len(A[i]["c3"]["areas_grises"]),n_ideas=len(A[i]["c3"]["ideas"]),
        n_conexiones=sum(t.count(f"**{k}**") for k in ("CONFIRMA","CONTRADICE","COMPLEMENTA","EXTIENDE","DEPENDE_DE","PRECEDE"))))
W(pd.DataFrame(vr),"fichas_bibliograficas")
print("CSV generados:",sorted(os.listdir(OUT)))
