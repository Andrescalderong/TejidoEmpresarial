"""Módulo de patentes de SYNAPSE V19.0 (lote L01): fichas, CSV e informe a partir de patentes_data.py y del OCR guardado en patentes/_ocr_texto/.
Ejecutar después de 14_patentes_ocr.py (OCR) y 14b_patentes_terminos.py (frecuencias de términos)."""
import sys, os, json, re, glob, collections
sys.path.insert(0, os.path.dirname(__file__))
from synlib import L, esc, slug, VALLES
import pandas as pd
from patentes_data import P

OUT = f"{L}/patentes"; FD = f"{OUT}/fichas"; CS = f"{OUT}/csv"
for d in (FD, CS): os.makedirs(d, exist_ok=True)
FECHA = "2026-10-15"
KW = json.load(open(f"{OUT}/csv/terminos_crudo.json"))

CITE = {"P002": ("Cella et al.", "2025a"), "P001": ("Cella et al.", "2025b"), "P003": ("Cella y Locke", "2026"), "P004": ("Cella et al.", "2026"),
        "P005": ("Cella et al.", "2022a"), "P006": ("Cella et al.", "2022b"), "P008": ("Cella et al.", "2022c"), "P010": ("Cella et al.", "2022d"),
        "P009": ("Cella et al.", "2022e"), "P007": ("Cella et al.", "2022f"), "P011": ("Berti y DeLuca", "2022")}
def cite(pid, par=True):
    a, y = CITE[pid]; return f"({a}, {y})" if par else f"{a} ({y})"
def ref(p):
    y = CITE[p["id"]][1]
    return f"{p['autores_apa']} ({y}). *{p['titulo']}* ({p['num_apa']}). U.S. Patent and Trademark Office."

def tabla(h, rows):
    s = "| " + " | ".join(h) + " |\n|" + "---|" * len(h) + "\n"
    for r in rows: s += "| " + " | ".join(esc(c) for c in r) + " |\n"
    return s

ORDEN_REF = sorted(P, key=lambda p: (p["autores_apa"].split(",")[0], p["autores_apa"], CITE[p["id"]][1], p["titulo"]))

def madurez(p):
    ev = ("Descripción de arquitectura y de realizaciones ('in embodiments') sin datos de prueba, desempeño ni usuarios en las páginas leídas.")
    return dict(trl=(2, ev, "Concepto tecnológico formulado y descrito (TRL 2 de la escala NASA); el texto no informa de pruebas analíticas ni experimentales que sustenten un nivel superior."),
                mrl=(None, "No aplica", "El documento no evalúa capacidad de manufactura ni producción."),
                brl=(None, "No determinable", "El documento no contiene datos de mercado, ingresos, clientes ni modelo de negocio verificables; la titularidad comercial no equivale a madurez de negocio."),
                irl=(2, "Las reivindicaciones definen interfaces entre capas y componentes (plataforma, aplicaciones, gemelo, sensores).", "Interfaces identificadas y descritas funcionalmente, sin prueba de integración."),
                drl=(2, "Se enumeran fuentes de datos (sensores, interfaces de programación, bases de datos) sin conjuntos de datos reales.", "Fuentes de datos identificadas, sin evidencia de disponibilidad ni calidad."),
                srl=(None, "No calculado", "No hay componentes con TRL y IRL evaluados por separado con evidencia que permitan aplicar la fórmula del analista."))

def vacios(p):
    t = p["titulo"].lower()
    return [("TERR", f"Titularidad y ejemplos en Estados Unidos; sin aplicación documentada en América Latina ni en zonas de alta sismicidad en las páginas leídas ({p['clave']})."),
            ("POBL", "No se describen empresas usuarias, tamaño, sector ni condición de las empresas afectadas por un evento."),
            ("TEMP", "No hay seguimiento longitudinal ni medidas de tiempo de reanudación o recuperación productiva."),
            ("MET", "No se reporta método de evaluación (experimento, caso, comparación con línea base) del sistema reivindicado."),
            ("VAR", "No se miden variables de resultado (ingresos, empleo, tiempo de reanudación, costo de interrupción)."),
            ("TEOR", "No se vincula con teoría de resiliencia organizacional ni de absorción de tecnología."),
            ("CAUS", "No hay diseño causal: la patente asevera funciones del sistema, no efectos medidos.")]

