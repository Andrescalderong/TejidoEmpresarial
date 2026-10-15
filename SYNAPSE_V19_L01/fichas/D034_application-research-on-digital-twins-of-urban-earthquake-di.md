# FB-L01-034 | D034 — Application research on digital twins of urban earthquake disasters

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/Application research on digital twins of urban earthquake disasters.pdf` · 24 páginas · Relevancia para el eje del corpus: **Núcleo** (Propone y demuestra por simulación un gemelo digital de una ciudad con sismo (modelo 3D de escena real y de base, intensidad sísmica, daño por edificio con análisis tiempo-historia y sensores que actualizan el daño) para apoyar el rescate y las decisiones de emergencia; es el documento del corpus que une más directamente gemelo digital, sismo urbano y decisiones posdesastre, aunque no modela recuperación económica ni empresas.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-034 / D034
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Yu, S., Lei, Q., Liu, C., Zhang, N., Shan, S., & Zeng, X. (2023). Application research on digital twins of urban earthquake disasters. *Geomatics, Natural Hazards and Risk*, *14*(1), Article 2278274. https://doi.org/10.1080/19475705.2023.2278274
- **Autores:** Yu, Sihan (57223232770); Lei, Qiyun (16175250400); Liu, Chao (57223230354); Zhang, Nan (58611985500); Shan, Shuaishuai (58684118900); Zeng, Xiaoming (58684119000)
- **Afiliaciones:** Earthquake Agency of Ningxia Hui Autonomous Region, Yinchuan, China; Institute of Geology, China Earthquake Administration, Beijing, China; School of Geography, Nanjing Normal University, Nanjing, China; Tianjin Research Institute for Water Transport Engineering, Tianjin, China
- **Fecha de publicación:** 2023
- **Fuente/contenedor:** Geomatics, Natural Hazards and Risk · vol. 14(1)
- **Identificador persistente:** DOI 10.1080/19475705.2023.2278274 · ISSN 19475705
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85176007198&doi=10.1080%2f19475705.2023.2278274&partnerID=40&md5=d9d035305374e6b84ae41a133d21220a
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 26

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Construir un gemelo digital de una ciudad afectada por un sismo que refleje en el espacio virtual los datos de las distintas etapas del desastre y asegure una sincronización y simulación elevadas, para mejorar la seguridad del personal de rescate y la capacidad de decisión de los responsables. El estudio integra un modelo urbano 3D de escena real y de base, un modelo de intensidad sísmica a partir de fallas activas y réplicas, un cálculo de respuesta y daño de cada edificio y sensores que registran cambios en tiempo real para corregir la evaluación, con el fin de proponer esquemas óptimos de rescate y evaluaciones precisas del desastre.

**Pregunta de investigación.** El artículo no formula preguntas de investigación. Las preguntas implícitas son cómo construir un gemelo digital urbano de bajo costo y actualización rápida, si un modelo de atenuación basado en la distancia mínima a la falla estima la intensidad sísmica de forma aplicable y cómo la información de sensores puede corregir la evaluación de daño para el rescate.

**Marco teórico.** El marco combina el concepto de gemelo digital urbano (ciudad física, ciudad virtual, análisis inteligente, percepción dinámica y gemelo) con cuatro etapas de madurez de los gemelos de ciudad (cartografía dinámica, gemelo de aprendizaje, gemelo de simulación y gemelo autónomo), con el reconocimiento de que hoy solo existe el tipo de simulación o 'análogo'. En ingeniería sísmica usa modelos de atenuación de la intensidad (distancia mínima a la falla, con parámetros de Mw, profundidad focal, coberturas y velocidad de onda de corte Vs30; y distancia equivalente de fuente para réplicas) y el análisis elastoplástico de historia en el tiempo de edificios con el índice de daño de la clasificación sísmica china. El paradigma es de ingeniería sísmica aplicada, geomática y gestión de emergencias, con orientación a decisión y rescate.

**Metodología.** El modelo urbano se obtuvo con fotogrametría oblicua de drones y nubes de puntos LiDAR (registro mediante el algoritmo ICP), y se combinó un modelo 3D de escena real en áreas clave con un modelo de base (bloques generados a partir de datos 2D de marco) en áreas no clave para reducir volumen, costo y tiempo de actualización. La intensidad se calculó con el modelo de distancia mínima a la falla (fórmulas para aceleración y velocidad pico, amplificación por Vs30) y con el de fuente equivalente a partir de réplicas, se verificó contra el sismo histórico de Yinchuan-Pingluo de 1739 (M 8, usado como Mw 8, profundidad de 20 km) y se aplicó al condado de Pingluo (6466 edificios), asignando atributos del censo de riesgo de desastres naturales (estructura, pisos, altura, materiales) y calculando la respuesta de cada edificio con análisis tiempo-historia elastoplástico con amortiguamiento de Rayleigh. Se describe un sensor con cámara en plataforma giratoria disparada por ondas sísmicas, transmisión por 5G y fusión de fotografías con el modelo 3D por parches. No se reporta una prueba de campo del sensor.

**Resultados principales.** La comparación con la intensidad histórica del sismo de 1739 mostró coincidencia en la orientación del eje largo y en la intensidad máxima (X a X+), pero áreas de intensidad calculadas por el modelo mayores que las históricas, con errores de -94,66 % (X a X+), -151,67 % (IX), -608,49 % (VIII) y -133,44 % (VII), que los autores atribuyen a la subestimación histórica, a la amplificación de la cuenca de Yinchuan y a la zona poco habitada del este. Con la intensidad simulada, siete ciudades quedarían en intensidad VII, cinco en VIII, cinco en IX y seis en X a X+. En el condado de Pingluo, con intensidad X a X+, solo 44 de 6466 edificios (0,68 %) quedaron intactos, 702 (10,86 %) con daño leve, 1322 (20,45 %) con daño moderado, 1370 (21,18 %) con daño severo y 3028 (46,83 %) destruidos o colapsados, es decir, cerca de 88 % con daño moderado o mayor. El gemelo propuesto actualiza el daño comparando el modelo 3D previo con el posterior fusionado con las fotos del sensor, y permitiría vigilar réplicas y amenazas secundarias; los autores reconocen que la lectura, el cálculo y la visualización de datos 3D son lentos y que el monitoreo depende de la red.

**Discusión y contribución.** Los autores concluyen que el modelo de escena real en zonas clave y de base en zonas no clave reduce el volumen de datos, la dificultad de actualización y el costo, que el modelo de distancia mínima a la falla es fiable para calcular la intensidad tras simular un sismo histórico y que, ante un sismo extremo con intensidad X a X+, la capacidad sísmica de los edificios es muy insuficiente. Sostienen que el gemelo permite monitorear el inicio, desarrollo y extinción de un desastre y acumular experiencia, y que ofrece base científica para la evaluación de riesgo previa y el rescate posterior. Mencionan que las medidas de refuerzo y aislamiento no se pueden realizar con rapidez y que sin prevención suficiente aumenta la presión sobre la recuperación y reconstrucción. Señalan limitaciones: volumen de datos 3D y dependencia de la red.

**Limitaciones declaradas.** Declaradas: gran volumen de datos 3D con lectura, cálculo y renderizado lentos, y dependencia de la red para el monitoreo en tiempo real. No declaradas: validación de intensidad con errores de área de -94,66 % a -608,49 %; evento simulado, no real; parámetros fijos (Mw 8, profundidad de 20 km); sin prueba de campo del sensor ni de la sincronización; sin validación del daño simulado con daños observados; sin incertidumbre de modelos ni costos.

**Trabajo futuro.** El texto no formula una sección de trabajo futuro explícita; implícitamente, mejorar la velocidad de lectura, cálculo y renderizado, la independencia de la red y la aplicación a escenarios reales.

**Palabras clave.** Declaradas: Digital twin; earthquake damage simulation; earthquake emergency rescue; three-dimensional reality | Inferidas: gemelo digital, sismo urbano, modelo 3D de escena real, intensidad sísmica, daño de edificios, rescate de emergencia, análisis tiempo-historia, fotogrametría oblicua, LiDAR, Ningxia

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un gemelo digital de ciudad que combina un modelo 3D de escena real en zonas clave y de base en zonas no clave, un modelo de intensidad por distancia mínima a la falla, el cálculo de respuesta y daño por edificio y sensores de actualización en tiempo real puede apoyar la evaluación del desastre y las decisiones de rescate tras un sismo, a menor costo y con actualización más rápida.

**Antítesis identificada.** La verificación del modelo de intensidad falla en su propia prueba: las áreas calculadas exceden las históricas en 95 % a 608 %, de modo que afirmar que 'la fiabilidad se determinó' es discutible, y las explicaciones (subestimación histórica, amplificación de cuenca, zona poco habitada) no se contrastan con datos. El daño por edificio se obtiene de propiedades asignadas desde un censo y de un modelo elastoplástico simplificado de masa y rigidez iguales por piso, sin validación con daños observados; el 88 % de edificios con daño moderado o mayor no se compara con un evento real. El 'gemelo' de ciudad es una simulación con un sensor propuesto, sin prueba de campo, sincronización medida ni tiempos de latencia, y los propios autores reconocen que solo es un gemelo de simulación. No se estiman costos del modelo híbrido, ni su efecto sobre decisiones de rescate, ni se considera la recuperación económica, la reapertura de servicios o la continuidad de empresas, a pesar de mencionar la presión sobre la recuperación.

**Síntesis propuesta.** La contribución consistente es un procedimiento integrado y de bajo costo para producir mapas de intensidad y de daño de edificios en una ciudad (modelo 3D híbrido, atenuación por distancia a la falla, respuesta por edificio) y una arquitectura de actualización con sensores, adecuado como componente de simulación de un gemelo de emergencia. Debe leerse como prueba de concepto por simulación, con una validación insuficiente del modelo de intensidad. Para el corpus, la síntesis consiste en extender este gemelo de daño hacia la funcionalidad: asociar el estado de daño de cada edificio con el tiempo de inhabilitación y con las empresas que lo ocupan, validar la distribución de daño con un sismo real y medir la mejora de decisiones de rescate y de reapertura frente a un tablero sin gemelo.

**Áreas grises detectadas.**

1. Validación del modelo de intensidad: la comparación con el sismo de 1739 muestra áreas de intensidad entre 1,9 y 7,1 veces las históricas (errores de -94,66 % a -608,49 %), y la conclusión de aplicabilidad se justifica con razones cualitativas (subestimación histórica, amplificación de cuenca y zonas poco pobladas) que no se verifican con datos.
2. Validación del daño de edificios: la respuesta por edificio se calcula con propiedades asignadas desde un censo y con masa y rigidez iguales por piso, y el resultado (46,83 % de edificios destruidos o colapsados con 88 % en daño moderado o mayor) no se contrasta con ningún sismo real ni con curvas de fragilidad independientes.
3. Evidencia del sensor y de la sincronización: el sistema de cámaras disparado por ondas sísmicas y transmitido por 5G se describe sin prueba de campo, sin tiempos de captura y transmisión ni precisión de la comparación 3D antes y después, de modo que la 'actualización en tiempo real' del gemelo no está demostrada.
4. Valor para decisiones: se afirma que el gemelo mejora la eficacia del rescate y reduce víctimas, pero no se evalúa con indicadores (tiempo de despliegue, víctimas, recursos asignados) ni se compara con un esquema sin gemelo; la recuperación posterior se menciona sin modelarse.

**Puntos oscuros aclarados.** Llama la atención que un artículo cuya validación del modelo de intensidad arroja errores de área de hasta 608 % concluya que el modelo es fiable, y que el gemelo se presente como herramienta de decisión de rescate sin medir ningún resultado de decisión. Una explicación plausible es que los autores consideran que la coincidencia de la orientación del eje largo y de la intensidad máxima es suficiente para fines de planificación, y que las áreas históricas están sesgadas a la baja por observación limitada de hace casi tres siglos, de modo que el 'error' reflejaría la imprecisión de la referencia. Esto sugiere que la verificación es débil por falta de un sismo moderno instrumentado, y que los resultados de daño por edificio solo son orientativos. Además, que la simulación asigne 88 % de edificios a daño moderado o mayor con intensidad X a X+ y sin considerar la variabilidad de calidad de construcción, hace probable una sobreestimación que, de usarse para planificar recursos, desviaría la asignación. La ausencia de funcionalidad, de empresas y de tiempos de recuperación confirma que el gemelo está orientado a la fase de emergencia.

**Ideas propositivas novedosas.**

1. Validación del gemelo de daño con un sismo instrumentado reciente: aplicar el modelo de intensidad y de daño a un sismo moderno con mapas de intensidad instrumental y con inspecciones de daño por edificio (por ejemplo, el sismo de Turquía de 2023 o el de Maduo de 2021 que los autores citan), y estimar errores de área de intensidad y de clasificación de daño con matrices de confusión. Fundamento: la única verificación presentada usa un sismo de 1739 con grandes diferencias. Verificabilidad: datos públicos de intensidad instrumental e inspecciones. Utilidad: define la confianza del gemelo antes de usarlo en decisiones de emergencia y orienta la calibración de parámetros.
2. Del daño a la funcionalidad y a la reapertura: asociar cada nivel de daño de edificio con un tiempo de inhabilitación esperado y con las empresas y servicios que alberga (catastro, registros mercantiles), y calcular tiempos de reapertura esperados por escenario, para priorizar inspección y apoyo. Fundamento: el gemelo estima daño pero no vincula el daño con uso económico. Verificabilidad: reconstrucción retrospectiva con registros de reapertura de empresas en un evento real. Utilidad: convierte el mapa de daño en un insumo de recuperación productiva y permite comparar el tablero de daño con un gemelo para decisiones de reapertura.

**Relaciones poco exploradas.**

1. Calidad del modelo de intensidad (condiciona) la estimación de daño por edificio: el error de área de intensidad se propaga al número de edificios con daño moderado o mayor, aunque el artículo no lo cuantifica.
2. Dependencia de la red y volumen de datos 3D (limitan) la actualización en tiempo real del gemelo: los autores reconocen que la lectura, el cálculo y el renderizado son lentos y que el monitoreo requiere conectividad, que puede fallar después de un sismo.

**Robustez argumentativa:** 2.8/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 3/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 6/10 — Ofrece una cadena metodológica integrada, desde modelo urbano 3D de bajo costo hasta mapas de intensidad y de daño por edificio y actualización por sensores, aplicada a un caso regional de China y vinculada a decisiones de rescate. Su valor para el corpus es alto por la coincidencia temática (gemelo, sismo urbano, emergencia); se reduce por la validación débil del modelo de intensidad, la falta de pruebas de campo del sensor, la ausencia de comparación con un esquema sin gemelo y la no inclusión de recuperación económica.

**Conexiones inter-documentales.**

- **CONFIRMA** D048 (Gemelo digital como imagen operativa común para respuesta sísmica): ambos estiman daño por edificio y necesidades de respuesta con gemelos urbanos y escenarios sísmicos; proceden de contextos y grupos distintos (Ningxia, China, y Kocaeli, Türkiye) [juicio del analista]
- **COMPLEMENTA** D064 (Gemelo digital, monitoreo sísmico y 5G con cómputo en el borde): D034 modela intensidad y daño por edificio con actualización por sensores; D064 aporta la arquitectura 5G y de borde para actualizar gemelos con baja latencia [juicio del analista]
- **PRECEDE** D013 (Gemelos digitales para gestión posdesastre y recuperación): es citado por D013 (verificado por coincidencia de título) [citación verificada]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 21 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Conclusión no respaldada por la verificación (Se concluye que el modelo es fiable pese a errores de área de intensidad de -94,66 % a -608,49 % frente a la referencia histórica (Sec. 3.1.3, p. 12; Sec. 5, p. 19)); Apelación a la novedad / a la tecnología (Se afirma que el gemelo mejora la eficacia del rescate y reduce víctimas sin evaluar resultados de decisión (Sec. 4.3, p. 18)); Generalización apresurada (Se infiere la insuficiencia sísmica de las edificaciones a partir de una simulación de un solo sismo extremo en un condado (Sec. 5, p. 19))
- **Bradford-Hill:** No aplica: es una simulación con verificación parcial; la relación entre el uso del gemelo y mejores decisiones o menos víctimas no se estima con datos ni diseño comparativo.
- **TRL asignado:** 4 — 'The elastic-plastic time history analysis method was used to calculate the seismic response results of each building' (p. 19)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (19 páginas más referencias). Las figuras de mapas y de la ruta técnica no son legibles en la extracción; las cifras de las tablas 1 y 2 se tomaron del texto. El porcentaje de 88,46 % con daño moderado o mayor es cálculo del analista (20,45 + 21,18 + 46,83).

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un gemelo digital de ciudad que combina un modelo 3D de escena real en zonas clave y de base en zonas no clave, un modelo de intensidad por distancia mínima a la falla, el cálculo de respuesta y daño por edificio y sensores de actualización en tiempo real puede apoyar la evaluación del desastre y las decisiones de rescate tras un sismo, a menor costo y con actualización más rápida.  | La verificación del modelo de intensidad falla en su propia prueba: las áreas calculadas exceden las históricas en 95 % a 608 %, de modo que afirmar que 'la fiabilidad se determinó' es discutible, y las explicaciones (subestimación histórica, amplificación de cuenca, zona poco habitada) no se contrastan con datos. El daño por edificio se obtiene de propiedades asignadas desde un censo y de un modelo elastoplástico simplificado de masa y rigidez iguales por piso, sin validación con daños observados; el 88 % de edificios con daño moderado o mayor no se compara con un evento real. El 'gemelo' de ciudad es una simulación con un sensor propuesto, sin prueba de campo, sincronización medida ni tiempos de latencia, y los propios autores reconocen que solo es un gemelo de simulación. No se estiman costos del modelo híbrido, ni su efecto sobre decisiones de rescate, ni se considera la recuperación económica, la reapertura de servicios o la continuidad de empresas, a pesar de mencionar la presión sobre la recuperación.  | La contribución consistente es un procedimiento integrado y de bajo costo para producir mapas de intensidad y de daño de edificios en una ciudad (modelo 3D híbrido, atenuación por distancia a la falla, respuesta por edificio) y una arquitectura de actualización con sensores, adecuado como componente de simulación de un gemelo de emergencia. Debe leerse como prueba de concepto por simulación, con una validación insuficiente del modelo de intensidad. Para el corpus, la síntesis consiste en extender este gemelo de daño hacia la funcionalidad: asociar el estado de daño de cada edificio con el tiempo de inhabilitación y con las empresas que lo ocupan, validar la distribución de daño con un sismo real y medir la mejora de decisiones de rescate y de reapertura frente a un tablero sin gemelo.  | 2.8/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Gemelo digital de ciudad con sismo' es un modelo 3D de la ciudad vinculado a modelos de intensidad y de daño que se actualiza con sensores; 'daño' se mide con un índice de 0 a 1 en cinco niveles.
- **P2 Supuestos:** Supone que el modelo de atenuación y las propiedades asignadas desde el censo representan el comportamiento real, que el sensor con cámara capta el daño y que la información acelera el rescate.
- **P3 Evidencia:** La evidencia es una simulación de un sismo histórico con verificación parcial de intensidad y un cálculo de daño de 6466 edificios, sin validación con daños observados.
- **P4 Consecuencias:** Si es cierto, las autoridades pueden planificar el rescate con mapas de daño por edificio; si es falso, pueden asignar recursos con base en una sobreestimación o subestimación de daño.
- **P5 Contraejemplos:** No se examinan sismos reales con datos de daño, ni casos en que el gemelo haya fallado por falta de red, ni la comparación con evaluación rápida convencional.
- **P6 Alternativas:** Alternativas: que un mapa de intensidad instrumental y un inventario de edificios basten para la decisión; que el costo del modelo 3D supere el beneficio; que la calidad del censo limite el resultado.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Edificios simulados en el condado de Pingluo | 6466 | edificios | Todos dentro de intensidad X a X+ | Sec. 4.2, p. 15-16 | Texto | Alta | Sismo simulado de 1739 |
| Edificios intactos | 44 | edificios | 0,68 % del total | Tabla 2, p. 17 | Tabla | Alta | Índice de daño de 0 a 0,1 |
| Edificios con daño leve | 702 | edificios | 10,86 % | Tabla 2, p. 17 | Tabla | Alta | Índice de 0,1 a 0,3 |
| Edificios con daño moderado | 1322 | edificios | 20,45 % | Tabla 2, p. 17 | Tabla | Alta | Índice de 0,3 a 0,55 |
| Edificios con daño severo | 1370 | edificios | 21,18 % | Tabla 2, p. 17 | Tabla | Alta | Índice de 0,55 a 0,85 |
| Edificios destruidos o colapsados | 3028 | edificios | 46,83 %; 88,46 % con daño moderado o mayor (cálculo del analista) | Tabla 2, p. 17 | Tabla | Alta | Sin validación con daño observado |
| Error de área de la intensidad X a X+ | -94,66 | % | Área del modelo de 6035,33 km2 frente a 3100,37 km2 histórica | Tabla 1, p. 13 | Tabla | Alta | Sobreestimación |
| Error de área de la intensidad VIII | -608,49 | % | 64.666,17 km2 frente a 9127,29 km2 | Tabla 1, p. 13 | Tabla | Alta | Mayor error |
| Magnitud y profundidad usadas en la simulación | 8 / 20 | Mw / km | Sismo de Yinchuan-Pingluo de 1739 | Sec. 3.1.1, p. 11 | Texto | Alta | Valores fijos |
| Ciudades por rango de intensidad | 7 / 5 / 5 / 6 | ciudades | Intensidades VII / VIII / IX / X a X+ | Sec. 4.2, p. 15-16 | Texto | Alta | Simulación |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'The elastic-plastic time history analysis method was used to calculate the seismic response results of each building' (p. 19) | Componentes validados parcialmente en simulación; el sistema de sensores y la sincronización no se probaron en campo. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'If the early prevention and preparation work is insufficient, it is difficult to respond promptly when an earthquake occurs' (p. 20) | Sin análisis de mercado, costos ni modelo de negocio; orientación a gestión pública de emergencias. |
| IRL | 3 | Sí | 'The real-time monitoring of an earthquake disaster is dependent on the network' (p. 20) | Integración de modelos 3D, simulación y sensores por 5G descrita como arquitectura; limitaciones de red reconocidas; sin pruebas de integración. |
| DRL | 3 | Sí | 'Few studies have been conducted on digital twin technology for emergency rescue management of earthquake disasters' (p. 3) | Necesidad argumentada con literatura; sin demanda de usuarios medida. |
| SRL | 1.0 | Sí | Componentes: Modelo urbano 3D híbrido y simulación de daño (TRL 4), Sensores de actualización por cámara y 5G (TRL 2) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 9.0; ÷9 → 1.00; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 4 con BRL 1 e IRL 3: simulación con verificación parcial y sensores sin prueba, sin costos ni evidencia de efecto sobre la decisión. · Estrategia de salida: Validación con un sismo real, pruebas de campo de los sensores y evaluación de decisiones con y sin gemelo.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Conclusión no respaldada por la verificación | Se concluye que el modelo es fiable pese a errores de área de intensidad de -94,66 % a -608,49 % frente a la referencia histórica (Sec. 3.1.3, p. 12; Sec. 5, p. 19) | Afirmación opuesta a la evidencia presentada |
| Apelación a la novedad / a la tecnología | Se afirma que el gemelo mejora la eficacia del rescate y reduce víctimas sin evaluar resultados de decisión (Sec. 4.3, p. 18) | Beneficio asumido |
| Generalización apresurada | Se infiere la insuficiencia sísmica de las edificaciones a partir de una simulación de un solo sismo extremo en un condado (Sec. 5, p. 19) | Resultados dependen de supuestos no validados |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Uso del gemelo de daño → decisiones de rescate más eficaces | Argumento de diseño; sin datos de decisión | Plausibilidad | Fuerza, experimento, comparación | Calidad del modelo, conectividad, capacidad institucional | 1 | Hipótesis no probada |
| Intensidad sísmica X a X+ → daño moderado o mayor en 88 % de edificios | Resultado de simulación con propiedades asignadas | Coherencia con ingeniería sísmica | Validación con eventos reales | Calidad constructiva, efecto de sitio | 3 | Simulación no validada |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Validación del modelo de intensidad y del daño de edificios con sismos instrumentados y daños observados | Crítico | Media | 9 |
| Tecnológico | Pruebas de campo de sensores, latencia, sincronización y operación con red degradada | Crítico | Media | 8 |
| Conocimiento | Vínculo entre daño de edificios, funcionalidad y reapertura de empresas y servicios | Crítico | Media | 9 |
| Mercado | Costos de modelación 3D híbrida y de operación frente a la mejora de decisiones | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Concepto de gemelo digital de ciudad con desastre sísmico | Diagrama | Ciudad física, ciudad virtual, análisis y percepción dinámica | 5 componentes | Alta |
| Fig. 3 | Modelo 3D de base local de la ciudad | Imagen | Modelo generado a partir de datos 2D de marco | No aplica | Baja |
| Fig. 4 | Ruta técnica de construcción del gemelo | Diagrama | Flujo de datos y módulos | No aplica | Media |
| Fig. 5 | Resultados de intensidad del modelo de atenuación | Mapa | Isosistas calculadas frente a históricas | X a X+; IX; VIII; VII | Alta |
| Tabla 1 | Comparación de intensidad calculada con la histórica | Tabla | Áreas por nivel de intensidad y errores | -94,66 % a -608,49 % | Alta |
| Fig. 8 | Distribución de daño de edificios en Pingluo | Mapa 3D | Daño por edificio | 6466 edificios | Alta |
| Tabla 2 | Daño de edificios | Tabla | Cinco niveles de daño | 44; 702; 1322; 1370; 3028 | Alta |
| Fig. 9 | Fusión de foto de ángulo predefinido y parche del modelo 3D | Imagen | Actualización de daño con sensor | No aplica | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Pantoja-Rosero et al. (modelos de elementos finitos a partir de imágenes para mampostería) | No especificado en documento | Academia | Evaluación posterremoto automatizada | Automatización | Un solo tipo de edificio | Creciendo |
| Hoskere et al., Levine y Spencer (drones para evaluar daño posterremoto) | No especificado en documento | Academia | Reconstrucción 3D y evaluación de daño con imágenes | Evidencia en campo | Sin gemelo de ciudad | Creciendo |
| Kusakabe et al. (modelo urbano de alta fidelidad con simulación multifísica) | Japón | Academia | Simulación sísmica urbana de alta fidelidad | Capacidad de cómputo | Costo computacional | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Índice de daño de edificios (0 a 1) y distribución en cinco niveles
- **X:** Intensidad sísmica simulada y propiedades de los edificios (estructura, pisos, altura, materiales)
- **Z (controles):** Tipo de estructura, edad y sitio (Vs30)
- **Datos:** 6466 edificios del condado de Pingluo; sismo histórico de 1739 simulado
- **Método:** Modelos de atenuación de intensidad y análisis elastoplástico tiempo-historia
- **Efecto reportado:** 46,83 % de edificios destruidos o colapsados; 88,46 % con daño moderado o mayor
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin análisis de sensibilidad de parámetros ni validación con daños reales

| Vacío | Tipo | Descripción |
|---|---|---|
| V-034-01 | TERR | Región de Ningxia, China; sin otras regiones ni América Latina |
| V-034-02 | POBL | Sin población, hogares ni empresas afectadas |
| V-034-03 | TEMP | Fase de emergencia y de daño inmediato; sin horizonte de recuperación |
| V-034-04 | MET | Validación de intensidad con errores de área grandes y daño sin contraste |
| V-034-05 | VAR | Faltan variables de funcionalidad, tiempo de inhabilitación, costos y empresas |
| V-034-06 | TEOR | Sin teoría de recuperación posdesastre ni de decisión bajo incertidumbre |
| V-034-07 | CAUS | Sin evidencia causal de efecto del gemelo sobre decisiones o víctimas |
