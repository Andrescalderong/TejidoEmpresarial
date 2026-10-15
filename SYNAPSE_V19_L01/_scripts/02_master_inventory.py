"""Construye el inventario maestro con DOC_ID y metadatos normalizados -> _fuente_analitica/inventario_maestro.json"""
import json, re, pandas as pd, sys
ROOT="/home/user/TejidoEmpresarial"; BASE=f"{ROOT}/SYNAPSE_V19_L01/_fuente_analitica"
inv=json.load(open(f"{BASE}/inventario.json"))
sc=pd.read_csv(f"{ROOT}/SCOPUS_Tejido empresarial/scopus.csv",dtype=str).fillna("")
se=pd.read_csv(f"{ROOT}/SciElo_tejido Empresarial/export_20261014.csv").fillna("")
se.columns=[c.strip() for c in se.columns]
se["ID"]=se["ID"].str.strip().str.strip('"')
wos=pd.read_csv(f"{ROOT}/WOS_Tejido Empresarial/literature_review_references.csv").fillna("")
def sc_meta(r):
    return dict(autores=r["Authors"], autores_completos=r["Author full names"], titulo=r["Title"], anio=str(r["Year"]),
      fuente=r["Source title"], volumen=str(r["Volume"]), numero=str(r["Issue"]), art_no=str(r["Art. No."]),
      pag_ini=str(r["Page start"]), pag_fin=str(r["Page end"]), citas_scopus=int(float(r["Cited by"] or 0)), doi=r["DOI"],
      afiliaciones=r["Affiliations"], resumen_autor=r["Abstract"], kw_autor=r["Author Keywords"], kw_indice=r["Index Keywords"],
      tipo_scopus=r["Document Type"], acceso_abierto=r["Open Access"], editorial=r["Publisher"], idioma=r["Language of Original Document"],
      issn=r["ISSN"], eid=r["EID"], n_refs_scopus=len([x for x in str(r["References"]).split(";") if x.strip()]),
      financiacion=r["Funding Details"], correspondencia=r["Correspondence Address"], link=r["Link"])
docs=[]
scopus=[d for d in inv if d["folder"]=="SCOPUS_Tejido empresarial"]
scopus.sort(key=lambda d:d["path"].lower())
n=1
for d in scopus:
    m=sc_meta(sc.loc[d["scopus_idx"]]); 
    d.update(doc_id=f"D{n:03d}", corpus="SCOPUS", meta=m); n+=1; docs.append(d)
selc=[d for d in inv if d["folder"]=="SciElo_tejido Empresarial"]
selc.sort(key=lambda d:d["path"])
for d in selc:
    num=re.search(r"a(\d\d)\.pdf",d["path"]).group(1)
    row=se[se["ID"].str.contains(f"00030{num}-col|0003000{num[1]}-col|00030{num}",regex=True)]
    row=se[se["ID"].str.endswith(f"3000{num}-col") | se["ID"].str.endswith(f"300{num}-col")]
    r=row.iloc[0] if len(row) else None
    meta=dict(titulo=r["Title"], autores=r["Author(s)"], anio=str(r["Publication year"]), fuente=r["Source"], revista=r["Journal"], idioma=r["Language(s)"], link=r["Fulltext URL"]) if r is not None else {}
    d.update(doc_id=f"D{n:03d}", corpus="SCIELO", meta=meta); n+=1; docs.append(d)
# WOS: solo el PDF no duplicado (los otros dos estan identicos por md5 a copias Scopus)
md5s={d["md5"]:d["doc_id"] for d in docs}
for d in sorted([d for d in inv if d["folder"]=="WOS_Tejido Empresarial"], key=lambda d:d["path"]):
    if d["md5"] in md5s:
        base=[x for x in docs if x["doc_id"]==md5s[d["md5"]]][0]; base.setdefault("copias_duplicadas",[]).append(d["path"]); continue
    # El PDF de WOS (Habibi Rad et al., 2021) no esta en el CSV de Scopus: el emparejamiento por titulo fue un falso positivo
    w=wos[wos["Título"].str.contains("Industry 4.0, Disaster Risk",regex=False)].iloc[0]
    m=dict(autores="Habibi Rad M.; Mojtahedi M.; Ostwald M.J.", titulo=w["Título"], anio=str(w["Año de publicación"]), fuente="Buildings", volumen="11", numero="9", art_no="411", doi=w["DOI"], resumen_autor=w["Resumen"], tipo_scopus="Review (WoS)", idioma="English", link=w["Enlace a la página del registro completo"])
    d["match_how"]="WOS-CSV (corregido manualmente)"; d["scopus_idx"]=None
    d.update(doc_id=f"D{n:03d}", corpus="WOS", meta=m); n+=1; docs.append(d)
# sintesis de buscador (meta-documentos)
for d in inv:
    if d["folder"]=="RAIZ":
        t="Scopus AI - Integrating Technology Transfer, Digital Twin, and IoT for Productive Recovery and Business Resilience after Earthquakes (2020-2024)" if d["path"].startswith("Scopus") else "Web of Science Research Assistant - sintesis sobre recuperacion productiva y resiliencia empresarial (3 documentos de referencia)"
        d.update(doc_id=f"D{n:03d}", corpus="SINTESIS_BUSCADOR", meta=dict(titulo=t, anio="2026", fuente="Scopus AI" if d["path"].startswith("Scopus") else "Clarivate WoS Research Assistant")); n+=1; docs.append(d)
for d in docs: d.pop("head",None); 
json.dump(docs,open(f"{BASE}/inventario_maestro.json","w"),indent=1,ensure_ascii=False)
print(len(docs),"documentos unicos"); 
import collections; print(collections.Counter(d["corpus"] for d in docs))
used={d["meta"].get("eid") for d in docs if d["corpus"]!="SCIELO"}
miss=sc[~sc["EID"].isin(used)]
print("Scopus sin PDF:"); 
for _,r in miss.iterrows(): print(" -",r["Year"],r["Title"][:110],"|",r["DOI"])
json.dump([dict(titulo=r["Title"],anio=str(r["Year"]),doi=r["DOI"],fuente=r["Source title"],autores=r["Authors"]) for _,r in miss.iterrows()],open(f"{BASE}/scopus_sin_pdf.json","w"),indent=1,ensure_ascii=False)
for d in docs[-18:]: print(d["doc_id"],d["pages"],d["path"][:60],"|",d["meta"].get("titulo","")[:70])