def socratica(p):
    return [("P1 Aclaración", f"¿Qué se reivindica exactamente? {p['reiv_resumen'][:260].rstrip()}…"),
            ("P2 Evidencia", f"¿Qué evidencia respalda la eficacia? {p['evidencia']}"),
            ("P3 Supuestos", f"¿Qué supone el documento sin probarlo? {p['grises'][0]}"),
            ("P4 Implicaciones", f"Si el sistema funcionara como se describe, ¿qué cambiaría para la recuperación productiva de una empresa afectada por un sismo? {p['sintesis'].split('. ')[0]}."),
            ("P5 Contraejemplo", f"¿Qué caso contradice o limita la tesis? {p['antitesis'].split('. ')[0]}."),
            ("P6 Hipótesis rival", f"¿Qué alternativa explicaría igual el resultado o resolvería el mismo problema? {p['comp'][0][0]}: {p['comp'][0][1].lower()}.")]

def kw_rows(p):
    k = KW[p["tag"]]; return k

def ficha(p, n):
    pid = p["id"]; k = KW[p["tag"]]; m = madurez(p)
    cov = f"{k['paginas']} de {p['paginas']} páginas ({100*k['paginas']/p['paginas']:.0f} %)"
    t = f"# FP-L01-{n:03d} | {pid} — {p['titulo']}\n\n"
    t += f"> Corpus de origen: **PATENTES (carpeta `Patentes /`, PDF de Lens.org)** · Archivo: `Patentes /{p['archivo']}` · {p['paginas']} páginas ({p['hojas']} hojas de dibujos) · Relevancia para el eje del corpus: **{p['relevancia']}** ({p['relevancia_just']})\n\n"
    t += "## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0, módulo de patentes)\n\n### Capa 1 — Núcleo bibliográfico\n\n"
    t += "\n".join([f"- **FP_ID / DOC_ID:** FP-L01-{n:03d} / {pid}",
        f"- **Tipo de recurso:** {p['tipo']}",
        f"- **Referencia APA 7:** {ref(p)}",
        f"- **Número:** {p['clave']}",
        f"- **Inventores:** {p['inventores']}",
        f"- **Titular / cesionario:** {p['titular']}",
        f"- **Solicitud:** {p['solicitud']} · presentada el {p['presentacion']}",
        f"- **Fecha del documento:** {p['fecha_doc']}",
        f"- **Publicación previa:** {p['publ_previa']}",
        f"- **Prioridad / familia:** {p['prioridad']}",
        f"- **Clasificación CPC (portada):** {p['cpc']}",
        f"- **Examen y representación:** {p['examen']}",
        f"- **Reivindicaciones:** {p['reiv']} en total; {p['reiv_nota']}",
        f"- **Estado legal:** {'Concedida (código de tipo B2); el registro actual de pagos y vigencia no está en el archivo' if p['clave'].endswith('B2') else 'Solicitud publicada (código A1); el estado posterior (concesión, abandono) no puede verificarse con el archivo'}",
        f"- **Fecha de consulta del archivo:** {FECHA}"]) + "\n\n"
    t += "### Capa 2 — Extracción técnica\n\n"
    t += f"**Objetivo de la invención.** {p['objetivo']}\n\n**Problema técnico.** {p['problema']}\n\n**Solución técnica.** {p['solucion']}\n\n"
    t += f"**Reivindicaciones independientes.** {p['reiv_resumen']}\n\n**Reivindicaciones dependientes.** {p['dependientes']}\n\n"
    t += f"**Evidencia empírica.** {p['evidencia']}\n\n**Sensores y fuentes de datos.** {p['sens']}\n\n**Limitaciones de la lectura.** {p['limites']}\n\n"
    t += "### Capa 3 — Abstracción propositiva\n\n"
    t += f"**Tesis.** {p['tesis']}\n\n**Antítesis.** {p['antitesis']}\n\n**Síntesis.** {p['sintesis']}\n\n**Zonas grises.**\n\n" + "\n".join(f"{i+1}. {g}" for i, g in enumerate(p["grises"])) + "\n\n"
    t += "**Ideas propositivas.**\n\n" + "\n".join(f"{i+1}. {g}" for i, g in enumerate(p["ideas"])) + "\n\n**Relaciones con otros documentos.**\n\n" + "\n".join(f"- **{r[0]}** {r[1]}: {r[2]}" for r in p["relaciones"]) + "\n\n"
    t += "### Capa 4 — Control de calidad\n\n"
    t += f"- **Cobertura de lectura:** {cov} leídas por reconocimiento óptico de caracteres (portada, 33 primeras páginas, una de cada 20 páginas intermedias, últimas 14 páginas con las reivindicaciones). El resto no se leyó.\n"
    t += "- **Confianza:** alta para datos de portada y reivindicaciones; media para la descripción (muestreo); baja para lo no leído.\n"
    t += "- **Advertencias:** los PDF son imágenes sin capa de texto; la lectura óptica puede omitir líneas. Las citas literales se limitan a fragmentos legibles.\n"
    t += f"- **Frecuencias en las páginas leídas:** gemelo digital {k['digital twin']}; sensor {k['sensor']}; aprendizaje automático {k['machine learning']}; cadena de bloques o contrato inteligente {k['blockchain/smart contract']}; sismo {k['earthquake/seismic']}; desastre {k['disaster']}; interrupción {k['disruption']}; resiliencia {k['resilience']}.\n\n"
    t += "## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO\n\n### B.1 Análisis dialéctico\n\n"
    t += tabla(["Momento", "Contenido"], [["Tesis", p["tesis"]], ["Antítesis", p["antitesis"]], ["Síntesis", p["sintesis"]]]) + "\n"
    t += "### B.2 Interrogación socrática\n\n" + "\n".join(f"- **{a}.** {b}" for a, b in socratica(p)) + "\n\n"
    t += "### B.3 Indicadores del documento\n\n"
    t += tabla(["Indicador", "Valor", "Unidad", "Ubicación", "Confianza"],
        [["Páginas del PDF", p["paginas"], "páginas", "Archivo", "Alta"], ["Hojas de dibujos", p["hojas"], "hojas", "Cabecera 'Sheet n of N'", "Alta"],
         ["Reivindicaciones", p["reiv"], "reivindicaciones", "Última página", "Alta"], ["Reivindicaciones independientes", len(p["indep"]), "reivindicaciones", "Reivindicaciones " + ", ".join(map(str, p["indep"])), "Alta"],
         ["Palabras leídas por OCR", k["palabras"], "palabras", "Páginas leídas", "Media"], ["Páginas leídas", k["paginas"], "páginas", "Muestreo", "Alta"]]) + "\n"
    t += "### B.4 Evaluación multinivel de madurez\n\n"
    t += tabla(["Dimensión", "Score", "Aplica", "Evidencia", "Justificación"],
        [[d.upper(), m[d][0] if m[d][0] is not None else "N/A", "Sí" if m[d][0] is not None else "No", m[d][1], m[d][2]] for d in ("trl", "mrl", "brl", "irl", "drl", "srl")]) + "\n"
    t += "**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · El documento describe una solución técnica sin evidencia de aplicación ni de mercado; la clasificación se limita al texto. Estrategia de salida: pruebas de concepto con datos reales y medidas de tiempo de reanudación en empresas afectadas por eventos.\n\n"
    t += "### B.5 Robustez argumentativa y causalidad\n\n"
    t += tabla(["Riesgo de lectura", "Evidencia", "Impacto"],
        [["Inferir eficacia de la concesión o de la publicación", f"{p['tipo']}: la concesión acredita requisitos legales, no desempeño", "Sobrestima la madurez tecnológica"],
         ["Generalizar al dominio sísmico", p["relevancia_just"], "Extrapolación sin respaldo textual"],
         ["Tomar listas de realizaciones como implementaciones", p["grises"][0], "Confunde alcance de protección con funcionamiento"]]) + "\n"
    t += "**Recomendación:** Usar como evidencia del estado de la técnica, no como evidencia de eficacia.\n\n"
    t += "### B.6 Gaps identificados\n\n"
    t += tabla(["Tipo", "Descripción", "Magnitud", "Viabilidad", "Prioridad"],
        [["Conocimiento", "Ausencia de evidencia de desempeño del sistema reivindicado en el dominio de recuperación tras sismos", "Crítico", "Media", 8],
         ["Metodológico", "Falta de comparación con una línea base y de medidas de resultado", "Significativo", "Alta", 7],
         ["Tecnológico", p["ideas"][0][:140].rstrip() + "…", "Significativo", "Media", 6]]) + "\n"
    t += "### B.7 Competidores / actores / alternativas tecnológicas\n\n"
    t += tabla(["Nombre", "Tipo", "Observación"], [[c[0], c[1], c[2]] for c in p["comp"]]) + "\n"
    t += "### B.8 Variables econométricas y vacíos\n\n"
    t += "- **Y, X, Z:** No aplica; el documento no reporta variables medidas.\n- **Datos y método:** No aplica.\n\n"
    t += tabla(["Tipo de vacío", "Descripción"], vacios(p)) + "\n"
    open(f"{FD}/{pid}_{slug(p['clave'])}.md", "w").write(t)
    return len(t.split())

