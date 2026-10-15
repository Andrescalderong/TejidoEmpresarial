# FB-L01-049 | D049 — “Saving Precious Seconds”—A Novel Approach to Implementing a Low-Cost Earthquake Early Warning System with Node-Level Detection and Alert Generation

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/informatics-09-00025-v3.pdf` · 32 páginas · Relevancia para el eje del corpus: **Adyacente** (Propone y prueba por simulación una arquitectura de alerta temprana sísmica de bajo costo con detección y generación de alertas en el nodo (acelerómetros MEMS en hogares, red definida por software SD-WAN con perforación de NAT y algoritmo PLUM modificado), frente a una arquitectura centralizada. Aporta la capa de IoT de borde de la cadena sensor-alerta-acción, con latencias medidas, pero en escenarios hipotéticos y sin evaluar efectos sobre empresas o recuperación.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-049 / D049
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Prasanna, R., Chandrakumar, C., Nandana, R., Holden, C., Punchihewa, A., Becker, J. S., Jeong, S., Liyanage, N., Ravishan, D., Sampath, R., & Tan, M. L. (2022). “Saving Precious Seconds”—A Novel Approach to Implementing a Low-Cost Earthquake Early Warning System with Node-Level Detection and Alert Generation. *Informatics*, *9*(1), Article 25. https://doi.org/10.3390/informatics9010025
- **Autores:** Prasanna, Raj (36519631800); Chandrakumar, Chanthujan (57193057522); Nandana, Rasika (57223327984); Holden, Caroline (36081665200); Punchihewa, Amal (16319943000); Becker, Julia S. (56576459900); Jeong, Seokho (57194606110); Liyanage, Nandika (57200207394); Ravishan, Danuka (57219622617); Sampath, Rangana (57197225245); Tan, Marion Lara (57193679072)
- **Afiliaciones:** Joint Centre for Disaster Research, Massey University, Wellington, 6021, New Zealand; School of Engineering and Computer Science, Victoria University of Wellington, Wellington, 6012, New Zealand; SeismoCity Ltd, Wellington, 6023, New Zealand; ADP Consultancy, Palmerston North, 4410, New Zealand; Department of Civil Engineering, Changwon National University, Changwon, 51140, South Korea; ALSO Germany, Straubing, 94315, Germany; Synopsys, Colombo, 00800, Sri Lanka; Datacom, Wellington, 6011, New Zealand
- **Fecha de publicación:** 2022
- **Fuente/contenedor:** Informatics · vol. 9(1)
- **Identificador persistente:** DOI 10.3390/informatics9010025 · ISSN 22279709
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85126687605&doi=10.3390%2finformatics9010025&partnerID=40&md5=888c82b742d8be140b777c3452420456
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 48

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Presentar una guía paso a paso para desarrollar una arquitectura de red de alerta temprana sísmica (EEW) de bajo costo, basada en acelerómetros MEMS alojados por el público, con procesamiento de datos descentralizado en el nodo y una red SD-WAN con tecnología de perforación de NAT, y evaluar sus latencias frente a una arquitectura centralizada. El estudio busca demostrar que el procesamiento en el nodo reduce el tiempo de generación de la alerta y alarga el tiempo de aviso para el usuario final, y que es viable un sistema comunitario con sensores baratos y seguridad adecuada.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si un algoritmo PLUM modificado puede ejecutarse en sensores MEMS de bajo costo, qué protocolo de comunicación (TCP, UDP, MQTT) minimiza la latencia de transmisión, cuánto tiempo se ahorra al detectar en el nodo frente a un servidor central y cómo mitigar los riesgos de seguridad de una red comunitaria.

**Marco teórico.** El marco combina tres elementos. Primero, la alerta temprana regional basada en el movimiento del suelo, con el algoritmo PLUM, que dispara una alerta cuando dos estaciones cercanas superan un umbral de intensidad dentro de un radio de 30 km. Segundo, una latencia del sistema definida como la suma del tiempo de detección, el tiempo de transmisión y el tiempo de viaje de la onda S entre la primera y la segunda estación. Tercero, una red definida por software (ZeroTier) que permite conectar nodos detrás de NAT con perforación UDP. El diseño toma la hipótesis de que la centralización genera cuellos de botella y puntos únicos de falla.

**Metodología.** La arquitectura utiliza sensores Raspberry Shake RS4D y un algoritmo PLUM modificado que se ejecuta en cada nodo, con comunicación entre sensores dentro de un radio de 30 km por TCP sobre ZeroTier. Se midió el retardo de transmisión con distintos protocolos (TCP, UDP, MQTT), el tiempo de detección en el nodo y el tiempo de viaje de la onda S en seis escenarios hipotéticos de sismos superficiales con ondas S de 3 km/s que llegan desde distintos acimuts a una red de cinco sensores instalados en Wellington. Se comparó con una arquitectura centralizada con un servidor virtual de Amazon Web Services (t2.micro, 1 GB de RAM), usando TCP y MQTT. Se informan resultados de sesenta simulaciones. Además se analizaron riesgos de seguridad de redes comunitarias y se implementaron medidas, y se probó la dependencia de la latencia con el número de sensores añadiendo sensores simulados a los cinco instalados en Wellington. Las latencias se obtuvieron como suma de los tiempos medidos de transmisión y de detección y del tiempo de viaje de la onda S calculado para cada geometría, de modo que la parte de la onda S es analítica y no medida.

**Resultados principales.** El tiempo de viaje de la onda S entre el primer y el segundo sensor varió entre 1,0 y 2,7 s según el escenario y la densidad de sensores en la dirección de la onda. La latencia total del sistema con procesamiento en el nodo varió entre 1,24 s y 2,88 s. En los seis escenarios, la latencia con arquitectura centralizada y MQTT fue de 3,24 a 4,57 s, con arquitectura centralizada y TCP de 1,48 a 3,13 s, y con la arquitectura descentralizada de 1,24 a 2,88 s (por ejemplo, escenario 1: 4,15; 2,94 y 2,65 s). La ventaja de la arquitectura descentralizada sobre la centralizada con TCP fue de 0,24 a 0,32 s, y sobre la centralizada con MQTT de unos 2 s. UDP superó a TCP en unos 35 ms. La pérdida de paquetes fue significativa con MQTT. Los autores concluyen que el tiempo de detección de la arquitectura descentralizada no varía con el número de sensores, mientras que en la centralizada aumenta, y que la pérdida de paquetes es despreciable en la descentralizada frente a la centralizada. También informan que la densidad de sensores en la dirección de propagación reduce el tiempo de viaje de la onda S entre las dos estaciones que confirman la alerta, y por tanto la latencia total.

**Discusión y contribución.** Los autores concluyen que la arquitectura descentralizada con TCP sobre SD-WAN genera las condiciones de alerta óptimas, ahorra segundos y es más robusta ante fallas porque la redundancia depende de la densidad de sensores en un radio de 30 km y no de un servidor único. Argumentan que el costo de los sistemas descentralizados disminuye con sensores cada vez más baratos y potentes, que el diseño se escala con facilidad y que puede extenderse a otros dominios, como alertas comunitarias de incendios forestales. Señalan que la seguridad de redes comunitarias casi no se trata en la literatura y proponen medidas de mitigación, y presentan el trabajo como guía de referencia para futuras redes.

**Limitaciones declaradas.** Declaradas: se trata de hallazgos de investigación en curso; las evaluaciones se hicieron con escenarios hipotéticos y la red experimental es pequeña. No declaradas: la comparación se hace con un servidor centralizado de baja capacidad (t2.micro), cuya especificación los autores admiten que no se describe en la literatura; la ventaja frente a la centralizada con TCP es de 0,24 a 0,32 s, y la mayor parte de la diferencia con la centralizada con MQTT proviene del protocolo; no se midió la precisión de detección, las falsas alarmas ni la tasa de pérdida de alertas con sismos reales; no hay evaluación del tiempo de entrega al usuario ni del efecto de la alerta; el costo del sistema no se cuantifica; la seguridad se describe sin pruebas de penetración ni auditoría independiente.

**Trabajo futuro.** Explícito: aplicar el concepto a otras amenazas con alertas comunitarias (incendios forestales) y usar la guía como referencia para redes futuras. Implícito: pruebas con sismos reales, redes más grandes, seguridad verificada y evaluación de falsas alarmas.

**Palabras clave.** Declaradas: Citizen science; Decentralised architecture; Earthquake early warning; MEMS; PLUM algorithm; Software-defined network | Inferidas: alerta temprana sísmica, sensores MEMS, procesamiento en el nodo, SD-WAN, ZeroTier, PLUM, latencia, TCP, MQTT, ciencia ciudadana, Nueva Zelanda

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** La detección y la generación de alertas en el nodo, con un algoritmo PLUM modificado en sensores MEMS de bajo costo comunicados por TCP sobre una SD-WAN con perforación de NAT, reducen la latencia del sistema frente a arquitecturas centralizadas (1,24 a 2,88 s frente a 3,24 a 4,57 s con MQTT), no dependen del número de sensores, resisten fallas de componentes y permiten sistemas comunitarios asequibles y escalables, con lo que aumentan el tiempo de aviso al usuario.

**Antítesis identificada.** El resultado se apoya en una comparación favorable al diseño propuesto. La ventaja principal proviene del protocolo (TCP frente a MQTT, unos 2 s), mientras que frente a una arquitectura centralizada que también usa TCP la mejora es de 0,24 a 0,32 s, del orden de 10 % a 20 %. El servidor centralizado es una máquina virtual de 1 GB de memoria, y las pruebas se limitan a cinco sensores reales y simulación de más, en escenarios hipotéticos. No se mide la calidad de las alertas (detección, falsas alarmas), el tiempo hasta que la alerta llega a las personas ni el valor de segundos ganados para decisiones. La afirmación de robustez ante fallas se argumenta, no se prueba. Faltan costos y pruebas de seguridad.

**Síntesis propuesta.** La contribución sostenible es una arquitectura documentada y una medición de latencias por componente que muestra que el procesamiento en el nodo es viable en hardware de bajo costo y que la elección del protocolo tiene un efecto mayor que la ubicación del procesamiento en el rango probado. El carácter de guía abierta y la atención a la seguridad de redes comunitarias son aportes prácticos. Su valor para el corpus es como eslabón de borde de IoT en la cadena sensor-alerta-acción de un sistema de continuidad, pendiente de evaluación con sismos reales, con costos medidos y de uso por empresas.

**Áreas grises detectadas.**

1. Magnitud de la ventaja: el resumen habla de superioridad de la arquitectura descentralizada, pero la Tabla 2 muestra que, con el mismo protocolo TCP, la diferencia es de 0,24 a 0,32 s; la mejora de aproximadamente 2 s se obtiene contra la arquitectura con MQTT, de modo que gran parte del efecto atribuido a la descentralización corresponde al protocolo.
2. Representatividad de la línea base: el servidor centralizado es una instancia virtual t2.micro de 1 GB, elegida porque la literatura no describe las especificaciones de servidores reales, y su capacidad puede ser inferior a la de sistemas operativos; con un servidor más potente la brecha de 0,24 a 0,32 s podría reducirse.
3. Evidencia con sismos: los seis escenarios son hipotéticos, con ondas S de velocidad constante de 3 km/s y sismos superficiales; no hay eventos reales, ni mediciones de falsas alarmas, ni detección, ni tiempo de alerta efectivo para personas, que es la variable que importa al usuario.
4. Costo y seguridad: se afirma menor costo que los sismógrafos científicos y mitigación de riesgos de seguridad, pero no hay cifras de costo por nodo ni de operación, ni pruebas de seguridad que verifiquen las medidas en un entorno hostil.

**Puntos oscuros aclarados.** Llama la atención que el artículo declare que la arquitectura descentralizada supera a la centralizada y que ahorra segundos valiosos, cuando la mejora frente a la arquitectura centralizada con el mismo protocolo es de entre 0,24 y 0,32 s y el grueso de la diferencia proviene del cambio de MQTT a TCP. También es notable que los autores reconozcan que no existe información sobre los servidores centralizados reales y que aun así comparen contra un servidor mínimo. El trabajo se describe como investigación en curso, pero se presenta como una guía integral y como referencia para otras amenazas. Además, la simulación usa cinco sensores reales y escenarios hipotéticos, y se extrapola a redes nacionales de cientos de sensores. Por último, el texto no informa el costo por nodo ni la tasa de falsas alarmas, dos variables que determinan la adopción por hogares y empresas, y no discute la dependencia del esquema de dos estaciones de confirmación, que añade por diseño entre 1,0 y 2,7 s a la latencia.

**Ideas propositivas novedosas.**

1. Medición del tiempo de aviso efectivo para empresas: combinar la latencia de 1,24 a 2,88 s con el tiempo de entrega al actuador (corte de gas, parada de línea) y el tiempo de viaje de la onda S hasta la planta, y calcular para cada escenario cuántos segundos de aviso efectivo ganaría una empresa a distintas distancias del epicentro. El resultado sería una curva de segundos útiles por ubicación, que permitiría decidir qué acciones automáticas caben y valorar la inversión de una pyme frente al costo de nodos de bajo costo, incluyendo el costo de una falsa alarma que detenga la producción sin necesidad.
2. Banco de pruebas con sismos reales y falsas alarmas: reproducir con registros de redes de sensores de bajo costo en Nueva Zelanda o California los eventos reales y medir tasas de detección, falsas alarmas y pérdida de alertas con la arquitectura descentralizada, contra una línea base centralizada de capacidad realista. Un resultado con intervalos de confianza permitiría estimar si el ahorro de 0,2 a 0,3 s justifica la complejidad de la descentralización y para qué densidad de sensores, además de reportar el consumo de energía y de ancho de banda por nodo en operación continua durante al menos tres meses.

**Relaciones poco exploradas.**

1. Procesamiento en el nodo (implementa) las líneas futuras de D045: la revisión D045 identificó el procesamiento descentralizado, el soporte multisensor y los algoritmos basados en el movimiento del suelo como áreas prioritarias, y D049 es una implementación con PLUM en el nodo; comparten autores del mismo grupo.
2. Computación en el borde para sensado (comparte enfoque con) D039: D039 corrige la sincronización de sensores de monitoreo con un modelo de 108 mil parámetros apto para el borde, y D049 ejecuta la detección en el nodo; ambos buscan reducir la dependencia de la conectividad central.

**Robustez argumentativa:** 2.7/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 3/10; generalizabilidad 3/10.

**Valor estratégico:** 6/10 — Aporta una arquitectura abierta y medida para alerta temprana de bajo costo con detección en el nodo, con latencias por componente, comparación entre protocolos y atención a la seguridad de redes comunitarias. Su valor para el corpus es adyacente-alto como capa de IoT de borde, y se reduce por la evaluación en escenarios hipotéticos, la línea base centralizada débil, la ventaja moderada frente a TCP centralizado, y la falta de costos, de falsas alarmas y de efecto sobre empresas.

**Conexiones inter-documentales.**

- **CONFIRMA** D073 (Alerta temprana sísmica con IoT, cómputo en la nube y localización con): ambos muestran que detectar y generar la alerta en el nodo reduce la latencia frente a arquitecturas centralizadas (D049 1,24 a 2,88 s; D073 localización más temprana en sismo de magnitud 5,4), con evidencia de simulación o datos históricos [juicio del analista]
- **CONFIRMA** D075 (Alerta temprana sísmica descentralizada con LoRa multisalto, resilienc): relación inversa de D075 CONFIRMA D049: comparten autoría (Prasanna, Holden): la arquitectura descentralizada reduce la latencia; la concordancia procede del mismo grupo [juicio del analista; autoría compartida]
- **COMPLEMENTA** D063 (Alerta temprana sísmica y respuesta de emergencia en ferrocarriles de ): relación inversa de D063 COMPLEMENTA D049: ambos aplican el principio PLUM: D063 a ferrocarriles de alta velocidad con arquitectura jerárquica y D049 de forma modificada en sensores MEMS de baj [juicio del analista]
- **PRECEDE** D045 (Alerta temprana sísmica de bajo costo con sensores MEMS (revisión)): es citado por D045 (verificado por coincidencia de título) [citación verificada]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 54 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Comparación con línea base débil (La arquitectura descentralizada se compara con un servidor centralizado de 1 GB de RAM y con MQTT, protocolo que añade unos 2 s (Sec. 4.5, p. 19-20; Sec. 5, p. 23)); Generalización apresurada (Se infiere comportamiento de redes nacionales de cientos de sensores a partir de cinco sensores reales y escenarios hipotéticos (Sec. 4.5, p. 20-21)); Afirmación sin evidencia (Se afirma menor costo y mayor robustez sin cifras de costo ni pruebas de falla (Sec. 5, p. 23-24))
- **Bradford-Hill:** No aplica: es un estudio de ingeniería con simulación; la relación entre procesar en el nodo y menor latencia es mecánica y plausible, pero no se estima ningún efecto causal sobre daños o decisiones.
- **TRL asignado:** 4 — 'With several hypothetical earthquake scenarios, experiments were conducted to evaluate the system latencies of the proposed decentralised EEW architecture' (p. 1)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (32 páginas). La Tabla 2 se leyó de líneas entrelazadas de la extracción; los valores por escenario se verificaron con el texto narrativo (rangos 1,48 a 3,13 y 3,24 a 4,57 s). La ventaja de 0,24 a 0,32 s sobre la centralizada con TCP es cálculo del analista.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| La detección y la generación de alertas en el nodo, con un algoritmo PLUM modificado en sensores MEMS de bajo costo comunicados por TCP sobre una SD-WAN con perforación de NAT, reducen la latencia del sistema frente a arquitecturas centralizadas (1,24 a 2,88 s frente a 3,24 a 4,57 s con MQTT), no dependen del número de sensores, resisten fallas de componentes y permiten sistemas comunitarios asequibles y escalables, con lo que aumentan el tiempo de aviso al usuario.  | El resultado se apoya en una comparación favorable al diseño propuesto. La ventaja principal proviene del protocolo (TCP frente a MQTT, unos 2 s), mientras que frente a una arquitectura centralizada que también usa TCP la mejora es de 0,24 a 0,32 s, del orden de 10 % a 20 %. El servidor centralizado es una máquina virtual de 1 GB de memoria, y las pruebas se limitan a cinco sensores reales y simulación de más, en escenarios hipotéticos. No se mide la calidad de las alertas (detección, falsas alarmas), el tiempo hasta que la alerta llega a las personas ni el valor de segundos ganados para decisiones. La afirmación de robustez ante fallas se argumenta, no se prueba. Faltan costos y pruebas de seguridad.  | La contribución sostenible es una arquitectura documentada y una medición de latencias por componente que muestra que el procesamiento en el nodo es viable en hardware de bajo costo y que la elección del protocolo tiene un efecto mayor que la ubicación del procesamiento en el rango probado. El carácter de guía abierta y la atención a la seguridad de redes comunitarias son aportes prácticos. Su valor para el corpus es como eslabón de borde de IoT en la cadena sensor-alerta-acción de un sistema de continuidad, pendiente de evaluación con sismos reales, con costos medidos y de uso por empresas.  | 2.7/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Latencia del sistema' es la suma del tiempo de detección, de transmisión y de viaje de la onda S entre dos estaciones; 'detección en el nodo' es ejecutar el algoritmo en el sensor; 'SD-WAN' es una red definida por software que conecta nodos detrás de NAT.
- **P2 Supuestos:** Supone que los escenarios hipotéticos con onda S constante representan sismos reales, que el servidor t2.micro representa un servidor centralizado típico y que la reducción de latencia se traduce en mayor tiempo de aviso útil.
- **P3 Evidencia:** La evidencia es una tabla de seis escenarios con latencias de tres arquitecturas, mediciones de protocolos y sesenta simulaciones en una red de cinco sensores reales.
- **P4 Consecuencias:** Si es cierto, comunidades y empresas pueden desplegar redes de alerta asequibles con ganancia de segundos; si es falso, pueden esperar una ventaja pequeña frente a una arquitectura centralizada bien configurada.
- **P5 Contraejemplos:** No se examinan sismos reales, falsas alarmas, detección, costos por nodo, pruebas de seguridad ni el tiempo de entrega al usuario.
- **P6 Alternativas:** Alternativas: que un servidor central mejor dimensionado iguale el desempeño; que el protocolo sea el factor dominante; que la densidad de sensores determine la latencia más que la arquitectura.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Latencia del sistema descentralizado (rango) | 1,24 a 2,88 | s | Seis escenarios hipotéticos con PLUM en el nodo | Sec. 4.5, p. 18 | Tabla | Alta | Red de cinco sensores |
| Latencia centralizada con MQTT (rango) | 3,24 a 4,57 | s | Servidor AWS t2.micro de 1 GB | Tabla 2, p. 19 | Tabla | Alta | Línea base tradicional |
| Latencia centralizada con TCP (rango) | 1,48 a 3,13 | s | Mismo servidor | Tabla 2, p. 19 | Tabla | Alta | Línea base con el mismo protocolo |
| Ventaja de la descentralizada sobre la centralizada con TCP | 0,24 a 0,32 | s | Cálculo del analista a partir de la Tabla 2 | Tabla 2, p. 19 | Tabla | Alta | Del 8 % al 19,5 % |
| Ventaja de la descentralizada sobre la centralizada con MQTT | ≈ 2 | s | Según la discusión | Sec. 5, p. 23 | Texto | Alta | Parte atribuible al protocolo |
| Tiempo de viaje de la onda S entre primer y segundo sensor | 1,0 a 2,7 | s | Seis escenarios | Sec. 4.5, p. 18 | Texto | Alta | Depende de la densidad de sensores |
| Ventaja de UDP sobre TCP | ≈ 35 | ms | Se prefiere TCP por confiabilidad | Sec. 5, p. 23 | Texto | Alta | Para aplicaciones críticas |
| Radio de comunicación entre sensores | 30 | km | Esquema PLUM | Sec. 4.3, p. 14 | Texto | Alta | Redundancia por densidad local |
| Simulaciones realizadas | 60 | simulaciones | Seis escenarios | Resumen, p. 1 | Texto | Media | Detalle de repeticiones no descrito en el texto leído |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'With several hypothetical earthquake scenarios, experiments were conducted to evaluate the system latencies of the proposed decentralised EEW architecture' (p. 1) | Validación en laboratorio con red de cinco sensores y escenarios hipotéticos; sin eventos reales ni despliegue operativo. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'the cost of the decentralised EEW architectures is becoming more affordable because MEMS-based sensors are getting cheaper' (p. 23) | Se argumenta que el costo baja, sin cifras ni modelo de negocio. |
| IRL | 4 | Sí | 'ZeroTier’s UDP hole-punching mechanism allows for connecting devices to communicate with the use of any type of data packet' (p. 10) | Integración de sensores, SD-WAN, protocolo TCP y algoritmo en el nodo probada en un banco experimental con cinco sensores. |
| DRL | 3 | Sí | 'Unavailability of the central processing capability due to the loss of connectivity may hinder the issuing of time-critical warnings to end-users' (p. 7) | Necesidad argumentada con literatura; sin demanda de usuarios medida. |
| SRL | 1.78 | Sí | Componentes: Sensores MEMS con PLUM en el nodo (TRL 4), Red SD-WAN con TCP (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 16.0; ÷9 → 1.78; nivel acotado a [1,9] = 1.78 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 2 e IRL 4: banco experimental con escenarios hipotéticos, sin sismos reales ni costos, con ventaja moderada frente a un TCP centralizado. · Estrategia de salida: Piloto con eventos reales, tasas de falsas alarmas, costos por nodo y pruebas de seguridad.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Comparación con línea base débil | La arquitectura descentralizada se compara con un servidor centralizado de 1 GB de RAM y con MQTT, protocolo que añade unos 2 s (Sec. 4.5, p. 19-20; Sec. 5, p. 23) | La ventaja frente a TCP centralizado es de 0,24 a 0,32 s |
| Generalización apresurada | Se infiere comportamiento de redes nacionales de cientos de sensores a partir de cinco sensores reales y escenarios hipotéticos (Sec. 4.5, p. 20-21) | Extrapolación sin datos de gran escala |
| Afirmación sin evidencia | Se afirma menor costo y mayor robustez sin cifras de costo ni pruebas de falla (Sec. 5, p. 23-24) | Argumento de diseño |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Procesar la detección en el nodo → menor latencia del sistema | Medición de latencias por componente | Mecanismo directo, consistencia entre escenarios | Sismos reales, línea base de servidor realista | Protocolo, capacidad del servidor, densidad de sensores | 3 | Efecto plausible pero de magnitud moderada frente a TCP centralizado |
| Menor latencia → más tiempo de aviso útil → menos daños | Argumento del resumen | Plausibilidad | Medición de tiempo de entrega y de pérdidas evitadas | Distancia al epicentro, reacción del usuario | 1 | No evaluado |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Evaluación con sismos reales, falsas alarmas y línea base centralizada realista | Crítico | Media | 8 |
| Conocimiento | Valor económico del aviso para empresas y tiempo de entrega al usuario | Crítico | Media | 8 |
| Tecnológico | Seguridad probada de la red comunitaria y escalabilidad a cientos de nodos | Significativo | Media | 7 |
| Mercado | Costo por nodo, operación y modelo de participación comunitaria | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Tabla 1 | Latencias promedio de los seis escenarios con la arquitectura descentralizada | Tabla | Detección, transmisión, onda S y total | 1,24 a 2,88 s | Alta |
| Tabla 2 | Latencias en seis escenarios con tres arquitecturas | Tabla | MQTT central, TCP central y TCP descentralizada | 1,24 a 4,57 s | Alta |
| Fig. 7 | Arquitectura centralizada de comparación | Diagrama | Servidor AWS y sensores | No aplica | Media |
| Fig. 8 | Pseudocódigo de procesamiento descentralizado y centralizado | Pseudocódigo | Bloques adicionales de identificación de región | No aplica | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Sistemas con MQTT y procesamiento centralizado en la nube (referencias 9 y 41) | No especificado en documento | Academia | Alerta con servidor central | Práctica común | Mayor latencia y punto único de falla | Estable |
| Redes de sensores de bajo costo de Taiwán, California y China | Taiwán; Estados Unidos; China | Academia | Alerta con MEMS | Experiencia operativa | Procesamiento centralizado | Creciendo |

### B.9 Variables econométricas y vacíos

- **Y:** Latencia del sistema de alerta (s)
- **X:** Arquitectura (descentralizada o centralizada) y protocolo (TCP, UDP, MQTT)
- **Z (controles):** Escenario sísmico hipotético, densidad de sensores
- **Datos:** Seis escenarios hipotéticos, red de cinco sensores en Wellington, sesenta simulaciones
- **Método:** Medición de latencias por componente y comparación entre arquitecturas
- **Efecto reportado:** Latencia de 1,24 a 2,88 s frente a 1,48 a 3,13 s (TCP central) y 3,24 a 4,57 s (MQTT central)
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Variación de escenarios y número de sensores; sin sismos reales ni línea base alternativa

| Vacío | Tipo | Descripción |
|---|---|---|
| V-049-01 | TERR | Wellington (Nueva Zelanda); sin otras regiones |
| V-049-02 | POBL | Hogares anfitriones de sensores; sin empresas ni usuarios finales evaluados |
| V-049-03 | TEMP | Latencia en segundos; sin operación prolongada |
| V-049-04 | MET | Escenarios hipotéticos, línea base mínima, sin sismos reales ni falsas alarmas |
| V-049-05 | VAR | Faltan costos, tasa de detección, falsas alarmas y tiempo de entrega al usuario |
| V-049-06 | TEOR | Sin teoría de respuesta a la alerta ni de valor de los segundos de aviso |
| V-049-07 | CAUS | Sin evidencia causal de efecto sobre daños o decisiones |
