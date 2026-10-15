# FB-L01-084 | D084 — Synchronized IoT Framework for Vibration-Based Structural Health Monitoring of Suspension Bridges

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/Synchronized_IoT_Framework_for_Vibration-Based_Structural_Health_Monitoring_of_Suspension_Bridges.pdf` · 17 páginas · Relevancia para el eje del corpus: **Adyacente** (Presenta el diseño, la implementación y la validación experimental de un sistema IoT de monitoreo de salud estructural de puentes colgantes con cinco nodos MEMS sincronizados por GPS, comunicación ESP-NOW, pasarela con enlace celular LTE y análisis modal en la nube, probado en un modelo de laboratorio sobre una mesa vibratoria con cuatro escenarios de daño. Aporta un patrón de sensado sincronizado de bajo costo y datos de consumo de energía para infraestructura, pertinente para IoT y estructuras sometidas a excitación sísmica, aunque la validación es a escala de laboratorio, con daño extremo, sin repeticiones y sin vínculo con empresas ni recuperación.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-084 / D084
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Hassan, M., Nassr, A. A., & AbdelRaheem, M. (2026). Synchronized IoT Framework for Vibration-Based Structural Health Monitoring of Suspension Bridges. *IEEE Open Journal of the Industrial Electronics Society*, *7*, 1051-1067. https://doi.org/10.1109/OJIES.2026.3706609
- **Autores:** Hassan, Muhammad (57668936600); Nassr, Amr A. (24462178600); AbdelRaheem, Mohamed (56597902300)
- **Afiliaciones:** Assiut University, Electrical Engineering Department, Asyut, 71515, Egypt; Ajman University, Department of Civil Engineering, Ajman, 346, United Arab Emirates; Rochester Institute of Technology—Dubai, Department of Electrical Engineering and Computing, Dubai, 341055, United Arab Emirates
- **Fecha de publicación:** 2026
- **Fuente/contenedor:** IEEE Open Journal of the Industrial Electronics Society · vol. 7
- **Identificador persistente:** DOI 10.1109/OJIES.2026.3706609 · ISSN 26441284
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105042939729&doi=10.1109%2fOJIES.2026.3706609&partnerID=40&md5=93dbbbe28ea98b65f35494c6e5e54713
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 0

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Presentar el diseño, la implementación y la validación experimental de un sistema de monitoreo de salud estructural (SHM) basado en el Internet de las cosas (IoT) para puentes colgantes, a partir de mediciones de vibración sincronizadas. La contribución principal declarada es la integración de extremo a extremo de sensado sincronizado de bajo consumo, comunicación inalámbrica en varios niveles y análisis de vibraciones en la nube dentro de un marco unificado, con validación en un puente colgante a escala de laboratorio. Los autores aclaran que la novedad radica en la integración del sistema, el diseño de comunicación y energía y la validación específica para puentes, y no en un nuevo algoritmo de detección de daño.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si nodos MEMS de bajo costo sincronizados por GPS pueden adquirir vibraciones con la alineación temporal que exige el análisis modal, si un enlace ESP-NOW con pasarela celular consume menos energía que TCP/IP sobre Wi-Fi, y si los cambios de frecuencias naturales, formas modales y criterio de aseguramiento modal (MAC) permiten detectar cuatro tipos de daño en cables y péndolas.

**Marco teórico.** El marco combina la detección de daño basada en vibraciones, con frecuencias naturales, formas modales y MAC, y las tecnologías IoT para SHM. Los autores sostienen que los puentes sufren corrosión y fatiga, que la inspección visual y las pruebas no destructivas no detectan daño interno menor, que el mantenimiento preventivo tiene costos que pueden llevar a diferirlo y que el análisis modal exige mediciones sincronizadas, pues un error de 1 ms a 10 Hz introduce un desfase de 3,6°. Se revisan tecnologías de comunicación (Wi-Fi, ESP-NOW, enlaces celulares 4G/LTE, LoRa y LoRaWAN) y sus compromisos de capacidad, alcance y energía, y se concluye que conviene una arquitectura híbrida con comunicación local de bajo consumo y retorno celular.

**Metodología.** Cada nodo de hoja integra una placa NodeMCU (ESP8266), un acelerómetro MEMS ADXL355 de 20 bits, un módulo GPS con señal de pulso por segundo para iniciar la adquisición, un oscilador externo de 1,024 MHz y una batería de 3,7 V y 2500 mAh con panel solar de 10 W. El nodo central usa un microcontrolador STM32F407, un módulo ESP8266 para el enlace local y un módulo LTE Quectel EC25, con tarjeta SD para almacenar datos ante cortes de internet. El servidor ejecuta MATLAB y MySQL, calcula densidades espectrales, identifica frecuencias y formas modales con descomposición en el dominio de la frecuencia y detección de picos en escala-espacio y aplica criterios de daño (descenso de frecuencia mayor de 5 %, MAC menor de 0,8). El muestreo es de 125 muestras por segundo y la transmisión de dos paquetes por segundo por nodo. El modelo de laboratorio es un puente colgante a escala con cinco nodos igualmente espaciados sobre una mesa vibratoria Quanser, con excitaciones senoidales, de barrido y un registro sísmico real, y cuatro escenarios de daño (retiro de una péndola, de dos péndolas, de un segmento del cable principal de borde y del cable principal entre torres).

**Resultados principales.** Los resultados indican que el reloj interno del acelerómetro mostró una variación de frecuencia de hasta 1 %, que podía causar una deriva de hasta 20 ms por segundo, y que el oscilador externo redujo el error de temporización a 50 microsegundos. ESP-NOW mantuvo la tensión de la batería por más tiempo y consumió menos energía por paquete que TCP/IP sobre Wi-Fi, y el modo de sueño extendió la vida de la batería de los nodos en alrededor de 40 %. En el modelo de prueba, la primera frecuencia natural cayó 23,4 % en el daño 1 (con las frecuencias segunda y tercera variando menos de 0,3 %), 47,6 % en el daño 2, 26,6 % en el daño 3 y 46,1 % en el daño 4. Los autores convierten la caída de la primera frecuencia en un índice de pérdida de rigidez equivalente, que ubican como moderada en el daño 1, intermedia en el daño 3 y severa en los daños 2 y 4. Las formas modales muestran distorsiones locales en los daños de péndolas y globales en los de cables, y el MAC conserva valores altos en el daño 1 y muestra acoplamiento modal en los daños 2 y 4 y una caída en el tercer modo en el daño 3. Los autores declaran que no se hizo análisis estadístico de repetibilidad.

**Discusión y contribución.** Los autores sostienen que el sistema demuestra la adquisición de vibraciones sincronizadas, la transmisión inalámbrica confiable y la captura de cambios modales sensibles al daño, que el diseño ESP-NOW y LTE reduce la energía de comunicación frente a TCP/IP sobre Wi-Fi y que, con el modo de sueño, extiende la vida de los nodos, y que el conjunto es una plataforma rentable, eficiente en energía y escalable para el monitoreo distribuido de estructuras. Reconocen que la validación se limita a condiciones de laboratorio con un modelo a escala, que el desempeño a largo plazo con condiciones ambientales reales y en puentes de tamaño real no está verificado, y que la escalabilidad del enlace local depende del alcance de ESP-NOW y de la capacidad de pares de la pasarela, por lo que en puentes largos se desplegarían varias pasarelas.

**Limitaciones declaradas.** Declaradas: la validación se hizo en laboratorio con un modelo a escala y no se hizo un análisis estadístico formal de repetibilidad; el rendimiento a largo plazo en condiciones ambientales y operativas reales y en puentes a escala real está por verificar; la deriva térmica del acelerómetro y las degradaciones de la señal GPS pueden afectar el desempeño al aire libre; la escalabilidad local depende del alcance de ESP-NOW y de la capacidad de pares de la pasarela. No declaradas: los escenarios de daño consisten en retirar cables y péndolas, con caídas de la primera frecuencia de 23 % a 48 %, muy por encima del umbral de detección de 5 %, de modo que la detección es un caso fácil frente a daños incipientes; no hay efectos de temperatura, de humedad ni de tráfico, y la excitación es de mesa vibratoria y no ambiental; solo cinco nodos, sin prueba de escalabilidad; las afirmaciones de bajo costo no se respaldan con una suma de costos; no se compara el desempeño con un sistema de referencia cableado o comercial; no se reportan latencia, pérdida de paquetes ni el consumo de la pasarela; el índice de rigidez equivalente supone masa modal constante; no se evalúan falsos positivos.

**Trabajo futuro.** Explícito: validación de campo en puentes reales, operación de largo plazo en condiciones ambientales prácticas y una evaluación completa de repetibilidad. Implícito: mediciones con excitación ambiental, detección de daños incipientes, despliegue de varias pasarelas y comparación con otros sistemas de referencia.

**Palabras clave.** Declaradas: Cellular network; Internet of Things (IoT); structural health monitoring (SHM); synchronized sampling | Inferidas: IoT, monitoreo de salud estructural, puente colgante, acelerómetro MEMS, sincronización GPS, ESP-NOW, análisis modal operacional, MAC, mesa vibratoria, bajo consumo

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Una red de cinco nodos con acelerómetros MEMS sincronizados por pulso GPS y oscilador externo (error de temporización de 50 microsegundos), comunicación local ESP-NOW y retorno por LTE hacia un servidor que calcula frecuencias naturales, formas modales y MAC permite detectar cuatro escenarios de daño en un modelo a escala de puente colgante, con caídas de la primera frecuencia de 23,4 % a 47,6 %, y extiende en alrededor de 40 % la vida de la batería con modo de sueño, lo que ofrece una plataforma de bajo costo y bajo consumo para el monitoreo vibracional.

**Antítesis identificada.** Los daños inducidos retiran elementos estructurales completos y producen caídas de frecuencia varias veces mayores que el umbral de 5 % que el propio artículo usa, de modo que la detección es trivial y no demuestra sensibilidad a daños incipientes. No hay repeticiones ni estadísticas de repetibilidad, el modelo está en un laboratorio sin variaciones de temperatura y la excitación es de mesa vibratoria. El carácter rentable y escalable se afirma sin suma de costos y con solo cinco nodos. La mejora de 40 % en la vida de batería se obtiene con un esquema de sueño ligero frente a un modo continuo no descrito con detalle, y no hay comparación con un sistema de referencia. El texto reconoce que el desempeño en campo está por verificar.

**Síntesis propuesta.** La contribución sostenible es un diseño de sensado sincronizado y de comunicación de bajo consumo, con parámetros explícitos de temporización y energía, que resuelve el problema de la sincronización de nodos baratos y entrega un flujo de datos completo hasta el análisis modal. Para el corpus, importa por mostrar cómo se logra la sincronización necesaria con MEMS baratos, por su relación con estructuras sometidas a excitación sísmica y por su enlace celular con almacenamiento local ante cortes. Su evidencia de detección es de una prueba de concepto extrema y requiere ensayos con daño incipiente, repeticiones, condiciones ambientales y comparación con referencia, además de costos, para ser útil a decisiones de reocupación o continuidad.

**Áreas grises detectadas.**

1. Severidad de los daños: los cuatro escenarios retiran péndolas o cables principales, y la primera frecuencia cae 23,4 %, 47,6 %, 26,6 % y 46,1 %, frente a un umbral de detección de 5 % que el texto cita de la literatura; el sistema se prueba en el extremo fácil del espacio de daños, de modo que no se sabe su sensibilidad a pérdidas de rigidez de unos pocos por ciento ni su tasa de falsos positivos con variaciones ambientales.
2. Repetibilidad y estadística: el texto declara que los estados estructurales se evaluaron más de una vez durante el desarrollo, pero que un análisis estadístico formal de repetibilidad estaba fuera de alcance, y los resultados se usan para demostrar funcionalidad; sin repeticiones no hay incertidumbre de las frecuencias ni de los valores de MAC reportados.
3. Alcance de rentable y escalable: la conclusión describe una plataforma rentable, de eficiencia energética y escalable, pero no se suman los costos de los componentes ni se prueba más allá de cinco nodos, y el propio texto limita la escalabilidad local al alcance de ESP-NOW y a la capacidad de pares de la pasarela.
4. Comparación de consumo de energía: el aumento de 40 % de vida de batería se atribuye al modo de sueño, y la ventaja de ESP-NOW frente a TCP/IP sobre Wi-Fi se mide con paquetes ficticios en una prueba de caída de tensión; no se compara el sistema completo con un nodo de referencia ni con otras tecnologías como LoRa, ni se mide la energía del GPS ni de la pasarela.

**Puntos oscuros aclarados.** Llama la atención que el resumen califique al sistema de rentable sin presentar ningún costo y que describa una prueba de excitación con registros sísmicos reales sin informar qué excitación se usó en cada escenario de daño. También es notable que la sección de resultados use el MAC para interpretar las características espaciales del daño, aunque el propio texto indica que el MAC no entrega la ubicación del daño respecto de los sensores. El criterio de sincronización se explica con un desfase de 3,6 grados para 1 ms a 10 Hz, pero el sistema final opera con un error de 50 microsegundos sin medida independiente de ese valor. Además, el índice de rigidez equivalente se calcula con la hipótesis de masa modal constante, que no se verifica tras quitar elementos que sí tienen masa. Por último, la sección de comunicación indica que cada muestra se guarda como un número de cuatro bytes y que se envían dos paquetes por segundo, lo que corresponde a un solo canal, mientras que el acelerómetro mide tres ejes.

**Ideas propositivas novedosas.**

1. Prueba de sensibilidad con daño incipiente y repeticiones: repetir los cuatro escenarios con pérdidas graduales de tensión de las péndolas del 2, 5, 10 y 20 por ciento (por ejemplo, con tensores calibrados) y 20 repeticiones por condición, con variaciones de temperatura controladas en una cámara, y reportar la curva de detección (sensibilidad y falsos positivos) del descenso de frecuencia y del MAC con intervalos de confianza. El resultado mostraría el nivel mínimo de daño detectable por el sistema con nodos baratos y si el umbral de 5 % es adecuado, requisito para usarlo en la verificación de puentes tras un sismo.
2. Piloto de campo en un puente pequeño y vínculo con decisiones de uso: instalar los nodos durante seis meses en una pasarela o puente de una ruta que conecta una zona industrial, registrar vibraciones ambientales, temperatura, pérdidas de paquetes, autonomía de la batería y cortes de internet, y construir una regla de decisión de cierre o apertura tras sismos menores basada en el cambio de frecuencias. Con ello se podría estimar el costo total por puente, la tasa de falsas alarmas y cuántas horas de cierre innecesario evita la regla, información para priorizar inversiones de monitoreo que protejan la continuidad logística de empresas.

**Relaciones poco exploradas.**

1. SHM con IoT de bajo costo (complementa) D068 y D064: D068 construye un gemelo de una viga con sensores de desplazamiento de decenas de dólares y D064 una arquitectura 5G con MEMS y retardos medidos; D084 aporta sincronización GPS, comunicación ESP-NOW y datos de energía para estructuras de mayor escala.
2. Inteligencia en el borde para estructuras (se relaciona con) D086 y D069: D086 clasifica anomalías con inteligencia de borde en monitoreo estructural inalámbrico y D069 valora el costo y beneficio de reforzar puentes con tiempo de recuperación; D084 ofrece la capa de adquisición que podría alimentar ambas.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 5/10 — Aporta un diseño de sensado IoT sincronizado completo hasta el análisis modal, con un error de temporización de 50 microsegundos, una ventaja de energía de ESP-NOW frente a TCP/IP, 40 % más de vida de batería con modo de sueño y cuatro escenarios de daño con caídas de frecuencia de 23 % a 48 %. Su valor para el corpus es medio porque se valida en un modelo de laboratorio con daños extremos, sin repeticiones ni efectos ambientales, con costos no reportados y sin conexión con la recuperación empresarial, pero resuelve un problema de sincronización relevante para sensores de bajo costo.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Prueba en el extremo fácil del problema (Se valida la detección retirando cables completos con caídas de frecuencia de 23 % a 48 % frente a un umbral de 5 % (Sec. IV.B, p. 11; Sec. V.B, p. 14)); Afirmación de bajo costo y escalabilidad sin datos (Se califica de rentable y escalable sin suma de costos y con cinco nodos (Resumen, p. 1; Sec. VI, p. 16)); Generalización desde un modelo de laboratorio (Se plantea la utilidad para puentes colgantes a partir de un modelo a escala sobre mesa vibratoria (Resumen, p. 1))
- **Bradford-Hill:** No aplica: es un estudio de ingeniería experimental; no se estima causalidad con datos observacionales.
- **TRL asignado:** 4 — 'Future work will focus on field validation on real bridge structures and long-term operation under practical environmental conditions' (p. 1)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (17 páginas de la revista, con los marcadores del PDF). Las Tablas 1 a 4 (comparación de sistemas, especificaciones y parámetros) y 5 y 6 (frecuencias e índice de rigidez) se extrajeron sin sus valores; solo se citan las cifras del texto. La referencia de ESP-NOW frente a TCP/IP se cita sin cifra de energía porque aparece en gráficos.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Una red de cinco nodos con acelerómetros MEMS sincronizados por pulso GPS y oscilador externo (error de temporización de 50 microsegundos), comunicación local ESP-NOW y retorno por LTE hacia un servidor que calcula frecuencias naturales, formas modales y MAC permite detectar cuatro escenarios de daño en un modelo a escala de puente colgante, con caídas de la primera frecuencia de 23,4 % a 47,6 %, y extiende en alrededor de 40 % la vida de la batería con modo de sueño, lo que ofrece una plataforma de bajo costo y bajo consumo para el monitoreo vibracional.  | Los daños inducidos retiran elementos estructurales completos y producen caídas de frecuencia varias veces mayores que el umbral de 5 % que el propio artículo usa, de modo que la detección es trivial y no demuestra sensibilidad a daños incipientes. No hay repeticiones ni estadísticas de repetibilidad, el modelo está en un laboratorio sin variaciones de temperatura y la excitación es de mesa vibratoria. El carácter rentable y escalable se afirma sin suma de costos y con solo cinco nodos. La mejora de 40 % en la vida de batería se obtiene con un esquema de sueño ligero frente a un modo continuo no descrito con detalle, y no hay comparación con un sistema de referencia. El texto reconoce que el desempeño en campo está por verificar.  | La contribución sostenible es un diseño de sensado sincronizado y de comunicación de bajo consumo, con parámetros explícitos de temporización y energía, que resuelve el problema de la sincronización de nodos baratos y entrega un flujo de datos completo hasta el análisis modal. Para el corpus, importa por mostrar cómo se logra la sincronización necesaria con MEMS baratos, por su relación con estructuras sometidas a excitación sísmica y por su enlace celular con almacenamiento local ante cortes. Su evidencia de detección es de una prueba de concepto extrema y requiere ensayos con daño incipiente, repeticiones, condiciones ambientales y comparación con referencia, además de costos, para ser útil a decisiones de reocupación o continuidad.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Sincronización' es la alineación temporal de las muestras de los nodos por pulso GPS; 'ESP-NOW' es un protocolo inalámbrico de bajo consumo sin conexión; 'MAC' es el criterio que compara formas modales de dos estados; 'frecuencias naturales' son las de resonancia de la estructura.
- **P2 Supuestos:** Supone que un modelo a escala representa un puente real, que quitar cables equivale a daño relevante, que las pruebas de energía con paquetes ficticios son representativas y que el desempeño en laboratorio se mantendrá con el clima y el tráfico.
- **P3 Evidencia:** La evidencia son cinco nodos en un modelo de laboratorio, cuatro escenarios de daño, mediciones de tensión de batería y tablas de frecuencias, sin repeticiones.
- **P4 Consecuencias:** Si es cierto, puentes colgantes podrían monitorearse con nodos baratos y datos en la nube; si es falso, el sistema puede generar falsas alarmas o no detectar daños pequeños con variaciones ambientales.
- **P5 Contraejemplos:** No se examinan daño incipiente, repeticiones, temperatura, escalabilidad más allá de cinco nodos, costos totales ni comparación con una referencia.
- **P6 Alternativas:** Alternativas: que un sistema cableado o comercial dé mejor precisión por costo; que LoRa baste para detectar cambios lentos; que el cuello de botella sea el análisis modal y no la adquisición.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Nodos de sensado sincronizados | 5 | nodos | Acelerómetro MEMS ADXL355 de 20 bits a 125 muestras por segundo | Sec. IV.A, p. 9 | Texto | Alta | Modelo de laboratorio |
| Error de temporización tras el oscilador externo | 50 | μs | Frente a una deriva de hasta 20 ms por segundo con el reloj interno | Sec. III.E, p. 9 | Texto | Media | Sin medida independiente |
| Caída de la primera frecuencia natural por escenario | 23,4; 47,6; 26,6; 46,1 | % | Daños 1 a 4 | Sec. V.B, p. 14 | Texto | Alta | Muy superior al umbral de 5 % |
| Variación de las frecuencias segunda y tercera en el daño 1 | 0,3 | % | Segunda en 10,7 Hz y tercera en 17,8 Hz | Sec. V.B, p. 14 | Texto | Alta | Daño localizado |
| Extensión de la vida útil de la batería con modo de sueño | 40 | % | Frente a operación normal | Sec. V.A, p. 13 | Texto | Media | Sueño ligero |
| Paquetes por segundo por nodo | 2 | paquetes/s | Muestras agrupadas de 4 bytes | Sec. III.C, p. 9 | Texto | Alta | Sin pérdida de paquetes reportada |
| Umbral de detección por frecuencia y por MAC | 5 y 0,8 | % e índice | Valores de la literatura | Sec. II.A, p. 4 | Texto | Alta | Sin calibración propia |
| Capacidad de batería por nodo | 2500 | mAh | 3,7 V y panel solar de 10 W | Sec. III.A, p. 6 | Texto | Alta | Sin costo reportado |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'Future work will focus on field validation on real bridge structures and long-term operation under practical environmental conditions' (p. 1) | Validación de componentes y del sistema integrado en laboratorio con un modelo a escala; sin entorno operativo. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'Despite the advantages of proactive maintenance, its financial demands may discourage infrastructure investment, potentially leading to deferred maintenance and an increased probability of structural failure' (p. 2) | Se plantea la barrera financiera del mantenimiento; sin costos del sistema ni modelo de negocio. |
| IRL | 4 | Sí | 'low-overhead ESP-NOW local communication, long-term evolution (LTE)/TCP-IP backhaul, and cloud-based modal analysis into a unified pipeline' (p. 3) | Integración de sensores, comunicación local, enlace celular y análisis en servidor probada en laboratorio. |
| DRL | 2 | Sí | 'Structural health monitoring (SHM) systems provide realtime feedback on the status of a structure, allowing early intervention' (p. 2) | Se identifica la necesidad de monitoreo; sin estudio de adopción por operadores de puentes. |
| SRL | 1.78 | Sí | Componentes: Nodos de sensado MEMS con sincronización GPS (TRL 4), Pasarela celular y análisis modal en la nube (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 16.0; ÷9 → 1.78; nivel acotado a [1,9] = 1.78 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 1 e IRL 4: sistema integrado probado solo en un modelo de laboratorio, sin costos, sin repeticiones y sin condiciones de campo. · Estrategia de salida: Piloto de campo, pruebas con daño incipiente y variaciones ambientales, análisis de costos y comparación con referencia.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Prueba en el extremo fácil del problema | Se valida la detección retirando cables completos con caídas de frecuencia de 23 % a 48 % frente a un umbral de 5 % (Sec. IV.B, p. 11; Sec. V.B, p. 14) | No muestra sensibilidad a daño incipiente |
| Afirmación de bajo costo y escalabilidad sin datos | Se califica de rentable y escalable sin suma de costos y con cinco nodos (Resumen, p. 1; Sec. VI, p. 16) | Afirmación no sustentada |
| Generalización desde un modelo de laboratorio | Se plantea la utilidad para puentes colgantes a partir de un modelo a escala sobre mesa vibratoria (Resumen, p. 1) | Reconocida como pendiente de validar en campo |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Sincronización GPS y oscilador externo → mediciones alineadas que permiten estimar formas modales | Error de temporización de 50 microsegundos | Mecanismo de temporización | Medición independiente del error y pruebas de larga duración | Calidad de la señal GPS, temperatura | 3 | Efecto plausible en laboratorio |
| Remoción de cables y péndolas → caída de frecuencia y distorsión modal | Cuatro escenarios con caídas de 23 % a 48 % | Relación física directa | Daño incipiente y variaciones ambientales | Temperatura, humedad, masa | 3 | Relación establecida para daño severo |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Repeticiones, sensibilidad a daño incipiente, falsos positivos y efectos ambientales | Crítico | Media | 9 |
| Tecnológico | Despliegue de campo, escalabilidad más allá de cinco nodos y comparación con sistemas de referencia | Crítico | Media | 8 |
| Mercado | Costo total por puente y beneficio frente a la inspección tradicional | Significativo | Media | 8 |
| Conocimiento | Conexión del cambio modal con decisiones de cierre y reapertura tras eventos sísmicos | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Arquitectura del marco SHM con nodos de hoja, nodo central y nube | Diagrama | Sensado sincronizado, ESP-NOW y LTE | No aplica | Media |
| Fig. 2-3 | Nodo de hoja y pasarela central | Diagrama y fotografía | Componentes de hardware | No aplica | Media |
| Fig. 6 | Modelo de puente colgante sobre mesa vibratoria con cinco nodos | Fotografía | Configuración experimental | 5 nodos | Media |
| Fig. 8-9 | Descenso de tensión de la batería, energía por paquete y vida útil con modo de sueño | Gráficos | Ventaja de ESP-NOW y 40 % de extensión | 40 % | Media |
| Tabla 5-6 | Frecuencias naturales e índice de pérdida de rigidez equivalente | Tablas | Primera frecuencia con caídas de 23 % a 48 % | 23,4-47,6 % | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Nodos Wi-Fi con TCP/IP para SHM | No especificado en documento | Academia | Transmisión de vibraciones por Wi-Fi | Alta capacidad | Mayor consumo y sobrecarga según el artículo | Estable |
| Nodos LoRa y LoRaWAN para SHM | No especificado en documento | Academia | Comunicación de largo alcance y bajo consumo | Alcance y baja energía | Baja tasa de datos para vibración continua | Creciente |
| Enlaces celulares 4G/LTE y LTE-M en cada nodo | No especificado en documento | Industria | Conectividad directa a la nube | Acceso directo | Costo y energía por nodo según el artículo | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Frecuencias naturales, MAC, error de temporización, energía y vida útil de batería
- **X:** Escenario de daño (cuatro) y esquema de comunicación (ESP-NOW frente a TCP/IP) y de sueño
- **Z (controles):** Excitación de la mesa vibratoria, posición de los nodos, parámetros de procesamiento
- **Datos:** Mediciones de cinco nodos en un modelo de laboratorio de puente colgante sobre mesa vibratoria
- **Método:** Experimentos de laboratorio con análisis modal operacional (FDD) y pruebas de energía
- **Efecto reportado:** Caída de la primera frecuencia de 23,4 % a 47,6 %; vida de batería +40 %; error de temporización de 50 μs
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin repeticiones ni análisis estadístico de repetibilidad

| Vacío | Tipo | Descripción |
|---|---|---|
| V-084-01 | TERR | Laboratorio no ubicado en el texto; autores en Egipto y Emiratos Árabes Unidos; sin puente real |
| V-084-02 | POBL | Un modelo a escala de puente; sin usuarios ni empresas |
| V-084-03 | TEMP | Experimentos de corta duración; sin monitoreo de largo plazo |
| V-084-04 | MET | Cuatro escenarios de daño severo sin repeticiones |
| V-084-05 | VAR | Faltan costos, temperatura, falsos positivos, daño incipiente y latencia |
| V-084-06 | TEOR | SHM vibracional e IoT; sin teoría de recuperación |
| V-084-07 | CAUS | Efecto de las alertas sobre decisiones de mantenimiento o cierre sin evidencia |
