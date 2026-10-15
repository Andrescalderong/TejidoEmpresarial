"""Figuras de madurez (matriz, radar, mapa de calor de brechas, diagrama de valles), red de relaciones y diagramas Mermaid."""
import sys, os, json, statistics, collections
sys.path.insert(0, os.path.dirname(__file__))
from synlib import *
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); matplotlib.rcParams["svg.fonttype"]="none"
import matplotlib.pyplot as plt

def heat(ax,Z,cmap,vmin=None,vmax=None):
    """mapa de calor vectorial (celdas editables en SVG)"""
    Z=np.ma.masked_invalid(Z); im=ax.pcolormesh(np.arange(Z.shape[1]+1)-0.5,np.arange(Z.shape[0]+1)-0.5,Z,cmap=cmap,vmin=vmin,vmax=vmax,edgecolors="face",linewidth=0.3)
    ax.set_xlim(-0.5,Z.shape[1]-0.5); ax.set_ylim(Z.shape[0]-0.5,-0.5); return im

from matplotlib.colors import ListedColormap
import networkx as nx
A=load_docs(); inv={d["doc_id"]:d for d in load_inv()}; FIG=f"{L}/figuras"; os.makedirs(FIG,exist_ok=True)
mm=pd.read_csv(f"{L}/csv/madurez_multinivel.csv").set_index("doc_id"); bg=pd.read_csv(f"{L}/csv/brechas_madurez.csv").set_index("doc_id")
order={"Núcleo":0,"Adyacente":1,"Periférico":2,"Ajeno":3}
tech=[i for i in sorted(A) if not (i>="D087" and i<="D098") and i not in ("D003","D012","D085","D100","D101") ] # documentos con al menos TRL o BRL asignado se filtran abajo
tech=[i for i in tech if not (pd.isna(mm.loc[i,"TRL"]) and pd.isna(mm.loc[i,"BRL"]))]
tech=sorted(tech,key=lambda i:(order[A[i]["relevancia"]],i))
cols=["TRL","MRL","BRL","IRL","DRL","SRL_nivel"]
M=mm.loc[tech,cols].astype(float).values
# 1) matriz de madurez
fig,ax=plt.subplots(figsize=(7.5,max(8,0.17*len(tech)+2)))
cmap=plt.cm.YlGnBu.copy(); cmap.set_bad("#eeeeee")
im=heat(ax,M,cmap,1,9)
ax.set_xticks(range(len(cols))); ax.set_xticklabels(["TRL","MRL","BRL","IRL","DRL","SRL"]); ax.set_yticks(range(len(tech))); ax.set_yticklabels([f"{i} ({A[i]['relevancia'][0]})" for i in tech],fontsize=5)
for r in range(M.shape[0]):
    for c in range(M.shape[1]):
        if not np.isnan(M[r,c]): ax.text(c,r,f"{M[r,c]:.0f}" if c<5 else f"{M[r,c]:.1f}",ha="center",va="center",fontsize=5,color="white" if M[r,c]>6 else "black")
ax.set_title(f"Matriz de madurez multinivel (n={len(tech)} documentos con TRL o BRL)\nN=núcleo, A=adyacente, P=periférico; gris = no aplica/no evaluable",fontsize=8)
plt.colorbar(im,ax=ax,fraction=0.03); plt.tight_layout(); plt.savefig(f"{FIG}/fig_matriz_madurez.png",dpi=170); plt.savefig(f"{FIG}/fig_matriz_madurez.svg"); plt.close()
# 2) radar por grupo de relevancia (medianas)
labels=["TRL","BRL","IRL","DRL","SRL"]; ang=np.linspace(0,2*np.pi,len(labels),endpoint=False).tolist(); ang+=ang[:1]
fig,ax=plt.subplots(figsize=(6.5,6.5),subplot_kw=dict(polar=True)); col={"Núcleo":"#d62728","Adyacente":"#1f77b4","Periférico":"#2ca02c"}
tabla=[]
for g in ("Núcleo","Adyacente","Periférico"):
    ids=[i for i in tech if A[i]["relevancia"]==g]
    med=[]
    for c in ["TRL","BRL","IRL","DRL","SRL_nivel"]:
        v=mm.loc[ids,c].dropna().astype(float).values; med.append(float(np.median(v)) if len(v) else 0.0)
    tabla.append(dict(grupo=g,n=len(ids),TRL=med[0],BRL=med[1],IRL=med[2],DRL=med[3],SRL=med[4]))
    ax.plot(ang,med+med[:1],color=col[g],label=f"{g} (n={len(ids)})"); ax.fill(ang,med+med[:1],color=col[g],alpha=.12)
