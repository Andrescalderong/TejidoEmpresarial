# FB-L01-063 | D063 — Research on earthquake early warning and emergency response for high-speed railways based on the PLUM principle

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/rs-08-2025-0027en.pdf` · 16 páginas · Relevancia para el eje del corpus: **Adyacente** (Diseña y valida mediante reproducción fuera de línea (82 sismos históricos y 61 estaciones) un método de alerta temprana y respuesta de emergencia para ferrocarriles de alta velocidad basado en el principio PLUM, con zonas de alerta trapezoidales superpuestas y una arquitectura jerárquica de estaciones propias y de la red nacional. Aporta el vínculo entre alerta sísmica y decisión operativa automática de una infraestructura crítica, pero no incluye gemelos, recuperación ni empresas.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-063 / D063
- **Tipo de recurso:** Artículo científico (journal peer-reviewed)
- **Referencia APA 7:** Gu, K., Yang, L., Zhou, D., Xi, N., & Tan, Z. (2025). Research on earthquake early warning and emergency response for high-speed railways based on the PLUM principle. *Railway Sciences*, 1-16. https://doi.org/10.1108/RS-08-2025-0027
- **Autores:** Gu, Kun (60745276000); Yang, Lin (57200207131); Zhou, Datian (14219857000); Xi, Nan (56740269700); Tan, Zhongwei (7201599610)
- **Afiliaciones:** China Academy of Railway Sciences Corporation Limited, Beijing, China; School of Electronic Information Engineering, Beijing Jiaotong University, Beijing, China; China Earthquake Networks Center, Beijing, China
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** Railway Sciences
- **Identificador persistente:** DOI 10.1108/RS-08-2025-0027 · ISSN 27550907
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105044807496&doi=10.1108%2fRS-08-2025-0027&partnerID=40&md5=ddd7fec04347cab3d71d905c3a9d6916
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 0

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Diseñar y validar un método de respuesta de emergencia para sistemas de alerta temprana sísmica (EEW) de ferrocarriles de alta velocidad basado en el principio de propagación del movimiento local no amortiguado (PLUM), con el fin de mejorar la oportunidad y la exactitud de las alertas ante amenazas sísmicas. El estudio busca emitir información de emergencia antes de la llegada de las ondas destructivas, reducir los retardos entre regiones y las alertas perdidas, y ofrecer una estrategia práctica adaptada a los requisitos operativos del ferrocarril.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si el método PLUM con zonas de alerta trapezoidales superpuestas emite información a tiempo y con exactitud para distintas magnitudes y distancias al epicentro, si reduce las alertas perdidas frente a zonas rectangulares y cómo se compara la oportunidad con algoritmos de rango de disposición basados en atenuación.

**Marco teórico.** El marco es la alerta temprana regional basada en el movimiento del suelo, en la que el método PLUM predice la aceleración pico (PGA) de un punto como el máximo de las aceleraciones observadas en estaciones dentro de un radio, sin estimar los parámetros de la fuente. Se adopta la aceleración como indicador de severidad por ser lo que miden directamente las estaciones a lo largo de la línea, y se supone que los efectos de sitio son despreciables porque la cimentación de las líneas de alta velocidad corresponde a suelos rígidos o roca (Vs30 de 500 a 800 m/s, con error normalizado inferior a 5 %). La arquitectura es jerárquica, con estaciones propias del ferrocarril como columna vertebral y la red sísmica nacional como complemento, y la respuesta se organiza por niveles de emergencia por región de alerta.

**Metodología.** El diseño usa regiones de alerta a lo largo de la vía, inicialmente rectangulares de 30 km por 60 km, que se transforman en trapecios isósceles superpuestos mediante la extensión de las líneas centrales de los lados largos, para que una estación cercana al límite de una región pueda activar también la contigua y se reduzcan los retardos entre regiones. El sistema actualiza cada 0,01 s la PGA de las estaciones de la línea y de la red general y decide de forma independiente la alerta de cada región, con niveles de mensaje (por ejemplo nivel 2 y nivel 3). La validación es una reproducción fuera de línea, aislada del sistema operativo, con 82 eventos históricos de magnitud 5,0 a 7,0 y registros de 61 estaciones, con las ubicaciones absolutas eliminadas y solo las relaciones espaciales relativas, sobre una línea de alta velocidad equipada y próxima a una región sísmicamente activa. Se analizan evolución temporal, exactitud y oportunidad.

**Resultados principales.** En un ensayo con un sismo de magnitud 5,5 a 43 km de la línea, la primera región emitió un mensaje de nivel 2 a los 7 s del sismo y lo elevó a nivel 3 a los 9 s, y la segunda región emitió nivel 2 a los 12 s, con actualizaciones secuenciales a medida que se propagaban las ondas. En la prueba de exactitud con tres eventos de magnitud 6,2, 6,3 y 6,4, con regiones divididas en tres subregiones de 10 km, el método avisó de forma confiable a casi todos los tramos de la vía sin alertas perdidas. En cuatro eventos de distinta magnitud, la oportunidad de PLUM fue superior en regiones cercanas al epicentro en sismos mayores, y la ventaja disminuyó para regiones lejanas frente a algoritmos de rango basados en atenuación. En 82 eventos, en regiones a menos de 100 km del epicentro, el método fue más oportuno en magnitudes mayores y dio más tiempo de aviso a regiones muy cercanas antes de las ondas más destructivas. Los autores concluyen que el diseño trapezoidal mejora la consistencia regional y reduce de forma significativa las alertas perdidas, aunque el texto leído no cuantifica esa reducción con una tasa comparada entre diseños.

**Discusión y contribución.** Los autores sostienen que el método basado en PLUM es práctico y robusto como estrategia de respuesta de emergencia para ferrocarriles de alta velocidad, que la superposición trapezoidal aumenta la consistencia regional y que la oportunidad es mayor en sismos grandes, para los que la ruptura extensa permite avisar a regiones muy cercanas antes de las ondas más destructivas. Afirman que es la primera aplicación sistemática de PLUM a la alerta de ferrocarriles de alta velocidad en China y que la simplificación a PGA, con umbrales predefinidos y suelos rígidos, hace despreciable el efecto de sitio. Plantean perspectivas de integración con la operación ferroviaria.

**Limitaciones declaradas.** Declaradas: se usó simulación fuera de línea por restricciones prácticas, con datos de una línea ya equipada. No declaradas: la validación es retrospectiva y no incluye falsas alarmas ni su costo (parada innecesaria de trenes); se omiten las ubicaciones absolutas, de modo que no se verifica el efecto de condiciones locales reales; la suposición de efecto de sitio despreciable se apoya en Vs30 de 500 a 800 m/s sin medición propia; la ventaja decrece con la distancia respecto de algoritmos de atenuación; no se evalúa el tiempo de actuación de los trenes ni la reducción de riesgo; muestra de 82 eventos de una región y magnitudes de 5,0 a 7,0.

**Trabajo futuro.** Explícito: sección de conclusiones y perspectivas sobre integración con la operación ferroviaria y refinamiento del método. Implícito: pruebas en línea, evaluación de falsas alarmas y acciones de control de trenes.

**Palabras clave.** Declaradas: Double-trapezoid warning zone; Earthquake early warning; Emergency response; High-speed railway safety; PLUM method; Simulation validation | Inferidas: alerta temprana sísmica, ferrocarril de alta velocidad, PLUM, zonas de alerta trapezoidales, aceleración pico del suelo, respuesta de emergencia, reproducción fuera de línea, red sísmica, infraestructura crítica

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** El principio PLUM, aplicado con zonas de alerta trapezoidales superpuestas y una arquitectura jerárquica de estaciones propias y de la red nacional, permite emitir información de emergencia a tiempo para ferrocarriles de alta velocidad, con alta confiabilidad en eventos de distintas magnitudes y distancias y menos alertas perdidas que con zonas rectangulares, y su oportunidad es mayor en sismos grandes para regiones próximas al epicentro.

**Antítesis identificada.** El estudio valida un procedimiento retrospectivo, sin falsas alarmas, sin acción sobre los trenes y sin efecto medido sobre el riesgo. La confiabilidad se afirma con tres eventos de exactitud y 82 de oportunidad en una sola región, y se reconoce que la ventaja disminuye con la distancia frente a algoritmos de atenuación. La supuesta irrelevancia del efecto de sitio descansa en un rango de Vs30 asumido para toda la línea. La eliminación de ubicaciones absolutas protege los datos pero impide verificar condiciones locales. No hay comparación cuantitativa de errores con otras alternativas, ni se informa cuántos segundos útiles ganaría un tren frente al tiempo de frenado.

**Síntesis propuesta.** La contribución sostenible es un diseño de zonas de alerta y de reglas de emisión para infraestructura lineal que usa solo aceleraciones observadas, y una evaluación retrospectiva que indica tiempos de emisión de 7 a 12 s en un ejemplo y un buen desempeño en eventos medianos y grandes. Para el corpus, aporta un modelo de cadena sensor, regla, acción para infraestructura crítica y una lección de diseño (superposición de zonas para reducir retardos), pero no mide pérdidas evitadas ni extiende a empresas, de modo que su aporte es de diseño y no de valor económico demostrado, y se debe completar con falsas alarmas y tiempos de acción.

**Áreas grises detectadas.**

1. Falsas alarmas: el artículo evalúa oportunidad y alertas perdidas, pero no informa falsas alarmas ni su costo operativo, un criterio central en un ferrocarril de alta velocidad donde una parada innecesaria tiene consecuencias económicas.
2. Efecto de sitio: se supone despreciable por Vs30 de 500 a 800 m/s y error normalizado inferior a 5 %, pero no se presentan mediciones del tramo ni sensibilidad; la conclusión depende de una calibración de zonas y umbrales que no se muestra.
3. Validez de la validación: la reproducción fuera de línea con 82 eventos históricos de una región y ubicaciones absolutas eliminadas impide verificar el efecto de la geometría real de la línea; solo tres eventos se usan para exactitud y cuatro para el análisis de eventos individuales.
4. Utilidad para la acción: no se cuantifica el tiempo disponible para frenar trenes ni la reducción de riesgo resultante, de modo que la mejora de oportunidad no se traduce en un beneficio medido.

**Puntos oscuros aclarados.** Llama la atención que el resumen califique el método de alta confiabilidad y estabilidad con una validación retrospectiva que no informa falsas alarmas, la métrica que determina si un operador ferroviario adoptaría la alerta. También es notable que la irrelevancia del efecto de sitio se afirme por un rango de Vs30 asumido y no por mediciones. El texto reconoce que la ventaja de oportunidad desaparece para regiones lejanas, donde los algoritmos de atenuación son mejores, pero la conclusión es favorable en general. Además, la eliminación de las coordenadas reales para evitar confusión con eventos reales limita la reproducibilidad. Por último, el artículo no relaciona el tiempo de emisión de 7 a 12 s con el tiempo de frenado de un tren de alta velocidad, el único criterio que da sentido a la alerta, y tampoco discute quién decide la acción sobre los trenes ni con qué protocolo ante un mensaje de nivel 2 o de nivel 3.

**Ideas propositivas novedosas.**

1. Valor económico de la alerta para infraestructura lineal y cadenas de suministro: combinar los tiempos de emisión (7 a 12 s) y la distancia al epicentro con el tiempo de frenado de un tren y con el costo de interrupción de servicio (horas de retraso, mercancías afectadas), para calcular el beneficio esperado de la alerta frente al costo de falsas alarmas. El resultado serviría como modelo de decisión que se podría transferir a otras infraestructuras críticas, como plantas o centros logísticos, donde también se acciona un paro automático, y se calibraría con datos reales del operador durante al menos seis meses de operación continua.
2. Zonas de alerta superpuestas para parques industriales: adaptar el diseño de zonas trapezoidales superpuestas a un parque industrial con varias plantas y estaciones de bajo costo, y comparar tiempos de emisión y alertas perdidas con zonas rectangulares simples. Con una red de sensores como las de D045 y D049, se evaluaría si la superposición reduce los retardos por región y cuántos segundos extra obtiene cada planta, con una prueba de reproducción fuera de línea con eventos reales y falsas alarmas reportadas, y con el costo de cada paro innecesario como variable de decisión para la gerencia.

**Relaciones poco exploradas.**

1. Alerta sísmica con PLUM (se relaciona con) D049 y D045: D049 implementa PLUM en el nodo con sensores de bajo costo y mide latencias, y D045 revisa los sistemas de alerta de bajo costo; D063 aplica PLUM a una infraestructura lineal con zonas de alerta y niveles de emergencia.
2. Infraestructura crítica con alerta y monitoreo (se relaciona con) D023 y D031: D023 describe un gemelo con monitoreo LoRaWAN de un puente ferroviario y D031 una arquitectura semántica de alerta; D063 aporta reglas de emisión para ferrocarril.

**Robustez argumentativa:** 2.8/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 3/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 5/10 — Aporta un diseño de zonas de alerta y de reglas de emisión para infraestructura lineal crítica con validación retrospectiva con 82 eventos, útil como modelo de cadena sensor-regla-acción. Su valor para el corpus es adyacente: no mide falsas alarmas, tiempo de frenado ni pérdidas evitadas, no incluye gemelos y se limita a una región.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Afirmación de confiabilidad con validación limitada (Se afirma alta confiabilidad y estabilidad con tres eventos de exactitud y sin falsas alarmas (Resumen, p. 1; Sec. 4.2, p. 11)); Supuesto no verificado (Se considera despreciable el efecto de sitio por un rango de Vs30 asumido (Sec. 2.3.2, p. 9)); Conclusión más amplia que la evidencia (Se concluye robustez práctica sin medir el tiempo de actuación ni el riesgo evitado (Sec. 5, p. 13-14))
- **Bradford-Hill:** No aplica: es una validación retrospectiva de un método; no estima efectos causales de la alerta sobre accidentes o pérdidas.
- **TRL asignado:** 4 — 'Offline replay experiments were conducted using 82 historical earthquake events and records from 61 seismic stations' (p. 1)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (14 páginas). Las figuras con resultados no son legibles; las cifras se tomaron del texto de las secciones 4.1 a 4.3. Las páginas siguen los marcadores del PDF (la numeración de la revista inicia en 666).

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| El principio PLUM, aplicado con zonas de alerta trapezoidales superpuestas y una arquitectura jerárquica de estaciones propias y de la red nacional, permite emitir información de emergencia a tiempo para ferrocarriles de alta velocidad, con alta confiabilidad en eventos de distintas magnitudes y distancias y menos alertas perdidas que con zonas rectangulares, y su oportunidad es mayor en sismos grandes para regiones próximas al epicentro.  | El estudio valida un procedimiento retrospectivo, sin falsas alarmas, sin acción sobre los trenes y sin efecto medido sobre el riesgo. La confiabilidad se afirma con tres eventos de exactitud y 82 de oportunidad en una sola región, y se reconoce que la ventaja disminuye con la distancia frente a algoritmos de atenuación. La supuesta irrelevancia del efecto de sitio descansa en un rango de Vs30 asumido para toda la línea. La eliminación de ubicaciones absolutas protege los datos pero impide verificar condiciones locales. No hay comparación cuantitativa de errores con otras alternativas, ni se informa cuántos segundos útiles ganaría un tren frente al tiempo de frenado.  | La contribución sostenible es un diseño de zonas de alerta y de reglas de emisión para infraestructura lineal que usa solo aceleraciones observadas, y una evaluación retrospectiva que indica tiempos de emisión de 7 a 12 s en un ejemplo y un buen desempeño en eventos medianos y grandes. Para el corpus, aporta un modelo de cadena sensor, regla, acción para infraestructura crítica y una lección de diseño (superposición de zonas para reducir retardos), pero no mide pérdidas evitadas ni extiende a empresas, de modo que su aporte es de diseño y no de valor económico demostrado, y se debe completar con falsas alarmas y tiempos de acción.  | 2.8/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'PLUM' predice la aceleración de un punto con las aceleraciones observadas en estaciones cercanas; 'zona de alerta trapezoidal' es una región superpuesta con la contigua; 'nivel 2' y 'nivel 3' son niveles de mensaje de emergencia.
- **P2 Supuestos:** Supone que el efecto de sitio es despreciable en toda la línea, que la reproducción fuera de línea representa la operación y que la oportunidad se traduce en seguridad.
- **P3 Evidencia:** La evidencia es una simulación con 82 eventos de magnitud 5,0 a 7,0 y 61 estaciones, con tres eventos para exactitud y sin falsas alarmas reportadas.
- **P4 Consecuencias:** Si es cierto, los trenes pueden recibir órdenes de emergencia antes de las ondas destructivas; si es falso, pueden producirse paradas innecesarias o alertas tardías.
- **P5 Contraejemplos:** No se examinan falsas alarmas, el tiempo de frenado, la operación en línea ni otras líneas y regiones.
- **P6 Alternativas:** Alternativas: que un algoritmo basado en ondas P sea mejor lejos del epicentro; que el efecto de sitio sí importe en tramos específicos; que el costo de falsas alarmas anule el beneficio.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Eventos históricos usados en la validación | 82 | eventos | Magnitudes de 5,0 a 7,0 | Resumen, p. 1; Sec. 4.3.2, p. 12 | Texto | Alta | Una región sísmica |
| Estaciones sísmicas utilizadas | 61 | estaciones | Línea y red general | Resumen, p. 1 | Texto | Alta | Reproducción fuera de línea |
| Tiempo del primer mensaje de nivel 2 (ensayo M5,5 a 43 km) | 7 | s | Elevado a nivel 3 a los 9 s | Sec. 4.1, p. 11 | Texto | Alta | Un ensayo |
| Tiempo del mensaje de nivel 2 en la segunda región | 12 | s | Tras el sismo | Sec. 4.1, p. 11 | Texto | Alta | Actualizaciones secuenciales |
| Eventos de exactitud (M6,2; 6,3; 6,4) | 3 | eventos | Tramos de 10 km, sin alertas perdidas | Sec. 4.2, p. 11 | Texto | Alta | Muestra pequeña |
| Dimensión de las regiones de alerta rectangulares base | 30 × 60 | km | Transformadas en trapecios superpuestos | Sec. 3.1, p. 10 | Texto | Alta | Diseño propuesto |
| Frecuencia de actualización del sistema | 0,01 | s | Lectura de PGA de las estaciones | Sec. 2.3, p. 9 | Texto | Alta | 100 Hz |
| Rango de Vs30 supuesto en la línea | 500 a 800 | m/s | Efecto de sitio despreciable; error normalizado menor de 5 % | Sec. 2.3.2, p. 9 | Texto | Media | Supuesto sin medición propia |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'Offline replay experiments were conducted using 82 historical earthquake events and records from 61 seismic stations' (p. 1) | Validación en laboratorio computacional con datos históricos, sin operación en línea. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'provides a practical and robust emergency response strategy' (p. 1) | Estrategia afirmada como práctica, sin costos ni análisis económico. |
| IRL | 3 | Sí | 'self-built stations along the railway serve as the backbone and the national seismic network provides supplementary data' (p. 1) | Integra estaciones propias y la red nacional en una arquitectura jerárquica; sin pruebas con el sistema operativo. |
| DRL | 3 | Sí | 'This work represents the first systematic application of the PLUM method to high-speed railway EEW in China' (p. 1) | Vacío de literatura afirmado; demanda del operador no medida. |
| SRL | 1.5 | Sí | Componentes: Algoritmo PLUM y reglas de emisión (TRL 4), Arquitectura de estaciones propias y red nacional (TRL 5) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 13.5; ÷9 → 1.50; nivel acotado a [1,9] = 1.50 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 2 e IRL 3: validación retrospectiva sin falsas alarmas ni pruebas en línea, sin costos y sin vínculo con el control de trenes. · Estrategia de salida: Pruebas en línea, falsas alarmas, tiempo de frenado y análisis de costo-beneficio.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Afirmación de confiabilidad con validación limitada | Se afirma alta confiabilidad y estabilidad con tres eventos de exactitud y sin falsas alarmas (Resumen, p. 1; Sec. 4.2, p. 11) | Muestra pequeña y métrica incompleta |
| Supuesto no verificado | Se considera despreciable el efecto de sitio por un rango de Vs30 asumido (Sec. 2.3.2, p. 9) | Sin medición propia |
| Conclusión más amplia que la evidencia | Se concluye robustez práctica sin medir el tiempo de actuación ni el riesgo evitado (Sec. 5, p. 13-14) | El beneficio operativo no se cuantifica |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Zonas trapezoidales superpuestas → menos retardos y alertas perdidas | Simulación fuera de línea | Mecanismo geométrico directo | Pruebas en línea y falsas alarmas | Densidad de estaciones, geometría de la línea | 3 | Efecto plausible dentro de la simulación |
| Alerta oportuna → acción de emergencia → menor daño | Argumento operativo | Plausibilidad | Medición de tiempos de frenado y daños | Tiempo de reacción del sistema ferroviario | 1 | No evaluado |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Falsas alarmas, costo operativo y validación en línea | Crítico | Media | 8 |
| Conocimiento | Relación entre tiempo de emisión, tiempo de frenado y reducción de riesgo | Crítico | Media | 8 |
| Tecnológico | Sensibilidad al efecto de sitio y a la densidad de estaciones | Significativo | Media | 7 |
| Mercado | Análisis costo-beneficio para operadores de infraestructura crítica | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 7 | Ilustración del algoritmo de predicción PLUM | Diagrama | Predicción de PGA en un punto | No aplica | Media |
| Fig. 8 | Regiones de alerta rectangulares y trapezoidales | Diagrama | Superposición de zonas | 30 km × 60 km | Alta |
| Fig. 10 | Evolución temporal de la información de emergencia en un ensayo | Gráfico | Niveles 2 y 3 por región | 7 s; 9 s; 12 s | Alta |
| Fig. 11 | Comparación de PGA predicha y observada en tres eventos | Gráfico | Tramos de 10 km | M6,2; 6,3; 6,4 | Alta |
| Fig. 13 | Oportunidad en 82 eventos para regiones a menos de 100 km | Gráfico | Magnitud 5,0 a 7,0 | 82 eventos | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Algoritmos de rango de disposición basados en atenuación | No especificado en documento | Gobierno | Estimación de intensidad con modelos de atenuación | Mayor oportunidad lejos del epicentro | Dependen de la estimación de la fuente | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Tiempo de emisión de alerta y alertas perdidas
- **X:** Diseño de la región de alerta (rectangular o trapezoidal) y magnitud del evento
- **Z (controles):** Distancia al epicentro, densidad de estaciones, Vs30
- **Datos:** 82 eventos históricos y 61 estaciones; reproducción fuera de línea
- **Método:** Simulación retrospectiva del método PLUM
- **Efecto reportado:** Emisión de nivel 2 a los 7 s en un ensayo; sin alertas perdidas en tres eventos de exactitud
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Variación de magnitudes y distancias; sin falsas alarmas ni validación en línea

| Vacío | Tipo | Descripción |
|---|---|---|
| V-063-01 | TERR | Línea de alta velocidad en China sin ubicación absoluta; sin América Latina |
| V-063-02 | POBL | Operadores ferroviarios; sin empresas ni pasajeros |
| V-063-03 | TEMP | Alertas de segundos; sin recuperación |
| V-063-04 | MET | Retrospectiva, sin falsas alarmas ni pruebas en línea |
| V-063-05 | VAR | Faltan falsas alarmas, tiempo de frenado, costos y pérdidas evitadas |
| V-063-06 | TEOR | Alerta basada en movimiento del suelo; sin teoría de respuesta organizacional |
| V-063-07 | CAUS | Efecto de la alerta sin evidencia |
