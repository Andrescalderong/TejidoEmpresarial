# FB-L01-010 | D010 — Real-time earthquake magnitude prediction using designed machine learning ensemble trained on real and CTGAN generated synthetic data

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/1-s2.0-S1674984724001204-main.pdf` · 19 páginas · Relevancia para el eje del corpus: **Adyacente** (Alerta sísmica temprana con aprendizaje automático para estimar magnitud a partir de los primeros segundos de la onda P; es un insumo de decisión previo al impacto, pero no trata gemelos digitales, IoT en sentido estricto ni recuperación empresarial.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-010 / D010
- **Tipo de recurso:** Artículo científico (journal peer-reviewed)
- **Referencia APA 7:** Joshi, A., Raman, B., & Mohan, C. K. (2025). Real-time earthquake magnitude prediction using designed machine learning ensemble trained on real and CTGAN generated synthetic data. *Geodesy and Geodynamics*, *16*(3), 350-368. https://doi.org/10.1016/j.geog.2024.10.001
- **Autores:** Joshi, Anushka (59826753300); Raman, Balasubramanian (23135470700); Mohan, C. Krishna (55325461200)
- **Afiliaciones:** Department of Computer Science and Engineering, Indian Institute of Technology, Uttarakhand, Roorkee, India; Department of Computer Science and Engineering, Indian Institute of Technology, Telangana, Hyderabad, India
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** Geodesy and Geodynamics · vol. 16(3)
- **Identificador persistente:** DOI 10.1016/j.geog.2024.10.001 · ISSN 16749847
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85216467087&doi=10.1016%2fj.geog.2024.10.001&partnerID=40&md5=14be615b348ac4daa560963eecae881f
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 19

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Desarrollar MagPred, un modelo de ensamble apilado que estima la magnitud de un sismo con los primeros 3, 4 y 5 segundos de la onda P registrada en una estación, y aprovechar redes generativas adversarias condicionales para datos tabulares (CTGAN) con el fin de generar datos sintéticos de terremotos de magnitud alta, que son escasos, de modo que se reduzca el error de predicción en el régimen de alto impacto y se mejoren las alertas tempranas y la respuesta de rescate. El trabajo evalúa además el desempeño con múltiples estaciones y en una región distinta, India y Nepal.

**Pregunta de investigación.** [INFERIDA] ¿Reduce el error de predicción de la magnitud, en particular para eventos grandes, entrenar un ensamble de modelos con datos reales y sintéticos generados por CTGAN frente a entrenar solo con datos reales y frente a relaciones de regresión tradicionales, y generaliza ese modelo a otra región sísmica?

**Marco teórico.** El marco combina la sismología de alerta temprana (EEW), con relaciones empíricas entre la magnitud y parámetros de la onda P como el periodo característico tau-c y el desplazamiento máximo del suelo (PGD) de Kanamori, Wu y Kumar, con el aprendizaje automático de tablas (aumento de datos, redes generativas adversarias tipo CTGAN con normalización específica por modo, ensambles de boosting y bosques aleatorios) y la optimización metaheurística de hiperparámetros con el Sanitized Grey Wolf Optimizer. Incluye 34 características de dominio del tiempo, de frecuencia y de ondículas más una característica del sitio (velocidad de onda de corte VS30). El paradigma es predictivo y orientado al desempeño estadístico, no a explicación física.

**Metodología.** Se usan 18.994 registros reales de la red K-NET (Japón) desde junio de 1996, componente vertical, con distancia epicentral menor de 200 km y magnitudes de 3,0 a 9,0 MJMA, preprocesados con corrección de línea base, filtro pasabanda Butterworth de cuarto orden (0,5 a 45 Hz) y detección de la onda P por STA/LTA. Los datos se dividen 70:21:9 en 13.295 registros de entrenamiento, 3.989 de prueba y 1.710 de validación. Para cada ventana de 3, 4 o 5 s se extraen 34 características. CTGAN se entrena durante 50 épocas por rango de magnitud (5 a 6, 6 a 7 y 7 a 9 MJMA) y genera 6.612, 5.211 y 6.621 registros sintéticos para SE3, SE4 y SE5, que se suman a los reales (conjuntos mixtos de 25.606, 24.205 y 25.615). El ensamble de primer nivel promedia XGB, SGWO-XGB, LGBM y CatBoost entrenados con datos reales y mixtos; en el segundo nivel una regla por tramos selecciona el resultado final (promedio de RF si la estimación está entre 2,9 y 3,9; promedio de XGB, CatB y SGWO-XGB entrenado con datos mixtos entre 4,0 y 6,0; promedio de todos los modelos por encima de 6,0). La evaluación usa MAE y RMSE, comparación con modelos NN, SVR y Tab-Net, con relaciones de regresión de PGD y tau-c, y con Zhu et al., más pruebas multiestación (terremotos de Kumamoto, Osaka, costa de Fukushima) y entre regiones con cinco eventos de India y Nepal (66 registros).

**Resultados principales.** El error absoluto medio del conjunto de prueba para una estación con los 3, 4 y 5 s de onda P es 0,41; 0,40 y 0,38 MJMA, con error medio de 0,03±0,56; 0,01±0,54 y 0,01±0,53 MJMA. Los modelos entrenados con datos mixtos tienen menor error que los entrenados solo con datos reales, y el ensamble supera a NN, SVR y Tab-Net y a las relaciones de regresión. En el estudio multiestación, las magnitudes ponderadas por estación se acercan más al valor oficial que las no ponderadas: por ejemplo, para el sismo principal de Kumamoto (7,3 MJMA) la estimación no ponderada es 6,3 a 6,6 y la ponderada 6,8 a 7,0; para Osaka (6,1) la no ponderada es 5,6 y la ponderada 6,0 a 6,6. En la validación entre regiones con eventos de India y Nepal de MW 4,0 a 5,7, el error absoluto medio por evento fluctúa entre 0,28 y 1,68 (RMSE hasta 1,69), con magnitudes medias predichas de 5,4 a 5,9 aun para eventos de MW 4,0 y 4,2 (error absoluto medio de 1,54 a 1,68 y 1,28 a 1,37, respectivamente); para el evento de MW 5,2 el error medio es de -0,32±0,19; -0,31±0,20 y -0,30±0,24 MW. Los autores dejan el código y el conjunto de prueba disponibles en un repositorio público.

**Discusión y contribución.** Los autores sostienen que CTGAN corrige el desbalance de eventos de alta magnitud, que los modelos entrenados con datos mixtos reducen el error y que el ensamble supera a las alternativas de aprendizaje automático y a las relaciones de regresión clásicas, con aplicación potencial a sistemas de alerta temprana en zonas con pocos datos sísmicos. Advierten que equilibrar totalmente la distribución destruiría la correlación entre las características y la magnitud, por lo que se ajustó un balance parcial, y que generar datos sintéticos requiere recursos computacionales y fidelidad estadística. Señalan como trabajo futuro métodos más sofisticados para tratar el desbalance y consideran que la validación entre regiones muestra la eficacia del enfoque.

**Limitaciones declaradas.** Declaradas parcialmente: costo computacional de generar datos sintéticos con GAN y necesidad de que los datos generados conserven las propiedades estadísticas de los reales.

**Trabajo futuro.** Introducir metodologías más sofisticadas para el problema de desbalance de datos y explorar aplicaciones donde exista escasez de datos sísmicos.

**Palabras clave.** Declaradas: CTGAN; Earthquake; Machine learning; Magnitude; Synthetic data | Inferidas: alerta sísmica temprana, onda P, magnitud, CTGAN, desbalance de datos, ensamble apilado, XGBoost, optimizador de lobos grises, K-NET, validación entre regiones

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Entrenar un ensamble con datos reales y datos sintéticos generados por CTGAN reduce el error de estimación de magnitud con los primeros segundos de la onda P, incluso para los eventos grandes escasos, y supera a las relaciones de regresión y a otros modelos de aprendizaje automático.

**Antítesis identificada.** El diseño de la evaluación admite sobreoptimismo: los registros de varias estaciones de un mismo evento comparten magnitud, y la división 70:21:9 se hace por registros y no por eventos, lo que puede filtrar información de un sismo entre entrenamiento y prueba. La regla por tramos del segundo nivel se justifica con tablas comparativas sobre los conjuntos de prueba y validación, es decir, se selecciona el modelo con el conjunto con el que luego se informa el desempeño. En la validación entre regiones, el error absoluto medio llega a 1,68 unidades de magnitud y los eventos pequeños se sobreestiman en más de un punto, resultado que contradice la presentación del resumen como evidencia de generalización. Los datos son offline y no hay medición de latencia ni de tiempo de alerta, de modo que 'tiempo real' en el título no se demuestra.

**Síntesis propuesta.** El trabajo muestra que el aumento tabular con CTGAN puede ser útil como técnica de regularización para el régimen de magnitud alta dentro de una base de datos homogénea, pero no demuestra que el modelo funcione de forma robusta fuera de ella ni que ofrezca ventaja operativa en una alerta real. La síntesis práctica es tratarlo como evidencia preliminar, que exige repetir la evaluación con partición por evento, con selección del modelo en un conjunto independiente y con pruebas de latencia y tiempo de alerta, antes de convertirlo en insumo para decisiones de protección de instalaciones productivas, y orientar la inversión hacia la calibración regional y la medición del valor económico de la alerta.

**Áreas grises detectadas.**

1. Partición de datos: se describe una división 70:21:9 de 18.994 registros sin precisar si es por evento o por registro; si las estaciones de un mismo sismo están en entrenamiento y prueba, la magnitud del evento se aprende de otras estaciones y el error se subestima.
2. Selección del modelo con datos de prueba: las Tablas 3 a 5 comparan modelos en el conjunto de prueba y validación para decidir la regla por tramos (umbrales 2,9, 3,9, 4,0, 6,0 y 6,2), de modo que el desempeño final de prueba no es independiente de la selección.
3. Validación entre regiones: el error absoluto medio por evento va de 0,28 a 1,68 y las magnitudes medias predichas son 5,4 a 5,9 aun para eventos de MW 4,0 y 4,2; el texto resume 'high potential for wide application', pese a un sesgo claro hacia sobreestimar eventos pequeños, con solo 66 registros.
4. Calidad de los sintéticos: se dice que CTGAN conserva las correlaciones (Fig. 5), pero no se informan pruebas estadísticas de fidelidad ni se comprueba que los sintéticos no repitan registros reales; además la distribución final de 500 registros por categoría 'no es factible' según el propio texto.
5. Tiempo real y utilidad operativa: el modelo se evalúa con registros archivados; no se calcula el tiempo de alerta ni la zona ciega (distancia en la que el aviso llega después de la onda S), que determina el valor de la alerta.

**Puntos oscuros aclarados.** La mejora de MAE de 0,41 a 0,38 MJMA al pasar de 3 a 5 s es pequeña frente a la desviación de 0,53 a 0,56, lo que indica que la información adicional de dos segundos aporta poco con este conjunto de características, a la vez que sacrifica tiempo de alerta. Esto sugiere que el cuello de botella no es la ventana sino la dispersión intrínseca de la relación entre onda P y magnitud, que ningún ajuste del modelo elimina. Los resultados multiestación muestran además subestimación sistemática de eventos grandes sin ponderación (por ejemplo, 6,3 a 6,6 para un evento de 7,3), consistente con la saturación de magnitud con ventanas cortas; la ponderación mejora porque da más peso a estaciones cercanas. Interpretado así, el aporte de CTGAN sería sobre todo una calibración del sesgo en la cola alta de la distribución, y no un avance en el contenido físico del pronóstico.

**Ideas propositivas novedosas.**

1. Valor económico de la alerta para sitios productivos: acoplar el modelo de magnitud con un modelo costo-pérdida que, para cada instalación (planta, almacén, hospital), calcule el umbral de magnitud y de distancia que minimiza la suma de costo de falsas alarmas y de pérdida evitada al detener procesos o cerrar válvulas. Fundamento: el artículo se enfoca en el error de magnitud y no en la decisión; el valor surge del umbral de acción. Verificabilidad: reproducir con Kumamoto y costa de Fukushima, con costos estimados por industria, y comparar con una regla fija de alerta. Utilidad: define cuándo conviene que una empresa active protocolos automáticos y cuantifica el beneficio de la alerta.
2. Validación por evento con ensayos de cola: repetir el experimento dejando fuera eventos completos de magnitud mayor a 6,5 y comparar CTGAN con SMOTE, reponderación y modelos cuantílicos, informando intervalos de confianza por evento y errores por rango de distancia. Fundamento: el beneficio más importante del enfoque está en la cola alta, donde hay pocos eventos independientes y por tanto alta variabilidad. Verificabilidad: validación cruzada por grupos con los mismos datos de K-NET. Utilidad: determina si los datos sintéticos añaden información real o solo ajustan el sesgo y orienta qué incorporar a sistemas operativos.

**Relaciones poco exploradas.**

1. Ventana de onda P (3 a 5 s) (se asocia con) un aumento marginal de precisión pero una reducción del tiempo de alerta: el costo en minutos de aviso para instalaciones lejanas no se cuantifica.
2. Distancia epicentral (modula) el error del modelo y la utilidad de la alerta: las figuras de error frente a distancia sugieren heterocedasticidad, y la zona ciega depende de la misma variable.

**Robustez argumentativa:** 4.8/10 (ponderación 30/30/25/15) — consistencia lógica 6/10; calidad de la evidencia 5/10; validez de inferencias causales 4/10; generalizabilidad 3/10.

**Valor estratégico:** 5/10 — Es un estudio técnico sólido en términos de comparación de modelos dentro de su base de datos y con código abierto, que informa claramente los errores por tramos. Para el corpus es útil como componente de alerta temprana previo al evento, pero su evidencia de generalización es débil y no mide el valor para decisiones empresariales ni de infraestructura.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Cherry picking (Selección de la regla por tramos con las mismas muestras de prueba y validación que luego reportan el desempeño (Sec. 4.2, Tablas 3-5)); Generalización apresurada (El estudio entre regiones con 66 registros se presenta como prueba de eficacia amplia pese a errores absolutos medios de hasta 1,68 (Sec. 4.3, Tabla 8)); Apelación a la novedad (Se atribuye el mérito a la técnica GAN sin comparar con otros métodos de aumento (SMOTE, reponderación) (Introducción, p. 2))
- **Bradford-Hill:** Las características de onda P y la magnitud tienen plausibilidad física y coherencia con la sismología (tau-c, PGD); la relación entre uso de datos sintéticos y menor error no se aísla con experimentos controlados por evento, por lo que fuerza, consistencia y experimento son limitados.
- **TRL asignado:** 4 — 'The source codes, along with the test dataset, are available for download' y evaluación con datos históricos de K-NET (p. 2, 6)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído; ecuaciones y tablas con símbolos degradados por la extracción. Los valores de las Tablas 3 a 7 se leen parcialmente y se usan solo los citados en el texto.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Entrenar un ensamble con datos reales y datos sintéticos generados por CTGAN reduce el error de estimación de magnitud con los primeros segundos de la onda P, incluso para los eventos grandes escasos, y supera a las relaciones de regresión y a otros modelos de aprendizaje automático.  | El diseño de la evaluación admite sobreoptimismo: los registros de varias estaciones de un mismo evento comparten magnitud, y la división 70:21:9 se hace por registros y no por eventos, lo que puede filtrar información de un sismo entre entrenamiento y prueba. La regla por tramos del segundo nivel se justifica con tablas comparativas sobre los conjuntos de prueba y validación, es decir, se selecciona el modelo con el conjunto con el que luego se informa el desempeño. En la validación entre regiones, el error absoluto medio llega a 1,68 unidades de magnitud y los eventos pequeños se sobreestiman en más de un punto, resultado que contradice la presentación del resumen como evidencia de generalización. Los datos son offline y no hay medición de latencia ni de tiempo de alerta, de modo que 'tiempo real' en el título no se demuestra.  | El trabajo muestra que el aumento tabular con CTGAN puede ser útil como técnica de regularización para el régimen de magnitud alta dentro de una base de datos homogénea, pero no demuestra que el modelo funcione de forma robusta fuera de ella ni que ofrezca ventaja operativa en una alerta real. La síntesis práctica es tratarlo como evidencia preliminar, que exige repetir la evaluación con partición por evento, con selección del modelo en un conjunto independiente y con pruebas de latencia y tiempo de alerta, antes de convertirlo en insumo para decisiones de protección de instalaciones productivas, y orientar la inversión hacia la calibración regional y la medición del valor económico de la alerta.  | 4.8/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Magnitud' es la estimación de MJMA/MW desde los primeros segundos de la onda P; 'datos sintéticos' son registros tabulares generados con CTGAN a partir de las 34 características.
- **P2 Supuestos:** Supone que la división de registros no filtra información entre conjuntos, que los sintéticos preservan la relación física y que un modelo entrenado en Japón es transferible a India y Nepal.
- **P3 Evidencia:** La evidencia son MAE y RMSE en un conjunto de prueba de 3.989 registros y en pocos eventos de otra región; los sintéticos solo se evalúan por correlaciones.
- **P4 Consecuencias:** Si es cierto, los sistemas de alerta podrían mejorar la estimación de eventos grandes; si es falso, se tendrían falsas confianzas en regiones con distinto contexto tectónico.
- **P5 Contraejemplos:** Los eventos pequeños de India y Nepal con errores mayores a un punto de magnitud son contraejemplos de la generalización.
- **P6 Alternativas:** Alternativas: relaciones físicas con corrección regional, modelos bayesianos con incertidumbre, aprendizaje por transferencia o redes neuronales sobre formas de onda.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Registros reales de K-NET | 18994 | registros | Datos desde junio de 1996, componente vertical | Sec. 3, p. 6 | Texto | Alta | No se precisa el número de eventos |
| Registros de entrenamiento | 13295 | registros | 70 % del conjunto real | Sec. 3, p. 6 | Texto | Alta | División por registros |
| Registros de prueba | 3989 | registros | 21 % del conjunto real | Sec. 3, p. 6 | Texto | Alta | Posible fuga entre eventos |
| Registros de validación | 1710 | registros | 9 % del conjunto real | Sec. 3, p. 6 | Texto | Alta | Usados también para elegir reglas |
| Características de entrada | 34 | variables | Dominio del tiempo, frecuencia, ondículas y sitio | Sec. 3, p. 7 | Texto | Alta | Selección por búsqueda en rejilla |
| Registros sintéticos SE3/SE4/SE5 | 6612 / 5211 / 6621 | registros | Generados con CTGAN, 50 épocas | Tabla 1, p. 6 | Tabla | Alta | Sin pruebas formales de fidelidad |
| Conjuntos mixtos SE3/SE4/SE5 | 25606 / 24205 / 25615 | registros | Reales más sintéticos | Tabla 3, p. 10 | Tabla | Alta | Coherente con las sumas |
| MAE de prueba con 3 s de onda P | 0.41 | MJMA | Predicción de una estación | Resumen, p. 1 | Texto | Alta | Intervalos de confianza no informados |
| MAE de prueba con 4 s de onda P | 0.40 | MJMA | Predicción de una estación | Resumen, p. 1 | Texto | Alta | Mejora marginal |
| MAE de prueba con 5 s de onda P | 0.38 | MJMA | Predicción de una estación | Resumen, p. 1 | Texto | Alta | Reduce el tiempo de alerta |
| Error medio ± desviación (5 s) | 0.01 ± 0.53 | MJMA | Conjunto de prueba | Sec. 5, p. 16 | Texto | Alta | Desviación elevada frente a la media |
| Eventos y registros de validación entre regiones | 5 / 66 | eventos / registros | India y Nepal, MW 4,0 a 5,7 | Tabla 1, p. 6 | Tabla | Alta | Muestra muy pequeña |
| MAE del evento Chamoli (MW 4,0) | 1.54-1.68 | MW | Validación entre regiones IRE3-IRE5 | Tabla 8, p. 13 | Tabla | Alta | Sobreestimación sistemática |
| Estimación ponderada del sismo principal de Kumamoto (MJMA 7,3) | 6.8-7.0 | MJMA | Frente a 6,3-6,6 sin ponderar | Tabla 9, p. 13 | Tabla | Alta | Una sola realización por evento |
| Estaciones en el evento de Kumamoto (principal) | 45 | estaciones | Prueba multiestación | Tabla 9, p. 13 | Tabla | Alta | Selección de eventos ilustrativos |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'The source codes, along with the test dataset, are available for download' y evaluación con datos históricos de K-NET (p. 2, 6) | Componentes validados en laboratorio computacional con datos archivados; sin despliegue en una red de alerta ni evaluación de latencia (TRL 4). |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'The study can be effective where less seismic data is available' (p. 1) | Concepto de utilidad sin modelo de negocio ni usuario validado. |
| IRL | N/A | No | No aplica | No se integra con sistemas de transmisión o actuación. |
| DRL | N/A | No | No aplica |  |
| SRL | N/A | No | Requiere IRL entre componentes | No calculable sin IRL |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | N/A | N/A |
| Gap BRL-DRL | N/A | N/A |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 1: investigación sin ruta a su uso operativo por agencias o empresas. · Estrategia de salida: Evaluar en un sistema de alerta real, medir latencia y tiempo de alerta y definir modelo de adopción con operadores.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Cherry picking | Selección de la regla por tramos con las mismas muestras de prueba y validación que luego reportan el desempeño (Sec. 4.2, Tablas 3-5) | Sobrestima el desempeño en datos nuevos |
| Generalización apresurada | El estudio entre regiones con 66 registros se presenta como prueba de eficacia amplia pese a errores absolutos medios de hasta 1,68 (Sec. 4.3, Tabla 8) | Limita la validez externa |
| Apelación a la novedad | Se atribuye el mérito a la técnica GAN sin comparar con otros métodos de aumento (SMOTE, reponderación) (Introducción, p. 2) | No aísla el efecto causal del componente sintético |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Datos sintéticos de CTGAN → menor error en magnitudes altas | Comparación de modelos con datos mixtos y reales | Plausibilidad, gradiente parcial | Consistencia entre regiones, experimento por evento, especificidad | Fuga entre eventos, selección del modelo con la prueba | 4 | Correlacional |
| Características de la onda P → magnitud | Relaciones empíricas y modelos | Plausibilidad física, coherencia, analogía | Experimento fuera de región | Saturación de magnitud, efectos de sitio | 6 | Causal física (asociación fuerte) |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Conocimiento | Evaluación por evento y entre regiones con muestras mayores, incluidos eventos pequeños y grandes | Crítico | Alta | 9 |
| Tecnológico | Medición de latencia y tiempo de alerta de extremo a extremo en una red real | Crítico | Media | 8 |
| Metodológico | Pruebas de fidelidad de datos sintéticos y comparación con otros métodos de aumento | Significativo | Alta | 7 |
| Mercado | Cuantificación del valor económico de la alerta para usuarios industriales | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Overall framework of the proposed work | Diagrama | Del disparo del evento a la predicción por estación y difusión del aviso | N = 3, 4, 5 s | Media |
| Fig. 3 | Pipeline for magnitude prediction with CTGAN | Diagrama | Cuatro etapas: extracción, síntesis, predicción y evaluación | No aplica | Alta |
| Fig. 4 | Stations and events in India-Nepal and Japan | Mapa | Estaciones (triángulos) y epicentros (estrellas) | No aplica | Baja |
| Fig. 5 | Pearson correlation matrices and magnitude distributions | Gráfico | Comparación real frente a mixto y conteos por magnitud | Correlaciones no legibles | Media |
| Figs. 7-9 | Comparison with PGD regression relations | Gráfico | Real frente a predicho y errores por distancia y magnitud | No tabulados | Alta |
| Figs. 10-13 | Case studies Kumamoto, Osaka, offshore, India-Nepal | Mapa/Gráfico | Predicción por estación y error frente a distancia | Mapas de contorno | Media |
| Tabla 1 | Parameter descriptions of SE3, SE4, SE5 | Tabla | Ventanas, rangos de magnitud, registros reales y sintéticos | 18.994; 6.612; 5.211; 6.621 | Alta |
| Tabla 8 | Five earthquakes in India and Nepal | Tabla | MAE, RMSE y media por evento IRE3-IRE5 | 0,28-1,68 MAE | Alta |
| Tabla 9 | Multi-station weighted and unweighted magnitude | Tabla | Cinco sismos, estimación ponderada y no ponderada | 6,3-7,3 MJMA | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Relaciones PGD y tau-c (Kumar; Wu; Bhardwaj) | India / Taiwán | Grupos de investigación | Regresión empírica con onda P | Interpretabilidad física | Mayor error | Estable |
| Zhu et al. (estimación de magnitud con cvav) | China / Estados Unidos | Grupo de investigación | Aprendizaje automático con parámetros de P | Resultados del estado del arte | No evaluado en otras regiones | Creciendo |
| Redes y modelos NN/SVR/Tab-Net | No especificado en documento | Algoritmos | Aprendizaje automático general | Flexibilidad | Mayor error en este conjunto | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Magnitud del sismo (MJMA/MW) estimada; error de predicción (MAE, RMSE)
- **X:** 34 características de la onda P y del sitio; ventana (3, 4, 5 s); uso de datos sintéticos
- **Z (controles):** Distancia epicentral, VS30, región
- **Datos:** 18.994 registros reales de K-NET y 66 registros de India y Nepal; sintéticos de CTGAN
- **Método:** Ensamble apilado (XGB, SGWO-XGB, LGBM, CatBoost, RF) con CTGAN; regla por tramos
- **Efecto reportado:** MAE de 0,38 a 0,41 MJMA; error medio -0,01 a 0,03 ± 0,53 a 0,56
- **Endogeneidad tratada:** No - no se trata la dependencia entre registros de un mismo evento
- **Instrumento:** No aplica
- **Robustez reportada:** Validación cruzada de cinco pliegues para hiperparámetros; prueba entre regiones con 5 eventos; sin intervalos de confianza

| Vacío | Tipo | Descripción |
|---|---|---|
| V-010-01 | TERR | Sin evidencia en Colombia, América Latina o contextos de subducción distintos de Japón |
| V-010-02 | POBL | No se evalúa el efecto en instalaciones o empresas usuarias de la alerta |
| V-010-03 | MET | No hay partición por evento, selección del modelo en un conjunto independiente ni intervalos de confianza |
| V-010-04 | VAR | Faltan variables de tiempo de alerta, latencia y costo de falsas alarmas |
| V-010-05 | TEOR | Sin modelo teórico de valor de la alerta ni de decisión bajo incertidumbre |
| V-010-06 | CAUS | No se aísla el efecto de los datos sintéticos frente a otras técnicas de balance |