ax.set_xticks(ang[:-1]); ax.set_xticklabels(labels); ax.set_ylim(0,9); ax.set_title("Perfil de madurez: mediana por grupo de relevancia",fontsize=10); ax.legend(loc="lower right",bbox_to_anchor=(1.2,0),fontsize=8)
plt.tight_layout(); plt.savefig(f"{FIG}/fig_radar_madurez.png",dpi=170); plt.savefig(f"{FIG}/fig_radar_madurez.svg"); plt.close()
pd.DataFrame(tabla).to_csv(f"{L}/csv/ml/madurez_medianas_por_grupo.csv",index=False,encoding="utf-8-sig")
# 3) mapa de calor de brechas
gcols=["gap_TRL_BRL","gap_TRL_IRL","gap_BRL_DRL"]
G=bg.loc[tech,gcols].astype(float).values
fig,ax=plt.subplots(figsize=(5.5,max(8,0.17*len(tech)+2)))
im=heat(ax,G,"RdBu_r",-4,6)
ax.set_xticks(range(3)); ax.set_xticklabels(["TRL−BRL","TRL−IRL","BRL−DRL"]); ax.set_yticks(range(len(tech))); ax.set_yticklabels(tech,fontsize=5)
for r in range(G.shape[0]):
    for c in range(3):
        if not np.isnan(G[r,c]): ax.text(c,r,f"{G[r,c]:.0f}",ha="center",va="center",fontsize=5)
ax.set_title("Brechas de madurez por documento\n(rojo: tecnología por delante del negocio o la integración)",fontsize=8); plt.colorbar(im,ax=ax,fraction=0.05)
plt.tight_layout(); plt.savefig(f"{FIG}/fig_mapa_calor_brechas.png",dpi=170); plt.savefig(f"{FIG}/fig_mapa_calor_brechas.svg"); plt.close()
# 4) diagrama de valles: TRL vs BRL con tamaño por frecuencia + barras por valle y severidad
pts=collections.Counter((int(mm.loc[i,"TRL"]),int(mm.loc[i,"BRL"])) for i in tech if not pd.isna(mm.loc[i,"TRL"]) and not pd.isna(mm.loc[i,"BRL"]))
fig,ax=plt.subplots(1,2,figsize=(13,5.5))
ax[0].fill_between([1,9],[-1,-1],[-1,7],color="#f4cccc",alpha=.6,label="Valle comercial (TRL−BRL ≥ 2)")
for (t,b),n in pts.items(): ax[0].scatter(t,b,s=60*n,color="#1f77b4",alpha=.65,edgecolor="k")
for (t,b),n in pts.items():
    if n>=4: ax[0].annotate(str(n),(t,b),ha="center",va="center",color="white",fontsize=8)
ax[0].plot([1,9],[1,9],"k--",lw=.8); ax[0].set_xlim(1,9); ax[0].set_ylim(0.5,6); ax[0].set_xlabel("TRL (nivel modal del documento o del campo)"); ax[0].set_ylabel("BRL"); ax[0].set_title("Valle de la muerte comercial: TRL frente a BRL"); ax[0].legend(fontsize=7,loc="upper left")
vc=collections.defaultdict(lambda:collections.Counter())
for i in A: vc[A[i]["valle"][0]][A[i]["valle"][2]]+=1
names=[VALLES[k] for k in sorted(vc)]; bottoms=np.zeros(len(vc))
for sev,c in (("Baja","#8fd694"),("Media","#f7c873"),("Alta","#e06666")):
    vals=np.array([vc[k][sev] for k in sorted(vc)]); ax[1].barh(names,vals,left=bottoms,color=c,label=sev); bottoms+=vals
ax[1].set_title("Documentos por valle de la muerte y severidad (n=101)"); ax[1].legend(); ax[1].tick_params(axis="y",labelsize=7)
plt.tight_layout(); plt.savefig(f"{FIG}/fig_diagrama_valles.png",dpi=170); plt.savefig(f"{FIG}/fig_diagrama_valles.svg"); plt.close()
# 5) red de relaciones entre documentos (sin D100 ni aristas de citación a D100)
E=pd.read_csv(f"{L}/csv/analisis_relacional.csv")
E=E[(E.origen!="D100")&(E.destino!="D100")&(E.tipo.isin(["CONFIRMA","CONTRADICE","COMPLEMENTA","EXTIENDE","DEPENDE_DE"]))]
Gr=nx.Graph(); colr={"CONFIRMA":"#2ca02c","CONTRADICE":"#d62728","COMPLEMENTA":"#7f7f7f","EXTIENDE":"#1f77b4","DEPENDE_DE":"#9467bd"}
for r in E.itertuples(): Gr.add_edge(r.origen,r.destino,tipo=r.tipo)
pos=nx.spring_layout(Gr,seed=42,k=0.55); fig,ax=plt.subplots(figsize=(13,10))
for t,c in colr.items():
    ee=[(u,v) for u,v,d in Gr.edges(data=True) if d["tipo"]==t]; nx.draw_networkx_edges(Gr,pos,edgelist=ee,edge_color=c,width=1.5 if t!="COMPLEMENTA" else .8,alpha=.7,ax=ax,label=t)
