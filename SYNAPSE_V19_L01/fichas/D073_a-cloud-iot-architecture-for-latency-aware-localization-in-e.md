# FB-L01-073 | D073 — A Cloud-IoT Architecture for Latency-Aware Localization in Earthquake Early Warning

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/sensors-23-08431.pdf` · 24 páginas · Relevancia para el eje del corpus: **Adyacente** (Propone y evalúa una arquitectura nube-IoT para alerta temprana sísmica regional en la que la detección de la onda P se hace en el dispositivo, la información se envía por MQTT a la nube de AWS, se localiza el epicentro con un algoritmo de hipérbolas y diferencias de tiempo de llegada y se notifica a los usuarios. Aporta medidas de latencia de extremo a extremo frente a PRESTo (3,39 s de ventaja) y de notificación, centrales para la alerta con IoT, aunque se evalúa por simulación con registros de estaciones de observatorio, un solo evento en la comparación, sin dispositivos físicos de bajo costo ni vínculo con empresas o recuperación.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-073 / D073
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Pierleoni, P., Concetti, R., Belli, A., Palma, L., Marzorati, S., & Esposito, M. (2023). A Cloud-IoT Architecture for Latency-Aware Localization in Earthquake Early Warning. *Sensors*, *23*(20), Article 8431. https://doi.org/10.3390/s23208431
- **Autores:** Pierleoni, Paola (7003839298); Concetti, Roberto (57207201813); Belli, Alberto (57190992867); Palma, Lorenzo (56347240100); Marzorati, Simone (6603252124); Esposito, Marco (57479883100)
- **Afiliaciones:** Department of Information Engineering (DII), Università Politecnica delle Marche, Ancona, 60131, Italy; Istituto di Istruzione Superiore Carlo Urbani, Porto Sant’Elpidio, 63821, Italy; Istituto Nazionale di Geofisica e Vulcanologia (INGV), Osservatorio Nazionale Terremoti, Ancona, 60131, Italy
- **Fecha de publicación:** 2023
- **Fuente/contenedor:** Sensors · vol. 23(20)
- **Identificador persistente:** DOI 10.3390/s23208431 · ISSN 14248220
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85175276750&doi=10.3390%2fs23208431&partnerID=40&md5=4c53d4388cf90c1ed3695243f6fbb27d
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 15

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Proponer una arquitectura IoT completa para la detección, la localización y la notificación de terremotos, diseñada, desplegada y probada en una plataforma estándar de nube, que traslada el picado de la onda P a los propios dispositivos IoT en lugar de procesar flujos de ondas en un centro de datos como en los sistemas regionales de alerta temprana. Los autores desarrollan, además, un algoritmo de localización basado en el método de la hipérbola con multilateración por diferencias de tiempo de llegada (TDoA), y buscan medir su exactitud y su latencia frente a PRESTo, el programa de referencia para alerta temprana regional en Italia y Europa.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si el picado en el dispositivo y el uso de MQTT reducen la latencia de localización y de declaración de eventos frente a un sistema regional centralizado, si el algoritmo de hipérbolas y TDoA ofrece errores aceptables para una alerta temprana, y si los servicios de nube entregan las notificaciones con retardos compatibles con la alerta.

**Marco teórico.** El marco distingue los sistemas de alerta temprana en sitio, regionales e híbridos. Los sistemas regionales detectan, localizan y estiman la magnitud con flujos de varias estaciones, como PRESTo (con FilterPicker, RTLoc y RTMag), el Virtual Seismologist en SeisComP y ShakeAlert. Los autores sostienen que la densificación de redes era costosa y que la tecnología IoT con acelerómetros MEMS, computación en la nube y en el borde y crowdsensing (MyShake, SeismoCloud, EarthCloud) permite redes de bajo costo, y que la localización por hipérbolas se vuelve atractiva por su rapidez y simplicidad. La Tabla 1 compara VS(SC), PRESTo y la propuesta y la Tabla 2 compara trabajos relacionados de localización por aprendizaje automático, redes convolucionales y métodos TDoA. La arquitectura tiene tres capas: percepción, aplicación y empresa.

**Metodología.** La capa de percepción se concibe como un computador de placa única con acelerómetro que muestrea la aceleración, detecta la onda P con FilterPicker y publica en un corredor MQTT un mensaje con las marcas de tiempo, además de un fragmento corto de traza para el cálculo de aceleración pico del suelo. En la nube de AWS, un módulo en una instancia EC2 asocia los picks con un criterio de coincidencia temporal (ondas P de 6,5 km/s, estaciones a menos de 40 km y diferencia máxima de 6 s), localiza el epicentro con hipérbolas construidas por TDoA con profundidad fija de unos 10 km, calcula la aceleración pico, estima el tiempo de llegada de la onda S a puntos objetivo y notifica por Amazon SNS si se supera un umbral. La evaluación usa 175 eventos de magnitud local mayor o igual a 3,5 ocurridos entre 2016 y 2020 en Italia central, con más de 5000 trazas de la base de movimiento fuerte del INGV, y simula el comportamiento en tiempo real de estaciones y dispositivos con una herramienta propia. La comparación con PRESTo se hace en modo de reproducción para el evento de magnitud 5,4 del 26 de octubre de 2016, con ambos sistemas en la misma instancia de AWS y con cinco estaciones como condición de parada, y se mide la notificación mediante registros de CloudWatch.

**Resultados principales.** Los resultados indican que, en el evento de referencia, el primer pick en la estación FEMA se detecta a los 0,312 s con la propuesta y a los 2,13 s con PRESTo, y que la propuesta localiza con un error de 1,341 km a los 251 ms tras el último pick, mientras que PRESTo ofrece su primera localización a los 1,64 s con un error de 13,34 km, de modo que el tiempo total de alerta es de 0,583 s frente a 4,05 s, con una ventaja de 3,39 s, una reducción de la zona ciega de unos 11 km y 17,88 s antes de la llegada de la onda S a Ancona (frente a 14,49 s). Con los 175 eventos, el error de localización tiene media de 9,6307 km, mediana de 5,2851 km, percentil 90 de 22,340 km y rango intercuartil de 8,804 km, y para magnitudes mayores de 4,5 la media sube a 13,7 km, la mediana es de 5,9 km y el percentil 90 es de 36 km, con valores atípicos por encima de 30 km. El tiempo de ejecución del algoritmo tiene media de 163 ms, desviación de 154 ms y máximo de 1,87 s. La regla de SNS tarda 143 ms en ejecutarse y la entrega al destino 207 ms en promedio, con casi 1000 mensajes sin pérdidas. Las conclusiones indican un error medio de 9,8 km, que no coincide con el de 9,6307 km del análisis.

**Discusión y contribución.** Los autores sostienen que el picado en el dispositivo y el uso de MQTT reducen la latencia de datos, que es el factor principal de la latencia de extremo a extremo en redes regionales, que los errores de localización son aceptables para la alerta temprana porque en este escenario prima la rapidez sobre la exactitud, y que la integración en la nube facilita servicios adicionales como almacenamiento, gestión de dispositivos y notificación. Señalan que, con una red más densa, el algoritmo podría detenerse antes y que un enfoque de cómputo en el borde de acceso múltiple con 5G y comunicaciones de baja latencia y alta confiabilidad podría adelantar aún más la localización. Reconocen que la estimación de magnitud no está implementada y que la comparación con PRESTo termina en la localización.

**Limitaciones declaradas.** Declaradas: el sistema no estima la magnitud del evento y la comparación con PRESTo se detiene en la localización; los valores de velocidad de propagación y de profundidad se fijan y deben ajustarse para otras regiones; la exactitud en alerta temprana es un compromiso con el tiempo de respuesta. No declaradas: la comparación de latencia con PRESTo se basa en un solo evento; los dispositivos se simulan con una herramienta y no hay unidades físicas desplegadas ni medición de consumo y carga de procesamiento del picado en una placa; la red de comunicación no se mide porque PRESTo, el servidor SeedLink y los dispositivos simulados se ejecutan en la misma máquina o región; los datos provienen de estaciones de observatorio de alta calidad y no de acelerómetros MEMS ruidosos; no se analizan falsas alarmas ni pérdida de estaciones; PRESTo se ejecuta con paquetes de 1 s, que inflan su tiempo de detección; el error del evento de referencia no es representativo del error medio del conjunto; no se reportan costos; no se publican datos ni código.

**Trabajo futuro.** Explícito: incorporar cómputo en el borde de acceso múltiple con 5G y comunicaciones de baja latencia y alta confiabilidad para adelantar la localización, reemplazar el módulo de localización por alternativas que aprovechen el picado descentralizado y desplegar más servicios en la nube. Implícito: estimación de magnitud, pruebas con dispositivos físicos de bajo costo, evaluación de falsas alarmas y despliegue en redes reales.

**Palabras clave.** Declaradas: cloud computing; early warning systems; earthquake localization; Internet of Things | Inferidas: alerta temprana sísmica, IoT, MQTT, computación en la nube, localización de epicentro, TDoA, picado de onda P, latencia, AWS, PRESTo

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Realizar el picado de la onda P en el dispositivo IoT, transmitir solo las marcas de tiempo por MQTT a una nube estándar y localizar el epicentro con hipérbolas por TDoA reduce la latencia de la alerta: en un sismo de magnitud 5,4 la propuesta emite la localización a los 0,583 s con un error de 1,341 km, 3,39 s antes que PRESTo, con un error medio de 9,6 km en 175 eventos, tiempos de ejecución de 163 ms y notificación en cerca de 350 ms.

**Antítesis identificada.** La comparación de latencia con PRESTo descansa en un solo evento, con un entorno de reproducción en el que los paquetes de 1 s retrasan la detección de PRESTo, sin retardo de red real y con dispositivos simulados en la misma máquina. La propuesta omite la estimación de magnitud, que PRESTo sí incluye, de modo que la ventaja no compara alertas equivalentes. El error medio de 9,6 km con profundidad y velocidad fijas empeora para los eventos de magnitud mayor de 4,5 (media de 13,7 km y valores por encima de 30 km), que son los que importan para la alerta. Las estaciones del conjunto son sensores de observatorio, no acelerómetros MEMS de bajo costo, y no se evalúan falsas alarmas, fallas de comunicación, consumo ni costos. La conclusión repite un error de 9,8 km que no coincide con el análisis.

**Síntesis propuesta.** La contribución sostenible es un diseño de referencia coherente, con picado en el dispositivo y mensajería MQTT sobre una nube comercial, que demuestra en simulación que el retardo de transporte y de empaquetado de flujos es una fracción importante de la latencia total y que puede reducirse. Para el corpus, importa por su cuantificación de la latencia de alerta con IoT y nube, por el uso de servicios que una empresa podría contratar y por su carácter modular. No obstante, la magnitud de la ventaja de 3,39 s depende de un solo evento y de condiciones favorables de simulación, y la evidencia debe ampliarse con dispositivos físicos, redes reales, más eventos y la estimación de magnitud antes de afirmar que supera a los sistemas regionales.

**Áreas grises detectadas.**

1. Representatividad de la comparación: la ventaja de 3,39 s se calcula con un único evento de magnitud 5,4 con cinco estaciones como condición de parada y PRESTo recibiendo paquetes de 1 s, de modo que su detección tarda 2,13 s frente a 0,312 s de la propuesta; no se repite la comparación con otros eventos ni con paquetes más pequeños, y el texto concluye una ventaja general.
2. Dispositivos y red simulados: el picado en el dispositivo se emula con una herramienta de simulación en una máquina, y el servidor SeedLink y los dispositivos simulados comparten máquina, por lo que no se miden los retardos de red móvil o satelital ni la carga de un computador de placa única con FilterPicker, que son la base de la afirmación de baja latencia y bajo consumo.
3. Estaciones frente a sensores de bajo costo: las 5000 trazas proceden de estaciones de movimiento fuerte del INGV, cuya calidad y sincronización de tiempo son superiores a las de un acelerómetro MEMS de placa única, y no se estudian el error de reloj ni el ruido que afectarían tanto el picado como la diferencia de tiempos de llegada.
4. Alcance de la alerta: la propuesta no estima magnitud ni evalúa falsas alarmas, y el error de los eventos grandes es mayor (media de 13,7 km con atípicos de más de 30 km), de modo que no se sabe cuán útil sería la alerta emitida a los 0,583 s para decidir acciones en una planta o un edificio.

**Puntos oscuros aclarados.** Llama la atención que el resumen presente una ventaja de 3,39 s sobre el estándar italiano como métrica tangible cuando proviene de un único evento y de un entorno de reproducción configurado por los propios autores. También es notable que el error de localización del evento de referencia sea de 1,341 km, mucho menor que la media de 9,6 km del conjunto, y que el error de 13,34 km de PRESTo se describa como error inicial sin indicar si su estimación se refina después, de modo que no se sabe si la comparación de exactitud es equivalente. La arquitectura se describe como desplegada en AWS, pero los dispositivos son simulados y la red de transporte es una máquina local. El texto indica que el rendimiento de MQTT frente a SeedLink se estableció en un trabajo previo y lo da por supuesto. La conclusión cita un error medio de 9,8 km, que difiere de 9,6307 km, y el conjunto de datos se describe como no disponible. Por último, la propuesta no maneja la profundidad ni la velocidad con datos locales y las fija en 10 km y 6,5 km/s, lo que limita su uso fuera de los Apeninos.

**Ideas propositivas novedosas.**

1. Piloto con dispositivos físicos de bajo costo: instalar entre 15 y 30 computadores de placa única con acelerómetros MEMS en edificios y plantas de Italia central, con picado FilterPicker local y comunicación MQTT por redes reales (4G y Wi-Fi), y registrar durante seis meses los picks de sismos reales y de falsos disparos, la latencia de extremo a extremo, el consumo y el error de reloj. Comparar con PRESTo en los eventos disponibles y con 20 o más eventos simulados permitiría saber si la ventaja de segundos se mantiene con hardware real y cuál es el costo por punto de medición, y qué porcentaje de falsas alarmas tolera una empresa que apagaría procesos.
2. Del segundo de alerta al valor para la empresa: definir tres acciones automáticas de una planta (detener líneas, cerrar válvulas, colocar equipos en posición segura) con tiempos de ejecución medidos, y calcular con simulaciones de 100 eventos cuántas de estas acciones se completan antes de la onda S según la latencia de la propuesta y de PRESTo. Con el costo de cada acción omitida se obtendría una estimación del valor monetario de cada segundo ganado, y se podría establecer a partir de qué distancia al epicentro la alerta deja de ser útil, información para decidir si una pyme invierte en una red propia de alerta.

**Relaciones poco exploradas.**

1. Detección sísmica en el borde (complementa) D049, D060 y D071: D049 procesa la detección en el nodo, D060 clasifica la intensidad en el borde y D071 aporta interoperabilidad semántica; D073 mide la latencia de extremo a extremo y de notificación con picado en el dispositivo.
2. Alertas con redes de bajo costo (se relaciona con) D075 y D064: D075 propone una red LoRa multisalto descentralizada para alerta y D064 una arquitectura 5G con cómputo en el borde para el gemelo de edificios; D073 muestra que la nube comercial y MQTT bastan para latencias de cientos de milisegundos en simulación.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 6/10 — Aporta una arquitectura nube-IoT con picado en el dispositivo, MQTT y localización TDoA, con medidas explícitas de latencia (0,583 s frente a 4,05 s de PRESTo), de error (media de 9,6 km en 175 eventos) y de notificación (143 y 207 ms). Su valor para el corpus es medio-alto por la coincidencia con IoT, sismo y latencia, y se reduce porque la comparación es de un solo evento, los dispositivos se simulan, no hay costos, falsas alarmas ni magnitud, y no se vincula con empresas, pero ofrece un patrón replicable y una referencia cuantitativa.

**Conexiones inter-documentales.**

- **CONFIRMA** D049 (Alerta temprana sísmica de bajo costo con procesamiento en el nodo): relación inversa de D049 CONFIRMA D073: ambos muestran que detectar y generar la alerta en el nodo reduce la latencia frente a arquitecturas centralizadas (D049 1,24 a 2,88 s; D073 localizac [juicio del analista]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 52 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Generalización desde un solo caso (La ventaja de 3,39 s sobre el estándar italiano se presenta como métrica de eficiencia general (Resumen, p. 1; Sec. 4.3, p. 20)); Comparación de exactitud sin equivalencia declarada (El error de 13,34 km de PRESTo se llama inicial y el de 1,341 km de la propuesta es el de la localización tras cinco picks (Sec. 4.3, p. 20)); Condiciones favorables presentadas como ventaja de diseño (PRESTo recibe paquetes de 1 s y la red no se simula (Sec. 4.3, p. 19-20))
- **Bradford-Hill:** No aplica: es un estudio de ingeniería de simulación; no se estima causalidad con datos observacionales.
- **TRL asignado:** 4 — 'The architecture, which has been designed, deployed, and tested on a standard cloud platform' (p. 1)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (24 páginas). La Tabla 4 repite el percentil 90 en dos filas; se cita la media, el máximo y el percentil 90 como aparecen. Las páginas siguen los marcadores del PDF. La cifra de 9,8 km de las conclusiones se cita como aparece y se señala la diferencia con 9,6307 km.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Realizar el picado de la onda P en el dispositivo IoT, transmitir solo las marcas de tiempo por MQTT a una nube estándar y localizar el epicentro con hipérbolas por TDoA reduce la latencia de la alerta: en un sismo de magnitud 5,4 la propuesta emite la localización a los 0,583 s con un error de 1,341 km, 3,39 s antes que PRESTo, con un error medio de 9,6 km en 175 eventos, tiempos de ejecución de 163 ms y notificación en cerca de 350 ms.  | La comparación de latencia con PRESTo descansa en un solo evento, con un entorno de reproducción en el que los paquetes de 1 s retrasan la detección de PRESTo, sin retardo de red real y con dispositivos simulados en la misma máquina. La propuesta omite la estimación de magnitud, que PRESTo sí incluye, de modo que la ventaja no compara alertas equivalentes. El error medio de 9,6 km con profundidad y velocidad fijas empeora para los eventos de magnitud mayor de 4,5 (media de 13,7 km y valores por encima de 30 km), que son los que importan para la alerta. Las estaciones del conjunto son sensores de observatorio, no acelerómetros MEMS de bajo costo, y no se evalúan falsas alarmas, fallas de comunicación, consumo ni costos. La conclusión repite un error de 9,8 km que no coincide con el análisis.  | La contribución sostenible es un diseño de referencia coherente, con picado en el dispositivo y mensajería MQTT sobre una nube comercial, que demuestra en simulación que el retardo de transporte y de empaquetado de flujos es una fracción importante de la latencia total y que puede reducirse. Para el corpus, importa por su cuantificación de la latencia de alerta con IoT y nube, por el uso de servicios que una empresa podría contratar y por su carácter modular. No obstante, la magnitud de la ventaja de 3,39 s depende de un solo evento y de condiciones favorables de simulación, y la evidencia debe ampliarse con dispositivos físicos, redes reales, más eventos y la estimación de magnitud antes de afirmar que supera a los sistemas regionales.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Picado' es la detección del arribo de la onda P; 'TDoA' es la diferencia de tiempo de llegada entre dos estaciones; 'MQTT' es un protocolo de mensajería ligero; 'zona ciega' es el área alrededor del epicentro donde la alerta llega después de la onda S.
- **P2 Supuestos:** Supone que el evento de referencia es representativo, que la simulación en una máquina refleja el retardo de una red real, que las estaciones del INGV representan sensores IoT y que un error de localización de 9,6 km es aceptable para decidir.
- **P3 Evidencia:** La evidencia son 175 eventos de Italia central con más de 5000 trazas, una comparación de latencia con PRESTo en un evento, tablas de error y de tiempo de ejecución, y una medición de unos 1000 mensajes de notificación.
- **P4 Consecuencias:** Si es cierto, una red densa de dispositivos baratos con nube comercial puede emitir alertas segundos antes que los sistemas regionales; si es falso, la ventaja puede desaparecer con redes reales, sensores ruidosos y falsas alarmas.
- **P5 Contraejemplos:** No se examinan dispositivos físicos, retardos de red reales, falsas alarmas, magnitud, costos, error de reloj ni el valor de la alerta para la decisión.
- **P6 Alternativas:** Alternativas: que PRESTo con paquetes más pequeños reduzca la diferencia; que la mejora provenga de cinco picks más que de la arquitectura; que una red LoRa local sea más robusta tras un sismo que una nube.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Ventaja de tiempo de alerta frente a PRESTo | 3,39 | s | 0,583 s frente a 4,05 s en un evento de magnitud 5,4 | Sec. 4.3, p. 20 | Texto | Media | Un solo evento; sin magnitud |
| Tiempo de detección de la onda P en la estación FEMA | 0,312 frente a 2,13 | s | Propuesta frente a PRESTo | Tabla 5, p. 20 | Tabla | Media | Paquetes de 1 s en PRESTo |
| Error de localización del evento de referencia | 1,341 frente a 13,34 | km | Propuesta a los 251 ms y PRESTo a los 1,64 s | Sec. 4.3, p. 20 | Texto | Media | Error inicial de PRESTo |
| Error medio de localización en 175 eventos | 9,6307 | km | Mediana de 5,2851 km y percentil 90 de 22,340 km | Tabla 3, p. 18 | Tabla | Alta | Profundidad y velocidad fijas |
| Error medio para magnitudes mayores de 4,5 | 13,7 | km | Mediana de 5,9 km y percentil 90 de 36 km | Tabla 3, p. 18 | Tabla | Media | Muestra menor |
| Tiempo de ejecución medio del algoritmo | 163 | ms | Máximo de 1,87 s | Tabla 4, p. 19 | Tabla | Alta | Instancia EC2 |
| Tiempo de ejecución de la regla de SNS y de entrega | 143 y 207 | ms | Casi 1000 mensajes sin pérdidas | Sec. 4.4, p. 21 | Texto | Alta | Misma región de AWS |
| Eventos y trazas del conjunto de datos | 175 y más de 5000 | eventos y trazas | Magnitud mayor o igual a 3,5; 2016 a 2020 | Sec. 4.1, p. 14 | Texto | Alta | Italia central |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'The architecture, which has been designed, deployed, and tested on a standard cloud platform' (p. 1) | Validación de la arquitectura en laboratorio y en la nube con registros reales reproducidos; dispositivos simulados y sin red física. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'Until a few years ago, the densification of seismic networks would have been challenging due to the high costs of dedicated seismic instrumentation' (p. 2) | Se plantea la ventaja de costo de IoT sin cifras de costos ni modelo de negocio. |
| IRL | 4 | Sí | 'During this benchmark, almost 1000 message were sent with no lost messages' (p. 21) | Integración de MQTT, EC2, SNS y simulación de dispositivos medida; sin dispositivos físicos ni redes reales. |
| DRL | 3 | Sí | 'PRESTo is, therefore, considered as the reference EEW software architecture for the tests carried out in this study' (p. 3) | Se identifica una referencia de uso institucional; sin estudio de demanda de empresas. |
| SRL | 1.56 | Sí | Componentes: Dispositivo IoT con picado local (TRL 3), Aplicación en la nube para asociación, localización y notificación (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 14.0; ÷9 → 1.56; nivel acotado a [1,9] = 1.56 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 2 e IRL 4: arquitectura medida en simulación con un solo evento de comparación, sin dispositivos físicos ni costos. · Estrategia de salida: Piloto con hardware de bajo costo, redes reales, evaluación de falsas alarmas y estimación de magnitud.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Generalización desde un solo caso | La ventaja de 3,39 s sobre el estándar italiano se presenta como métrica de eficiencia general (Resumen, p. 1; Sec. 4.3, p. 20) | Un evento no establece una distribución |
| Comparación de exactitud sin equivalencia declarada | El error de 13,34 km de PRESTo se llama inicial y el de 1,341 km de la propuesta es el de la localización tras cinco picks (Sec. 4.3, p. 20) | No se indica si PRESTo refina su estimación |
| Condiciones favorables presentadas como ventaja de diseño | PRESTo recibe paquetes de 1 s y la red no se simula (Sec. 4.3, p. 19-20) | La diferencia puede deberse en parte a la configuración |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Picado en el dispositivo y MQTT → menor latencia de detección y de alerta | Comparación en un evento con tiempos de detección de 0,3 s frente a 2 s | Mecanismo directo de eliminación de paquetes y transmisión | Pruebas en redes reales y en más eventos | Tamaño de paquete, retardo de red, hardware | 3 | Efecto plausible en simulación |
| Más estaciones con picks → menor error de localización | Evolución del error en el evento de referencia | Relación mecánica | Datos con ruido de sensores de bajo costo | Geometría de la red, velocidad y profundidad | 3 | Efecto establecido en el evento |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Comparación con PRESTo en múltiples eventos, con paquetes pequeños y con retardos de red reales | Crítico | Media | 9 |
| Tecnológico | Dispositivos físicos de bajo costo con consumo, error de reloj y falsas alarmas | Crítico | Media | 9 |
| Conocimiento | Valor de la alerta para acciones de empresas y estimación de magnitud | Crítico | Alta | 8 |
| Mercado | Costos de red y de operación frente a servicios de alerta existentes | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Flujo lógico del módulo de localización y declaración de eventos | Diagrama | Picks, asociación, localización y notificación | No aplica | Media |
| Fig. 3 | Visión general de la aplicación nube-IoT con servicios adicionales | Diagrama | Capas de percepción, aplicación y empresa | 3 capas | Media |
| Fig. 9 | Evolución del error de localización al detectar cada estación | Gráfico | Error menor de 6 km con dos estaciones y menor de 2 km con cuatro | 6 km; 2 km | Alta |
| Tabla 3 | Estadísticas de error para el conjunto completo y para magnitudes mayores de 4,5 | Tabla | Media de 9,6307 km y de 13,7 km | 9,6307; 13,7 | Alta |
| Tabla 5 | Tiempos de detección de PRESTo y de la propuesta en cinco estaciones | Tabla | Detección de 0,286 a 0,410 s frente a 1,84 a 2,41 s | 0,286-0,410 s | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| PRESTo (PRobabilistic and Evolutionary early warning SysTem) | Italia | Academia | Alerta temprana regional con picado, localización y magnitud | Referencia italiana y europea | Picado centralizado con latencia de flujo | Estable |
| Virtual Seismologist en SeisComP VS(SC) | No especificado en documento | Academia | Alerta temprana regional | Uso extendido en Europa | Picado centralizado | Estable |
| MyShake, SeismoCloud y EarthCloud | No especificado en documento | Academia | Alerta con teléfonos, sensores y geófonos en la nube | Cobertura y bajo costo | Arquitecturas distintas de picado | Creciente |

### B.9 Variables econométricas y vacíos

- **Y:** Tiempo de alerta (s), error de localización (km), tiempo de ejecución y de notificación (ms)
- **X:** Arquitectura con picado en el dispositivo y MQTT frente a PRESTo con flujo SeedLink
- **Z (controles):** Número de estaciones, velocidad de propagación, profundidad fija, tamaño de paquete, magnitud
- **Datos:** 175 eventos de Italia central de 2016 a 2020 con más de 5000 trazas de la base de movimiento fuerte del INGV
- **Método:** Simulación en modo de reproducción con comparación en un evento y estadística descriptiva de error
- **Efecto reportado:** Ventaja de 3,39 s en el evento de referencia; error medio de 9,6307 km en el conjunto
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin repeticiones de la comparación con PRESTo, sin intervalos de confianza

| Vacío | Tipo | Descripción |
|---|---|---|
| V-073-01 | TERR | Italia central (Apeninos); evento de 2016 con epicentro en 42,879 N y 13,129 E y objetivo en Ancona |
| V-073-02 | POBL | Estaciones sísmicas; sin usuarios ni empresas específicas |
| V-073-03 | TEMP | Eventos de 2016 a 2020; latencias de milisegundos a segundos |
| V-073-04 | MET | Simulación con dispositivos emulados, red local y un solo evento de comparación |
| V-073-05 | VAR | Faltan costos, consumo, error de reloj, falsas alarmas y magnitud |
| V-073-06 | TEOR | Alerta temprana e IoT; sin teoría de continuidad de operaciones |
| V-073-07 | CAUS | Efecto de la alerta sobre acciones y pérdidas sin evidencia |
