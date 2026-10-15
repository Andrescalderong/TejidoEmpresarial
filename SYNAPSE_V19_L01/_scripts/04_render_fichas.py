"""Renderiza fichas FBA + analisis SYNAPSE por documento -> fichas/D###_slug.md"""
import sys, os
sys.path.insert(0,os.path.dirname(__file__))
from synlib import *
def S(x): return (x or "").strip()
def bullets(lst): return "\n".join(f"{i+1}. {S(x)}" for i,x in enumerate(lst))
def render(d, a, conns):
    m=d["meta"]; did=d["doc_id"]; fb=f"FB-L01-{did[1:]}"
    c2,c3=a["c2"],a["c3"]; mad=a["madurez"]
    g,crit,critv=gaps(a); sr=srl_calc(mad.get("srl"))
    kw_decl = m.get("kw_autor") or "No declaradas / no disponibles en el registro"
    o=[]
    o.append(f"# {fb} | {did} — {m.get('titulo','')}\n")
    o.append(f"> Corpus de origen: **{d['corpus']}** · Archivo: `{d['path']}` · {d['pages']} páginas · Relevancia para el eje del corpus: **{a['relevancia']}** ({a.get('relevancia_just','')})\n")
    if d.get("copias_duplicadas"): o.append(f"> Copia idéntica (MD5) en: {', '.join('`'+p+'`' for p in d['copias_duplicadas'])}\n")
    o.append("## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)\n")
    o.append("### Capa 1 — Núcleo bibliográfico\n")
    o.append(f"- **FB_ID / DOC_ID:** {fb} / {did}\n- **Tipo de recurso:** {a['tipo_recurso']}\n- **Referencia APA 7:** {apa_ref(d)}\n- **Autores:** {m.get('autores_completos') or m.get('autores','No especificado')}\n- **Afiliaciones:** {S(m.get('afiliaciones','')) or 'No especificado en el registro'}\n- **Fecha de publicación:** {m.get('anio','')}\n- **Fuente/contenedor:** {m.get('fuente','')}{(' · vol. '+m['volumen']) if m.get('volumen') else ''}{('('+m['numero']+')') if m.get('numero') else ''}\n- **Identificador persistente:** {('DOI '+m['doi']) if m.get('doi') else 'No disponible'}{(' · ISSN '+m['issn']) if m.get('issn') else ''}\n- **URL de acceso:** {m.get('link') or 'No especificada'}\n- **Fecha de consulta:** {FECHA}\n- **Citas Scopus (a la fecha del export):** {m.get('citas_scopus','No aplica')}\n")
    o.append("### Capa 2 — Extracción metodológica\n")
    for k,t in [("objetivo","Objetivo de la investigación"),("pregunta","Pregunta de investigación"),("marco","Marco teórico"),("metodologia","Metodología"),("resultados","Resultados principales"),("discusion","Discusión y contribución"),("limitaciones","Limitaciones declaradas"),("futuro","Trabajo futuro")]:
        o.append(f"**{t}.** {S(c2[k])}\n")
    o.append(f"**Palabras clave.** Declaradas: {kw_decl} | Inferidas: {', '.join(a['kw_inferidas'])}\n")
    o.append("### Capa 3 — Abstracción propositiva\n")
    o.append(f"**Tesis central (abstraída).** {S(c3['tesis'])}\n")
    o.append(f"**Antítesis identificada.** {S(c3['antitesis'])}\n")
    o.append(f"**Síntesis propuesta.** {S(c3['sintesis'])}\n")
    o.append("**Áreas grises detectadas.**\n\n"+bullets(c3["areas_grises"])+"\n")
    o.append(f"**Puntos oscuros aclarados.** {S(c3['puntos_oscuros'])}\n")
    o.append("**Ideas propositivas novedosas.**\n\n"+bullets(c3["ideas"])+"\n")
    o.append("**Relaciones poco exploradas.**\n\n"+bullets(c3["relaciones"])+"\n")
    r=c3["robustez"]; glob_r=round(0.3*r[0]+0.3*r[1]+0.25*r[2]+0.15*r[3],1)
    o.append(f"**Robustez argumentativa:** {glob_r}/10 (ponderación 30/30/25/15) — consistencia lógica {r[0]}/10; calidad de la evidencia {r[1]}/10; validez de inferencias causales {r[2]}/10; generalizabilidad {r[3]}/10.\n")
    o.append(f"**Valor estratégico:** {c3['valor'][0]}/10 — {S(c3['valor'][1])}\n")
    cl=conns.get(did,[])
    o.append("**Conexiones inter-documentales.**\n\n"+("\n".join(f"- {x}" for x in cl) if cl else "- (Se completan en el Análisis Relacional de la Parte final del lote.)")+"\n")
    o.append("### Capa 4 — Control de calidad\n")
    fal="; ".join(f"{f[0]} ({f[1]})" for f in a["falacias"]) or "Ninguna detectada"
    o.append(f"- **Falacias detectadas:** {fal}\n- **Bradford-Hill:** {S(a['bradford'])}\n- **TRL asignado:** {mad['trl'][0] if mad['trl'][0] is not None else 'N/A'} — {mad['trl'][1]}\n- **Versión de ficha:** v1.0 | {FECHA} | SYNAPSE V19.0\n- **Notas de proceso:** {S(a.get('notas','')) or 'Sin observaciones'}\n")
    o.append("---\n\n## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO\n")
    o.append("### B.1 Análisis dialéctico\n\n| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |\n|---|---|---|---|\n"+f"| {esc(c3['tesis'])} | {esc(c3['antitesis'])} | {esc(c3['sintesis'])} | {glob_r}/10 |\n")
    o.append("### B.2 Interrogación socrática\n")
    so=a["socratica"]
    for k,t in [("p1","P1 Definición"),("p2","P2 Supuestos"),("p3","P3 Evidencia"),("p4","P4 Consecuencias"),("p5","P5 Contraejemplos"),("p6","P6 Alternativas")]:
        o.append(f"- **{t}:** {S(so[k])}")
    o.append("\n### B.3 KPIs extraídos\n\n| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |\n|---|---|---|---|---|---|---|---|")
    for k in a["kpis"]: o.append("| "+" | ".join(esc(x) for x in k)+" |")
    o.append("\n### B.4 Evaluación multinivel de madurez\n\n| Dimensión | Score | Aplica | Evidencia | Justificación |\n|---|---|---|---|---|")
    t=mad["trl"]; o.append(f"| TRL | {t[0] if t[0] is not None else 'N/A'} | {'Sí' if t[0] is not None else 'No'} | {esc(t[1])} | {esc(t[2])} |")
    x=mad["mrl"]; o.append(f"| MRL | {x[1] if x[0] else 'N/A'} | {'Sí' if x[0] else 'No'} | {esc(x[2])} | {esc(x[3])} |")
    t=mad["brl"]; o.append(f"| BRL | {t[0] if t[0] is not None else 'N/A'} | {'Sí' if t[0] is not None else 'No'} | {esc(t[1])} | {esc(t[2])} |")
    x=mad["irl"]; o.append(f"| IRL | {x[1] if x[0] else 'N/A'} | {'Sí' if x[0] else 'No'} | {esc(x[2])} | {esc(x[3])} |")
    x=mad["drl"]; o.append(f"| DRL | {x[1] if x[0] else 'N/A'} | {'Sí' if x[0] else 'No'} | {esc(x[2])} | {esc(x[3]) if len(x)>3 else ''} |")
    o.append(f"| SRL | {sr['nivel'] if sr else 'N/A'} | {'Sí' if sr else 'No'} | {'Componentes: '+', '.join(f'{c[0]} (TRL {c[1]})' for c in mad['srl']['componentes']) if sr else 'Requiere IRL entre componentes'} | {esc(sr['formula']) if sr else 'No calculable sin IRL'} |")
    o.append("\n**Análisis de brechas**\n\n| Brecha | Valor | Interpretación |\n|---|---|---|")
    def interp(v,pos,neg):
        if v is None: return "N/A"
        return pos if v>=3 else (neg if v<=-3 else "Desarrollo relativamente balanceado (|brecha|<3)")
    o.append(f"| Gap TRL-BRL | {g['TB']} | {interp(g['TB'],'TRL >> BRL: tecnología sin mercado (riesgo comercial)','BRL >> TRL: demanda sin solución técnica')} |")
    o.append(f"| Gap TRL-MRL | {g['TM'] if g['TM'] is not None else 'N/A'} | {interp(g['TM'],'TRL >> MRL: tecnología no escalable','MRL >> TRL: capacidad sin tecnología definida')} |")
    o.append(f"| Gap TRL-IRL | {g['TI'] if g['TI'] is not None else 'N/A'} | {interp(g['TI'],'Componentes listos, integración inmadura','IRL >> TRL')} |")
    o.append(f"| Gap BRL-DRL | {g['BD'] if g['BD'] is not None else 'N/A'} | {interp(g['BD'],'Más capacidad comercial que demanda','Demanda mayor que capacidad de servir')} |")
    o.append(f"| Brecha crítica | {critv if critv is not None else 'N/A'} | {crit} |")
    v=a["valle"]
    o.append(f"\n**Valle de la muerte:** {VALLES[v[0]]} · Severidad: {v[2]} · {S(v[1])} · Estrategia de salida: {S(v[3])}\n")
    o.append("### B.5 Robustez argumentativa y causalidad\n\n| Falacia | Evidencia | Impacto |\n|---|---|---|")
    for f in a["falacias"]: o.append("| "+" | ".join(esc(y) for y in f)+" |")
    if not a["falacias"]: o.append("| Ninguna detectada | — | — |")
    o.append(f"\n**Recomendación:** {a['recomendacion']}\n\n| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |\n|---|---|---|---|---|---|---|")
    for c in a["causal"]: o.append("| "+" | ".join(esc(y) for y in c)+" |")
    o.append("\n### B.6 Gaps identificados\n\n| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |\n|---|---|---|---|---|")
    for q in a["gaps"]: o.append("| "+" | ".join(esc(y) for y in q)+" |")
    o.append("\n### B.7 Figuras y tablas clave\n\n| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |\n|---|---|---|---|---|---|")
    for q in a["figuras"]: o.append("| "+" | ".join(esc(y) for y in q)+" |")
    o.append("\n### B.8 Competidores / actores / alternativas tecnológicas\n\n| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |\n|---|---|---|---|---|---|---|")
    for q in a["competidores"]: o.append("| "+" | ".join(esc(y) for y in q)+" |")
    e=a["econ"]
    o.append(f"\n### B.9 Variables econométricas y vacíos\n\n- **Y:** {e['Y']}\n- **X:** {e['X']}\n- **Z (controles):** {e['Z']}\n- **Datos:** {e['datos']}\n- **Método:** {e['metodo']}\n- **Efecto reportado:** {e['efecto']}\n- **Endogeneidad tratada:** {e['endogeneidad']}\n- **Instrumento:** {e['instrumento']}\n- **Robustez reportada:** {e['robustez']}\n")
    o.append("| Vacío | Tipo | Descripción |\n|---|---|---|")
    for i,q in enumerate(a["vacios"]): o.append(f"| V-{did[1:]}-{i+1:02d} | {q[0]} | {esc(q[1])} |")
    return "\n".join(o)+"\n"
if __name__=="__main__":
    inv={d["doc_id"]:d for d in load_inv()}; A=load_docs()
    cf=f"{BASE}/conexiones.json"; conns=json.load(open(cf)) if os.path.exists(cf) else {}
    os.makedirs(f"{L}/fichas",exist_ok=True)
    for did,a in A.items():
        d=inv[did]; fn=f"{L}/fichas/{did}_{slug(d['meta'].get('titulo','doc'))}.md"
        open(fn,"w").write(render(d,a,conns))
    print(len(A),"fichas renderizadas")