rc={"Núcleo":"#d62728","Adyacente":"#1f77b4","Periférico":"#2ca02c","Ajeno":"#aaaaaa"}
nx.draw_networkx_nodes(Gr,pos,node_color=[rc[A[n]["relevancia"]] for n in Gr],node_size=[60+25*Gr.degree(n) for n in Gr],ax=ax,alpha=.9)
nx.draw_networkx_labels(Gr,pos,font_size=6,ax=ax); ax.legend(fontsize=8,loc="lower left"); ax.set_title("Red de relaciones tipificadas entre documentos (color del nodo = relevancia; excluye la síntesis D100)"); ax.axis("off")
plt.tight_layout(); plt.savefig(f"{FIG}/fig_red_relaciones.png",dpi=160); plt.savefig(f"{FIG}/fig_red_relaciones.svg"); plt.close()
cent=pd.DataFrame([dict(doc_id=n,grado=Gr.degree(n),intermediacion=round(b,4)) for n,b in nx.betweenness_centrality(Gr).items()]).sort_values("grado",ascending=False)
cent.to_csv(f"{L}/csv/ml/red_relaciones_centralidad.csv",index=False,encoding="utf-8-sig")
# 6) Mermaid
nucleo=[i for i in sorted(A) if A[i]["relevancia"]=="Núcleo"]
lines=["```mermaid","graph LR"]
for i in nucleo: lines.append(f'  {i}["{i}: {inv[i]["meta"].get("titulo","")[:44].replace(chr(34),"")}"]')
Es=E[E.origen.isin(nucleo)&E.destino.isin(nucleo)&(E.origen<E.destino)]
arrow={"CONFIRMA":"-->|confirma|","CONTRADICE":"-.->|contradice|","COMPLEMENTA":"---|complementa|","EXTIENDE":"==>|extiende|","DEPENDE_DE":"-->|depende de|"}
for r in Es.itertuples(): lines.append(f"  {r.origen} {arrow[r.tipo]} {r.destino}")
lines.append("```")
flow=["```mermaid","flowchart TD","  A[\"101 documentos únicos\\n(103 PDF; 2 duplicados MD5)\"] --> B[\"Texto limpio\\n(pdftotext)\"]","  B --> C[\"Lectura completa y YAML por documento\\n(validación de mínimos)\"]","  C --> D[\"101 fichas de 4 capas\"]","  B --> E[\"TF-IDF, k-means, jerárquico,\\nDBSCAN, LDA, PCA, t-SNE\"]","  C --> F[\"19 CSV y matrices\"]","  E --> G[\"Sensibilidad con y sin bloque SciELO\"]","  F --> H[\"Triangulación, patrones y tensiones\"]","  D --> I[\"Relaciones tipificadas\\n(citación verificada y juicio)\"]","  I --> J[\"Análisis relacional y proposiciones emergentes\"]","  G --> K[\"Informe del lote y FICHA_RESUMEN_LOTE\"]","  H --> K","  J --> K","```"]
val=["```mermaid","flowchart LR","  subgraph Valle[\"Valle de la muerte dominante (V1)\"]","    T[\"TRL mediano 4\"] --> B[\"BRL mediano 2\"]","    T --> I[\"IRL mediano 3\"]","  end","  B --> X[\"Sin costos ni modelos de negocio\"]","  I --> Y[\"Sin interoperabilidad validada\"]","  X --> Z[\"Salida: pilotos con empresas posteriores a sismos\"]","  Y --> Z","```"]
open(f"{L}/informe/diagramas_mermaid.md","w").write("# Diagramas Mermaid del lote L01\n\n## Flujo de proceso\n\n"+"\n".join(flow)+"\n\n## Relaciones entre documentos del núcleo\n\n"+"\n".join(lines)+"\n\n## Estructura del valle de la muerte\n\n"+"\n".join(val)+"\n")
print("figuras:",sorted(os.listdir(FIG)))
print(pd.DataFrame(tabla).to_string())