W = {}
for n, p in enumerate(P, 1): W[p["id"]] = ficha(p, n)
print("fichas de patentes:", W)

# ---------------- CSV
def W_(df, name): df.to_csv(f"{CS}/{name}.csv", index=False, encoding="utf-8-sig")
W_(pd.DataFrame([dict(doc_id=p["id"], numero=p["clave"], tipo=p["tipo"], titulo=p["titulo"], inventores=p["inventores"], titular=p["titular"], solicitud=p["solicitud"], presentacion=p["presentacion"],
    fecha_documento=p["fecha_doc"], publicacion_previa=p["publ_previa"], prioridad=p["prioridad"], cpc=p["cpc"], paginas_pdf=p["paginas"], hojas_dibujos=p["hojas"], reivindicaciones=p["reiv"],
    independientes=", ".join(map(str, p["indep"])), relevancia=p["relevancia"], referencia_apa7=ref(p), archivo=p["archivo"], palabras_ficha=W[p["id"]]) for p in P]), "patentes_inventario")
rows = []
for p in P:
    m = madurez(p)
    rows.append(dict(doc_id=p["id"], **{d.upper(): m[d][0] for d in ("trl", "mrl", "brl", "irl", "drl", "srl")}, TRL_evidencia=m["trl"][1], TRL_justificacion=m["trl"][2], BRL_justificacion=m["brl"][2], IRL_justificacion=m["irl"][2], DRL_justificacion=m["drl"][2], valle="V1 Investigación sin aplicación"))
W_(pd.DataFrame(rows), "patentes_madurez")
W_(pd.DataFrame([dict(doc_id=p["id"], tipo_relacion=r[0], documento_relacionado=r[1], justificacion=r[2]) for p in P for r in p["relaciones"]]), "patentes_relaciones")
W_(pd.DataFrame([dict(doc_id=p["id"], tag=p["tag"], **KW[p["tag"]]) for p in P]), "patentes_terminos")
W_(pd.DataFrame([dict(doc_id=p["id"], tipo=v[0], descripcion=v[1]) for p in P for v in vacios(p)]), "patentes_vacios")
W_(pd.DataFrame([dict(doc_id=p["id"], competidor=c[0], tipo=c[1], observacion=c[2]) for p in P for c in p["comp"]]), "patentes_competidores")
W_(pd.DataFrame([dict(doc_id=p["id"], referencia_apa7=ref(p), cita=cite(p["id"])) for p in ORDEN_REF]), "patentes_bibliografia")
print("CSV de patentes generados")
json.dump({p["id"]: p["tag"] for p in P}, open(f"{CS}/_ids.json", "w"))
