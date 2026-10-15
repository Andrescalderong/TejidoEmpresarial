# FB-L01-023 | D023 — A demonstration of a digital twin framework for structural health monitoring: Application to bridge infrastructures

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/1-s2.0-S2772991525000477-main.pdf` · 16 páginas · Relevancia para el eje del corpus: **Adyacente** (Demuestra durante seis meses un gemelo digital de monitoreo estructural de un puente ferroviario con sensores IoT de red LoRaWAN, modelo de elementos finitos y fotogrametría con drones; aporta evidencia de operación real de un gemelo con IoT y sus limitaciones, pero no trata sismos, recuperación posdesastre ni dimensión empresarial.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-023 / D023
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Nasim, M., Rajabifard, A., Chen, Y., & Samali, B. (2026). A demonstration of a digital twin framework for structural health monitoring: Application to bridge infrastructures. *Journal of Infrastructure Intelligence and Resilience*, *5*(1), Article 100184. https://doi.org/10.1016/j.iintel.2025.100184
- **Autores:** Nasim, Maryam (57205210961); Rajabifard, Abbas (6603307682); Chen, Yiqun (56784058600); Samali, Bijan (7003397589)
- **Afiliaciones:** Department of Infrastructure Engineering, Centre for Spatial Data Infrastructures and Land Administration (CSDILA), University of Melbourne, Australia; Centre for Infrastructure Engineering, School of Engineering Design and Built Infrastructure, Western Sydney University, Australia
- **Fecha de publicación:** 2026
- **Fuente/contenedor:** Journal of Infrastructure Intelligence and Resilience · vol. 5(1)
- **Identificador persistente:** DOI 10.1016/j.iintel.2025.100184 · ISSN 27729915
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105024348142&doi=10.1016%2fj.iintel.2025.100184&partnerID=40&md5=5a1f72a2dde1c0c8d622c03b4e2f95d6
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 17

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Presentar un marco de gemelo digital (GD) multicapa para fortalecer la resiliencia de puentes envejecidos mediante monitoreo de salud estructural (SHM) en tiempo real y apoyo a decisiones basado en datos, y demostrarlo en un puente ferroviario de armadura operativo y patrimonial en Australia. El marco integra modelado de elementos finitos (FEM) basado en física, fotogrametría con drones y redes de sensores inalámbricos para construir una representación dinámica del activo, con retroalimentación en lazo cerrado para actualizar el modelo y detectar anomalías, con la finalidad de sentar bases del mantenimiento predictivo y de la optimización del ciclo de vida.

**Pregunta de investigación.** El artículo investiga tres aspectos: el diseño e integración del marco que combina modelado físico y sensado con IoT en una plataforma unificada de GD y SHM, la confiabilidad del marco para detectar eventos y condiciones, y la escalabilidad del enfoque a diversas tipologías de puentes (concreto, acero, madera, colgantes).

**Marco teórico.** El marco combina la ingeniería estructural (análisis modal operacional con transformada rápida de Fourier y descomposición en el dominio de la frecuencia), la asimilación de datos (filtro de Kalman, actualización bayesiana) para calibrar parámetros del FEM, y un concepto de gemelo digital como réplica sincronizada de un activo físico con sensores en tiempo real. Propone cinco capas funcionales (con una de interoperabilidad e integración) y un lazo de retroalimentación entre predicciones del modelo y parámetros modales extraídos del campo, con umbrales por niveles para eventos. El paradigma es de ingeniería civil aplicada con orientación a la gestión de activos y no incluye teoría de adopción tecnológica ni de economía del mantenimiento.

**Metodología.** Se desarrolló un modelo FEM del puente en Space-Gass, un modelo fotogramétrico 3D georreferenciado y visualizado con CesiumJS en formato 3D Tiles, y una red de ocho acelerómetros inalámbricos triaxiales con transmisión LoRaWAN en puntos estratégicos de la armadura (por ejemplo, cuerdas centrales). Cada nodo opera con adquisición programada (cada hora, 102 s a 80 Hz) y con adquisición por eventos que se activa con un umbral de 30 mg, con alertas escalonadas de 100 mg, 200 mg (advertencia) y 500 mg (crítica). Tras filtrado y eliminación de tendencia, se extraen frecuencias modales por picos de la transformada rápida de Fourier, se comparan con las del FEM (con tolerancia indicativa de 5 %) y se prevé la actualización del modelo con filtros de Kalman. El monitoreo se hizo durante seis meses (mayo a agosto de 2025 para los coeficientes de variación) con pasadas de trenes de carga. No se realizó validación cuantitativa de la actualización del modelo.

**Resultados principales.** La red operó de manera continua durante seis meses con transmisión estable de los ocho nodos, aunque con pérdida aproximada de 5 % de paquetes durante los tres primeros meses en áreas con interferencia junto al corredor de carga, y con descarte de paquetes inciertos. Se capturaron todas las pasadas importantes de trenes de carga y no se produjeron falsas alarmas críticas. Los coeficientes de variación de las frecuencias modales (modos 0 a 2, ejes X, Y, Z) fueron menores o cercanos a 0,5 %, sin deriva persistente en seis meses. Las frecuencias observadas se agruparon en torno a 2,8 a 4,3 Hz (modo 0), 5,8 a 6,0 Hz (modo 1) y 7,0 a 7,5 Hz (modo 2), con amortiguamiento de 2,5 a 3 % en el primer modo y de 3 a 4 % en los superiores. La comparación preliminar con el FEM mostró frecuencias calculadas de 1,96, 2,45 y 2,47 Hz frente a observadas de 2,85, 4,4 y 6,03 Hz, atribuidas a condiciones de borde y materiales idealizados. Los autores presentan esta comparación solo como prueba de concepto del lazo de calibración y declaran que la validación cuantitativa completa se hará en trabajos futuros con monitoreo extendido, configuraciones de sensores refinadas y técnicas modales avanzadas.

**Discusión y contribución.** Los autores sostienen que el marco es práctico, escalable y validado en un puente operativo, y que muestra integración de extremo a extremo de modelado, drones, IoT y análisis en un entorno único. Reconocen que el alcance demostrativo se centra en la capacidad operativa y no en la validación cuantitativa de la precisión del diagnóstico estructural; que la identificación modal usa un picado simple de espectro; que falta el análisis completo de correlación con condiciones ambientales; que seis meses ofrecen información limitada sobre estacionalidad y degradación; y que los costos, la seguridad de acceso, la ubicación de sensores y la coordinación de actores son desafíos. Proponen incorporar aprendizaje automático, redes neuronales informadas por física, realidad aumentada y virtual, estandarización y despliegues en carteras de activos.

**Limitaciones declaradas.** Declaradas: identificación modal elemental por picos de FFT, correlación incompleta con variables ambientales, seis meses de monitoreo, validación cuantitativa pendiente, un solo puente, costos y condiciones de acceso. No declaradas: ausencia de eventos de daño que permitan evaluar sensibilidad; umbrales provisionales; discrepancia de más de 40 % entre frecuencias del FEM y observadas; pérdida de paquetes de 5 %.

**Trabajo futuro.** Extender el monitoreo a ciclos anuales, aplicar métodos modales avanzados (FDD, SSI-COV), integrar aprendizaje automático y redes neuronales informadas por física, desplegar en varios activos y tipologías, usar sensores de recolección de energía y computación en el borde, y avanzar en estándares abiertos e interfaces de realidad aumentada y virtual.

**Palabras clave.** Declaradas: Bridge asset management; Digital twin; Infrastructure resilience; Predictive maintenance; Real-time monitoring; Structural health monitoring | Inferidas: gemelo digital, monitoreo de salud estructural, puente ferroviario, LoRaWAN, modelo de elementos finitos, fotogrametría con drones, mantenimiento predictivo, frecuencias modales, resiliencia de infraestructura, patrimonio

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un marco de gemelo digital que integra FEM, fotogrametría con drones y una red LoRaWAN de acelerómetros puede operar de manera continua en un puente ferroviario en servicio, ofrecer mediciones estables de frecuencias modales y sentar una base escalable de mantenimiento predictivo y gestión de activos envejecidos.

**Antítesis identificada.** La demostración establece la capacidad operativa del sistema de sensado, no la utilidad diagnóstica del gemelo: no hubo eventos de daño, no se validó la actualización del modelo y la comparación entre el FEM y las frecuencias observadas muestra diferencias de 45 % a más de 140 % que superan la tolerancia de 5 % definida por los propios autores. La afirmación de que no hubo falsas alarmas críticas no prueba la validez de los umbrales, porque tampoco se registraron eventos críticos. El texto informa de modos agrupados en un rango de 2,8 a 4,3 Hz con coeficientes de variación menores de 0,5 %, lo que exige aclarar a qué corresponde el rango. El adjetivo 'pionero' y la afirmación de escalabilidad a puentes colgantes y de madera carecen de evidencia más allá de un caso. La pérdida del 5 % de paquetes y la limitación de ancho de banda reducen la reproducción en tiempo real que define a un gemelo digital, y no se reportan costos.

**Síntesis propuesta.** La contribución verificable es una evidencia de operación sostenida de un sistema de sensado inalámbrico de bajo consumo integrado con un entorno de visualización geoespacial en un activo en servicio, con lecciones sobre pérdida de paquetes, ancho de banda y umbrales. El gemelo se encuentra en fase de monitor con calibración pendiente, no de gemelo plenamente actualizado. Para el corpus, la síntesis consiste en utilizar este caso como referencia de madurez y de costos operativos de un gemelo con IoT (lo que funciona, lo que se pierde, lo que falta) y exigir, para cualquier gemelo de recuperación, la medición explícita de disponibilidad de datos, de la brecha modelo-realidad y del costo de mantener el sistema, de modo que la recomendación se base en desempeño demostrado.

**Áreas grises detectadas.**

1. Brecha modelo-realidad: las frecuencias calculadas con el FEM (1,96, 2,45 y 2,47 Hz) difieren mucho de las observadas (2,85, 4,4 y 6,03 Hz), y también de las 'pruebas iniciales' (2,3, 4,6 y 7,9 Hz) que se describen como alineadas con el FEM; el texto atribuye la diferencia a condiciones de borde sin cuantificar ni mostrar la calibración.
2. Validez de los umbrales: se concluye la validez operativa de los umbrales de 30, 100, 200 y 500 mg porque no hubo falsas alarmas críticas, pero no se registraron eventos críticos ni de daño, por lo que no se puede estimar sensibilidad ni especificidad.
3. Consistencia de los resultados modales: el texto reporta coeficientes de variación menores de 0,5 % y a la vez rangos de 2,8 a 4,3 Hz para el modo 0 y diferencias de 0,05 a 0,10 Hz; la tabla de estadísticos no permite verificar si los rangos corresponden a ejes, a sensores o a eventos distintos.
4. Escalabilidad y costos: se afirma adaptabilidad a puentes colgantes, de madera y a otros activos, y se menciona que el costo puede ser prohibitivo para agencias con presupuesto limitado, pero no se informa el costo del despliegue, de la conectividad ni del mantenimiento, ni la pérdida de disponibilidad de datos en el tiempo.

**Puntos oscuros aclarados.** Resulta llamativo que un artículo que se presenta como demostración de un gemelo digital 'validado' reconozca que su cálculo de calibración es solo una prueba de concepto y que el FEM sub-estima las frecuencias de manera sistemática, y que el único criterio de éxito sea el funcionamiento continuo de la red. Una explicación plausible es que el valor inmediato del sistema es la infraestructura de datos y de visualización, que puede mostrarse sin resultados de daño, mientras que la calibración del modelo exige campañas más largas, modelos mejor definidos y eventos que no ocurrieron en los seis meses. Esto indica que el gemelo está más cerca de un panel de monitoreo con un modelo de referencia que de un gemelo con sincronización bidireccional, y que el beneficio económico (mantenimiento predictivo) está por demostrarse. La pérdida de paquetes en el corredor de carga y la limitación de ancho de banda muestran, además, que la conectividad de bajo consumo impone un compromiso entre cobertura y continuidad de datos que debe medirse en cualquier uso posterior a un desastre.

**Ideas propositivas novedosas.**

1. Registro de desempeño de un gemelo con IoT: adoptar un conjunto mínimo de indicadores (disponibilidad de datos, pérdida de paquetes, error entre modelo y observación, tiempo hasta actualización del modelo, costo de operación mensual) y reportarlos para cada despliegue de gemelo en el corpus, con el caso del puente como línea base. Fundamento: el artículo informa solo parcialmente (5 % de pérdida, variación de frecuencias) y no costos ni brecha cuantificada. Verificabilidad: aplicación a otros despliegues con definiciones comunes. Utilidad: hace comparables los gemelos entre proyectos, evita que la sofisticación sustituya a la evidencia de desempeño y permite fijar umbrales mínimos de aceptación antes de recomendar un gemelo para decisiones de reapertura o de mantenimiento.
2. Ensayo de sensibilidad de umbrales con eventos inducidos: realizar pruebas controladas (cargas conocidas, cambios de rigidez simulados con masa añadida o apoyos modificados) para estimar la sensibilidad de los umbrales y de la detección de cambios de frecuencia, y calibrar el FEM con esos eventos. Fundamento: la ausencia de eventos de daño impide validar la detección. Verificabilidad: ensayos con resultados repetibles y análisis de error. Utilidad: permite pasar de la operación demostrada a la validación diagnóstica antes de usar el gemelo para decidir mantenimiento o reapertura, y estima la tasa de falsos negativos que cada umbral implica para el operador del activo.

**Relaciones poco exploradas.**

1. Pérdida de paquetes y ancho de banda limitado (reducen) la continuidad de datos del gemelo: los autores reportan 5 % de fallos de transmisión y priorización de eventos por limitación de ancho de banda, lo que afecta la sincronización.
2. Idealización de condiciones de borde y de materiales en el FEM (explica) la discrepancia con las frecuencias observadas: según los autores, las frecuencias medidas son mayores que las predichas por supuestos de apoyos simplificados.

**Robustez argumentativa:** 4.0/10 (ponderación 30/30/25/15) — consistencia lógica 5/10; calidad de la evidencia 4/10; validez de inferencias causales 3/10; generalizabilidad 4/10.

**Valor estratégico:** 6/10 — Aporta evidencia de seis meses de operación de un sistema de gemelo con IoT en una infraestructura real, con datos de estabilidad modal, pérdida de paquetes y diseño de umbrales, útil como referencia de madurez y de lecciones de despliegue. Su valor se limita porque el gemelo no está calibrado de forma cuantitativa, no hay eventos de daño ni costos reportados, y el dominio es un puente ferroviario sin sismos.

**Conexiones inter-documentales.**

- **COMPLEMENTA** D084 (IoT sincronizado de bajo costo para monitoreo vibracional de puentes c): relación inversa de D084 COMPLEMENTA D023: D084 valida nodos en laboratorio y D023 opera un gemelo con LoRaWAN en un puente ferroviario en servicio, lo que muestra la brecha entre prototipo y c [juicio del analista]
- **COMPLEMENTA** D035 (Actualización de modelo en gemelos digitales de puentes): D023 mantiene medición continua con LoRaWAN y D035 actualiza el modelo por algoritmo genético en el puente de acero; ambos aportan a gemelos de puentes [juicio del analista]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 76 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Falacia de la ausencia de evidencia (Se afirma que no hubo falsas alarmas críticas y que los umbrales son válidos, aunque tampoco hubo eventos críticos (Sec. 5.8, p. 13)); Apelación a la novedad (Se califica la implementación de 'pioneering' y 'novel' sin comparación sistemática con otros despliegues de campo (Resumen, p. 1; Sec. 6, p. 14)); Generalización apresurada (Se afirma adaptabilidad a puentes colgantes, de madera y de otras tipologías a partir de un puente de armadura (Sec. 1, p. 2; Sec. 7, p. 14))
- **Bradford-Hill:** No aplica: es una demostración de operación sin diseño causal; la estabilidad de frecuencias modales no se vincula con daño o integridad mediante comparación con eventos conocidos, gradiente o experimento.
- **TRL asignado:** 6 — 'The deployment confirms that the DT–SHM system can operate continuously on a live and operational bridge' (p. 13)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (15 páginas más referencias). Las tablas 1 y 2 se extrajeron con el orden desordenado; los estadísticos modales de la Tabla 2 no son legibles en detalle y se emplean solo las cifras del texto. Los porcentajes de diferencia entre frecuencias de FEM y observadas son cálculo del analista a partir de los tres pares citados.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un marco de gemelo digital que integra FEM, fotogrametría con drones y una red LoRaWAN de acelerómetros puede operar de manera continua en un puente ferroviario en servicio, ofrecer mediciones estables de frecuencias modales y sentar una base escalable de mantenimiento predictivo y gestión de activos envejecidos.  | La demostración establece la capacidad operativa del sistema de sensado, no la utilidad diagnóstica del gemelo: no hubo eventos de daño, no se validó la actualización del modelo y la comparación entre el FEM y las frecuencias observadas muestra diferencias de 45 % a más de 140 % que superan la tolerancia de 5 % definida por los propios autores. La afirmación de que no hubo falsas alarmas críticas no prueba la validez de los umbrales, porque tampoco se registraron eventos críticos. El texto informa de modos agrupados en un rango de 2,8 a 4,3 Hz con coeficientes de variación menores de 0,5 %, lo que exige aclarar a qué corresponde el rango. El adjetivo 'pionero' y la afirmación de escalabilidad a puentes colgantes y de madera carecen de evidencia más allá de un caso. La pérdida del 5 % de paquetes y la limitación de ancho de banda reducen la reproducción en tiempo real que define a un gemelo digital, y no se reportan costos.  | La contribución verificable es una evidencia de operación sostenida de un sistema de sensado inalámbrico de bajo consumo integrado con un entorno de visualización geoespacial en un activo en servicio, con lecciones sobre pérdida de paquetes, ancho de banda y umbrales. El gemelo se encuentra en fase de monitor con calibración pendiente, no de gemelo plenamente actualizado. Para el corpus, la síntesis consiste en utilizar este caso como referencia de madurez y de costos operativos de un gemelo con IoT (lo que funciona, lo que se pierde, lo que falta) y exigir, para cualquier gemelo de recuperación, la medición explícita de disponibilidad de datos, de la brecha modelo-realidad y del costo de mantener el sistema, de modo que la recomendación se base en desempeño demostrado.  | 4.0/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Gemelo digital' es un modelo físico sincronizado con sensores que se actualiza en un lazo cerrado; 'validado' significa aquí que el sistema funcionó en un puente en servicio durante seis meses.
- **P2 Supuestos:** Supone que la estabilidad de frecuencias modales indica ausencia de daño, que los umbrales conservadores sirven y que el éxito operativo se traslada a otros activos.
- **P3 Evidencia:** La evidencia son seis meses de datos de ocho acelerómetros, coeficientes de variación y una comparación preliminar con el FEM; no hay eventos de daño ni validación cuantitativa.
- **P4 Consecuencias:** Si es cierto, las agencias pueden desplegar gemelos con LoRaWAN en activos envejecidos con costo reducido; si es falso, se pueden instalar sistemas cuya utilidad diagnóstica no se ha probado.
- **P5 Contraejemplos:** No se discuten casos en que un monitoreo simple por umbrales, sin FEM, logre la misma detección, ni el costo comparativo.
- **P6 Alternativas:** Alternativas: que la estabilidad se deba a que no hubo cambios estructurales; que el FEM mal calibrado reste valor al gemelo; que la conectividad limite la reproducción en tiempo real.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Duración del monitoreo | 6 | meses | Mayo a agosto de 2025 para los coeficientes de variación | Sec. 5.7, p. 11-12 | Texto | Alta | Ciclo anual no cubierto |
| Acelerómetros triaxiales | 8 | nodos | LoRaWAN; armadura del puente | Sec. 5.2, p. 9 | Texto | Alta | Un solo puente |
| Frecuencia de muestreo | 80 | Hz | Adquisición programada de 102 s cada hora | Sec. 5.3, p. 10; Sec. 5.7, p. 11 | Texto | Alta | Modo por eventos con umbral de 30 mg |
| Umbrales de alerta | 30 / 100 / 200 / 500 | mg | Activación / alerta / advertencia / crítico | Sec. 5.3, p. 10; Sec. 5.8, p. 13 | Texto | Alta | Provisionales |
| Pérdida de paquetes | 5 | % | Primeros tres meses; áreas con interferencia | Sec. 2.1.1, p. 3 | Texto | Alta | Paquetes inciertos descartados |
| Coeficiente de variación de frecuencias modales | menos de 0,5 | % | Modos 0 a 2; ejes X, Y, Z | Sec. 5.7, p. 12 | Texto/Tabla | Media | Rangos de modos mayores aparecen en el texto |
| Frecuencias del FEM | 1,96 / 2,45 / 2,47 | Hz | Primeros tres modos | Sec. 5.8, p. 13 | Texto | Alta | Comparación preliminar |
| Frecuencias observadas | 2,85 / 4,4 / 6,03 | Hz | Respuestas operacionales | Sec. 5.8, p. 13 | Texto | Alta | Diferencias de 45 % a 144 % (cálculo del analista) |
| Amortiguamiento estimado | 2,5 a 4 | % | 2,5-3 % en el primer modo; 3-4 % en modos superiores | Sec. 5.7, p. 12 | Texto | Media | Estudio por modo pendiente |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 6 | Sí | 'The deployment confirms that the DT–SHM system can operate continuously on a live and operational bridge' (p. 13) | Prototipo de sistema demostrado en entorno operativo real durante seis meses; la calibración del gemelo es preliminar. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'can substantially increase implementation and maintenance expenses, which may be prohibitive for agencies operating with limited budgets' (p. 13) | Costos reconocidos como barrera; sin modelo de negocio, precios ni cliente pagador. |
| IRL | 5 | Sí | 'The proposed DT framework integrates physics-based modelling with signal processing and statistical analysis for anomaly detection and adaptive calibration' (p. 3) | Integración operativa de sensado, comunicación, visualización y modelo; la actualización del modelo con datos no está validada. |
| DRL | 3 | Sí | 'Dense sensor networks, UAV-based surveys, and continuous data pipelines' (p. 13) | Necesidad argumentada por envejecimiento de puentes y limitaciones de la inspección tradicional; sin estudio de demanda. |
| SRL | 2.78 | Sí | Componentes: Red LoRaWAN de acelerómetros y gateways (TRL 6), Modelo FEM con lazo de calibración (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 25.0; ÷9 → 2.78; nivel acotado a [1,9] = 2.78 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 4 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 4 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V2 Prototipo sin escalamiento · Severidad: Media · TRL 6 con BRL 2 e IRL 5: sistema operativo en campo, sin modelo de negocio ni validación cuantitativa de la calibración del modelo. · Estrategia de salida: Campañas de más de un año, validación con eventos conocidos y estimación de costo-beneficio frente al monitoreo convencional.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Falacia de la ausencia de evidencia | Se afirma que no hubo falsas alarmas críticas y que los umbrales son válidos, aunque tampoco hubo eventos críticos (Sec. 5.8, p. 13) | No se prueba sensibilidad ni especificidad |
| Apelación a la novedad | Se califica la implementación de 'pioneering' y 'novel' sin comparación sistemática con otros despliegues de campo (Resumen, p. 1; Sec. 6, p. 14) | Sobrestima la contribución |
| Generalización apresurada | Se afirma adaptabilidad a puentes colgantes, de madera y de otras tipologías a partir de un puente de armadura (Sec. 1, p. 2; Sec. 7, p. 14) | Sin evidencia de escalabilidad |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Estabilidad de frecuencias modales → ausencia de pérdida de rigidez | Coeficiente de variación menor de 0,5 % durante seis meses | Coherencia con teoría modal | Sensibilidad probada, eventos de daño, control ambiental | Temperatura, carga de trenes, condiciones de borde | 3 | Correlacional |
| Retroalimentación FEM-sensores → modelo sincronizado con el puente | Comparación preliminar con diferencias de 45 % a 144 % | Plausibilidad | Validación cuantitativa, convergencia del modelo | Idealización de apoyos y materiales | 2 | Hipótesis no probada |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Validación cuantitativa de la calibración del gemelo y de la sensibilidad de detección con eventos conocidos | Crítico | Media | 9 |
| Tecnológico | Continuidad de datos con LoRaWAN en corredores con interferencia y uso de múltiples puertas de enlace | Significativo | Media | 7 |
| Mercado | Costo de instalación, conectividad y mantenimiento frente al valor de evitar fallas o cierres | Crítico | Media | 8 |
| Conocimiento | Escalabilidad a otras tipologías y a redes de activos, incluidos eventos extremos y sismos | Significativo | Media | 8 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Esquema del lazo de calibración híbrido de IA y FEM | Diagrama | Comparación de predicciones modales y parámetros de campo | No aplica | Media |
| Tabla 1 | Comparación de LoRaWAN con otros sistemas de SHM | Tabla | Costo, energía, alcance, tasa de datos y latencia | 0,3-50 kbps; 4-10 años de batería | Media |
| Fig. 11 | Visualización del gemelo con ubicación de acelerómetros | Captura | Disposición de ocho nodos y respuesta en frecuencia del sensor 7 | 8 nodos | Media |
| Fig. 12 | Panel operativo del sistema SHM instalado | Captura | Estado de sensores y puertas de enlace | No aplica | Baja |
| Tabla 2 | Estadísticos de frecuencias modales (media, desviación, mínimo, máximo y CV) | Tabla | Modos 0 a 2 por eje | CV menor de 0,5 % | Alta |
| Fig. 15 | Mapa de calor del coeficiente de variación por modo y eje | Gráfico | Estabilidad modal | CV menor de 1 % | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Qin et al. (enfoque híbrido físico-datos con FEM y medición en tiempo real) | No especificado en documento | Academia | Alineación de la estructura con su gemelo | Combina FEM y medición | Sin despliegue comparable | Creciendo |
| Torzoni et al. (gemelo predictivo con modelos gráficos probabilísticos y aprendizaje profundo) | No especificado en documento | Academia | Diagnóstico en tiempo real y planificación de mantenimiento | Enfoque probabilístico | Validación distinta | Creciendo |
| Sistemas SHM cableados tradicionales (citados) | No especificado en documento | Industria | Instrumentación de alta tasa de datos y baja latencia | Alta fiabilidad de datos | Costo de instalación y mantenimiento | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** No aplica: no se estima una variable resultado
- **X:** No aplica
- **Z (controles):** Tipo de evento (pasada de tren), ejes X, Y, Z, modo
- **Datos:** Seis meses de datos de ocho acelerómetros; muestreo a 80 Hz
- **Método:** Análisis modal operacional por FFT con comparación contra FEM; estadísticos descriptivos de frecuencias
- **Efecto reportado:** No cuantificado en términos de decisión o costo
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin análisis de sensibilidad; correlación ambiental incompleta

| Vacío | Tipo | Descripción |
|---|---|---|
| V-023-01 | TERR | Un solo puente ferroviario en Australia; sin zonas sísmicas ni América Latina |
| V-023-02 | POBL | Sin análisis de usuarios, operadores ferroviarios ni impactos económicos de interrupciones |
| V-023-03 | TEMP | Seis meses; sin ciclo estacional anual ni degradación de largo plazo |
| V-023-04 | MET | Identificación modal elemental y calibración no validada |
| V-023-05 | VAR | Faltan variables de costo, disponibilidad de datos, daño y condiciones ambientales |
| V-023-06 | TEOR | Sin teoría de gestión de activos ni de decisión bajo incertidumbre |
| V-023-07 | CAUS | Sin evidencia causal de beneficio del gemelo sobre mantenimiento o seguridad |
