"""Pipeline ML/NLP real sobre texto limpio + metadatos. Salidas: csv/ml/*.csv, figuras/*.png, ml_resumen.json.
Ejecuta: TF-IDF, k-means (selección por silueta), jerárquico (Ward sobre SVD), DBSCAN (coseno), LDA, PCA/SVD y t-SNE,
redes de co-palabras y co-autoría, estadísticas bibliométricas y sensibilidad con/sin bloque SciELO D087-D098."""
import sys, os, re, json, glob, warnings, itertools, collections
sys.path.insert(0, os.path.dirname(__file__))
warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
from synlib import *
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, ENGLISH_STOP_WORDS
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import TruncatedSVD, LatentDirichletAllocation, PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.preprocessing import normalize
import networkx as nx
import matplotlib; matplotlib.use("Agg"); matplotlib.rcParams["svg.fonttype"]="none"
import matplotlib.pyplot as plt
CLEAN="/tmp/claude-0/-home-user/9a736d69-a05b-5f2d-be75-7dffdbaa2f82/scratchpad/clean"
OUT=f"{L}/csv/ml"; FIG=f"{L}/figuras"; os.makedirs(OUT,exist_ok=True); os.makedirs(FIG,exist_ok=True)
SEED=42
ES_STOP=set("""de la que el en y a los del se las por un para con no una su al lo como más pero sus le ya o este sí porque esta entre cuando muy sin sobre también me hasta hay donde quien desde todo nos durante todos uno les ni contra otros ese eso ante ellos e esto mí antes algunos qué unos yo otro otras otra él tanto esa estos mucho quienes nada muchos cual poco ella estar estas algunas algo nosotros mi mis tú te ti tu tus ellas nosotras vosotros vosotras os mío mía míos mías tuyo tuya suyo suya nuestro nuestra son fue ser han fueron sido es era estudio resultados método métodos análisis tabla figura cuadro p pp et al""".split())
EXTRA=set("""javeriana pontificia universidad downloaded licensed authorized xplore utc october restrictions apply emerald et al fig figure table tables doi https http www com org elsevier springer ieee mdpi copyright license licensee ltd inc published received accepted revised available online article journal vol pp page pages also may can use used using one two three based study studies paper results result however thus therefore within among per via section sec eq equation""".split())
STOP=list(ENGLISH_STOP_WORDS|ES_STOP|EXTRA)
BOILER=[r"authorized licensed use limited to[^.]*?restrictions apply\.?",r"downloaded (?:from|on) [^.]*?(?:restrictions apply|user on \d+ [a-z]+ \d{4}|\d{4})",r"pontificia universidad javeriana",r"ieee xplore",r"scopus ai",r"página \d+ de \d+"]
def tok_clean(t):
    t=t.lower()
    for b in BOILER: t=re.sub(b," ",t)
    t=re.sub(r"\[\[p\.\d+\]\]"," ",t); t=re.sub(r"https?://\S+"," ",t); t=re.sub(r"\b\d[\d.,]*\b"," ",t)
    t=t.lower(); t=re.sub(r"[^a-záéíóúñü\- ]"," ",t); t=re.sub(r"\s+"," ",t); return t
inv={d["doc_id"]:d for d in load_inv()}; A=load_docs()
ids=sorted(inv); texts={}
for i in ids:
    p=f"{CLEAN}/{i}.txt"; texts[i]=tok_clean(open(p).read()) if os.path.exists(p) else ""
