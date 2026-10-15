# FB-L01-075 | D075 — Rapid and Resilient LoRa Leap: A Novel Multi-Hop Architecture for Decentralised Earthquake Early Warning Systems

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/sensors-24-05960-v2.pdf` · 42 páginas · Relevancia para el eje del corpus: **Adyacente** (Propone y evalúa una arquitectura de comunicación LoRa de difusión multisalto como alternativa a internet público para la alerta temprana sísmica descentralizada, con sensores MEMS de bajo costo en hogares de Nueva Zelanda, simulación de 30 km de radio, un experimento de campo a escala reducida con ocho dispositivos y una comparación con el sistema por internet de CRISiSLab en seis escenarios en Wellington. Aporta una vía de comunicación independiente de la infraestructura de telecomunicaciones tras un sismo, con medidas de latencia y ventana de alerta, y menciona la automatización de equipos, aunque la evidencia es simulada, no prueba fallas de nodos y no trata empresas ni recuperación.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-075 / D075
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Ranasinghe, V., Udara, N., Mathotaarachchi, M., Thenuwara, T., Dias, D., Prasanna, R., Edirisinghe, S., Gayan, S., Holden, C., Punchihewa, A., Stephens, M., & Drummond, P. (2024). Rapid and Resilient LoRa Leap: A Novel Multi-Hop Architecture for Decentralised Earthquake Early Warning Systems. *Sensors*, *24*(18), Article 5960. https://doi.org/10.3390/s24185960
- **Autores:** Ranasinghe, Vinuja (59347698000); Udara, Nuwan (59347698100); Mathotaarachchi, Movindi (59347427600); Thenuwara, Tharindu (59347698200); Dias, Dileeka (24463669100); Prasanna, Raj (36519631800); Edirisinghe, Sampath (57202089398); Gayan, Samiru (56418587200); Holden, Caroline (36081665200); Punchihewa, Amal (16319943000); Stephens, Max (39362352300); Drummond, Paul (59347838000)
- **Afiliaciones:** Department of Electronic & Telecommunication Engineering, University of Moratuwa, Moratuwa 10400, Sri Lanka; Joint Centre for Disaster Research, Massey University, Wellington, 6021, New Zealand; Department of Computer Engineering, University of Sri Jayewardenepura, Ratmalana, 10390, Sri Lanka; SeismoCity Ltd., Wellington, 6023, New Zealand; ADP Consultancy, Palmerston North, 4410, New Zealand; Civil and Environmental Engineering, Faculty of Engineering, University of Auckland, Auckland, 1023, New Zealand; Canterbury Seismic, Christchurch, 8442, New Zealand
- **Fecha de publicación:** 2024
- **Fuente/contenedor:** Sensors · vol. 24(18)
- **Identificador persistente:** DOI 10.3390/s24185960 · ISSN 14248220
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85205242079&doi=10.3390%2fs24185960&partnerID=40&md5=82489c2460762ef352282edca3201b51
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 10

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Introducir una arquitectura de comunicación LoRa multisalto como alternativa a internet público para la alerta temprana sísmica (EEW) y examinar su eficacia para generar una ventana de alerta útil en la red descentralizada de sensores de CRISiSLab en Nueva Zelanda, que detecta sismos con una versión adaptada del algoritmo PLUM y procesa los datos en cada nodo. La arquitectura busca que las alertas se difundan por saltos cortos con un factor de dispersión bajo, incluso cuando la red de telecomunicaciones falla tras un sismo grande o durante las réplicas, y que se mantenga un servicio ininterrumpido.

**Pregunta de investigación.** La pregunta de investigación declarada es si un enfoque de comunicación de datos LoRa multisalto puede alcanzar los niveles de latencia requeridos por un sistema de alerta temprana que opera con detección, generación y difusión de advertencias completamente descentralizadas y que apoya un servicio ininterrumpido.

**Marco teórico.** El marco combina la alerta temprana sísmica basada en sensores MEMS de bajo costo con el algoritmo PLUM de movimiento del suelo, con un disparo de dos estaciones para reducir falsas alarmas, y la tecnología LoRa de modulación por espectro ensanchado, cuyo factor de dispersión (SF) de 7 a 12 intercambia alcance por tiempo de transmisión. Los autores sostienen que los sistemas nacionales de alerta son costosos de implementar y mantener, que los sistemas centralizados dependen de internet y de servidores remotos, vulnerables tras un terremoto, y que LoRaWAN en topología de estrella no sirve para comunicaciones de baja latencia. Se revisan trabajos de redes LoRa en malla y de comunicaciones de emergencia, y se concluye que no existía un estudio con esta arquitectura para difundir mensajes en un área grande con restricciones estrictas de latencia.

**Metodología.** La arquitectura tiene nodos finales (EN) que detectan, generan y difunden alertas, nodos de relevo (RN) fijos y predeterminados que retransmiten con una caché de cinco mensajes y un contador de tiempo de vida, y una pasarela personalizada que monitorea y configura. Se construyó un experimento de campo con ocho dispositivos Lilygo LoRa32 (ESP32 y transceptor SX1276) con potencia mínima de 2 dBm y SF 8, y una simulación con el marco FLoRa en OMNeT++, ampliado a difusión multisalto, con modelo de sombreado log-normal de parámetros medidos en la Universidad de Moratuwa, 100 nodos finales aleatorios, ventanas de 30 km de radio, 25 corridas por SF y rejillas de relevos de 2,6 a 6,5 km según el SF. El mensaje de alerta tiene 11 bytes (identificador de nodo, tiempo de vida y marca de tiempo de detección). El caso de estudio reproduce con LoRa seis escenarios hipotéticos de terremotos en Wellington con cinco sensores Raspberry Shake 4D, sustituyendo los tiempos de transmisión por internet de un estudio previo por los simulados, y calcula la latencia del sistema y la ventana de alerta para cada sensor.

**Resultados principales.** Los resultados indican que con SF 8 y una rejilla de relevos de 3,2 km (361 relevos para 60 por 60 km) el mensaje llega al 100 % de los nodos finales en un máximo de 2,5 s y en promedio 1,18 s, con hasta 22 saltos, y que la velocidad efectiva de propagación mediana es de unos 20 km/s, entre 4 y 30 km/s, muy por encima de la de la onda S de unos 3 km/s. Con SF 12 el tiempo máximo es de 17,5 s. En el experimento de campo, las tasas de entrega son 90 %, 82 % y 48 % en los nodos 6, 7 y 8, con enlaces deficientes por obstrucciones. En el caso de estudio, el retardo de transmisión del nodo detector al verificador sube a entre 0,210 y 0,436 s frente a 0,05 s por internet, la ventana de alerta con LoRa varía de 1,01 a 5,93 s y la de internet de 1,51 a 6,75 s, de modo que LoRa queda ligeramente por detrás. Los autores concluyen que la red es resiliente por la existencia de rutas múltiples. No se prueban fallas de relevos, colisiones por mensajes simultáneos, consumo de energía ni seguridad.

**Discusión y contribución.** Los autores sostienen que el estudio demuestra la factibilidad de LoRa como tecnología principal de transmisión para alerta temprana, que las latencias del sistema son suficientes para superar la velocidad de los movimientos destructivos del suelo, que la red es escalable a cualquier número de nodos finales porque solo los relevos transmiten, y que las ventanas de uno a seis segundos permiten la preparación psicológica, acciones de protección sencillas como agacharse, cubrirse y sujetarse y acciones automáticas como apagar o reducir la velocidad de maquinaria, en particular durante réplicas hasta que se restablezca la telecomunicación. Reconocen que la ventana es corta y que el desempeño frente a sistemas basados en telefonía móvil no se ha comparado.

**Limitaciones declaradas.** Declaradas: se supone que los parámetros de propagación medidos en Moratuwa valen en promedio para Wellington, de terreno distinto; el posicionamiento de relevos en grandes áreas es difícil y requiere pruebas de campo; el mantenimiento y la alimentación de los dispositivos fuera de hogares son retos; faltan análisis de colisiones, pérdidas y tolerancia a fallas de los relevos, de mensajes casi simultáneos, de consumo de energía y de seguridad; se utilizan dispositivos simples de un solo canal. No declaradas: el caso de estudio usa seis terremotos hipotéticos y cinco sensores y no datos de un evento real; los resultados de latencia son simulados y no incluyen interferencia de otras redes LoRa; el ciclo de trabajo de 1 % de las bandas libres restringe la retransmisión y no se explora en eventos múltiples; se afirma resiliencia sin simular daño o falla de nodos; la alimentación continua de relevos tras un sismo con corte de energía no se discute; no se reportan costos del despliegue de relevos.

**Trabajo futuro.** Explícito: analizar el desempeño ante fallas de nodos de relevo, colisiones y mensajes casi simultáneos, el consumo de energía y la seguridad, que los nodos finales puedan retransmitir en redes densas, comparar con sistemas de alerta por telefonía móvil, aprovechar la detección de la onda P para ampliar la ventana, y usar la plataforma para otros mensajes de emergencia, como avisos de estar a salvo y verificación de edificios e infraestructura. Implícito: pruebas a gran escala con terreno variado y despliegues con sismos reales.

**Palabras clave.** Declaradas: broadcast; delay; earthquake; EEW; FLoRa; LoRa; multi-hop; PLUM | Inferidas: alerta temprana sísmica, LoRa, multisalto, difusión, PLUM, sensores MEMS, Raspberry Shake, resiliencia de la comunicación, factor de dispersión, ventana de alerta

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Una red LoRa de difusión multisalto con SF 8, relevos fijos cada 3,2 km y mensajes de 11 bytes disemina una alerta sísmica a todos los nodos en un área de 30 km de radio en 2,4 s o menos, con múltiples rutas, y produce ventanas de alerta de 1,01 a 5,93 s en seis escenarios de Wellington, ligeramente menores que los 1,51 a 6,75 s del sistema por internet, de modo que ofrece una alternativa descentralizada y resiliente cuando la infraestructura de telecomunicaciones falla.

**Antítesis identificada.** La resiliencia se afirma por la existencia de rutas múltiples, pero no se simula ni se prueba la falla de relevos, el corte de energía o la saturación, que son las condiciones en que la red alternativa debe operar. Los resultados del caso de estudio son simulados y con terremotos hipotéticos y cinco sensores, con parámetros de propagación de otro país. El experimento de campo tiene ocho nodos a potencia mínima y entrega de 48 % en un nodo. La ventana de uno a seis segundos es corta, el ciclo de trabajo de 1 % limita las retransmisiones, no se estudian mensajes simultáneos y los relevos fijos exigen un despliegue que tiene costos y alimentación no cuantificados. La comparación con sistemas de telefonía móvil, que son el competidor práctico, queda pendiente.

**Síntesis propuesta.** La contribución sostenible es una arquitectura de comunicación sencilla, con parámetros de diseño explícitos, que cuantifica en simulación el costo en latencia de prescindir de internet y muestra que la pérdida es de fracciones de segundo en la transmisión y de unos 0,5 a 0,8 s en la ventana. Para el corpus, importa porque trata de forma directa la comunicación que debe seguir funcionando tras un sismo, vincula la alerta con la automatización de maquinaria y es replicable con hardware barato. Su evidencia de resiliencia es indirecta y simulada, y requiere pruebas de falla, de energía y de mensajes simultáneos, además de estimaciones de costos y de valor para quienes reciben la alerta.

**Áreas grises detectadas.**

1. Resiliencia sin pruebas de falla: el artículo concluye que la red es resiliente porque hay rutas múltiples hacia cada nodo, y muestra rutas alternativas en ejemplos, pero no simula la falla de uno o varios relevos, la pérdida de energía de la zona ni el daño de antenas, y reconoce que el análisis de tolerancia a fallas de los relevos es trabajo futuro.
2. Realismo del caso de estudio: la comparación con internet reproduce seis terremotos hipotéticos con cinco sensores Raspberry Shake de un estudio previo y sustituye los tiempos de transmisión por valores simulados, con modelos de propagación medidos en Sri Lanka y aplicados a Wellington, de modo que las ventanas de 1,01 a 5,93 s no se observan en eventos reales.
3. Escenario de múltiples alertas: la evaluación estudia la propagación de un solo mensaje, mientras que en un sismo varios nodos detectan casi al mismo tiempo, y con el ciclo de trabajo de 1 % de LoRa y una caché de cinco mensajes el comportamiento de colisiones y de retransmisiones puede cambiar la latencia y la cobertura; el texto lo identifica como una extensión importante pero no lo evalúa.
4. Costos y operación de los relevos: el diseño exige relevos fijos con alimentación y mantenimiento, 361 dispositivos para 60 por 60 km con SF 8, pero no se estima el costo del despliegue, de la alimentación autónoma ni de la pérdida de relevos, que condiciona la ventaja económica sobre una red nacional de alerta.

**Puntos oscuros aclarados.** Llama la atención que el resumen destaque la resiliencia como característica central cuando el artículo no incluye ninguna simulación de falla, y que la ventana de LoRa se presente como lista para la automatización sin medir el tiempo de actuación de ningún equipo. También es notable que el experimento de campo, que sustenta la prueba de concepto, tenga una entrega de 48 % en uno de tres receptores, con enlaces calificados de pobres, y que el texto lo resuelva con una nota sobre la ubicación de los nodos. Los tiempos de retardo de transmisión por internet de un estudio previo (0,05 s) se comparan con simulaciones de LoRa, sin repetir las mediciones de internet en las mismas condiciones. La velocidad efectiva de 20 km/s se calcula en el centro de la distribución, y el texto reconoce que en ciertos nodos baja a 4 km/s. Además, se afirma escalabilidad a cualquier número de nodos finales con una simulación de 100 nodos, y se declara que el sistema se activa solo con alertas, sin analizar las colisiones por mensajes simultáneos. Por último, varios autores trabajan en empresas del sector sísmico, aspecto que se declara y que no afecta el método pero conviene registrar.

**Ideas propositivas novedosas.**

1. Prueba de tolerancia a fallas de relevos: simular y probar en campo con 20 dispositivos la desactivación aleatoria de 10, 20 y 30 por ciento de los relevos, de la caída de la energía en una zona y de la llegada simultánea de cinco alertas, midiendo el porcentaje de nodos alcanzados, la latencia máxima y la ventana de alerta con 100 repeticiones por condición. El resultado indicaría cuántos relevos redundantes son necesarios para mantener la entrega por encima de 95 por ciento y a qué costo, y daría sustento empírico a la afirmación de resiliencia que hoy se apoya en rutas múltiples.
2. De la alerta LoRa a la acción en la planta: conectar un receptor LoRa a un controlador que detenga una línea de producción o cierre válvulas en una planta pequeña de Wellington o Lima, y medir la latencia desde la alerta hasta la actuación, la tasa de falsas activaciones durante tres meses y las pérdidas evitadas en simulacros. Con ello se podría determinar si ventanas de uno a seis segundos bastan para acciones que importan a la continuidad, qué acciones pueden completarse y cuánto cuesta cada falsa parada, información para decidir si una empresa financia su propia red de alerta.

**Relaciones poco exploradas.**

1. Alerta temprana con IoT (complementa) D073 y D071: D073 mide la latencia de una arquitectura nube-IoT con picado en el dispositivo y D071 propone interoperabilidad semántica; D075 aporta una vía de comunicación independiente de la nube y de internet.
2. Comunicación posterremoto y gemelos (se relaciona con) D064 y D066: D064 usa 5G y cómputo en el borde con retardos de 2,1 ms para un gemelo de edificios y D066 propone orquestación en el borde con microclústeres con consenso; D075 muestra que una red local de baja potencia puede cubrir la alerta cuando la red pública falla.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 6/10 — Aporta una arquitectura LoRa de difusión multisalto con parámetros de diseño explícitos (SF 8, rejilla de 3,2 km, 11 bytes), una simulación de 25 corridas por configuración que llega a todos los nodos en 2,4 s o menos y un caso de estudio que cuantifica la ventana de alerta (1,01 a 5,93 s frente a 1,51 a 6,75 s por internet). Su valor para el corpus es medio-alto por tratar la comunicación posterremoto con bajo costo, y se reduce porque la evidencia es simulada, con eventos hipotéticos, sin pruebas de falla, energía, mensajes simultáneos ni costos, y sin vínculo directo con la recuperación empresarial.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Resiliencia afirmada sin prueba de falla (Se concluye resiliencia por rutas múltiples sin simular fallas de relevos (Resumen, p. 1; Sec. 9.3, p. 34)); Generalización desde seis escenarios hipotéticos (La viabilidad frente a internet se concluye de seis terremotos hipotéticos y cinco sensores (Sec. 8, p. 25; Sec. 9, p. 33)); Transferencia de parámetros entre regiones (Se asume que los parámetros de propagación de Sri Lanka valen para Wellington (Sec. 9.2, p. 34))
- **Bradford-Hill:** No aplica: es un estudio de ingeniería de simulación; no se estima causalidad con datos observacionales.
- **TRL asignado:** 4 — 'This exercise is a precursor as a proof of concept at the hardware level to a more detailed simulation study of the architecture' (p. 16)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (42 páginas). El PDF presenta texto duplicado con marcas de revisión en las páginas 13 a 33, por lo que algunas tablas (14 a 17) se leyeron con columnas desordenadas y se usaron las cifras citadas en el texto. Las páginas siguen los marcadores del PDF. Los valores de la ventana de alerta son los de la Sec. 9 (1,01 a 5,93 s para LoRa y 1,51 a 6,75 s para internet); el resumen los redondea a 1-6 s y 1,5-6,75 s. La Tabla 10 indica un máximo de 19 saltos para SF 8, mientras que el texto indica hasta 22 saltos; se cita el texto.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Una red LoRa de difusión multisalto con SF 8, relevos fijos cada 3,2 km y mensajes de 11 bytes disemina una alerta sísmica a todos los nodos en un área de 30 km de radio en 2,4 s o menos, con múltiples rutas, y produce ventanas de alerta de 1,01 a 5,93 s en seis escenarios de Wellington, ligeramente menores que los 1,51 a 6,75 s del sistema por internet, de modo que ofrece una alternativa descentralizada y resiliente cuando la infraestructura de telecomunicaciones falla.  | La resiliencia se afirma por la existencia de rutas múltiples, pero no se simula ni se prueba la falla de relevos, el corte de energía o la saturación, que son las condiciones en que la red alternativa debe operar. Los resultados del caso de estudio son simulados y con terremotos hipotéticos y cinco sensores, con parámetros de propagación de otro país. El experimento de campo tiene ocho nodos a potencia mínima y entrega de 48 % en un nodo. La ventana de uno a seis segundos es corta, el ciclo de trabajo de 1 % limita las retransmisiones, no se estudian mensajes simultáneos y los relevos fijos exigen un despliegue que tiene costos y alimentación no cuantificados. La comparación con sistemas de telefonía móvil, que son el competidor práctico, queda pendiente.  | La contribución sostenible es una arquitectura de comunicación sencilla, con parámetros de diseño explícitos, que cuantifica en simulación el costo en latencia de prescindir de internet y muestra que la pérdida es de fracciones de segundo en la transmisión y de unos 0,5 a 0,8 s en la ventana. Para el corpus, importa porque trata de forma directa la comunicación que debe seguir funcionando tras un sismo, vincula la alerta con la automatización de maquinaria y es replicable con hardware barato. Su evidencia de resiliencia es indirecta y simulada, y requiere pruebas de falla, de energía y de mensajes simultáneos, además de estimaciones de costos y de valor para quienes reciben la alerta.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Factor de dispersión' (SF) es el número de bits por símbolo de LoRa, que reduce la velocidad y aumenta el alcance al crecer; 'nodo final' detecta y difunde alertas; 'nodo de relevo' retransmite sin detectar; 'ventana de alerta' es el tiempo entre la recepción de la alerta y la llegada de la onda S.
- **P2 Supuestos:** Supone que los parámetros de propagación medidos en Sri Lanka son válidos en Nueva Zelanda, que múltiples rutas implican resiliencia, que un mensaje aislado representa la carga de un sismo y que seis eventos hipotéticos bastan para comparar con internet.
- **P3 Evidencia:** La evidencia son 25 corridas de simulación por SF con 100 nodos, un experimento de campo con ocho dispositivos y un caso de estudio con cinco sensores y seis escenarios de la literatura previa.
- **P4 Consecuencias:** Si es cierto, una comunidad puede mantener su alerta sin internet con dispositivos de bajo costo; si es falso, la red puede fallar por falta de energía, relevos dañados, colisiones o ciclos de trabajo, justo cuando se necesita.
- **P5 Contraejemplos:** No se examinan fallas de relevos, energía, mensajes simultáneos, seguridad, comparación con telefonía móvil, costos ni actuación de equipos.
- **P6 Alternativas:** Alternativas: que los mensajes por telefonía móvil o satélite superen en robustez a LoRa; que los nodos finales relevantes bastan con menos relevos; que la ventana de alerta sea demasiado corta para acciones automáticas útiles.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Tiempo máximo para alcanzar todos los nodos con SF 8 | 2,5 | s | Promedio de 1,18 s y hasta 22 saltos | Tabla 10, p. 21 | Tabla | Alta | Simulación de 100 nodos |
| Cobertura del mensaje con SF 8 | 100 | % | Nodos finales alcanzados en 25 corridas | Tabla 10, p. 21 | Tabla | Alta | 0,34 % de relevos sin alcanzar |
| Separación de relevos y número de relevos con SF 8 | 3200 y 361 | m y relevos | Para un área de 60 km por 60 km | Tabla 9, p. 21 | Tabla | Alta | Cálculo con sombreado log-normal |
| Velocidad efectiva de propagación del mensaje con SF 8 | 20 | km/s | Mediana, entre 4 y 30 km/s | Sec. 7.2.1, p. 23 | Texto | Media | Frente a unos 3 km/s de la onda S |
| Ventana de alerta con LoRa frente a internet | 1,01-5,93 frente a 1,51-6,75 | s | Seis escenarios hipotéticos en Wellington | Sec. 9, p. 33 | Texto | Media | Tiempos de LoRa simulados |
| Retardo de transmisión del detector al verificador | 0,210-0,436 frente a 0,05 | s | LoRa multisalto frente a internet | Tabla 14, p. 30 | Tabla | Media | Dos pares de sensores |
| Tasa de entrega en el experimento de campo | 90, 82 y 48 | % | Nodos 6, 7 y 8 | Sec. 4.4, p. 18 | Texto | Media | Ocho dispositivos a 2 dBm |
| Tamaño del mensaje de alerta | 11 | bytes | Identificador, tiempo de vida y marca de tiempo | Sec. 6.2, p. 22 | Texto | Alta | Ciclo de trabajo de 1 % |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'This exercise is a precursor as a proof of concept at the hardware level to a more detailed simulation study of the architecture' (p. 16) | Prueba de concepto de hardware a escala reducida y simulación; sin despliegue en entorno operativo ni eventos reales. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'Among these challenges, extreme implementation costs [4,13–15] and high operating and maintenance costs are the most critical [11]' (p. 2) | Se reconoce el costo como obstáculo y se propone una alternativa de bajo costo, sin cifras de costos ni modelo de negocio. |
| IRL | 3 | Sí | 'we replicate our previously reported Wellington-based scenarios on OMNET++ FLoRa-based simulation substituting TCP/IP data transmission with LoRa' (p. 25) | Integración de la red LoRa con la detección descentralizada probada en simulación; sin integración física con los sensores. |
| DRL | 3 | Sí | 'Our goal is to transmit alert messages using LoRa to all nodes within a 30 km radius before the S-wave reaches them' (p. 4) | Se identifica una necesidad comunitaria con participación de hogares; sin estudio de adopción. |
| SRL | 1.33 | Sí | Componentes: Red LoRa multisalto (nodos finales, relevos y pasarela) (TRL 4), Sensores MEMS con detección PLUM descentralizada (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 12.0; ÷9 → 1.33; nivel acotado a [1,9] = 1.33 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 2 e IRL 3: prueba de concepto con ocho dispositivos y simulación, sin pruebas de falla, energía ni costos. · Estrategia de salida: Piloto con relevos reales, fallas inyectadas, eventos simultáneos, costos y evaluación frente a telefonía móvil.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Resiliencia afirmada sin prueba de falla | Se concluye resiliencia por rutas múltiples sin simular fallas de relevos (Resumen, p. 1; Sec. 9.3, p. 34) | Propiedad no medida |
| Generalización desde seis escenarios hipotéticos | La viabilidad frente a internet se concluye de seis terremotos hipotéticos y cinco sensores (Sec. 8, p. 25; Sec. 9, p. 33) | No hay datos de un evento real |
| Transferencia de parámetros entre regiones | Se asume que los parámetros de propagación de Sri Lanka valen para Wellington (Sec. 9.2, p. 34) | Supuesto reconocido sin contraste |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Menor SF y saltos cortos → menor latencia de difusión | Tabla 10 con tiempos de 0,86 a 5,69 s según el SF | Mecanismo físico directo | Medición en campo a gran escala | Sombreado, colisiones, ciclo de trabajo | 3 | Relación establecida en simulación |
| Rutas múltiples → resiliencia del servicio de alerta | Ejemplos de rutas alternativas en una rejilla | Mecanismo de redundancia | Pruebas con fallas inyectadas | Pérdida de energía, daño físico, congestión | 2 | Relación plausible sin evidencia |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Pruebas de falla de relevos, de energía y de mensajes simultáneos con repeticiones | Crítico | Media | 9 |
| Tecnológico | Despliegue a gran escala con alimentación autónoma y comparación con telefonía móvil | Crítico | Media | 8 |
| Conocimiento | Valor de ventanas de uno a seis segundos para acciones automáticas en empresas | Crítico | Alta | 8 |
| Mercado | Costo de la red de relevos frente a sistemas nacionales de alerta | Significativo | Media | 8 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 6 | Etapas de difusión de una alerta por la red multisalto | Esquema | Origen, relevos cercanos y relevos lejanos | No aplica | Media |
| Fig. 8 | Topología del experimento de campo escalado | Mapa | Ocho nodos en un campus | 8 nodos | Media |
| Fig. 12 | Porcentaje de nodos finales alcanzados en función del tiempo | Gráfico | 100 % en 2,4 s con SF 8 | 2,4 s | Alta |
| Tabla 10 | Estadísticas de diseminación por factor de dispersión | Tabla | Tiempo promedio de 0,86 a 5,69 s | 0,86-5,69 s | Alta |
| Tabla 17 | Comparación de la ventana de alerta con internet y con LoRa | Tabla | Ventana de LoRa de 1,01 a 5,93 s | 1,01-5,93 s | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Sistema de alerta descentralizado con internet de CRISiSLab (referencia propia) | Nueva Zelanda | Academia | Alerta con sensores Raspberry Shake y SD-WAN | Ventana de 1,51 a 6,75 s | Depende de internet | Estable |
| Sistemas nacionales de alerta de Japón, Estados Unidos, Taiwán y México | Japón, Estados Unidos, Taiwán y México | Gobierno | Alerta nacional | Operación oficial | Costos de implementación y mantenimiento extremos | Estable |
| LoRaWAN en topología de estrella | No especificado en documento | Industria | Redes de baja potencia y largo alcance | Estándar abierto | Alta latencia para alerta | Creciente |

### B.9 Variables econométricas y vacíos

- **Y:** Tiempo de difusión (s), cobertura (%), ventana de alerta (s) y tasa de entrega (%)
- **X:** Factor de dispersión (SF), separación de relevos y tipo de comunicación (LoRa o internet)
- **Z (controles):** Modelo de propagación (sombreado), número de saltos, ciclo de trabajo, ubicación de sensores
- **Datos:** Simulaciones FLoRa de 25 corridas por SF con 100 nodos, ocho nodos de campo y seis escenarios hipotéticos con cinco sensores
- **Método:** Simulación de eventos discretos y experimento de campo a escala reducida
- **Efecto reportado:** Cobertura de 100 % en 2,4 s o menos con SF 8; ventana de 1,01 a 5,93 s frente a 1,51 a 6,75 s por internet
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** 25 corridas por configuración y relevos con ± 100 m de desplazamiento; sin pruebas de falla

| Vacío | Tipo | Descripción |
|---|---|---|
| V-075-01 | TERR | Wellington (Nueva Zelanda) para el caso; Moratuwa (Sri Lanka) para medir la propagación |
| V-075-02 | POBL | Hogares de la comunidad con sensores; sin empresas ni industrias |
| V-075-03 | TEMP | Mensajes de 2,4 s o menos; escenarios hipotéticos sin evolución de réplicas |
| V-075-04 | MET | Simulación y ocho nodos de campo; sin eventos reales ni fallas |
| V-075-05 | VAR | Faltan costos, energía, seguridad, colisiones y desempeño frente a telefonía móvil |
| V-075-06 | TEOR | Comunicaciones LPWAN y alerta temprana; sin teoría de continuidad de operaciones |
| V-075-07 | CAUS | Efecto de la alerta de segundos sobre acciones y pérdidas sin evidencia |
