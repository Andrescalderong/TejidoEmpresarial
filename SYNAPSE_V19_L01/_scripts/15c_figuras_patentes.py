"""Figuras del módulo de patentes: frecuencias de términos por 1.000 palabras leídas y relaciones con el corpus."""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from synlib import L
import pandas as pd, numpy as np
import matplotlib; matplotlib.use("Agg"); matplotlib.rcParams["svg.fonttype"]="none"
import matplotlib.pyplot as plt

def heat(ax,Z,cmap,vmin=None,vmax=None):
    """mapa de calor vectorial (celdas editables en SVG)"""
    Z=np.ma.masked_invalid(Z); im=ax.pcolormesh(np.arange(Z.shape[1]+1)-0.5,np.arange(Z.shape[0]+1)-0.5,Z,cmap=cmap,vmin=vmin,vmax=vmax,edgecolors="face",linewidth=0.3)
    ax.set_xlim(-0.5,Z.shape[1]-0.5); ax.set_ylim(Z.shape[0]-0.5,-0.5); return im

C = f"{L}/patentes/csv"; F = f"{L}/figuras"
t = pd.read_csv(f"{C}/patentes_terminos.csv"); inv = pd.read_csv(f"{C}/patentes_inventario.csv"); rel = pd.read_csv(f"{C}/patentes_relaciones.csv")
cols = [("digital twin", "Gemelo digital"), ("sensor", "Sensor"), ("machine learning", "Aprendizaje automático"), ("blockchain/smart contract", "Cadena de bloques / contrato inteligente"),
        ("disruption", "Interrupción"), ("resilience", "Resiliencia"), ("disaster", "Desastre"), ("natural hazard (flood,hurricane,storm)", "Amenaza natural"), ("earthquake/seismic", "Sismo")]
M = np.array([[r[c] / r["palabras"] * 1000 for c, _ in cols] for _, r in t.iterrows()])
fig, ax = plt.subplots(figsize=(10, 5.2))
im = heat(ax, M, "YlGnBu", 0)
ax.set_xticks(range(len(cols))); ax.set_xticklabels([n for _, n in cols], rotation=30, ha="right", fontsize=8)
ax.set_yticks(range(len(t))); ax.set_yticklabels([f"{d} ({c})" for d, c in zip(t.doc_id, inv.numero)], fontsize=8)
for i in range(M.shape[0]):
    for j in range(M.shape[1]): ax.text(j, i, f"{M[i,j]:.2f}" if M[i, j] else "0", ha="center", va="center", fontsize=7, color="white" if M[i, j] > M.max() * 0.55 else "black")
ax.set_title("Frecuencia de términos por 1.000 palabras en las páginas leídas de cada patente", fontsize=10)
fig.colorbar(im, ax=ax, fraction=0.03, label="apariciones por 1.000 palabras"); fig.tight_layout(); fig.savefig(f"{F}/fig_patentes_terminos.png",dpi=150); fig.savefig(f"{F}/fig_patentes_terminos.svg"); plt.close(fig)

# relaciones patentes -> documentos del corpus y entre patentes
col = {"CONFIRMA": "#2ca02c", "COMPLEMENTA": "#888888", "CONTRADICE": "#d62728", "EXTIENDE": "#1f77b4", "DEPENDE_DE": "#9467bd"}
docs = sorted({d for d in rel.documento_relacionado if d.startswith("D")})
pats = list(inv.doc_id)
ypat = {p: i for i, p in enumerate(pats)}; ydoc = {d: i * (len(pats) - 1) / max(1, len(docs) - 1) for i, d in enumerate(docs)}
fig, ax = plt.subplots(figsize=(9, 7))
colr = {"Adyacente": "#ff7f0e", "Periférico": "#1f77b4"}
for r in rel.itertuples():
    if r.documento_relacionado.startswith("D"):
        ax.plot([0, 1], [ypat[r.doc_id], ydoc[r.documento_relacionado]], color=col[r.tipo_relacion], lw=1.3, alpha=.8)
    else:
        a, b = ypat[r.doc_id], ypat[r.documento_relacionado]; ax.annotate("", xy=(-0.05, b), xytext=(-0.05, a), arrowprops=dict(arrowstyle="-", color=col[r.tipo_relacion], lw=1, connectionstyle="arc3,rad=-0.35", alpha=.6))
for p, rv in zip(inv.doc_id, inv.relevancia): ax.scatter(0, ypat[p], s=140, color=colr[rv], zorder=3); ax.text(-0.04, ypat[p], p, ha="right", va="center", fontsize=8)
for d in docs: ax.scatter(1, ydoc[d], s=90, color="#2b8a3e", zorder=3); ax.text(1.03, ydoc[d], d, ha="left", va="center", fontsize=8)
ax.set_xlim(-0.35, 1.2); ax.set_ylim(len(pats), -1); ax.axis("off")
import matplotlib.lines as ml
ax.legend(handles=[ml.Line2D([], [], color=c, label=k) for k, c in col.items() if k in set(rel.tipo_relacion)] + [ml.Line2D([], [], marker="o", ls="", color=colr[k], label=f"Patente {k.lower()}") for k in colr],
          loc="lower center", ncol=3, fontsize=8, frameon=False, bbox_to_anchor=(0.5, -0.02))
ax.set_title("Relaciones tipificadas entre las patentes (izquierda) y los documentos del corpus (derecha)", fontsize=10)
fig.tight_layout(); fig.savefig(f"{F}/fig_patentes_relaciones.png",dpi=150); fig.savefig(f"{F}/fig_patentes_relaciones.svg"); plt.close(fig)
print("figuras de patentes generadas")
