"""informe_patentes.md del módulo de patentes (cifras desde patentes_data.py, terminos_crudo.json y los CSV)."""
import sys, os, json, re, collections
sys.path.insert(0, os.path.dirname(__file__))
from synlib import L, esc
import pandas as pd
from patentes_data import P
import importlib.util
spec = importlib.util.spec_from_file_location("p15", os.path.join(os.path.dirname(__file__), "15_patentes.py"))
OUT = f"{L}/patentes"; KW = json.load(open(f"{OUT}/csv/terminos_crudo.json"))
CITE = {"P002": ("Cella et al.", "2025a"), "P001": ("Cella et al.", "2025b"), "P003": ("Cella y Locke", "2026"), "P004": ("Cella et al.", "2026"),
        "P005": ("Cella et al.", "2022a"), "P006": ("Cella et al.", "2022b"), "P008": ("Cella et al.", "2022c"), "P010": ("Cella et al.", "2022d"),
        "P009": ("Cella et al.", "2022e"), "P007": ("Cella et al.", "2022f"), "P011": ("Berti y DeLuca", "2022")}
def ref(p): return f"{p['autores_apa']} ({CITE[p['id']][1]}). *{p['titulo']}* ({p['num_apa']}). U.S. Patent and Trademark Office."
def c(pid): return f"{CITE[pid][0]}, {CITE[pid][1]}"
def tabla(h, rows):
    s = "| " + " | ".join(h) + " |\n|" + "---|" * len(h) + "\n"
    for r in rows: s += "| " + " | ".join(esc(x) for x in r) + " |\n"
    return s
T = {p["id"]: KW[p["tag"]] for p in P}
pag_leidas = sum(t["paginas"] for t in T.values()); pag_tot = sum(p["paginas"] for p in P); pal = sum(t["palabras"] for t in T.values())
tot = lambda k: sum(t[k] for t in T.values())
sf = [p for p in P if "Strong Force" in p["titular"]]; ibm = [p for p in P if "International Business" in p["titular"]]
b2 = [p for p in P if p["clave"].endswith("B2")]; a1 = [p for p in P if p["clave"].endswith("A1")]
nrel = collections.Counter(p["relevancia"] for p in P)
rel = pd.read_csv(f"{OUT}/csv/patentes_relaciones.csv"); rc = rel.tipo_relacion.value_counts().to_dict()
def flag(p, rx): return "Sí" if re.search(rx, (p["reiv_resumen"] + " " + p["dependientes"]), re.I) else "No"
tec = [[p["id"], flag(p, r"digital twin|gemelo"), flag(p, r"sensor|IoT|internet of things|internet de las cosas"), flag(p, r"machine[- ]learn|aprendizaje automático|machine-learned|artificial intelligence|inteligencia artificial"),
        flag(p, r"blockchain|cadena de bloques|ledger|libro mayor|smart contract|contrato inteligente"), flag(p, r"robotic process|RPA")] for p in P]
