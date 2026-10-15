# FB-L01-001 | D001 — Energy-efficient task scheduling and physiological assessment in disaster management using UAV-assisted networks

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/1-s2.0-S0140366419318638-main.pdf` · 8 páginas · Relevancia para el eje del corpus: **Adyacente** (Gestión de desastres con IoT y UAV, sin dimensión sísmica específica ni empresarial; aporta arquitectura de recolección de datos en emergencia.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-001 / D001
- **Tipo de recurso:** Artículo científico (journal peer-reviewed)
- **Referencia APA 7:** Ejaz, W., Ahmed, A., Mushtaq, A., & Ibnkahla, M. (2020). Energy-efficient task scheduling and physiological assessment in disaster management using UAV-assisted networks. *Computer Communications*, *155*, 150-157. https://doi.org/10.1016/j.comcom.2020.03.019
- **Autores:** Ejaz, Waleed (35810235000); Ahmed, Arslan (57214309869); Mushtaq, Aliza (58461968700); Ibnkahla, Mohamed (24773088300)
- **Afiliaciones:** Department of Engineering & Applied Science, Thompson Rivers University, Kamloops, BC, Canada; Data Science and Insights Team, IBM Canada Ltd., Toronto, ON, Canada; King Edward Medical University, Lahore, Pakistan; Department of Systems and Computer Engineering, Carleton University, Ottawa, ON, Canada
- **Fecha de publicación:** 2020
- **Fuente/contenedor:** Computer Communications · vol. 155
- **Identificador persistente:** DOI 10.1016/j.comcom.2020.03.019 · ISSN 01403664
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85082014011&doi=10.1016%2fj.comcom.2020.03.019&partnerID=40&md5=4515be795470aa3ab6f1b632371ecf6a
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 88

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Proponer una arquitectura de recolección de datos por vehículos aéreos no tripulados (UAV) desde una red IoT terrestre en zonas de desastre y un esquema de programación de tareas que minimice el consumo de energía del UAV, complementado con un clasificador de árbol de decisión que estime el estado de riesgo fisiológico de las personas afectadas a partir de signos vitales, con el fin de priorizar la atención de los equipos de primera respuesta en las primeras horas posteriores a un evento adverso, cuando la infraestructura terrestre de comunicaciones suele estar degradada.

**Pregunta de investigación.** [INFERIDA] ¿En qué medida la selección de tareas y la optimización de la ruta del UAV reducen el consumo energético frente a un enfoque que visita todos los nodos cabeza de clúster, y puede un árbol de decisión reproducir el estado de riesgo derivado de NEWS2 con precisión suficiente para priorizar clústeres?

**Marco teórico.** El trabajo se apoya en la literatura de gestión de desastres con redes inalámbricas de sensores, IoT y UAV con conectividad 5G, y en la teoría de optimización combinatoria (ruteo de vehículos y algoritmos evolutivos). El componente clínico adopta el National Early Warning Score (NEWS) del Royal College of Physicians (versión 2, 2017) como patrón de referencia para estratificar el riesgo de deterioro. El paradigma es positivista de ingeniería: modelo matemático, simulación y evaluación mediante métricas de clasificación (precisión, exhaustividad, F1) y validación cruzada. No declara una teoría de resiliencia ni de gestión organizacional; el desastre se trata como un problema de captura y priorización de datos.

**Metodología.** Estudio de simulación con dos módulos. Primero, un modelo de pérdida de trayecto log-distancia con sombreado gaussiano (ecuaciones 2-3) y un modelo de energía del UAV como potencia constante por tiempo de vuelo (ecuación 4); el problema de minimización (ecuación 7) se resuelve con un algoritmo genético de población 100, 10.000 iteraciones, dos mutaciones por reproducción y sin cruce. La simulación considera un solo UAV, redes de 500×500, 1000×1000 y 1500×1500 m², entre 10 y 18 cabezas de clúster y entre 0 y 20 tareas (Tabla 3). Segundo, un clasificador de árbol de decisión (índice de Gini) entrenado sobre 16.671 registros de signos vitales de 32 pacientes del Royal Adelaide Hospital (Universidad de Queensland), usando frecuencia cardiaca, saturación de oxígeno, presión sistólica y frecuencia respiratoria; la temperatura se excluyó por escasez de datos. Se limpiaron valores anómalos (p. ej. presión de 10.000 mmHg), se imputaron faltantes por relleno e interpolación, y se derivaron las etiquetas de riesgo con NEWS2. Partición 50/30/20 (entrenamiento/validación/prueba) y validación cruzada de cinco pliegues. Software: no se declara más allá de scikit-learn como referencia.

**Resultados principales.** En la simulación de ruteo, la distancia recorrida y la energía crecen de forma aproximadamente lineal con el número de tareas; con todas las tareas el esquema converge al enfoque tradicional (hovering sobre todos los nodos). El número de cabezas de clúster no altera el consumo para un tamaño de red dado, y el tamaño de red tiene una relación lineal positiva con la energía (Figs. 5-6). El texto no reporta porcentajes de ahorro. En la clasificación, la matriz de confusión (Tabla 5) suma 3.325 casos de prueba y sus diagonales suman 3.007, es decir, una exactitud de 90,4 % calculada por el analista; la validación cruzada reporta exactitud media de 87,2 % (rango 82,6-95,3 %, desviación 0,04). Precisión por clase: 0,86 (ninguno), 0,95 (bajo), 0,86 (bajo-medio), 0,80 (medio), 0,82 (alto); exhaustividad: 0,89, 0,90, 0,89, 0,95, 0,80; F1 entre 0,81 y 0,93. El modelo identifica 27 personas de riesgo alto en el conjunto de prueba. Las estadísticas descriptivas de la base (Tabla 4) indican frecuencia cardiaca media de 81,49 lpm, saturación de 98,98 %, presión sistólica de 117,47 mmHg y frecuencia respiratoria de 12,68 respiraciones por minuto, valores compatibles con pacientes mayoritariamente estables, lo que explica el predominio de las clases 'ninguno' y 'bajo' (2.298 de 3.325 casos de prueba, es decir, 69 %, según las sumas por fila de la Tabla 5).

**Discusión y contribución.** Los autores sostienen que la selección adecuada de tareas conserva energía y prolonga el tiempo de vuelo, y que el árbol de decisión es suficientemente preciso para desplegar equipos médicos en los clústeres de mayor riesgo. La contribución declarada es triple: arquitectura de recolección basada en tareas, esquema de programación energéticamente eficiente y análisis de datos fisiológicos con aprendizaje automático. Reconocen que el análisis de la acción de los primeros respondientes queda fuera de alcance. La evaluación, sin embargo, compara contra una línea base débil y usa etiquetas generadas por una regla determinista aplicada a las mismas variables de entrada, de modo que la discusión sobreestima el valor práctico del clasificador.

**Limitaciones declaradas.** No declaradas de forma explícita. Se reconocen implícitamente: un solo UAV, uso de datos hospitalarios en lugar de datos de campo y exclusión de la temperatura por datos faltantes.

**Trabajo futuro.** Extensión a múltiples UAV con asignación de tareas, mejora de protocolos de comunicación UAV-cabeza de clúster y UAV-centro de monitoreo, y ruteo priorizado por el factor de riesgo de cada clúster tras una primera pasada de recolección.

**Palabras clave.** Declaradas: Disaster management; Early warning score; Energy efficiency; Internet of Things; Physiologic monitoring; Unmanned aerial vehicles; Vital signs | Inferidas: programación de tareas, algoritmo genético, árbol de decisión, NEWS2, clúster de nodos IoT, 5G, ruteo de UAV, triaje

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un UAV que visita solo las cabezas de clúster seleccionadas, con ruta optimizada por algoritmo genético, consume menos energía que la recolección exhaustiva, y los signos vitales recolectados permiten clasificar con aprendizaje automático el riesgo de las personas para priorizar la respuesta.

**Antítesis identificada.** El árbol de decisión se entrena para reproducir una función determinista (NEWS2 calculado con cuatro de las variables) a partir de esas mismas variables; una exactitud alta mide la capacidad de aproximar umbrales, no la capacidad de predecir deterioro clínico. Además, los datos proceden de 32 pacientes bajo monitoreo hospitalario, con observaciones temporalmente autocorrelacionadas que, al repartirse al azar entre entrenamiento y prueba, filtran información entre particiones. Del lado del ruteo, el problema con 10-18 nodos admite solución exacta o heurísticas de ruteo estándar, y el modelo energético de potencia constante ignora el vuelo estacionario frente al crucero, el viento y la autonomía de batería. La conclusión de eficiencia energética descansa en una comparación con una línea base que nadie usaría si pudiera elegir tareas.

**Síntesis propuesta.** La contribución sostenible es la arquitectura conceptual de recolección por tareas y la formulación del problema, no los resultados numéricos. El valor del clasificador solo se demostraría si predijera un desenlace futuro (deterioro a las horas siguientes) o si se evaluara con datos de personas afectadas por desastres y particiones por paciente. En consecuencia, el documento debe leerse como una propuesta de arquitectura y de formulación del problema, con evidencia de desempeño todavía preliminar. En el marco de recuperación productiva, el hallazgo útil es la idea de un puntaje de alerta temprana calculado sobre sensores y priorizado por clúster, trasladable al estado operativo de empresas y líneas vitales.

**Áreas grises detectadas.**

1. Línea base 'tradicional': se define como hovering sobre todos los cabezas de clúster, sin comparar con ruteo exacto, vecino más cercano ni otros metaheurísticos; el ahorro energético se afirma sin cifras (Figs. 4-6); tampoco se informa el tiempo de cómputo del algoritmo genético en relación con la latencia que los autores consideran crítica.
2. Etiquetas circulares: el riesgo se deriva de NEWS2 con cuatro variables y luego se predice con las mismas; el texto presenta Tabla 6 como evidencia de utilidad clínica sin una referencia independiente de desenlace (muerte, ingreso a UCI).
3. Inconsistencia de datos: se citan 16.671 registros (Sec. 5.2) y 16.600 puntos (Sec. 5.2, validación cruzada); la partición 50/30/20 se describe junto a una validación cruzada de cinco pliegues sin aclarar cuál produce las cifras de la Tabla 6.
4. Validez externa: el conjunto procede de 32 pacientes en un hospital de Adelaida y no de víctimas de desastre; la distribución de signos vitales en terremotos (trauma, hipotermia, aplastamiento) difiere.

**Puntos oscuros aclarados.** La independencia del consumo energético respecto del número de cabezas de clúster que reportan los autores no es un hallazgo empírico, sino una consecuencia del diseño: el programador elige tareas y la energía depende de la longitud de la ruta, que a su vez depende del conjunto de tareas elegido y no de cuántos nodos existen. El resultado sería distinto si las tareas se asignaran de forma forzosa por cobertura o si los nodos se distribuyeran en clústeres espaciales. Sobre el clasificador, la brecha entre la exactitud calculada de la matriz (90,4 %) y la media de validación cruzada (87,2 %) apunta a variabilidad por paciente, y el rango 82,6-95,3 % sugiere que el desempeño depende de qué pacientes caen en cada pliegue; una validación dejando fuera un paciente por vez reduciría probablemente la cifra. La clase 'alto' tiene solo 27 casos predichos, de modo que su exhaustividad de 0,80 descansa en muy pocas observaciones.

**Ideas propositivas novedosas.**

1. Puntaje de alerta temprana empresarial ('NEWS empresarial'): sustituir los signos vitales por indicadores operativos de cada establecimiento (energía, conectividad, inventario refrigerado, asistencia de personal) captados por sensores o UAV, y aplicar el mismo esquema de agregación por clúster productivo para priorizar visitas de recuperación. Fundamento: la arquitectura del documento es agnóstica al tipo de dato. Verificabilidad: construir el puntaje en una zona post-sismo y medir si predice el tiempo de reapertura de cada negocio mediante una regresión de supervivencia con covariables de tamaño, sector y daño físico. Utilidad: focaliza apoyo a empresas en riesgo de cierre definitivo y permite asignar los recursos escasos de apoyo productivo según el riesgo de cada clúster económico.
2. Evaluación prospectiva del clasificador: entrenar para predecir la clase de riesgo a t+Δ en lugar de la clase actual, con partición por paciente. Fundamento: elimina la circularidad señalada y mide el valor agregado del aprendizaje automático sobre la regla. Verificabilidad: la base de Queensland tiene series temporales; basta con desplazar las etiquetas y comparar con la regla persistente (el riesgo actual como pronóstico). Utilidad: determina si el aprendizaje automático agrega información más allá de reglas clínicas simples antes de desplegarlo en campo, y establece un protocolo de evaluación replicable por otros equipos que trabajen con sensores corporales o con sensores de infraestructura.

**Relaciones poco exploradas.**

1. Energía del UAV (depende de) número de tareas asignadas y longitud de la ruta, no del número de cabezas de clúster: merece prueba con distribuciones espaciales agrupadas y con costos de hovering diferenciados.
2. Factor de riesgo del clúster Θc (podría determinar) el orden de visita del UAV: el artículo propone cerrar el ciclo pero no lo prueba; equivale a un problema de orientación con premios proporcionales al riesgo.

**Robustez argumentativa:** 4.3/10 (ponderación 30/30/25/15) — consistencia lógica 6/10; calidad de la evidencia 4/10; validez de inferencias causales 3/10; generalizabilidad 4/10.

**Valor estratégico:** 4/10 — Aporta una formulación clara y reutilizable de recolección por tareas con restricción de cobertura y energía, pero su evidencia empírica es débil y está desligada de contextos sísmicos o empresariales; su valor estratégico para el corpus es sobre todo conceptual: ofrece una arquitectura de priorización por clúster que puede reutilizarse para estados operativos de empresas y líneas vitales, aunque exige reemplazar las etiquetas y los datos de entrada.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Petición de principio (Etiquetas de riesgo calculadas con NEWS2 sobre las mismas variables que alimentan el clasificador (Sec. 4.2.1, p. 4)); Hombre de paja (Línea base 'tradicional' = hovering sobre todos los cabezas de clúster (Sec. 5.1, p. 6)); Generalización apresurada (Datos de 32 pacientes hospitalarios para inferir riesgo en víctimas de desastre (Sec. 4.2.1, p. 4))
- **Bradford-Hill:** No aplica a relaciones causales sobre personas; la única relación causal es mecánica (más tareas implican más distancia y energía), con plausibilidad física y gradiente, pero sin experimento independiente.
- **TRL asignado:** 3 — 'we are not collecting real-time vital signs data from people in disaster-affected areas; instead, we use an existing database' (p. 4)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto extraído sin pérdida; las ecuaciones aparecen desordenadas por la extracción (Secs. 3-4). Tabla 5 interpretada con columnas = clase predicha, lo que reproduce la Tabla 6.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un UAV que visita solo las cabezas de clúster seleccionadas, con ruta optimizada por algoritmo genético, consume menos energía que la recolección exhaustiva, y los signos vitales recolectados permiten clasificar con aprendizaje automático el riesgo de las personas para priorizar la respuesta.  | El árbol de decisión se entrena para reproducir una función determinista (NEWS2 calculado con cuatro de las variables) a partir de esas mismas variables; una exactitud alta mide la capacidad de aproximar umbrales, no la capacidad de predecir deterioro clínico. Además, los datos proceden de 32 pacientes bajo monitoreo hospitalario, con observaciones temporalmente autocorrelacionadas que, al repartirse al azar entre entrenamiento y prueba, filtran información entre particiones. Del lado del ruteo, el problema con 10-18 nodos admite solución exacta o heurísticas de ruteo estándar, y el modelo energético de potencia constante ignora el vuelo estacionario frente al crucero, el viento y la autonomía de batería. La conclusión de eficiencia energética descansa en una comparación con una línea base que nadie usaría si pudiera elegir tareas.  | La contribución sostenible es la arquitectura conceptual de recolección por tareas y la formulación del problema, no los resultados numéricos. El valor del clasificador solo se demostraría si predijera un desenlace futuro (deterioro a las horas siguientes) o si se evaluara con datos de personas afectadas por desastres y particiones por paciente. En consecuencia, el documento debe leerse como una propuesta de arquitectura y de formulación del problema, con evidencia de desempeño todavía preliminar. En el marco de recuperación productiva, el hallazgo útil es la idea de un puntaje de alerta temprana calculado sobre sensores y priorizado por clúster, trasladable al estado operativo de empresas y líneas vitales.  | 4.3/10 |

### B.2 Interrogación socrática

- **P1 Definición:** Define 'riesgo' como la categoría ordinal (ninguno, bajo, bajo-medio, medio, alto) derivada de NEWS2 con HR, SpO2, presión sistólica y frecuencia respiratoria; define 'eficiencia' como menor energía de vuelo.
- **P2 Supuestos:** Supone que los signos vitales de pacientes hospitalizados se parecen a los de víctimas; que cada nodo IoT corresponde a una persona; que los nodos cabeza de clúster agregan datos sin pérdida; que la energía es potencia constante por tiempo.
- **P3 Evidencia:** La evidencia energética es simulada y cualitativa; la evidencia clínica es una exactitud de 87-90 % contra etiquetas derivadas de una regla, sin desenlace clínico independiente.
- **P4 Consecuencias:** Si es verdadero, los equipos priorizarían clústeres con más personas de riesgo alto; si es falso por circularidad, la priorización replicaría una regla que ya existe sin añadir información.
- **P5 Contraejemplos:** Un contraejemplo es el ruteo exacto de 10-18 nodos, que domina a la heurística; otro es una zona sin cobertura donde los nodos no sobreviven al sismo.
- **P6 Alternativas:** Alternativas: ruteo por vecino más cercano o por programación entera; clasificación por la regla NEWS2 directamente; recolección con enjambres de UAV o con vehículos terrestres.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Pacientes en la base de signos vitales | 32 | pacientes | Base de la Universidad de Queensland, Royal Adelaide Hospital | Sec. 4.2.1, p. 4 | Texto | Alta | Muestra pequeña; no son víctimas de desastre |
| Registros de signos vitales | 16671 | registros | Conjunto usado para análisis | Sec. 5.2, p. 6 | Texto | Media | Se menciona también 16.600 en p. 7 (inconsistencia) |
| Partición entrenamiento/validación/prueba | 50/30/20 | % | División del conjunto de datos | Sec. 4.2.1, p. 4 | Texto | Alta | Convive con validación cruzada de 5 pliegues |
| Exactitud media validación cruzada (k=5) | 87.2 | % | Clasificador de árbol de decisión | Sec. 5.2, p. 7 | Texto | Alta | Rango 82,6-95,3 %; desviación 0,04 |
| Exactitud derivada de la matriz de confusión | 90.4 | % | 3007 aciertos sobre 3325 casos (cálculo del analista) | Tabla 5, p. 7 | Tabla | Media | Cálculo propio; asume columnas como clase predicha |
| Precisión clase alto riesgo | 0.82 | razón | Tabla 6 | Tabla 6, p. 7 | Tabla | Alta | Basada en 27 casos predichos |
| Exhaustividad clase medio | 0.95 | razón | Tabla 6 | Tabla 6, p. 7 | Tabla | Alta | Una sola partición |
| F1 rango entre clases | 0.81-0.93 | razón | Tabla 6 | Tabla 6, p. 7 | Tabla | Alta | Sin intervalos de confianza |
| Personas de riesgo alto detectadas | 27 | personas | Conjunto de prueba | Sec. 5.2, p. 7 | Texto | Alta | Conteo pequeño |
| Población del algoritmo genético | 100 | individuos | Parámetro del solver | Sec. 4.1, p. 4 | Texto | Alta | Sin análisis de sensibilidad |
| Iteraciones del algoritmo genético | 10000 | iteraciones | Criterio de parada | Sec. 4.1, p. 4 | Texto | Alta | Sin cruce; dos mutaciones por reproducción |
| Tamaños de red simulados | 500x500; 1000x1000; 1500x1500 | m2 | Simulación | Tabla 3, p. 6 | Tabla | Alta | Un solo UAV |
| Número de cabezas de clúster | 10-18 | nodos | Simulación | Tabla 3, p. 6 | Tabla | Alta | Fig. 5 usa 20 cabezas, fuera del rango de la tabla |
| Velocidad y potencia del UAV | 30; 500 | km/h; W | Parámetros de simulación | Tabla 3, p. 6 | Tabla | Alta | Potencia constante en el modelo |
| Frecuencia cardiaca media (SD) | 81.49 (17.07) | lpm | Estadísticos de la base | Tabla 4, p. 7 | Tabla | Alta | Valores sin filtrar por paciente |
| Ahorro energético del esquema propuesto | No especificado en documento | N/A | Comparación con enfoque tradicional | Sec. 5.1, p. 6 | Figura | Baja | Carece de datos duros: solo curvas |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 3 | Sí | 'we are not collecting real-time vital signs data from people in disaster-affected areas; instead, we use an existing database' (p. 4) | Prueba de concepto analítica y experimental en simulación con datos hospitalarios; sin prototipo físico ni entorno relevante (TRL 3 NASA). |
| MRL | N/A | No | No aplica | No hay proceso de manufactura ni producción en el documento. |
| BRL | 1 | Sí | 'the methodology of action by first responders is beyond the scope of this paper' (p. 2) | Idea conceptual sin análisis de mercado ni modelo de negocio; usuarios (primeros respondientes) mencionados sin validación. |
| IRL | 2 | Sí | 'cluster heads communicate their location information and UAVs share their capabilities with the controller' (p. 3) | Interfaces UAV-nodo-centro descritas funcionalmente (Fig. 1) sin prototipo de integración. |
| DRL | N/A | No | No aplica |  |
| SRL | 1.0 | Sí | Componentes: Programador de tareas y ruteo UAV (TRL 3), Clasificador de riesgo (TRL 3) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 6.0; ÷9 → 0.67; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | N/A | N/A |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 3 con BRL 1 e IRL 2: investigación sin ruta explícita a la aplicación; sin colaboración con agencias de emergencia ni datos de campo. · Estrategia de salida: Validar con datos de simulacros o de víctimas reales, vincular con una entidad de gestión de riesgos y comparar contra ruteo exacto.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Petición de principio | Etiquetas de riesgo calculadas con NEWS2 sobre las mismas variables que alimentan el clasificador (Sec. 4.2.1, p. 4) | La exactitud no demuestra valor predictivo clínico |
| Hombre de paja | Línea base 'tradicional' = hovering sobre todos los cabezas de clúster (Sec. 5.1, p. 6) | Sobrestima el ahorro energético del esquema propuesto |
| Generalización apresurada | Datos de 32 pacientes hospitalarios para inferir riesgo en víctimas de desastre (Sec. 4.2.1, p. 4) | Limita la validez externa de las conclusiones |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Número de tareas → energía del UAV | Relación lineal en Figs. 5-6 | Fuerza, gradiente, plausibilidad, temporalidad | Experimento físico, especificidad | Distancias entre nodos, altura de vuelo | 6 | Causal mecánica (simulada) |
| Signos vitales → estado de riesgo | Exactitud 87-90 % contra NEWS2 | Fuerza | Temporalidad, experimento, coherencia con desenlaces | Circularidad de etiquetas, autocorrelación por paciente | 2 | Espuria respecto de desenlaces clínicos |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Tecnológico | Integración de ruteo energéticamente eficiente con priorización por riesgo del clúster en una sola formulación (problema de orientación con premios) | Significativo | Alta | 7 |
| Conocimiento | Ausencia de validación con datos de víctimas de desastres y con desenlaces clínicos independientes | Crítico | Media | 8 |
| Metodológico | Falta de comparación contra ruteo exacto/heurísticas estándar y de validación por paciente | Significativo | Alta | 6 |
| Mercado | Sin análisis de adopción por agencias de gestión de riesgo ni de costo de UAV | Moderado | Media | 4 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | IoT platform for disaster management using UAVs | Diagrama | Arquitectura con nodos terrestres, cabezas de clúster, UAV y centro de monitoreo | No aplica | Alta |
| Fig. 2 | Histogram of vital signs | Gráfico | Histogramas de HR, SpO2, NBP, awRR y temperatura; la temperatura es dispersa | Distribuciones sin valores tabulados | Media |
| Fig. 3 | Linear correlation between the features | Gráfico | Mapa de calor de correlación de Pearson entre variables | Coeficientes no legibles en texto | Baja |
| Fig. 4 | Route of UAV for data collection | Gráfico | Rutas para Tk=4, 6 y 8 en red de 500×500 m | No tabulados | Media |
| Fig. 5 | Energy consumption versus number of tasks | Gráfico | Energía lineal en tareas para tres tamaños de red, 20 cabezas de clúster | No tabulados | Alta |
| Fig. 6 | Energy consumption of UAV versus number of cluster heads and network size | Gráfico | Energía independiente del número de cabezas de clúster | No tabulados | Media |
| Tabla 1 | NEWS scoring system | Tabla | Umbrales de puntuación de HR, SpO2, NBP, awRR y temperatura | Umbrales NEWS2 | Alta |
| Tabla 5 | Confusion matrix | Tabla | Matriz de confusión 5×5 con 3.325 casos | Diagonal 468, 1607, 684, 226, 22 | Alta |
| Tabla 6 | Evaluation metrics | Tabla | Precisión, exhaustividad y F1 por clase | Rangos 0,80-0,95 | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Enfoque tradicional de recolección por hovering | No especificado en documento | Tecnología | UAV visita todos los cabezas de clúster | Cobertura completa | Mayor energía y latencia | Declinando |
| NEWS2 / mEWS (Royal College of Physicians) | Reino Unido | Estándar clínico | Reglas de puntuación de signos vitales | Validado clínicamente, interpretable | Requiere variables adicionales (conciencia, oxígeno suplementario) | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Energía consumida por el UAV; clase de riesgo (5 niveles)
- **X:** Número de tareas, tamaño de red, número de cabezas de clúster; HR, SpO2, NBP, awRR
- **Z (controles):** Altura de vuelo, velocidad y potencia (parámetros fijos); no hay controles estadísticos
- **Datos:** Simulación (corte transversal de configuraciones) y 16.671 registros de 32 pacientes (series de tiempo agrupadas)
- **Método:** Algoritmo genético; árbol de decisión con validación cruzada
- **Efecto reportado:** Energía crece linealmente con tareas; exactitud 87,2 % (validación cruzada)
- **Endogeneidad tratada:** No - no hay inferencia causal; circularidad de etiquetas no tratada
- **Instrumento:** No aplica
- **Robustez reportada:** Validación cruzada k=5; sin análisis de sensibilidad del algoritmo genético

| Vacío | Tipo | Descripción |
|---|---|---|
| V-001-01 | TERR | Sin validación en regiones sísmicas ni en contextos latinoamericanos |
| V-001-02 | POBL | Víctimas de desastre y trabajadores de empresas afectadas no están representados |
| V-001-03 | MET | Sin comparación con ruteo exacto ni con multi-UAV; sin validación por paciente |
| V-001-04 | VAR | Ausencia de variables empresariales y de infraestructura (energía, conectividad, inventario) |
| V-001-05 | TEOR | Sin marco de resiliencia ni de continuidad operativa |
| V-001-06 | CAUS | No se identifica efecto causal de la recolección eficiente sobre vidas salvadas o tiempos de recuperación |
