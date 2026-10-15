# FB-L01-060 | D060 — Employing Machine Learning for Seismic Intensity Estimation Using a Single Station for Earthquake Early Warning

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/remotesensing-16-02159.pdf` · 20 páginas · Relevancia para el eje del corpus: **Adyacente** (Propone un modelo de aprendizaje automático (2S1C1S) que clasifica la intensidad sísmica en el sitio con 2 s de datos tras la llegada de la onda P, de una sola estación y un solo componente, con el conjunto INSTANCE de la red sísmica italiana, y lo vincula con un sistema IoT centralizado para alertas. Aporta una pieza de alerta sísmica en el borde con métricas de clasificación, pero se valida solo sobre datos históricos y no trata infraestructura, empresas ni recuperación.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-060 / D060
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Abdalzaher, M. S., Soliman, M. S., Krichen, M., Alamro, M. A., & Fouda, M. M. (2024). Employing Machine Learning for Seismic Intensity Estimation Using a Single Station for Earthquake Early Warning. *Remote Sensing*, *16*(12), Article 2159. https://doi.org/10.3390/rs16122159
- **Autores:** Abdalzaher, Mohamed S. (57189244642); Soliman, M. Sami (57197341217); Krichen, Moez (8973115500); Alamro, Meznah A. (57215605596); Fouda, Mostafa M. (35955834000)
- **Afiliaciones:** Department of Seismology, National Research Institute of Astronomy and Geophysics, Helwan, 11421, Egypt; ReDCAD Laboratory, University of Sfax, Sfax, 3038, Tunisia; Department of Information Technology, College of Computer and Information Science, Princess Nourah Bint Abdul Rahman University, P.O. Box 84428, Riyadh, 11671, Saudi Arabia; Department of Electrical and Computer Engineering, College of Science and Engineering, Idaho State University, Pocatello, 83209, ID, United States
- **Fecha de publicación:** 2024
- **Fuente/contenedor:** Remote Sensing · vol. 16(12)
- **Identificador persistente:** DOI 10.3390/rs16122159 · ISSN 20724292
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85197306904&doi=10.3390%2frs16122159&partnerID=40&md5=88356b8a2a1fdc32a00468b0825e9878
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 27

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Introducir un enfoque de aprendizaje automático para determinar con precisión y prontitud la intensidad de un sismo a partir del análisis de la actividad sísmica durante los 2 s posteriores al inicio de la onda P, con datos de una sola estación y un solo componente (modelo 2S1C1S), para apoyar sistemas de alerta temprana sísmica (EEWS). El estudio busca que el modelo se integre en un sistema IoT centralizado que transmita alertas a las autoridades, y compararlo con la solución manual convencional, tomada como referencia.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si una ventana corta de formas de onda (1 s antes y 2 s después de la onda P) de un solo componente basta para clasificar la intensidad en el sitio con alta exactitud, qué modelo de aprendizaje automático lo logra mejor y cómo se comparan las dos conversiones de aceleración pico a intensidad (la del USGS y la de Faenza y colaboradores).

**Marco teórico.** El marco es la alerta temprana sísmica en el sitio, que estima la intensidad local con los primeros segundos de la onda P y permite avisar antes de la llegada de las ondas más dañinas. La intensidad se obtiene a partir de la aceleración pico del suelo (PGA) mediante dos ecuaciones de conversión. El enfoque de aprendizaje es discriminativo y supervisado, con cinco modelos (entre ellos XGBoost, bosque aleatorio y vecinos más cercanos) y métricas de exactitud, R2, F1, kappa, coeficiente de Matthews, matriz de confusión y tasas de alerta falsa y alerta perdida. La integración con IoT se plantea como canal de transmisión de alertas.

**Metodología.** Se usó el conjunto INSTANCE, de la red sísmica nacional italiana, que contiene alrededor de 1,2 millones de trazas de tres componentes de unos 50 000 eventos entre enero de 2005 y enero de 2020, con magnitudes de 0,0 a 6,5, trazas de 120 s a 100 Hz, convertidas a unidades físicas, con filtros de 0,01 a 40 Hz y un ángulo de rotación aleatorio. El modelo recibe una ventana de 3 s (1 s antes y 2 s después de la onda P), de un solo componente y una estación. Las clases de intensidad se expresan en la escala de Mercalli modificada y se derivan de la PGA con dos conversiones, y se excluyen los eventos de categoría I para evitar el sesgo por abundancia de eventos poco relevantes. Se aplica aumento de datos y se entrenan cinco algoritmos con una división aleatoria de 70 % para entrenamiento, 15 % para validación y 15 % para prueba, midiendo exactitud, R2, F1, kappa, MCC y matriz de confusión. Se afirma el uso de 27 531 registros de 386 estaciones, mientras el resumen menciona 50 000 instancias y 150 000 ventanas.

**Resultados principales.** El modelo con XGBoost alcanzó una exactitud de 99,05 % al clasificar la intensidad con cualquier componente individual, y superó a otros algoritmos de referencia en las métricas reportadas. El texto indica que la razón de alertas falsas es de 14,7 % y la de alertas perdidas de aproximadamente 0,03 %. Las tablas muestran, además, valores de exactitud, R2, F1 y kappa para los cinco modelos con las dos conversiones de intensidad, así como la matriz de confusión, con valores de las métricas entre 0,78 y 0,99 según el modelo y la conversión. Las curvas de aprendizaje del mejor modelo (XGBoost) muestran una exactitud de validación de aproximadamente 90 % con la conversión de intensidad del primer método y de 87 % con la del segundo, cifras inferiores al 99,05 % del resumen; las curvas ROC se presentan para las dos conversiones y el texto señala que el desempeño podría mejorar con más datos. Los autores comparan los resultados con la solución manual de referencia y con trabajos previos de la literatura, y afirman que el modelo es rentable porque solo requiere la forma de onda de velocidad en el sitio, sin estaciones de movimiento fuerte y débil por separado.

**Discusión y contribución.** Los autores sostienen que su modelo supera a los sistemas previos de alerta temprana por clasificar la intensidad en 3 s con 99,05 % de exactitud, por emplear dos metodologías de conversión de PGA a intensidad, por ser económico y por usar técnicas avanzadas de aprendizaje automático que minimizan evaluaciones erróneas de peligro. Recomiendan la adopción por las partes interesadas y la integración con sistemas IoT para alertas rápidas y planes de evacuación, y señalan que la evaluación de peligro con datos de una sola estación simplifica la recolección de datos y optimiza los recursos. Concluyen que diferenciar intensidades es esencial para sistemas eficaces de alerta temprana.

**Limitaciones declaradas.** Declaradas: no hay sección de limitaciones; se menciona que la evaluación se hace con datos históricos. No declaradas: la inconsistencia entre el número de registros (50 000 instancias o 150 000 ventanas frente a 27 531 registros de 386 estaciones); la exactitud global de 99,05 % puede estar dominada por clases de baja intensidad desbalanceadas, y con una razón de alertas falsas de 14,7 % el desempeño útil para decisiones es menor; las etiquetas de intensidad se derivan de la PGA de las mismas formas de onda, lo que exige verificar que no haya fuga de información entre entrenamiento y prueba (por evento o estación); no se evalúa con eventos fuera del conjunto o de otra región; no se mide el tiempo de aviso ni la latencia del IoT; el conjunto es italiano, con magnitudes hasta 6,5.

**Trabajo futuro.** El texto no formula una sección de trabajo futuro detallada; sugiere ampliar el uso con integración en sistemas IoT y adopción por las partes interesadas.

**Palabras clave.** Declaradas: earthquake early warning (EEW); machine learning (ML); on-site intensity; peak ground acceleration (PGA); synthetic ground motion | Inferidas: alerta temprana sísmica, intensidad en el sitio, aprendizaje automático, XGBoost, onda P, aceleración pico del suelo, INSTANCE, IoT, estación única, clasificación

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un modelo de aprendizaje automático con XGBoost, que usa una ventana de 3 s de una sola estación y un solo componente, clasifica la intensidad sísmica en el sitio con 99,05 % de exactitud, supera a otros algoritmos y a las soluciones convencionales y, al integrarse con un sistema IoT centralizado, puede transmitir alertas rápidas a las autoridades con un costo reducido, al no requerir estaciones de movimiento fuerte y débil por separado.

**Antítesis identificada.** La exactitud de 99,05 % no basta para respaldar la tesis. Las clases de intensidad suelen estar fuertemente desbalanceadas, de modo que la exactitud global puede reflejar la clase mayoritaria, y el propio texto reporta una razón de alertas falsas de 14,7 %, alta para una alerta operativa. No se verifica que la partición evite la fuga de información entre trazas de un mismo evento o estación, y las etiquetas se obtienen de la misma forma de onda de la que se extraen las características. El tamaño de datos es contradictorio entre secciones. La comparación con la solución manual no se detalla, no se mide el tiempo de aviso ni la latencia del IoT, y no hay validación independiente con otros sismos o regiones. La integración con IoT es una recomendación, no un componente probado.

**Síntesis propuesta.** La contribución sostenible es una prueba de concepto sólida en términos de desempeño predictivo sobre un conjunto amplio y público: una ventana corta de una componente contiene información suficiente para clasificar la intensidad con exactitud alta en el conjunto INSTANCE. La utilidad operativa depende de las tasas de alertas falsas y de la validación independiente, y la partición aleatoria de las trazas puede sobrestimar el desempeño si trazas del mismo evento caen en conjuntos distintos. Para el corpus, aporta una pieza de borde para la capa de sensado y alerta, con ventajas de costo, y un contraste útil con D041: aquí los datos de entrada son formas de onda y el desempeño es muy superior.

**Áreas grises detectadas.**

1. Consistencia de los datos: el resumen señala 50 000 instancias y 150 000 ventanas de 2 s en tres componentes, y la sección de contribuciones indica 27 531 registros de 386 estaciones; el texto no explica la diferencia, por lo que no se puede reconstruir el tamaño real del conjunto de entrenamiento y prueba.
2. Desbalance y alertas falsas: se reporta 99,05 % de exactitud, pero también 14,7 % de alertas falsas y 0,03 % de alertas perdidas; el texto no muestra la distribución de clases por intensidad ni el desempeño por clase para intensidades altas, que son las críticas.
3. Posible fuga de información: las etiquetas de intensidad se calculan a partir de la PGA de las mismas trazas y la rotación es aleatoria; no se indica si la partición entrenamiento-prueba se hizo por evento o por estación, lo cual es necesario para descartar optimismo en el desempeño.
4. Exactitud de validación: las curvas de aprendizaje del modelo XGBoost indican una exactitud de validación de aproximadamente 90 % y 87 % según la conversión de intensidad, mientras el resumen y la conclusión citan 99,05 %; el texto no aclara si la cifra mayor corresponde a otro conjunto, a entrenamiento o a una métrica distinta.
5. Aplicabilidad operativa: no se mide el tiempo desde la onda P hasta la alerta ni la latencia de la red IoT, y no se evalúa en otra región, de modo que la afirmación de alerta rápida y de integración con IoT carece de pruebas.

**Puntos oscuros aclarados.** Llama la atención que el resumen califique de impresionante una exactitud de 99,05 %, mientras las curvas de aprendizaje del mismo modelo muestran exactitud de validación de 90 % y 87 %, sin discutir el desbalance de clases, mientras el cuerpo reporta una razón de alertas falsas de 14,7 %, que sería, a juicio del analista, alta para una alerta pública. También es notable que el tamaño del conjunto de datos se describa de dos maneras distintas en el mismo artículo (50 000 instancias y 150 000 ventanas frente a 27 531 registros de 386 estaciones). El texto presenta la comparación con la solución manual como referencia sin detallar su método ni su error. Además, el estudio evalúa con datos italianos de magnitud hasta 6,5, y la conclusión de efectividad para sistemas de alerta no menciona la validación con eventos grandes o de otras regiones. Por último, la integración con IoT es una promesa sin implementación ni medición de latencia, y la partición aleatoria 70/15/15 sin agrupar por evento o estación es un riesgo metodológico que los autores no discuten.

**Ideas propositivas novedosas.**

1. Evaluación de utilidad de decisión de la alerta de intensidad: convertir las clasificaciones del modelo en acciones de continuidad (parar líneas, cortar gas) y calcular, con las tasas de 14,7 % de alertas falsas y 0,03 % de alertas perdidas, el costo esperado por evento para una empresa con parada de 30 minutos por falsa alarma y pérdida por alerta omitida. El resultado sería un umbral de decisión óptimo y una estimación del valor del sistema para una pyme, que hoy no existe en el corpus, y permitiría ajustar el umbral de clasificación a la tolerancia de cada usuario, comparando el costo de una alerta omitida con el de una falsa en cada tipo de actividad económica.
2. Validación por evento y por región: repetir el entrenamiento con partición por evento y por estación, evaluar con eventos de magnitud superior a 6 y con datos de otra red (por ejemplo, de Japón o Chile), y reportar desempeño por clase, intervalos de confianza y calibración de probabilidades. Con ello se establecería, además de la exactitud global, si el 99,05 % se sostiene fuera del conjunto italiano y se podría decidir si el modelo es adecuado para regiones sísmicas de América Latina sin reentrenamiento local.

**Relaciones poco exploradas.**

1. Alerta temprana con aprendizaje (contrasta con) D041: D041 predice magnitud con cuatro variables de metadatos y obtiene R2 de 0,16, y D060 usa formas de onda y alcanza 99,05 % de exactitud en intensidad; la diferencia ilustra el valor de la señal frente a los metadatos.
2. Alerta en el borde con sensores de bajo costo (se relaciona con) D045 y D049: D045 clasifica los EEWS de bajo costo y D049 mide latencias de la arquitectura descentralizada; D060 aporta el componente de clasificación de intensidad por estación.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 5/10 — Aporta un modelo de clasificación de intensidad con una ventana de 3 s y una sola estación, con un conjunto amplio y desempeño alto en datos históricos, útil como pieza de alerta en el borde. Su valor para el corpus es adyacente: refuerza la capa de sensado y alerta, pero la validación es interna, los datos son inconsistentes entre secciones, hay una razón de alertas falsas de 14,7 % y no se mide el tiempo de aviso ni el efecto sobre empresas.

**Conexiones inter-documentales.**

- **CONTRADICE** D041 (Alerta temprana sísmica con aprendizaje automático y visualización geo): D060 reporta que XGBoost supera a otros algoritmos en intensidad sísmica (99,05 %) y D041 que una red neuronal supera a XGBoost en magnitud; las tareas, datos y métricas difieren, por lo que el orden de modelos no es transferible [juicio del analista]
- **COMPLEMENTA** D019 (IoT y alerta temprana en la gestión de desastres sísmicos): relación inversa de D019 COMPLEMENTA D060: comparten autoría (Abdalzaher, Krichen): D019 revisa tecnologías emergentes y D060 aplica aprendizaje automático a intensidad sísmica en sitio [juicio del analista; citación verificada de D019 a D060; autoría compartida]
- **DEPENDE_DE** D031 (IoT semántico y alerta temprana de amenazas geológicas): cita a D031 en su lista de referencias (verificado por coincidencia de título); D031: IoT semántico y alerta temprana de amenazas geológicas [citación verificada]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 57 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Exactitud global como prueba de utilidad (Se destaca 99,05 % de exactitud sin tratar el desbalance de clases ni el 14,7 % de alertas falsas (Resumen, p. 1; Sec. 7, p. 17)); Inconsistencia interna (El conjunto se describe como 50 000 instancias y 150 000 ventanas, y también como 27 531 registros de 386 estaciones (Resumen, p. 1; Sec. 1.2, p. 3)); Generalización apresurada (Se recomienda la adopción por las partes interesadas desde datos históricos italianos (Sec. 7, p. 17))
- **Bradford-Hill:** No aplica: es un estudio predictivo sin diseño causal; la relación entre las primeras ondas y la intensidad tiene base física, pero el desempeño no se contrasta fuera de muestra.
- **TRL asignado:** 4 — 'The 2S1C1S model can be seamlessly integrated into a centralized IoT system' (p. 1)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (18 páginas). Las tablas de métricas se leyeron con columnas desordenadas; se citan rangos y no valores por modelo. La inconsistencia entre 50 000 instancias y 27 531 registros aparece así en el texto. Las páginas siguen los marcadores del PDF.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un modelo de aprendizaje automático con XGBoost, que usa una ventana de 3 s de una sola estación y un solo componente, clasifica la intensidad sísmica en el sitio con 99,05 % de exactitud, supera a otros algoritmos y a las soluciones convencionales y, al integrarse con un sistema IoT centralizado, puede transmitir alertas rápidas a las autoridades con un costo reducido, al no requerir estaciones de movimiento fuerte y débil por separado.  | La exactitud de 99,05 % no basta para respaldar la tesis. Las clases de intensidad suelen estar fuertemente desbalanceadas, de modo que la exactitud global puede reflejar la clase mayoritaria, y el propio texto reporta una razón de alertas falsas de 14,7 %, alta para una alerta operativa. No se verifica que la partición evite la fuga de información entre trazas de un mismo evento o estación, y las etiquetas se obtienen de la misma forma de onda de la que se extraen las características. El tamaño de datos es contradictorio entre secciones. La comparación con la solución manual no se detalla, no se mide el tiempo de aviso ni la latencia del IoT, y no hay validación independiente con otros sismos o regiones. La integración con IoT es una recomendación, no un componente probado.  | La contribución sostenible es una prueba de concepto sólida en términos de desempeño predictivo sobre un conjunto amplio y público: una ventana corta de una componente contiene información suficiente para clasificar la intensidad con exactitud alta en el conjunto INSTANCE. La utilidad operativa depende de las tasas de alertas falsas y de la validación independiente, y la partición aleatoria de las trazas puede sobrestimar el desempeño si trazas del mismo evento caen en conjuntos distintos. Para el corpus, aporta una pieza de borde para la capa de sensado y alerta, con ventajas de costo, y un contraste útil con D041: aquí los datos de entrada son formas de onda y el desempeño es muy superior.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** '2S1C1S' es dos segundos, un componente y una estación; 'intensidad en el sitio' es la severidad local derivada de la PGA; 'alerta falsa' es una alerta sin sismo dañino.
- **P2 Supuestos:** Supone que la ventana de 2 s tras la onda P contiene la información de la intensidad, que la partición evita fuga y que los resultados italianos se generalizan.
- **P3 Evidencia:** La evidencia es una clasificación sobre datos históricos con 99,05 % de exactitud, 14,7 % de alertas falsas y 0,03 % de alertas perdidas.
- **P4 Consecuencias:** Si es cierto, se pueden emitir alertas locales en segundos con una sola estación; si es falso, el sistema puede producir falsas alarmas costosas o fallar en intensidades altas.
- **P5 Contraejemplos:** No se examinan eventos de otras regiones, la distribución de clases, la partición por evento ni la latencia del IoT.
- **P6 Alternativas:** Alternativas: que la exactitud refleje la clase mayoritaria; que una regla de umbral de PGA con la onda P iguale el desempeño; que la fuga de datos explique parte del resultado.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Exactitud del modelo con XGBoost | 99,05 | % | Clasificación de intensidad con un componente | Resumen, p. 1 | Texto | Media | Posible desbalance de clases |
| Razón de alertas falsas | 14,7 | % | Reportada en el texto | Sec. 7, p. 17 | Texto | Alta | Alta para una alerta pública |
| Exactitud de validación en curvas de aprendizaje de XGBoost | ≈ 90 / 87 | % | Según la conversión de intensidad usada | Sec. 6, p. 14 | Texto | Alta | Inferior al 99,05 % del resumen |
| Razón de alertas perdidas | 0,03 | % | Casi nula | Sec. 7, p. 17 | Texto | Alta | Para el modelo propuesto |
| Ventana de datos del modelo | 3 | s | 1 s antes y 2 s después de la onda P | Sec. 1.2, p. 3 | Texto | Alta | Una estación, un componente |
| Trazas de tres componentes del conjunto INSTANCE | 1,2 | millones | Unos 50 000 eventos de 2005 a 2020 | Sec. 3.1, p. 5 | Texto | Alta | Magnitudes de 0,0 a 6,5 |
| Registros de 386 estaciones usados según las contribuciones | 27 531 | registros | Frente a 50 000 instancias del resumen | Sec. 1.2, p. 3 | Texto | Media | Inconsistencia no explicada |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'The 2S1C1S model can be seamlessly integrated into a centralized IoT system' (p. 1) | Modelo validado sobre datos históricos en laboratorio computacional; integración con IoT solo planteada. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'The method is cost-effective, relying only on on-site velocity waveforms' (p. 3) | Se afirma menor costo, sin cifras ni modelo de negocio. |
| IRL | 2 | Sí | 'Integration with IoT systems is recommended for reliable, swift alerts to decisionmakers' (p. 3) | Integración con IoT recomendada, sin implementación ni pruebas de latencia. |
| DRL | 3 | Sí | 'An earthquake early-warning system (EEWS) is an indispensable tool for mitigating loss of life caused by earthquakes' (p. 1) | Necesidad argumentada; sin estudio de usuarios. |
| SRL | 1.0 | Sí | Componentes: Modelo 2S1C1S de clasificación de intensidad (TRL 4), Transmisión de alertas por IoT (TRL 2) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 6.0; ÷9 → 0.67; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 2 e IRL 2: modelo con alto desempeño en datos históricos, sin pruebas de tiempo real, con 14,7 % de alertas falsas y sin integración IoT probada. · Estrategia de salida: Validación por evento y región, medición de latencia y de tiempo de aviso, y reducción de alertas falsas.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Exactitud global como prueba de utilidad | Se destaca 99,05 % de exactitud sin tratar el desbalance de clases ni el 14,7 % de alertas falsas (Resumen, p. 1; Sec. 7, p. 17) | La métrica no refleja el desempeño en clases críticas |
| Inconsistencia interna | El conjunto se describe como 50 000 instancias y 150 000 ventanas, y también como 27 531 registros de 386 estaciones (Resumen, p. 1; Sec. 1.2, p. 3) | No se explica la diferencia |
| Generalización apresurada | Se recomienda la adopción por las partes interesadas desde datos históricos italianos (Sec. 7, p. 17) | Sin validación externa |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Forma de onda inicial (2 s tras la onda P) → intensidad posterior en el sitio | Clasificación supervisada con 99,05 % de exactitud | Coherencia física | Validación por evento y región | Distancia, magnitud, efecto de sitio | 3 | Relación predictiva plausible |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Partición por evento, distribución de clases, desempeño por clase y validación externa | Crítico | Media | 9 |
| Tecnológico | Latencia del IoT, tiempo de aviso y reducción de alertas falsas | Crítico | Media | 8 |
| Conocimiento | Valor económico de la alerta de intensidad para empresas | Significativo | Media | 8 |
| Mercado | Costos de estaciones de un componente y de operación | Moderado | Baja | 5 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Distribución espacial de eventos y estaciones del conjunto | Mapa | Red sísmica italiana | No aplica | Media |
| Tabla de métricas | Exactitud, R2, F1 y kappa de los modelos por conversión de intensidad | Tabla | Cinco modelos y dos conversiones | 0,78 a 0,99 | Alta |
| Matriz de confusión | Predicción frente a clase real de intensidad | Matriz | Clasificación de intensidad | No aplica | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Sistemas de alerta en el sitio con umbral de PGA y onda P | No especificado en documento | Gobierno | Alerta local con reglas físicas | Simplicidad | Menor precisión de intensidad | Estable |
| MagNet y modelos de aprendizaje profundo para magnitud | No especificado en documento | Academia | Estimación de magnitud desde la forma de onda | Uso de la señal | No clasifican intensidad en el sitio | Creciendo |

### B.9 Variables econométricas y vacíos

- **Y:** Clase de intensidad en el sitio (derivada de la PGA)
- **X:** Características de la ventana de 3 s de un componente
- **Z (controles):** Algoritmo (XGBoost, bosque aleatorio, KNN, entre otros) y conversión de intensidad (USGS o Faenza)
- **Datos:** Conjunto INSTANCE de la red sísmica italiana (2005 a 2020; magnitudes de 0,0 a 6,5)
- **Método:** Clasificación supervisada con métricas de exactitud, F1, kappa y MCC
- **Efecto reportado:** Exactitud de 99,05 %; alertas falsas 14,7 %; alertas perdidas 0,03 %
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Comparación de cinco algoritmos y dos conversiones; sin validación externa

| Vacío | Tipo | Descripción |
|---|---|---|
| V-060-01 | TERR | Italia; sin América Latina |
| V-060-02 | POBL | Sin usuarios ni empresas |
| V-060-03 | TEMP | Ventana de 3 s; sin latencia de la red ni tiempo de aviso medido |
| V-060-04 | MET | Inconsistencia de datos, posible desbalance y fuga, sin validación externa |
| V-060-05 | VAR | Faltan distribución de clases, costos, latencia y desempeño por clase |
| V-060-06 | TEOR | Sismología de alerta temprana; sin teoría de respuesta a la alerta |
| V-060-07 | CAUS | Relación predictiva sin efecto en decisiones |