md = f"""# Módulo de patentes — SYNAPSE V19.0, lote L01

`MODE=COMPUTE FILES=TRUE BATCH=L01 MODULE=PATENTES DOCS_PATENTES={len(P)} STATUS=COMPLETE_WITH_LIMITS`

## 1. Alcance y método

La carpeta `Patentes /` del repositorio contiene {len(P)} documentos de patente en formato PDF, descargados de Lens.org ({len(b2)} patentes concedidas con código B2 y {len(a1)} publicaciones de solicitud con código A1). Los archivos son imágenes escaneadas sin capa de texto. Se aplicó reconocimiento óptico de caracteres (RapidOCR, sobre imágenes de 150 ppp, lectura por columnas) a una parte de cada documento: la portada, las primeras 33 páginas (hojas de dibujos), las últimas 14 páginas (reivindicaciones) y una de cada 20 páginas intermedias. En total se leyeron {pag_leidas} de {pag_tot:,} páginas ({100*pag_leidas/pag_tot:.1f} %), equivalentes a {pal:,} palabras. El texto reconocido se conserva en `patentes/_ocr_texto/`.

Las patentes forman un módulo separado del lote de 101 documentos (DOCS=101 no cambia). Se identifican con claves P001 a P{len(P):03d}, se les asignó una ficha de cuatro capas adaptada a documentos de patente y se evaluaron con las mismas dimensiones de madurez, vacíos y relaciones que los demás documentos. Las adaptaciones son tres: la referencia APA 7 usa el formato de patente; el estado legal no se asume (solo el código de tipo indica concesión); y los niveles TRL, IRL y DRL se limitan a lo que el texto sustenta, sin inferir madurez comercial de la titularidad.

Limitaciones de método. La lectura parcial implica que la ausencia de un término en las páginas leídas no equivale a ausencia en el documento; las frecuencias que se presentan son de las páginas leídas. La lectura óptica puede omitir líneas, por lo que se citan fragmentos literales solo cuando son legibles. El estado legal posterior de las solicitudes y la vigencia de las concedidas no pueden verificarse con los archivos.

## 2. Inventario

""" + tabla(["ID", "Número", "Tipo", "Titular", "Presentación", "Reivindicaciones (indep.)", "Páginas", "Relevancia"],
    [[p["id"], p["clave"], "B2" if p["clave"].endswith("B2") else "A1", p["titular"].split(" (")[0], p["presentacion"], f"{p['reiv']} ({', '.join(map(str, p['indep']))})", p["paginas"], p["relevancia"]] for p in P]) + f"""
Diez de las once patentes ({len(sf)}) pertenecen a Strong Force VCN Portfolio 2019, LLC y una a International Business Machines Corporation. Los seis documentos P005 a P010 son publicaciones de solicitudes presentadas el 30 de agosto de 2021 como continuaciones de la solicitud internacional PCT/US2020/059227, con una descripción común de 82 hojas de dibujos y párrafos numerados hasta cerca de [2093]; difieren en el título y en las reivindicaciones. P001 es la patente concedida de otra solicitud de la misma familia (17/460,995, publicada como US 2022/0035341 A1, que no está en la carpeta). P002, P003 y P004 pertenecen a otras familias del mismo titular, con prioridades de 2021 a 2023. P011 pertenece a una familia distinta de IBM presentada en 2020.

## 3. Resultados

### 3.1 Contenido tecnológico de las reivindicaciones

La tabla indica si las reivindicaciones independientes y dependientes transcritas en las fichas mencionan cada tecnología.

""" + tabla(["ID", "Gemelo digital", "Sensores o IoT", "Aprendizaje automático o IA", "Cadena de bloques o contratos inteligentes", "RPA"], tec) + f"""
El gemelo digital aparece en las reivindicaciones de {sum(1 for r in tec if r[1]=='Sí')} de {len(P)} patentes y los sensores o el IoT en {sum(1 for r in tec if r[2]=='Sí')}. El aprendizaje automático o la inteligencia artificial figuran en {sum(1 for r in tec if r[3]=='Sí')}, y la automatización robótica de procesos en {sum(1 for r in tec if r[5]=='Sí')}. Las tres tecnologías que el corpus de 101 documentos asocia con la recuperación (gemelo digital, IoT y análisis de datos) están presentes, pero aplicadas a cadenas de valor, manufactura y mantenimiento de activos, no a recuperación tras un sismo.

### 3.2 Términos del eje del corpus en las páginas leídas

""" + tabla(["ID", "Páginas leídas", "Gemelo digital", "Sismo o terremoto", "Desastre", "Amenaza natural", "Interrupción", "Resiliencia", "Recuperación", "Pandemia"],
    [[p["id"], T[p["id"]]["paginas"], T[p["id"]]["digital twin"], T[p["id"]]["earthquake/seismic"], T[p["id"]]["disaster"], T[p["id"]]["natural hazard (flood,hurricane,storm)"], T[p["id"]]["disruption"], T[p["id"]]["resilience"], T[p["id"]]["recovery"], T[p["id"]]["pandemic"]] for p in P]) + f"""
El gemelo digital es el término más frecuente ({tot('digital twin')} apariciones en {pag_leidas} páginas leídas). Las menciones de sismo suman {tot('earthquake/seismic')}, las de desastre {tot('disaster')}, las de interrupción {tot('disruption')}, las de resiliencia {tot('resilience')} y las de recuperación {tot('recovery')}. Estas frecuencias provienen de un muestreo y deben leerse como límites inferiores. Los pasajes identificados que sustentan la relación con el eje del corpus incluyen: la referencia a 'a natural disaster or epidemic' como evento externo que puede interrumpir operaciones y la lista de tareas de mitigación (proveedores múltiples, inventario de amortiguación, transporte alterno) en {c('P002')} (P002); la inclusión de 'earthquakes' entre los factores ambientales posibles en {c('P011')} (P011); la exposición a condiciones ambientales adversas o daño detectada por sensores en {c('P003')} (P003), cuya descripción menciona además 'natural disasters' entre los eventos que activan la predicción de necesidades de recursos de flota. Con el muestreo realizado no se encontraron otras menciones de sismo.

### 3.3 Relevancia para el eje del corpus

Ninguna patente se clasifica como núcleo. P002 se clasifica como adyacente por tratar la interrupción de la cadena de valor como objeto de predicción y mitigación con un gemelo digital alimentado por sensores. Las demás se clasifican como periféricas ({nrel['Periférico']} documentos): comparten tecnología (gemelos digitales, sensores, aprendizaje automático, contratos inteligentes) pero no el dominio de recuperación productiva tras sismos. La clasificación no es una valoración de calidad de las patentes.

### 3.4 Madurez

Todas las patentes se evaluaron con TRL 2 (concepto formulado y descrito), IRL 2 y DRL 2, porque las páginas leídas no contienen pruebas experimentales, integración probada ni conjuntos de datos reales. El BRL, el MRL y el SRL no se determinan: los documentos no contienen datos de mercado, de manufactura ni componentes evaluados por separado. La titularidad por una empresa comercial no se interpretó como madurez de negocio. El valle de la muerte aplicable es V1 (investigación sin aplicación), limitado a lo que el texto permite afirmar.

## 4. Análisis dialéctico del módulo

La tesis es que los gemelos digitales alimentados por sensores y gestionados con aprendizaje automático y automatización de procesos permiten automatizar decisiones de cadena de valor que reducen interrupciones, lo que sustentaría la continuidad operativa tras un evento. La antítesis es que una patente delimita lo reivindicable y no lo comprobado: las {len(P)} patentes no informan de datos de desempeño, las listas de realizaciones son amplias y el disparador de la reivindicación 1 de {c('P002')} es un umbral de demanda y las reivindicaciones 5 y 6 añaden la determinación de una interrupción mediante simulación, sin que las páginas leídas describan un modelo de daño físico. La síntesis es que el módulo aporta un inventario técnico de funciones (recolección de datos, simulación, recomendación, ejecución automática, contratación automatizada) que puede traducirse en requisitos de un sistema de continuidad empresarial, y que la hipótesis de que dichas funciones reduzcan el tiempo de reanudación tras un sismo permanece sin evidencia en este material.

Preguntas socráticas del módulo. ¿Qué parte de las reivindicaciones describe funciones ya implementadas y cuál describe una cobertura de protección? Los documentos no permiten responder. ¿Qué cambia en el diseño si el disparador es el daño y no la demanda? Cambia el modelo de simulación del gemelo, que debería representar la pérdida de capacidad productiva y logística, y los modelos de recuperación del corpus (por ejemplo, D011) proporcionan esa estructura. ¿Qué hipótesis rival explicaría la misma utilidad con menor complejidad? Reglas de inventario de seguridad y contratos paramétricos de seguro pueden cubrir parte de la función sin gemelo digital, alternativa que ningún documento del módulo evalúa.

## 5. Conexión con el corpus de 101 documentos

Se registraron {len(rel)} relaciones tipificadas entre patentes y documentos del lote o entre patentes ({', '.join(f'{k} {v}' for k, v in rc.items())}). Las relaciones con documentos del corpus son de complementariedad en su mayoría: las patentes aportan el nivel de implementación técnica (funciones, interfaces) que las revisiones y los estudios empíricos del corpus no desagregan, mientras que el corpus aporta modelos de recuperación y evidencia de asociaciones que las patentes no tienen. Las conexiones principales son las siguientes.

- **D081 y D037** (resiliencia de la cadena de suministro y gemelos digitales): las tareas de mitigación de {c('P002')} y las pruebas de estrés de {c('P003')} se corresponden con capacidades que D081 clasifica por etapa de resiliencia; D081 advierte que el rebote y el crecimiento tienen menos evidencia, y las patentes no la suplen.
- **D011 y D053** (recuperación empresarial y tiempos de recuperación): ofrecen la estructura de bloqueos y tiempos que falta a los disparadores de las patentes.
- **D004 y D028** (revisiones de gemelos digitales): coinciden en la ausencia de evidencia empírica de desempeño; las patentes reproducen la misma brecha en otra clase documental.
- **D068, D020 y D014** (monitorización estructural): el sistema de colocación de sensores recomendada por aprendizaje de {c('P009')} puede contrastarse con los criterios de la literatura de monitorización.
- **D023 y D034** (gemelos de puentes y de ciudades sísmicas): {c('P011')} propone iniciar un gemelo por similitud ambiental, idea que podría extenderse a parámetros sísmicos.

## 6. Discusión de controversias

Primera controversia: valor probatorio. Una patente concedida acredita novedad y actividad inventiva ante una oficina, no eficacia. Tratar las patentes como evidencia de madurez tecnológica sobrestima el nivel de preparación. Por ello el módulo las clasifica como estado de la técnica. Segunda controversia: amplitud de las reivindicaciones. Las listas dependientes enumeran decenas de funciones (en {c('P001')}, 29 dependientes), lo que puede interpretarse como cobertura defensiva; el texto leído no permite distinguir funciones implementadas de funciones solo reivindicadas. Tercera controversia: familias repetidas. Seis documentos comparten descripción, de modo que sus frecuencias de términos no son observaciones independientes; contarlas como seis fuentes duplicaría el peso de un mismo texto. Cuarta controversia: libertad de operación. La existencia de reivindicaciones amplias sobre plataformas de cadena de valor con gemelos digitales puede condicionar desarrollos posteriores; este informe no constituye un análisis jurídico y no determina infracción ni libertad de operación.

## 7. Premortem y escenarios

Premortem. Causas probables de que la incorporación de las patentes lleve a conclusiones erróneas: (1) tratar la titularidad comercial como evidencia de uso; (2) extrapolar a sismos a partir de menciones aisladas; (3) contar como independientes documentos de una misma familia; (4) leer solo una parte del documento y concluir ausencia; (5) asumir estado legal vigente. Contingencias: mantener las patentes como módulo separado, registrar la cobertura de lectura, ponderar por familia y verificar el estado legal en una base oficial antes de cualquier uso jurídico o comercial.

""" + tabla(["Futuro", "Objetivo", "Tres opciones viables"],
    [["A. Se acumula evidencia empírica sobre gemelos digitales en recuperación", "Medir desempeño", "Piloto con empresas de una zona sísmica; caso con datos de simulacros; evaluación con datos abiertos de cadenas de suministro"],
     ["A. Se acumula evidencia empírica sobre gemelos digitales en recuperación", "Integrar con modelos de recuperación", "Acoplar parámetros del gemelo con los bloqueos de D011; calibrar con D053; validar con registros de reanudación"],
     ["A. Se acumula evidencia empírica sobre gemelos digitales en recuperación", "Reducir costo de inicialización", "Plantillas por similitud sísmica como en P011; bibliotecas abiertas de gemelos; reutilización entre activos similares"],
     ["B. La evidencia sigue siendo escasa", "Mantener vigilancia tecnológica", "Registro anual de patentes y solicitudes; alertas por clasificación G06Q y G16Y; revisión de estado legal"],
     ["B. La evidencia sigue siendo escasa", "Acotar la hipótesis", "Reducir el alcance a una función (inventario de seguridad); probar un solo disparador; comparar con reglas simples"],
     ["B. La evidencia sigue siendo escasa", "Priorizar documentos de mayor valor", "Concentrar la lectura completa en P002, P003 y P009; ampliar OCR completo; consultar listados oficiales de reivindicaciones"],
     ["C. Las reivindicaciones amplias condicionan el desarrollo", "Evaluar libertad de operación", "Análisis jurídico por abogado de patentes; revisión de estado legal; diseño alternativo sin las funciones reivindicadas"],
     ["C. Las reivindicaciones amplias condicionan el desarrollo", "Usar alternativas abiertas", "Gemelos con estándares abiertos; contratos paramétricos de seguro; reglas de inventario sin plataforma propietaria"],
     ["C. Las reivindicaciones amplias condicionan el desarrollo", "Cooperar con titulares", "Licencias de investigación; acuerdos de transferencia; pilotos conjuntos con universidades"]]) + f"""
## 8. ¿Qué se me escapa?

Se escapan seis aspectos. (1) La mayor parte del texto de cada patente no se leyó (cobertura {100*pag_leidas/pag_tot:.1f} %); una lectura completa por OCR de unas {pag_tot:,} páginas aumentaría la cobertura y permitiría un conteo exacto de términos. (2) El estado legal de las solicitudes y la vigencia de las concedidas. (3) Las publicaciones previas faltantes de la familia, como US 2022/0035341 A1. (4) Patentes de otros titulares y de otras jurisdicciones sobre gemelos digitales aplicados a edificios y a recuperación sísmica; la carpeta contiene una muestra que no es una búsqueda sistemática. (5) El análisis de citas hacia delante y hacia atrás entre patentes y literatura científica del corpus. (6) La verificación por un abogado de patentes de la interpretación de las reivindicaciones. Rutas de solución: OCR completo por lotes, consulta de registros oficiales (USPTO) para el estado legal, búsqueda sistemática por clasificación (G06Q 10, G05B 19, G16Y) y revisión jurídica.

## 9. Valor estratégico

El módulo fija qué parte del conocimiento sobre gemelos digitales e IoT en cadenas de valor está documentada como estado de la técnica y qué parte está respaldada por evidencia. Para la decisión de inversión o de investigación, indica que las funciones técnicas existen como diseños protegidos, que ninguna está respaldada por datos de desempeño en el material leído, y que el vacío central del corpus (medir el efecto sobre el tiempo de reanudación de empresas tras un sismo) no se cierra con este material. El valor práctico es de insumo para especificar requisitos y para orientar una búsqueda de patentes con cobertura sistemática.

## 10. Referencias

""" + "\n\n".join(ref(p) for p in sorted(P, key=lambda p: (p["autores_apa"].split(",")[0], p["autores_apa"], CITE[p["id"]][1], p["titulo"]))) + "\n"
open(f"{OUT}/informe_patentes.md", "w").write(md)
print("informe_patentes palabras:", len(md.split()))