def run(ids_sel, tag, k_range=range(2,11), n_topics=6, save=True):
    docs=[texts[i] for i in ids_sel]
    tf=TfidfVectorizer(stop_words=STOP,ngram_range=(1,2),min_df=2,max_df=0.8,sublinear_tf=True,max_features=6000)
    X=tf.fit_transform(docs); terms=np.array(tf.get_feature_names_out())
    # k-means con selección por silueta (coseno ~ euclídea sobre vectores normalizados)
    sil={}; models={}
    for k in k_range:
        km=KMeans(n_clusters=k,n_init=20,random_state=SEED).fit(X); sil[k]=silhouette_score(X,km.labels_,metric="cosine"); models[k]=km
    kbest=max(sil,key=sil.get); km=models[kbest]; lab_km=km.labels_
    # jerárquico: Ward sobre SVD normalizado
    svd=TruncatedSVD(n_components=min(30,X.shape[0]-1),random_state=SEED); Z=normalize(svd.fit_transform(X))
    hc=AgglomerativeClustering(n_clusters=kbest,linkage="ward").fit(Z); lab_hc=hc.labels_
    # DBSCAN coseno: eps por percentil de distancia al 3er vecino
    from sklearn.neighbors import NearestNeighbors
    nn=NearestNeighbors(n_neighbors=4,metric="cosine").fit(X); dist,_=nn.kneighbors(X); eps=float(np.percentile(dist[:,3],60))
    db=DBSCAN(eps=eps,min_samples=3,metric="cosine").fit(X); lab_db=db.labels_
    # LDA sobre conteos
    cv=CountVectorizer(stop_words=STOP,min_df=3,max_df=0.7,max_features=3000); C=cv.fit_transform(docs); cterms=np.array(cv.get_feature_names_out())
    lda=LatentDirichletAllocation(n_components=n_topics,learning_method="batch",random_state=SEED,max_iter=60).fit(C); theta=lda.transform(C)
    perp=float(lda.perplexity(C))
    # proyecciones
    pca=PCA(n_components=2,random_state=SEED).fit(Z); P=pca.transform(Z)
    perpx=max(5,min(20,(len(ids_sel)-1)//4)); ts=TSNE(n_components=2,perplexity=perpx,random_state=SEED,init="pca",metric="cosine").fit_transform(Z)
    res=dict(tag=tag,n=len(ids_sel),n_terms=int(X.shape[1]),kbest=int(kbest),sil_by_k={int(k):round(v,4) for k,v in sil.items()},
             sil_kmeans=round(sil[kbest],4),n_dbscan_clusters=int(len(set(lab_db))-(1 if -1 in lab_db else 0)),dbscan_noise=int((lab_db==-1).sum()),dbscan_eps=round(eps,4),
             lda_perplexity=round(perp,1),pca_var=[round(float(v),4) for v in pca.explained_variance_ratio_],ari_km_hc=round(adjusted_rand_score(lab_km,lab_hc),4))
    top=[]
    for c in range(kbest):
        idx=np.argsort(-km.cluster_centers_[c])[:12]; top.append(", ".join(terms[idx]))
    ltop=[]
    for t in range(n_topics):
        idx=np.argsort(-lda.components_[t])[:12]; ltop.append(", ".join(cterms[idx]))
    return dict(X=X,terms=terms,lab_km=lab_km,lab_hc=lab_hc,lab_db=lab_db,theta=theta,P=P,ts=ts,res=res,top=top,ltop=ltop,Z=Z,ids=ids_sel)
FULL=run(ids,"completo_101")
SIN_SCIELO=[i for i in ids if not ("D087"<=i<="D098")]
SENS=run(SIN_SCIELO,"sin_SciELO_89")
SIN_SYNTH=[i for i in SIN_SCIELO if i not in ("D100","D101")]
SENS2=run(SIN_SYNTH,"sin_SciELO_ni_sintesis_87")
# ---- salidas por documento
rows=[]
for n,i in enumerate(ids):
    rows.append(dict(doc_id=i,relevancia=A[i]["relevancia"],cluster_kmeans=int(FULL["lab_km"][n]),cluster_jerarquico=int(FULL["lab_hc"][n]),cluster_dbscan=int(FULL["lab_db"][n]),
        topico_lda_dominante=int(FULL["theta"][n].argmax()),peso_topico=round(float(FULL["theta"][n].max()),3),pca1=round(float(FULL["P"][n,0]),4),pca2=round(float(FULL["P"][n,1]),4),tsne1=round(float(FULL["ts"][n,0]),3),tsne2=round(float(FULL["ts"][n,1]),3),
        titulo=inv[i]["meta"].get("titulo","")[:120]))
pd.DataFrame(rows).to_csv(f"{OUT}/ml_asignacion_documentos.csv",index=False,encoding="utf-8-sig")
tr=[]
for c,t in enumerate(FULL["top"]): tr.append(dict(modelo="kmeans_completo",grupo=c,n_docs=int((FULL["lab_km"]==c).sum()),terminos_top=t))
for c,t in enumerate(FULL["ltop"]): tr.append(dict(modelo="LDA_completo",grupo=c,n_docs=int(sum(FULL["theta"].argmax(1)==c)),terminos_top=t))
for c,t in enumerate(SENS["top"]): tr.append(dict(modelo="kmeans_sin_SciELO",grupo=c,n_docs=int((SENS["lab_km"]==c).sum()),terminos_top=t))
for c,t in enumerate(SENS["ltop"]): tr.append(dict(modelo="LDA_sin_SciELO",grupo=c,n_docs=int(sum(SENS["theta"].argmax(1)==c)),terminos_top=t))
pd.DataFrame(tr).to_csv(f"{OUT}/ml_terminos_por_grupo.csv",index=False,encoding="utf-8-sig")
# sensibilidad: ARI entre asignaciones sobre documentos comunes
common=[i for i in SIN_SCIELO]; ix_full=[ids.index(i) for i in common]
ari_km=adjusted_rand_score(FULL["lab_km"][ix_full],SENS["lab_km"]); ari_hc=adjusted_rand_score(FULL["lab_hc"][ix_full],SENS["lab_hc"])
sci_in_full=[ (i,int(FULL["lab_km"][ids.index(i)])) for i in ids if "D087"<=i<="D098"]
sci_clusters=collections.Counter(c for _,c in sci_in_full)
kfix=SENS["res"]["kbest"]
km_fix=KMeans(n_clusters=kfix,n_init=20,random_state=SEED).fit(FULL["X"])
ari_fix=adjusted_rand_score(km_fix.labels_[ix_full],SENS["lab_km"])
share_sci_fix=collections.Counter(int(km_fix.labels_[ids.index(i)]) for i in ids if "D087"<=i<="D098")
sens=dict(ARI_kmeans_completo_vs_sin_SciELO_k_propio=round(float(ari_km),4),ARI_jerarquico_completo_vs_sin_SciELO_k_propio=round(float(ari_hc),4),
          k_fijo=kfix,ARI_kmeans_k_fijo_completo_vs_sin_SciELO=round(float(ari_fix),4),clusters_SciELO_con_k_fijo=dict(share_sci_fix),
          cluster_kmeans_de_los_12_SciELO=dict(sci_clusters),
          k_mejor=dict(completo=FULL["res"]["kbest"],sin_SciELO=SENS["res"]["kbest"],sin_SciELO_ni_sintesis=SENS2["res"]["kbest"]),
          silueta=dict(completo=FULL["res"]["sil_kmeans"],sin_SciELO=SENS["res"]["sil_kmeans"],sin_SciELO_ni_sintesis=SENS2["res"]["sil_kmeans"]),
          dbscan=dict(completo=[FULL["res"]["n_dbscan_clusters"],FULL["res"]["dbscan_noise"]],sin_SciELO=[SENS["res"]["n_dbscan_clusters"],SENS["res"]["dbscan_noise"]]))
# ---- redes: co-palabras (palabras clave de autor+índice, Scopus/WoS) y co-autoría
def kws(m):
    out=[]
    for f in ("kw_autor","kw_indice"):
        v=m.get(f) or ""
        out+= [re.sub(r"\s+"," ",k.strip().lower()) for k in re.split(r";|\|",v) if k.strip()]
    # unificar sinónimos básicos
    mp={"digital twins":"digital twin","internet of things (iot)":"internet of things","iot":"internet of things","earthquakes":"earthquake","disasters":"disaster","disaster management":"disaster management","digital twin (dt)":"digital twin","structural health monitoring (shm)":"structural health monitoring","artificial intelligence (ai)":"artificial intelligence"}
    return sorted(set(mp.get(k,k) for k in out))
G=nx.Graph(); occ=collections.Counter()
for i in ids:
    ks=kws(inv[i]["meta"]); 
    for k in ks: occ[k]+=1
    for a,b in itertools.combinations(ks,2): G.add_edge(a,b,weight=G.get_edge_data(a,b,{"weight":0})["weight"]+1)
Gs=G.subgraph([n for n in G if occ[n]>=3]).copy()
comm=list(nx.algorithms.community.greedy_modularity_communities(Gs,weight="weight")) if Gs.number_of_nodes() else []
cw=[]
for ci,cs in enumerate(comm):
    cs=set(cs); inn=sum(d["weight"] for u,v,d in Gs.edges(data=True) if u in cs and v in cs); ext=sum(d["weight"] for u,v,d in Gs.edges(data=True) if (u in cs)!=(v in cs))
    dens=inn/max(1,len(cs)); cen=ext
    cw.append(dict(comunidad=ci,n_palabras=len(cs),densidad=round(dens,2),centralidad=int(cen),palabras=", ".join(sorted(cs,key=lambda n:-occ[n])[:12])))
pd.DataFrame(cw).to_csv(f"{OUT}/red_copalabras_comunidades.csv",index=False,encoding="utf-8-sig")
deg=dict(Gs.degree(weight="weight")); bet=nx.betweenness_centrality(Gs) if Gs.number_of_nodes() else {}
pd.DataFrame([dict(palabra=n,frecuencia=occ[n],grado_ponderado=deg[n],intermediacion=round(bet.get(n,0),4)) for n in sorted(Gs,key=lambda n:-occ[n])]).to_csv(f"{OUT}/red_copalabras_nodos.csv",index=False,encoding="utf-8-sig")
def authors(m):
    full=m.get("autores_completos") or ""
    if full: return [re.sub(r"\s*\(\d+\)\s*$","",a.strip()) for a in full.split(";") if a.strip()]
    return [a.strip() for a in (m.get("autores") or "").split(";") if a.strip()]
GA=nx.Graph(); aut_docs=collections.defaultdict(set)
for i in ids:
    if "D087"<=i<="D098" or i in ("D100","D101"): continue
    au=authors(inv[i]["meta"])
    for a in au: aut_docs[a].add(i); GA.add_node(a)
    for a,b in itertools.combinations(au,2): GA.add_edge(a,b)
compo=sorted(nx.connected_components(GA),key=len,reverse=True)
big=[c for c in compo if len(c)>2]
pd.DataFrame([dict(componente=n,n_autores=len(c),n_documentos=len(set().union(*[aut_docs[a] for a in c])),ejemplos="; ".join(sorted(c)[:4])) for n,c in enumerate(big[:25])]).to_csv(f"{OUT}/red_coautoria_componentes.csv",index=False,encoding="utf-8-sig")
multi=[(a,len(d)) for a,d in aut_docs.items() if len(d)>=2]
pd.DataFrame(sorted(multi,key=lambda x:-x[1]),columns=["autor","n_documentos"]).to_csv(f"{OUT}/red_coautoria_autores_repetidos.csv",index=False,encoding="utf-8-sig")
# ---- bibliometría descriptiva
meta=pd.DataFrame([dict(doc_id=i,anio=int(inv[i]["meta"].get("anio") or 0),citas=inv[i]["meta"].get("citas_scopus"),fuente=inv[i]["meta"].get("fuente",""),corpus=inv[i]["corpus"]) for i in ids])
bib=dict(docs_por_anio=meta[meta.anio>0].groupby("anio").size().to_dict(),fuentes_top=meta.groupby("fuente").size().sort_values(ascending=False).head(12).to_dict(),
         n_autores_unicos=len(aut_docs),autores_con_2plus_docs=len(multi),componentes_coautoria_gt2=len(big),
         n_nodos_copalabras=Gs.number_of_nodes(),n_aristas_copalabras=Gs.number_of_edges(),n_comunidades=len(comm),modularidad=round(nx.algorithms.community.modularity(Gs,comm,weight="weight"),4) if comm else None)
cit=meta.dropna(subset=["citas"]).sort_values("citas",ascending=False); cit["acum"]=cit["citas"].cumsum()/cit["citas"].sum()
bib["pareto_citas_80pct_docs"]=int((cit["acum"]<=0.8).sum()+1); bib["n_docs_con_citas"]=len(cit); bib["citas_total"]=int(cit["citas"].sum())
# ---- figuras ML
colors=plt.cm.tab10.colors
fig,ax=plt.subplots(1,2,figsize=(13,5.5))
for a,(XY,ttl) in zip(ax,[(FULL["P"],"PCA (sobre SVD de TF-IDF)"),(FULL["ts"],"t-SNE (coseno)")]):
    for c in range(FULL["res"]["kbest"]):
        m=FULL["lab_km"]==c; a.scatter(XY[m,0],XY[m,1],s=38,color=colors[c%10],label=f"k-means {c}",alpha=.85,edgecolor="k",linewidth=.3)
    for n,i in enumerate(ids):
        if "D087"<=i<="D098": a.scatter(XY[n,0],XY[n,1],s=90,facecolors="none",edgecolors="red",linewidth=1)
    a.set_title(ttl); a.set_xticks([]); a.set_yticks([])
ax[0].legend(fontsize=7,ncol=2,loc="best")
fig.suptitle("Mapa de documentos por contenido (círculos rojos: bloque SciELO D087-D098)")
plt.tight_layout(); plt.savefig(f"{FIG}/fig_ml_pca_tsne.png",dpi=150); plt.savefig(f"{FIG}/fig_ml_pca_tsne.svg"); plt.close()
# dendrograma
from scipy.cluster.hierarchy import linkage, dendrogram
Lk=linkage(FULL["Z"],method="ward"); fig,ax=plt.subplots(figsize=(15,5)); dendrogram(Lk,labels=ids,leaf_font_size=6,ax=ax,color_threshold=0.0); ax.set_title("Dendrograma jerárquico (Ward) de los 101 documentos"); plt.tight_layout(); plt.savefig(f"{FIG}/fig_ml_dendrograma.png",dpi=150); plt.savefig(f"{FIG}/fig_ml_dendrograma.svg"); plt.close()
# red de co-palabras
if Gs.number_of_nodes():
    pos=nx.spring_layout(Gs,seed=SEED,weight="weight",k=0.9); fig,ax=plt.subplots(figsize=(13,10))
    cmap={}
    for ci,cs in enumerate(comm):
        for n in cs: cmap[n]=colors[ci%10]
    nx.draw_networkx_edges(Gs,pos,alpha=.15,width=[0.2+0.3*Gs[u][v]["weight"] for u,v in Gs.edges()],ax=ax)
    nx.draw_networkx_nodes(Gs,pos,node_size=[40+40*occ[n] for n in Gs],node_color=[cmap[n] for n in Gs],alpha=.85,ax=ax)
    nx.draw_networkx_labels(Gs,pos,labels={n:n for n in Gs if occ[n]>=5},font_size=7,ax=ax); ax.set_title("Red de co-palabras clave (frecuencia ≥ 3)"); ax.axis("off")
    plt.tight_layout(); plt.savefig(f"{FIG}/fig_red_copalabras.png",dpi=150); plt.savefig(f"{FIG}/fig_red_copalabras.svg"); plt.close()
# diagrama estratégico (centralidad-densidad)
if cw:
    d=pd.DataFrame(cw); fig,ax=plt.subplots(figsize=(8,6.5)); ax.scatter(d.centralidad,d.densidad,s=d.n_palabras*25,alpha=.6,color=[colors[i%10] for i in d.comunidad],edgecolor="k")
    for _,r in d.iterrows(): ax.annotate(f"C{int(r.comunidad)}: "+r.palabras.split(", ")[0],(r.centralidad,r.densidad),fontsize=8,xytext=(4,4),textcoords="offset points")
    ax.axvline(d.centralidad.median(),ls="--",c="gray"); ax.axhline(d.densidad.median(),ls="--",c="gray")
    ax.set_xlabel("Centralidad (enlaces externos ponderados)"); ax.set_ylabel("Densidad (enlaces internos por palabra)"); ax.set_title("Mapa estratégico centralidad-densidad (comunidades de palabras clave)")
    plt.tight_layout(); plt.savefig(f"{FIG}/fig_mapa_centralidad_densidad.png",dpi=150); plt.savefig(f"{FIG}/fig_mapa_centralidad_densidad.svg"); plt.close()
# Pareto de citas
fig,ax=plt.subplots(figsize=(12,5)); ax.bar(range(len(cit)),cit["citas"],color="#4c78a8"); ax2=ax.twinx(); ax2.plot(range(len(cit)),cit["acum"]*100,color="#e45756"); ax2.axhline(80,ls="--",c="gray")
ax.set_xlabel("Documentos ordenados por citas (Scopus)"); ax.set_ylabel("Citas"); ax2.set_ylabel("% acumulado"); ax.set_title("Pareto de citas: {} documentos concentran 80 % de las citas".format(bib["pareto_citas_80pct_docs"])); plt.tight_layout(); plt.savefig(f"{FIG}/fig_pareto_citas.png",dpi=150); plt.savefig(f"{FIG}/fig_pareto_citas.svg"); plt.close()
# producción anual
yy=meta[(meta.anio>0)].groupby("anio").size(); fig,ax=plt.subplots(figsize=(9,4)); ax.bar(yy.index.astype(str),yy.values,color="#59a14f"); ax.set_title("Documentos por año de publicación (n=101)"); plt.tight_layout(); plt.savefig(f"{FIG}/fig_produccion_anual.png",dpi=150); plt.savefig(f"{FIG}/fig_produccion_anual.svg"); plt.close()
summary=dict(completo=FULL["res"],sin_SciELO=SENS["res"],sin_SciELO_ni_sintesis=SENS2["res"],sensibilidad=sens,bibliometria=bib,
             kmeans_terminos=FULL["top"],lda_terminos=FULL["ltop"],kmeans_terminos_sin_SciELO=SENS["top"],lda_terminos_sin_SciELO=SENS["ltop"])
json.dump(summary,open(f"{OUT}/ml_resumen.json","w"),ensure_ascii=False,indent=1,default=str)
print(json.dumps({k:summary[k] for k in ("completo","sin_SciELO","sensibilidad","bibliometria")},ensure_ascii=False,indent=1,default=str)[:5000])
