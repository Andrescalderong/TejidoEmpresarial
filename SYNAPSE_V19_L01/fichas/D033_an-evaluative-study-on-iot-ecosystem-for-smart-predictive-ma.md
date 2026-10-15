# FB-L01-033 | D033 — An Evaluative Study on IoT Ecosystem for Smart Predictive Maintenance (IoT-SPM) in Manufacturing: Multiview Requirements and Data Quality

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/An_Evaluative_Study_on_IoT_Ecosystem_for_Smart_Predictive_Maintenance_IoT-SPM_in_Manufacturing_Multiview_Requirements_and_Data_Quality.pdf` · 25 páginas · Relevancia para el eje del corpus: **Adyacente** (Revisión evaluativa del ecosistema IoT para mantenimiento predictivo inteligente (IoT-SPM) como parte de un gemelo digital en manufactura, con requisitos de arquitectura y componentes y un diagnóstico de la brecha de calidad de datos IoT (valores atípicos, datos faltantes y selección de sensores); aporta la capa de calidad de datos de un gemelo con IoT, aunque en manufactura y sin tratar sismos ni recuperación.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-033 / D033
- **Tipo de recurso:** Artículo de revisión (journal peer-reviewed)
- **Referencia APA 7:** Liu, Y., Yu, W., Rahayu, W., & Dillon, T. (2023). An Evaluative Study on IoT Ecosystem for Smart Predictive Maintenance (IoT-SPM) in Manufacturing: Multiview Requirements and Data Quality. *IEEE Internet of Things Journal*, *10*(13), 11160-11184. https://doi.org/10.1109/JIOT.2023.3246100
- **Autores:** Liu, Yuehua (57210568224); Yu, Wenjin (57210554592); Rahayu, Wenny (6603033227); Dillon, Tharam (24724020500)
- **Afiliaciones:** La Trobe University, Department of Computer Science and Computer Engineering, Melbourne, 3086, VIC, Australia
- **Fecha de publicación:** 2023
- **Fuente/contenedor:** IEEE Internet of Things Journal · vol. 10(13)
- **Identificador persistente:** DOI 10.1109/JIOT.2023.3246100 · ISSN 23274662
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85149379059&doi=10.1109%2fJIOT.2023.3246100&partnerID=40&md5=113899564d0bfabc7e4f038a3737175b
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 78

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Presentar los gemelos digitales y su relación con el mantenimiento predictivo inteligente basado en IoT (IoT-SPM), proponer un ecosistema de referencia IoT-SPM y ofrecer una visión sistemática del campo desde varias perspectivas (arquitectura, plataformas y componentes). El artículo identifica los requisitos clave del ecosistema (IoT y sistemas ciberfísicos, datos de monitoreo IoT, plataformas de macrodatos, un paradigma de cómputo actualizado y análisis de datos basado en aprendizaje automático), se enfoca en los problemas de los datos IoT cuando se aplican modelos analíticos en sistemas industriales reales, identifica una brecha en la calidad de datos IoT y evalúa de forma cualitativa las soluciones existentes.

**Pregunta de investigación.** El artículo no formula preguntas de investigación. Los aportes declarados son identificar los requisitos de un ecosistema IoT-SPM, investigar el desarrollo de IoT y las características y desafíos de los datos, discutir las plataformas de macrodatos y la actualización del cómputo, identificar problemas de calidad de datos desde la práctica industrial y evaluar de forma cualitativa las soluciones a esos problemas.

**Marco teórico.** El marco es una arquitectura de tres capas (dispositivos, red y aplicación) para IoT industrial y una descomposición de componentes (IoT y sistemas ciberfísicos, datos de monitoreo, plataformas de macrodatos orientadas a API, distribución de cómputo en nube, niebla y borde, y minería de datos con aprendizaje automático). Se apoya en la tesis de que 'los datos, no la infraestructura, determinan la calidad del análisis' y en una caracterización de los datos IoT (ruidosos, redundantes en sensores, macrodatos de cinco V, parcialmente etiquetados, con problemas de seguridad y heterogéneos). Se organiza la calidad de datos en tres tareas (detección de valores atípicos, imputación de datos faltantes y selección de sensores). El enfoque es de ingeniería de sistemas y ciencia de datos, descriptivo y comparativo.

**Metodología.** Es una revisión evaluativa narrativa. Para la sección de calidad de datos se buscó en Scopus con la cadena KEY("IoT*") O KEY("Internet of Thing*") Y KEY("data quality"), que arrojó 78 documentos; se excluyeron los no relacionados con calidad de datos IoT, los no escritos en inglés, los sin texto completo y los publicados antes de 2010. Para cada una de las tres tareas (valores atípicos, imputación y selección de sensores) se hicieron búsquedas adicionales con palabras clave específicas y se comparó cualitativamente cada enfoque (supervisado, no supervisado, basado en aprendizaje profundo) por ventajas, limitaciones y aplicabilidad al contexto de IoT industrial. El texto no aporta una tabla del proceso de selección, el número de estudios finales por tarea ni criterios de evaluación de calidad, y la comparación no se acompaña de experimentos propios, de métricas de desempeño homogéneas entre los estudios ni de una síntesis cuantitativa de los resultados reportados por cada enfoque.

**Resultados principales.** El artículo concluye que existe una brecha entre los datos recogidos por IoT y el análisis con aprendizaje automático, ocupada por el preprocesamiento que convierte datos crudos en datos aptos para análisis, y que los estudios sobre calidad de datos IoT están en su infancia y suelen ser generales, sin trabajos específicos de mantenimiento inteligente que detallen técnicas para mejorarla. Describe seis características de los datos IoT (ruido, redundancia de sensores, macrodatos de cinco V, etiquetado parcial, seguridad y heterogeneidad) y seis tipos de problemas de calidad al trabajar con casos industriales reales. La evaluación comparativa indica que los métodos supervisados de selección de variables dependen de etiquetas uno a uno difíciles de obtener en entornos industriales; que los no supervisados basados en componentes principales dividen las variables por varianza y no necesariamente seleccionan las mejores para detectar fallas; y que existe una brecha amplia para métodos no supervisados o débilmente supervisados eficientes. Se propone un ecosistema de referencia IoT-SPM centrado en datos con operaciones de procesamiento motivadas por calidad. El texto cita sin fuente primaria que se dedica 80 % del tiempo de proyectos de aprendizaje automático al preprocesamiento y que las empresas pierden entre 8 % y 12 % de ingresos por datos de baja calidad.

**Discusión y contribución.** Los autores sostienen que, aunque la infraestructura IoT es madura, la calidad de los datos es el factor decisivo para el desempeño de las aplicaciones de analítica, que la investigación académica usa conjuntos de datos públicos limpios, pequeños y desactualizados poco representativos de plantas reales, y que la escasa colaboración con la industria por secreto comercial limita el avance. Señalan que los sistemas de mantenimiento inteligente desplegados en producción se encuentran sobre todo en grandes empresas por el costo de reunir expertos de la industria y de la academia. Concluyen con una lista de asuntos abiertos: sensores más diversos y con monitoreo continuo, comunicación entre numerosos dispositivos, métodos de calidad de datos no supervisados o débilmente supervisados y evaluación con datos industriales reales.

**Limitaciones declaradas.** No se presenta una sección de limitaciones. Implícitas: revisión narrativa sin protocolo completo; sin experimentos propios; comparación cualitativa; cifras de pérdidas por datos de baja calidad sin fuente primaria; limitación a manufactura.

**Trabajo futuro.** Investigación en métodos de calidad de datos IoT no supervisados o débilmente supervisados, integración de preprocesamiento de calidad en el ecosistema IoT-SPM, evaluación con datos industriales reales y mayor colaboración entre industria y academia.

**Palabras clave.** Declaradas: Data quality; ecosystem requirements; Internet of Things (IoT); reference IoT ecosystem; smart manufacturing | Inferidas: internet de las cosas, mantenimiento predictivo inteligente, gemelo digital, calidad de datos, detección de valores atípicos, imputación de datos faltantes, selección de sensores, manufactura inteligente, plataformas de macrodatos, computación en el borde

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** El éxito de un ecosistema IoT de mantenimiento predictivo, y por extensión de un gemelo digital, depende más de la calidad de los datos que de la arquitectura, y existe una brecha de investigación en métodos de calidad de datos IoT no supervisados o débilmente supervisados aplicados a datos industriales reales.

**Antítesis identificada.** La revisión no sigue un protocolo sistemático completo ni cuantifica los estudios incluidos por tarea, y la afirmación de que 'no hay artículos sobre calidad de datos en mantenimiento inteligente con IoT' se basa en una búsqueda por palabras clave de una sola base de datos que puede omitir trabajos publicados con otros términos. Las cifras que sostienen la importancia del problema (80 % del tiempo en preprocesamiento y pérdidas de 8 % a 12 % de ingresos) se atribuyen a analistas sin fuente primaria. La evaluación es cualitativa y no ofrece criterios de comparación cuantitativos, y el 'ecosistema de referencia' propuesto no se implementa ni valida. El artículo no discute los costos de las soluciones de calidad de datos ni el grado de adopción industrial, aunque afirma que los sistemas desplegados se limitan a grandes empresas.

**Síntesis propuesta.** El aporte útil es la formulación de la calidad de datos como requisito de primer orden de un gemelo con IoT, con una tipología de problemas (ruido, redundancia, etiquetas, heterogeneidad) y tres tareas de preprocesamiento. Debe leerse como mapa conceptual y de brechas, no como evidencia del efecto de la calidad de datos sobre el desempeño. Para el corpus, la síntesis consiste en incorporar indicadores explícitos de calidad de datos (disponibilidad, valores faltantes, sensores fallidos, latencia) en cualquier evaluación de gemelos con IoT, y en cuantificar con datos reales el efecto de la calidad sobre la precisión del diagnóstico, de modo que la inversión en sensores se compare con la inversión en limpieza y mantenimiento de datos.

**Áreas grises detectadas.**

1. Rigor de la revisión: el texto no presenta un diagrama de flujo de selección ni el número de documentos incluidos por tarea de calidad, ni criterios de evaluación de calidad de los estudios, y la afirmación de ausencia de trabajos específicos en mantenimiento inteligente se basa en palabras clave de una sola base.
2. Cifras sin fuente primaria: se afirma que se dedica 80 % del tiempo de proyectos de aprendizaje automático al preprocesamiento y que las empresas pierden de 8 % a 12 % de ingresos por datos de baja calidad, citando a analistas sin identificar el informe, de modo que la magnitud del problema no es verificable.
3. Ecosistema de referencia sin validación: el ecosistema IoT-SPM propuesto no se implementa ni se prueba con datos industriales, y la comparación entre métodos de calidad de datos no incluye métricas comunes (error, tiempo, costo), por lo que las recomendaciones se basan en juicio de los autores.
4. Transferibilidad: el análisis se centra en manufactura; la aplicación a infraestructura civil, entornos de desastre o pymes con sensores de bajo costo, donde la calidad de datos es más crítica, no se discute.

**Puntos oscuros aclarados.** Llama la atención que los autores afirmen que la tecnología IoT ya está en una etapa muy madura y que, a la vez, indiquen que los sistemas de mantenimiento inteligente en producción solo existen en grandes empresas por el costo de articular a expertos de industria y academia. Una explicación plausible es que la madurez declarada se refiere a componentes (sensores, redes, plataformas) y no a sistemas completos con datos de calidad, de modo que la brecha de adopción está en la integración y en el mantenimiento de datos, que la literatura académica con conjuntos públicos limpios no estudia. Esto sugiere que la mayor parte de la evidencia de desempeño de modelos de mantenimiento proviene de condiciones que no representan la planta real, y que los beneficios declarados del mantenimiento predictivo (reducción de costos, ampliación de vida útil) deben leerse con cautela. En el contexto de un gemelo para recuperación posdesastre, donde los sensores operan con interrupciones de energía y comunicaciones, el problema de datos faltantes y atípicos sería aún más agudo.

**Ideas propositivas novedosas.**

1. Presupuesto de calidad de datos de un gemelo con IoT: estimar, para un gemelo de recuperación o de monitoreo, el porcentaje esperado de datos faltantes, atípicos y de sensores redundantes bajo condiciones de falla de energía y comunicaciones, y medir cuánto degradan la precisión del diagnóstico cada tipo de problema y cada método de imputación o selección de sensores. Fundamento: el artículo identifica la calidad de datos como brecha crítica pero no cuantifica su efecto. Verificabilidad: experimentos con conjuntos de datos reales y con pérdidas simuladas, con métricas comunes. Utilidad: permite fijar umbrales mínimos de calidad y asignar presupuesto entre sensores y mantenimiento de datos.
2. Protocolo común de evaluación de métodos de calidad de datos IoT: definir métricas (error de reconstrucción, falsos positivos de atípicos, tiempo de cómputo en el borde, necesidad de etiquetas) y un conjunto de datos de referencia con perturbaciones realistas (apagones, derivas de calibración, ruido), y evaluar los métodos revisados de detección de atípicos, imputación y selección de sensores bajo el mismo protocolo. Fundamento: la comparación de la revisión es cualitativa. Verificabilidad: publicación del protocolo, datos y código. Utilidad: ofrece una base para elegir métodos livianos y robustos para gemelos desplegados en pequeñas empresas y para comparar propuestas de proveedores con criterios comunes.

**Relaciones poco exploradas.**

1. Calidad de los datos IoT (condiciona) la precisión de los modelos de aprendizaje automático de mantenimiento: los autores la identifican como factor decisivo del desempeño de los sistemas, con base en literatura y no en medición propia.
2. Falta de etiquetas y de acceso a datos industriales reales (limita) el avance de métodos supervisados en mantenimiento inteligente: el secreto comercial reduce la colaboración y obliga a usar conjuntos públicos poco representativos.

**Robustez argumentativa:** 3.0/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 3/10; validez de inferencias causales 3/10; generalizabilidad 3/10.

**Valor estratégico:** 5/10 — Ofrece un marco claro de requisitos de un ecosistema IoT para mantenimiento predictivo y una tipología de problemas de calidad de datos, junto con la identificación de brechas en métodos no supervisados y en datos industriales reales. Su valor para el corpus es de requisito transversal de calidad de datos en gemelos con IoT; se reduce por el rigor limitado de la revisión, las cifras sin fuente primaria y la ausencia de validación del ecosistema propuesto.

**Conexiones inter-documentales.**

- **PRECEDE** D086 (IoT, inteligencia en el borde y monitoreo de salud estructural): relación inversa de D086 DEPENDE_DE D033: D086 clasifica anomalías de datos a bordo, lo que atiende el hallazgo de D033 de que la calidad del dato pesa más que la arquitectura [juicio del analista]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 65 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Apelación a la autoridad sin fuente (Se citan estimaciones de analistas (80 % de tiempo y 8 a 12 % de ingresos) sin identificar fuentes primarias (Sec. IV.A, p. 12)); Argumento desde la ausencia (Se afirma que no hay trabajos de calidad de datos específicos de mantenimiento inteligente a partir de una búsqueda por palabras clave en una base (Sec. VI, p. 16)); Generalización apresurada (Se concluye que la calidad de datos es el factor decisivo en cualquier ecosistema IoT sin evidencia comparativa con otros factores (Sec. IV.A, p. 12))
- **Bradford-Hill:** No aplica: es una revisión conceptual; la relación entre calidad de datos y desempeño analítico se afirma por plausibilidad, sin estimación con datos y sin gradiente ni experimento.
- **TRL asignado:** 6 — 'IoT technologies have already been developed to a very mature stage' (p. 12)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (25 páginas más referencias). Las figuras 1 a 8 no son legibles; se usó el texto. Las cifras de 80 % y de 8 a 12 % se reportan tal como las cita el artículo, sin verificar la fuente primaria.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| El éxito de un ecosistema IoT de mantenimiento predictivo, y por extensión de un gemelo digital, depende más de la calidad de los datos que de la arquitectura, y existe una brecha de investigación en métodos de calidad de datos IoT no supervisados o débilmente supervisados aplicados a datos industriales reales.  | La revisión no sigue un protocolo sistemático completo ni cuantifica los estudios incluidos por tarea, y la afirmación de que 'no hay artículos sobre calidad de datos en mantenimiento inteligente con IoT' se basa en una búsqueda por palabras clave de una sola base de datos que puede omitir trabajos publicados con otros términos. Las cifras que sostienen la importancia del problema (80 % del tiempo en preprocesamiento y pérdidas de 8 % a 12 % de ingresos) se atribuyen a analistas sin fuente primaria. La evaluación es cualitativa y no ofrece criterios de comparación cuantitativos, y el 'ecosistema de referencia' propuesto no se implementa ni valida. El artículo no discute los costos de las soluciones de calidad de datos ni el grado de adopción industrial, aunque afirma que los sistemas desplegados se limitan a grandes empresas.  | El aporte útil es la formulación de la calidad de datos como requisito de primer orden de un gemelo con IoT, con una tipología de problemas (ruido, redundancia, etiquetas, heterogeneidad) y tres tareas de preprocesamiento. Debe leerse como mapa conceptual y de brechas, no como evidencia del efecto de la calidad de datos sobre el desempeño. Para el corpus, la síntesis consiste en incorporar indicadores explícitos de calidad de datos (disponibilidad, valores faltantes, sensores fallidos, latencia) en cualquier evaluación de gemelos con IoT, y en cuantificar con datos reales el efecto de la calidad sobre la precisión del diagnóstico, de modo que la inversión en sensores se compare con la inversión en limpieza y mantenimiento de datos.  | 3.0/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Calidad de datos IoT' abarca ruido, valores atípicos, datos faltantes, redundancia y heterogeneidad; 'IoT-SPM' es el mantenimiento predictivo basado en sensores como parte de un gemelo digital.
- **P2 Supuestos:** Supone que la calidad de datos es el factor principal del desempeño, que la búsqueda en Scopus identifica la literatura relevante y que los métodos de otros dominios son transferibles.
- **P3 Evidencia:** La evidencia es una revisión cualitativa de métodos y la ausencia de estudios específicos detectada con palabras clave.
- **P4 Consecuencias:** Si es cierto, conviene invertir primero en calidad y gobernanza de datos antes que en modelos más complejos; si es falso, se podría subinvertir en modelado o sensado.
- **P5 Contraejemplos:** No se examinan casos de sistemas con datos pobres que lograron buen desempeño, ni el costo de corregir la calidad.
- **P6 Alternativas:** Alternativas: que el mayor obstáculo sea organizacional y de acceso a datos; que los modelos robustos a ruido reduzcan la necesidad de limpieza; que la calidad dependa del diseño del sensor.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Documentos de la búsqueda de calidad de datos IoT | 78 | documentos | Scopus; KEY(IoT) y KEY(data quality) | Sec. VI, p. 16 | Texto | Alta | Antes de aplicar exclusiones |
| Tiempo dedicado al preprocesamiento en proyectos de aprendizaje automático | 80 | % | Frente a 20 % de construcción de modelos | Sec. IV.A, p. 12 | Texto | Baja | Cifra sin fuente primaria |
| Pérdida de ingresos por datos de baja calidad | 8 a 12 | % | Estimación atribuida a analistas | Sec. IV.A, p. 12 | Texto | Baja | Cifra sin fuente primaria |
| Capas de la arquitectura IoT | 3 | capas | Dispositivos, red y aplicación | Sec. I, p. 2 | Texto | Alta | Marco descriptivo |
| Características de los datos IoT | 6 | características | Ruido, redundancia, macrodatos, etiquetado parcial, seguridad y heterogeneidad | Sec. IV.B, p. 13 | Texto | Alta | Fig. 8 |
| Tareas de calidad de datos | 3 | tareas | Valores atípicos, imputación y selección de sensores | Sec. VI, p. 16 | Texto | Alta | Comparación cualitativa |
| Beneficios del IoT-SPM | 4 | beneficios | Costos de mantenimiento, vida útil, producción e inventario | Sec. I, p. 2 | Texto | Media | Sin cuantificación |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 6 | Sí | 'IoT technologies have already been developed to a very mature stage' (p. 12) | TRL modal del campo revisado, inferido: tecnologías IoT maduras con sistemas de mantenimiento inteligente en grandes empresas; métodos de calidad de datos poco probados con datos reales. |
| MRL | N/A | No | No aplica | Sin manufactura propia evaluada. |
| BRL | 3 | Sí | 'only found in large companies' (p. 12) | BRL modal inferido: sistemas desplegados en grandes empresas y barreras de costo para otras; cifras de pérdidas por mala calidad atribuidas a analistas. |
| IRL | 4 | Sí | 'there is a gap between IoT-collected data and data analytics using machine learning methods' (p. 13) | Integración entre captura de datos y analítica con una capa de preprocesamiento faltante o poco estudiada. |
| DRL | 4 | Sí | 'Analysts have estimated that firms lose 8% to 12% of their revenue due to poor-quality data' (p. 12) | Necesidad respaldada por estimaciones de analistas y práctica industrial; sin estudio de mercado propio. |
| SRL | 2.0 | Sí | Componentes: Captura de datos IoT y plataformas (TRL 6), Preprocesamiento de calidad y analítica (TRL 3) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 18.0; ÷9 → 2.00; nivel acotado a [1,9] = 2.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V3 Tecnología sin negocio · Severidad: Media · TRL modal 6 con BRL 3 e IRL 4: sistemas en grandes empresas, con métodos de calidad de datos sin validación industrial y barreras de costo para otras organizaciones. · Estrategia de salida: Colaboración industria-academia con datos reales, protocolos de evaluación y soluciones de calidad de datos de bajo costo.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Apelación a la autoridad sin fuente | Se citan estimaciones de analistas (80 % de tiempo y 8 a 12 % de ingresos) sin identificar fuentes primarias (Sec. IV.A, p. 12) | Magnitud del problema no verificable |
| Argumento desde la ausencia | Se afirma que no hay trabajos de calidad de datos específicos de mantenimiento inteligente a partir de una búsqueda por palabras clave en una base (Sec. VI, p. 16) | Puede deberse a la estrategia de búsqueda |
| Generalización apresurada | Se concluye que la calidad de datos es el factor decisivo en cualquier ecosistema IoT sin evidencia comparativa con otros factores (Sec. IV.A, p. 12) | Afirmación sin medición |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Calidad de datos IoT → precisión del modelo de mantenimiento predictivo | Afirmaciones de la literatura; sin medición propia | Plausibilidad, coherencia con la práctica de ciencia de datos | Fuerza medida, experimento con perturbaciones controladas | Tipo de sensor, modelo y entorno | 3 | Hipótesis no probada |
| IoT-SPM → reducción de costos y mayor vida útil de máquinas | Beneficios enumerados en la introducción | Plausibilidad | Cuantificación, consistencia | Tamaño de la empresa, calidad de datos | 2 | Hipótesis no probada |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Revisión sistemática con protocolo y protocolo común de evaluación cuantitativa de métodos de calidad de datos | Crítico | Alta | 8 |
| Tecnológico | Métodos de calidad de datos no supervisados o débilmente supervisados, livianos y robustos para datos industriales reales | Crítico | Media | 9 |
| Conocimiento | Efecto cuantificado de la calidad de datos sobre el desempeño de gemelos y sistemas de mantenimiento | Significativo | Media | 8 |
| Mercado | Costos de calidad de datos y acceso a soluciones para organizaciones pequeñas | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Estructura general del artículo | Diagrama | Secciones y contribuciones | 6 contribuciones | Baja |
| Fig. 8 | Características de los datos IoT | Diagrama | Seis características | 6 características | Media |
| Tablas comparativas | Evaluación cualitativa de métodos de detección de atípicos, imputación y selección de sensores | Tabla | Ventajas y desventajas de cada enfoque | 3 tareas | Media |
| Ecosistema de referencia | Ecosistema IoT-SPM centrado en datos | Diagrama | Operaciones de procesamiento motivadas por calidad | No aplica | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Karkouch et al. (calidad de datos en IoT) | No especificado en documento | Academia | Base teórica de calidad de datos en IoT | Teoría de factores | Sin enfoque en mantenimiento | Estable |
| Alwan et al. (calidad de datos en sistemas ciberfísicos) | No especificado en documento | Academia | Revisión de retos de calidad de datos en CPS | Alcance en CPS | Alcance limitado | Estable |
| Liu et al. (veracidad de datos IoT para decisiones) | No especificado en documento | Academia | Impacto de la veracidad de macrodatos en la decisión | Enfoque de decisión | Sin soluciones técnicas detalladas | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** No aplica: no se estima una variable resultado
- **X:** No aplica
- **Z (controles):** Tarea de calidad de datos y tipo de método
- **Datos:** 78 documentos de Scopus como punto de partida de la sección de calidad de datos
- **Método:** Revisión evaluativa cualitativa
- **Efecto reportado:** No cuantificado
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin evaluación de calidad ni cuantificación de efectos

| Vacío | Tipo | Descripción |
|---|---|---|
| V-033-01 | TERR | Sin análisis de países ni de zonas sísmicas |
| V-033-02 | POBL | Foco en grandes empresas de manufactura; pymes y organizaciones sin recursos fuera del análisis |
| V-033-03 | TEMP | Sin análisis de operación prolongada ni de eventos extremos |
| V-033-04 | MET | Revisión sin protocolo completo; comparación cualitativa |
| V-033-05 | VAR | Faltan variables de costo, precisión del diagnóstico y degradación por pérdida de datos |
| V-033-06 | TEOR | Sin teoría de calidad de datos aplicada a decisiones de continuidad |
| V-033-07 | CAUS | Sin evidencia causal del efecto de la calidad de datos |
