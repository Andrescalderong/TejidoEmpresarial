# FB-L01-064 | D064 — Design and evaluation of 5G-based architecture supporting data-driven digital twins updating and matching in seismic monitoring

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/s10518-022-01329-8.pdf` · 21 páginas · Relevancia para el eje del corpus: **Núcleo** (Diseña y evalúa una arquitectura con red 5G (comunicaciones de baja latencia y alta confiabilidad) y cómputo en el borde (MEC) para sostener la actualización y el emparejamiento de gemelos digitales basados en datos en el monitoreo sísmico de edificios, con una placa de sensores MEMS de bajo costo, un modelo de elementos finitos de un edificio de concreto en L'Aquila y retardos medidos de red. Reúne gemelo digital, IoT, sismo y reconstrucción posterremoto en un caso real, aunque la validación es con datos simulados.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-064 / D064
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, número especial de monitoreo sísmico)
- **Referencia APA 7:** Gattulli, V., Franchi, F., Graziosi, F., Marotta, A., Rinaldi, C., Potenza, F., & Sabatino, U. D. (2022). Design and evaluation of 5G-based architecture supporting data-driven digital twins updating and matching in seismic monitoring. *Bulletin of Earthquake Engineering*, *20*(9), 4345-4365. https://doi.org/10.1007/s10518-022-01329-8
- **Autores:** Gattulli, Vincenzo (6603769681); Franchi, Fabio (57193013263); Graziosi, Fabio (7004365263); Marotta, Andrea (57191035019); Rinaldi, Claudia (56649934400); Potenza, Francesco (23397637500); Sabatino, Umberto Di (56707463100)
- **Afiliaciones:** Department of Structural and Geotechnical Engineering, Sapienza University of Rome, Via Eudossiana 18, Rome, 00184, Italy; Department of Information Engineering, Computer Science and Mathematics, Università degli Studi dell’Aquila, Via Vetoio, L’Aquila, 67100, Italy; Department of Engineering and Geology, University G. D’Annunzio of Chieti-Pescara, Viale Pindaro 42, Pescara, 65127, Italy; Department of Civil, Construction-Architectural and Environmental Engineering, Università degli Studi dell’Aquila, Piazzale E. Pontieri 2, L’Aquila, 67100, Italy
- **Fecha de publicación:** 2022
- **Fuente/contenedor:** Bulletin of Earthquake Engineering · vol. 20(9)
- **Identificador persistente:** DOI 10.1007/s10518-022-01329-8 · ISSN 1570761X
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85124739302&doi=10.1007%2fs10518-022-01329-8&partnerID=40&md5=909d57f07f06e3a2626fe832c1a122f7
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 30

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Presentar una solución que aproveche modelos de gemelo digital (DT) para el monitoreo de salud estructural (SHM) y para mejorar las soluciones de alerta temprana sísmica (EEW), con una arquitectura de comunicación 5G de baja latencia y alta confiabilidad y cómputo en el borde (MEC), de modo que el procesamiento y la actualización en tiempo real de los modelos con datos de redes de sensores sean posibles. El estudio se ubica en la experimentación 5G de la ciudad de L'Aquila y usa una placa de sensores muy adaptable y acelerómetros MEMS, y busca verificar el comportamiento del servicio con datos de un edificio en condición sana y dañada.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si una red 5G con cómputo en el borde cumple la latencia necesaria para actualizar un gemelo y emitir alertas, si acelerómetros MEMS de bajo costo y sin calibrar pueden servir para SHM y EEW, y si un modelo basado en datos puede detectar daño a partir de series de tiempo y actualizarse de forma continua.

**Marco teórico.** El marco articula el Internet de Todo (IoE) y las aplicaciones de ciudades inteligentes con el concepto de gemelo digital que se alimenta de información procesada de SHM de largo plazo. La arquitectura se organiza en una placa de sensores (SHM-Board v2) con microcontrolador de ultra bajo consumo, acelerómetro MEMS siempre activo con umbral configurable y convertidor analógico-digital de 24 bits a 100 Hz, con procesamiento a bordo, una puerta de enlace del edificio, un nodo de cómputo en el borde (MEC) y una nube remota. Se usan los servicios 5G de comunicaciones masivas de máquina y de baja latencia y alta confiabilidad. El contexto es una ciudad en reconstrucción tras el sismo de 2009.

**Metodología.** La placa SHM-Board v2 se diseñó a partir de la experiencia con placas IMOTE usadas durante cinco años en el monitoreo de la Basílica de Collemaggio, y se identificaron y probaron dos acelerómetros adecuados, con un procedimiento de calibración definido para comparar con la respuesta estructural. Se construyó un modelo de elementos finitos en Midas Gen de un edificio de concreto armado (Coppito 1) con condiciones de borde fijas en la base, y se generaron series de tiempo de condición sana y dañada con ruido blanco limitado en banda en Simulink; el daño se modeló como una reducción de aproximadamente 10 % del módulo elástico. Una aplicación prototipo en MATLAB conectada por socket UDP a la puerta de enlace implementó un enfoque de aprendizaje automático para refinar el modelo. Se midió el retardo de la red a nivel de aplicación con mensajes publicados cada 10 ms hacia el borde y la nube remota.

**Resultados principales.** El daño simulado, de aproximadamente 10 % de reducción del módulo elástico, se refleja con claridad en las densidades espectrales de potencia como reducción de las frecuencias modales, en especial en los modos de traslación. El retardo medio de la red a nivel de aplicación sigue una distribución normal con media de 2,1 ms y desviación estándar de 0,9 ms. El mismo procesamiento desplegado en nodos de borde procesa los datos casi en tiempo real con baja latencia y, si detecta una estructura dañada, envía una alarma al edificio. Los datos de sensores se enviaron al borde y a la nube remota y se compararon los retardos. La aplicación actualiza el modelo basado en datos con series de tiempo del edificio en condición elástica. Los autores indican que la identificación modal con vibraciones ambientales está en desarrollo, y que los resultados se obtuvieron con series generadas por el modelo y no con datos medidos. El modelo de elementos finitos usa 8 secciones distintas de vigas y 3 de placas, con base empotrada, y las tablas de frecuencias modales comparan la configuración sana con la dañada. La aplicación MATLAB se conecta con la puerta de enlace del edificio por UDP y la misma aplicación en nodos de borde procesa las series con baja latencia, y se evaluaron también los retardos hacia la nube remota.

**Discusión y contribución.** Los autores sostienen que el sistema, con sensores de bajo costo, red 5G de baja latencia y cómputo en el borde, permite aplicar algoritmos basados en datos para el aprovechamiento de la información y para la alerta temprana, y que dichos algoritmos pueden mejorar periódicamente los modelos a medida que llegan datos y la estructura evoluciona o se degrada. Destacan el potencial de la ciudad de L'Aquila como laboratorio urbano dado que su reconstrucción tras 2009 sigue en curso. Reconocen que la validación con datos experimentales en tiempo real queda como trabajo futuro y que la detección de daño real exige identificar frecuencias y formas modales depuradas de efectos ambientales.

**Limitaciones declaradas.** Declaradas: los resultados provienen de series generadas por un modelo numérico y no de datos medidos en tiempo real; la detección de daño real requiere depurar los efectos ambientales (temperatura, humedad); el daño se simplificó como una reducción del módulo elástico. No declaradas: un solo edificio y un solo caso de daño de 10 %; sin análisis de falsos positivos de daño ni de la sensibilidad al nivel de ruido; retardos medidos en un banco 5G de experimentación sin carga de red real; sin comparación con alternativas de comunicación (LoRa, Wi-Fi) ni de cómputo; sin costos de operación ni de despliegue; la actualización del gemelo se prueba con datos del propio modelo, lo que no demuestra desempeño con datos medidos.

**Trabajo futuro.** Explícito: explotar datos experimentales en tiempo real para validar el servicio, y completar la identificación modal operacional para identificar frecuencias con vibraciones ambientales. Implícito: pruebas con edificios reales y comparación de arquitecturas de comunicación.

**Palabras clave.** Declaradas: 5G network; Earthquake early warning (EEW); Massive machine-type communications (mMTC); MEMS accelerometers; Multiaccess edge computing (MEC); Structural health monitoring (SHM); Ultra-reliable and low latency communications (uRLCC) | Inferidas: gemelo digital, monitoreo de salud estructural, alerta temprana sísmica, 5G, cómputo en el borde, acelerómetros MEMS, L'Aquila, baja latencia, actualización de modelos, comunicaciones masivas de máquina

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Una arquitectura con placas de sensores MEMS de bajo costo, red 5G de baja latencia y cómputo en el borde permite actualizar gemelos digitales de edificios y emitir alertas en casi tiempo real, con un retardo medio de aplicación de 2,1 ms (desviación de 0,9 ms), y detectar un daño del orden del 10 % en el módulo elástico por el cambio en las frecuencias modales, lo que ofrece una base para SHM y EEW en ciudades en reconstrucción como L'Aquila.

**Antítesis identificada.** La demostración de detección de daño y de actualización del gemelo usa series sintéticas generadas con un modelo de elementos finitos, de modo que no prueba la capacidad con datos medidos, con ruido ambiental, variaciones de temperatura y sensores reales. El retardo de 2,1 ms se mide en un banco de experimentación sin tráfico real y con mensajes de 10 ms, sin comparación con otras redes. El daño se modela como reducción uniforme del módulo, un caso favorable para la detección. No hay falsas alarmas, sensibilidad al ruido, costos ni uso del gemelo para decisiones. La actualización del modelo con datos de su propio modelo no evalúa la deriva real de una estructura.

**Síntesis propuesta.** La contribución sostenible es una arquitectura de referencia y una caracterización de latencia que muestran que los requisitos de tiempo para SHM y EEW pueden cumplirse con 5G y cómputo en el borde, con una placa de bajo costo derivada de experiencia en la reconstrucción de L'Aquila. La detección de daño y el gemelo se presentan como prueba de concepto con datos simulados, y su valor depende de que se repita el experimento con registros reales de un edificio. Para el corpus, es una pieza clave del eslabón gemelo-IoT-sismo, pendiente de validación con datos reales y de extensión a empresas y a la recuperación.

**Áreas grises detectadas.**

1. Datos de validación: los resultados de daño y de actualización del gemelo se obtienen de series generadas por el modelo de elementos finitos (con daño de 10 % del módulo elástico) y no de mediciones del edificio; los autores plantean la validación con datos experimentales como trabajo futuro.
2. Condiciones de la red: el retardo medio de 2,1 ms (desviación de 0,9 ms) se midió en un escenario de experimentación 5G con mensajes cada 10 ms, sin tráfico competidor ni pérdida de paquetes, de modo que no representa la red tras un sismo, cuando la carga y las fallas pueden ser altas.
3. Representatividad del daño: el daño se simula como una reducción uniforme de rigidez; los daños reales son localizados y no lineales, y depuran peor con efectos ambientales; la sensibilidad al nivel de daño, al ruido y a la temperatura no se evalúa.
4. Utilidad para la decisión: el sistema emite una alarma al edificio dañado en el escenario simulado, pero no se evalúa cuánto reduce el tiempo de inspección ni de reocupación, ni su costo, que son los criterios que importan a propietarios y empresas.

**Puntos oscuros aclarados.** Llama la atención que un artículo cuyo título habla de diseño y evaluación de una arquitectura que soporta la actualización y el emparejamiento de gemelos digitales basados en datos valide la actualización con datos sintéticos del propio modelo que debe ser emparejado. También es notable que el retardo de 2,1 ms se mida en un banco sin carga y se presente como evidencia de cumplimiento de requisitos de alerta. El daño de 10 % del módulo elástico se describe como simplificación para controlar el sistema informático, lo cual significa que el estudio prueba más el sistema de tecnologías de la información que el diagnóstico estructural. Además, la ciudad de L'Aquila se invoca como contexto de reconstrucción, pero no se usan datos del sismo de 2009 ni de edificios dañados. Finalmente, no se discute el costo del despliegue 5G, que condiciona su uso por pequeñas empresas, ni la disponibilidad de la red tras un sismo, cuando la propia infraestructura de telecomunicaciones puede resultar dañada.

**Ideas propositivas novedosas.**

1. Piloto con datos reales y comparación de redes: instrumentar un edificio de L'Aquila con la placa SHM-Board v2, registrar vibraciones ambientales durante tres meses y comparar la identificación modal en el borde 5G con la de un enlace LoRa o Wi-Fi, midiendo retardo, pérdida de paquetes, costo y consumo. El resultado permitiría saber si la ventaja de la baja latencia de 5G se justifica para SHM o solo para EEW, y cuál es el costo de comunicaciones por edificio, dato clave para evaluar adopción por pymes, y se complementaría con una prueba de corte de energía de la estación base y de saturación de la red durante un simulacro.
2. Del diagnóstico al tiempo de reocupación: conectar el gemelo de L'Aquila con un modelo de tiempo de recuperación funcional como el de D053, de modo que la alerta de daño produzca una estimación probabilística de tiempo hasta la reocupación y apertura de las empresas del edificio. Se podría validar con un simulacro de sismo en un edificio piloto, midiendo el tiempo entre la alerta y la decisión de inspección, y comparando con el procedimiento manual vigente de evaluación de seguridad, con registro del costo de cada inspección y del número de ocupantes y empresas afectados.

**Relaciones poco exploradas.**

1. Gemelo de edificio con sensores (complementa) D014 y D035: D014 construye un gemelo de la Basílica María Auxiliadora de Lima con SHM y D035 un gemelo de puente con actualización genética del modelo; D064 aporta la arquitectura de comunicación y cómputo en el borde para sostener esa actualización.
2. Cómputo en el borde con alerta sísmica (se relaciona con) D049 y D060: D049 procesa la detección en el nodo y D060 clasifica la intensidad en el borde; D064 usa el borde 5G para detectar daño y emitir alarmas.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 7/10 — Aporta una arquitectura concreta y medida que une gemelo digital, sensores MEMS de bajo costo, 5G y cómputo en el borde para SHM y alerta sísmica en una ciudad en reconstrucción, con retardos medidos de 2,1 ms. Su valor para el corpus es alto por coincidencia temática (gemelo, IoT, sismo, reconstrucción); se reduce por la validación con datos sintéticos de un modelo, la red de experimentación sin carga, un solo edificio y caso de daño y la ausencia de costos y de vínculo con la recuperación empresarial.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Validación circular (El gemelo se actualiza y se evalúa con series generadas por el mismo modelo que lo sustenta (Sec. 5.2-5.3, p. 16-17)); Condiciones favorables presentadas como evidencia general (El retardo de 2,1 ms se mide en un banco 5G sin carga y se usa como evidencia de cumplir requisitos de alerta (Sec. 5.3, p. 17)); Simplificación del fenómeno (El daño se reduce a una disminución uniforme del 10 % del módulo elástico (Sec. 5.2, p. 17))
- **Bradford-Hill:** No aplica: es un diseño con simulación; no se estima causalidad con datos observados.
- **TRL asignado:** 4 — 'Future works are devoted toward the exploitation of real-time experimental data for service validation' (p. 18)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (21 páginas). Las tablas 3 y 4 con valores de frecuencias modales se leyeron con orden de columnas desordenado y no se interpretan. Las páginas siguen los marcadores del PDF (la numeración de la revista inicia en 4345).

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Una arquitectura con placas de sensores MEMS de bajo costo, red 5G de baja latencia y cómputo en el borde permite actualizar gemelos digitales de edificios y emitir alertas en casi tiempo real, con un retardo medio de aplicación de 2,1 ms (desviación de 0,9 ms), y detectar un daño del orden del 10 % en el módulo elástico por el cambio en las frecuencias modales, lo que ofrece una base para SHM y EEW en ciudades en reconstrucción como L'Aquila.  | La demostración de detección de daño y de actualización del gemelo usa series sintéticas generadas con un modelo de elementos finitos, de modo que no prueba la capacidad con datos medidos, con ruido ambiental, variaciones de temperatura y sensores reales. El retardo de 2,1 ms se mide en un banco de experimentación sin tráfico real y con mensajes de 10 ms, sin comparación con otras redes. El daño se modela como reducción uniforme del módulo, un caso favorable para la detección. No hay falsas alarmas, sensibilidad al ruido, costos ni uso del gemelo para decisiones. La actualización del modelo con datos de su propio modelo no evalúa la deriva real de una estructura.  | La contribución sostenible es una arquitectura de referencia y una caracterización de latencia que muestran que los requisitos de tiempo para SHM y EEW pueden cumplirse con 5G y cómputo en el borde, con una placa de bajo costo derivada de experiencia en la reconstrucción de L'Aquila. La detección de daño y el gemelo se presentan como prueba de concepto con datos simulados, y su valor depende de que se repita el experimento con registros reales de un edificio. Para el corpus, es una pieza clave del eslabón gemelo-IoT-sismo, pendiente de validación con datos reales y de extensión a empresas y a la recuperación.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Emparejamiento' (matching) es mantener el gemelo alineado con el edificio físico; 'MEC' es cómputo en el borde de la red 5G; 'uRLLC' es comunicación de baja latencia y alta confiabilidad; 'daño' es una reducción del 10 % del módulo elástico.
- **P2 Supuestos:** Supone que un modelo de elementos finitos representa el edificio, que el retardo medido es representativo y que el daño uniforme es un buen sustituto del daño real.
- **P3 Evidencia:** La evidencia es un retardo medio de 2,1 ms, un modelo numérico con daño simulado y una aplicación prototipo con series generadas, sin datos medidos.
- **P4 Consecuencias:** Si es cierto, los edificios pueden alertar y actualizar su gemelo en milisegundos; si es falso, el sistema puede fallar con ruido real, daños localizados o redes saturadas.
- **P5 Contraejemplos:** No se examinan datos medidos, falsos positivos, otros enlaces, costos ni el uso para decisiones de reocupación.
- **P6 Alternativas:** Alternativas: que un enlace de menor costo baste para SHM; que el cuello de botella esté en la identificación modal; que el 5G no esté disponible tras un sismo.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Retardo medio de la red a nivel de aplicación | 2,1 | ms | Desviación estándar de 0,9 ms; mensajes cada 10 ms | Sec. 5.3, p. 17 | Texto | Alta | Banco de experimentación 5G |
| Desviación estándar del retardo | 0,9 | ms | Distribución normal | Sec. 5.3, p. 17 | Texto | Alta | Sin carga real reportada |
| Reducción simulada del módulo elástico (daño) | ≈ 10 | % | Daño uniforme en el modelo | Sec. 5.2, p. 17 | Texto | Alta | Serie sintética |
| Frecuencia de muestreo del conversor de la placa | 100 | Hz | 4 canales de 24 bits | Sec. 4.1, p. 9 | Texto | Alta | SHM-Board v2 |
| Periodo de monitoreo previo con placas IMOTE en la Basílica de Collemaggio | 5 | años | Experiencia posterior al sismo de 2009 | Sec. 4.1, p. 9 | Texto | Alta | Base de la nueva placa |
| Intervalo de publicación de mensajes del sensor | 10 | ms | Medición de retardo | Sec. 5.3, p. 17 | Texto | Alta | Hacia borde y nube |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'Future works are devoted toward the exploitation of real-time experimental data for service validation' (p. 18) | Validación de componentes en laboratorio con modelo numérico y banco 5G; sin datos medidos de un edificio en operación. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'The board has been designed in order to examine the possible adoption of low cost, un-calibrated, MEMS accelerometers for both SHM and EEW scenarios' (p. 9) | Se explora la adopción de acelerómetros de bajo costo, sin cifras de costo ni modelo de negocio. |
| IRL | 4 | Sí | 'The average delay of the network, at application layer, follows a normal distribution with an average value of 2.1ms and a standard deviation of 0.9ms' (p. 17) | Integración de sensores, puerta de enlace, borde 5G y nube probada en un banco; sin edificio real instrumentado. |
| DRL | 3 | Sí | 'In this case real time processing and updating in systems using sensor networks for SHM need low latency and reliable communication' (p. 1) | Necesidad técnica argumentada; sin estudio de demanda de propietarios. |
| SRL | 2.0 | Sí | Componentes: Placa de sensores MEMS y puerta de enlace (TRL 5), Cómputo en el borde 5G y actualización del gemelo (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 18.0; ÷9 → 2.00; nivel acotado a [1,9] = 2.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 2 e IRL 4: arquitectura medida en banco y validada con series sintéticas, sin edificio real instrumentado ni costos. · Estrategia de salida: Piloto con datos medidos, comparación de enlaces y vínculo con decisiones de reocupación.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Validación circular | El gemelo se actualiza y se evalúa con series generadas por el mismo modelo que lo sustenta (Sec. 5.2-5.3, p. 16-17) | No demuestra desempeño con datos medidos |
| Condiciones favorables presentadas como evidencia general | El retardo de 2,1 ms se mide en un banco 5G sin carga y se usa como evidencia de cumplir requisitos de alerta (Sec. 5.3, p. 17) | Escenario no representativo del posterremoto |
| Simplificación del fenómeno | El daño se reduce a una disminución uniforme del 10 % del módulo elástico (Sec. 5.2, p. 17) | El daño real es localizado y no lineal |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Cómputo en el borde 5G → menor latencia → alerta y actualización en casi tiempo real | Retardos medidos en banco | Mecanismo directo | Medición bajo carga real | Cobertura 5G, saturación, energía | 3 | Efecto establecido en el banco |
| Cambio de frecuencias modales → detección de daño | Series sintéticas con 10 % de reducción del módulo | Física estructural | Datos medidos con efectos ambientales | Temperatura, humedad, ruido | 2 | Relación plausible con datos simulados |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Validación con datos medidos, falsos positivos y sensibilidad al ruido y a la temperatura | Crítico | Media | 9 |
| Tecnológico | Operación de la red tras un sismo y comparación con otros enlaces de comunicación | Crítico | Media | 8 |
| Conocimiento | Vínculo entre la detección de daño y el tiempo de reocupación de edificios y empresas | Crítico | Media | 9 |
| Mercado | Costos de sensores, de comunicaciones 5G y de cómputo en el borde | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 3 | Placa de sensores SHM-Board v2 | Fotografía | Microcontrolador y acelerómetros MEMS | 4 canales; 24 bits; 100 Hz | Media |
| Fig. 10 | Modelo de elementos finitos del edificio Coppito 1 | Modelo | Tipologías de elementos y condiciones de borde | No aplica | Media |
| Fig. 12-13 | Series de tiempo y densidades espectrales de potencia en condición sana y dañada | Gráficos | Reducción de frecuencias modales con 10 % de daño | ≈ 10 % | Alta |
| Tabla 2 | Secciones y espesores del modelo de elementos finitos | Tabla | 8 secciones de vigas y 3 de placas | 8; 3 | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Sistemas de monitoreo con enlaces LoRa o Wi-Fi para edificios | No especificado en documento | Empresa | Transmisión de datos de bajo costo | Menor costo | Latencia y confiabilidad menores | Estable |
| Placas IMOTE usadas en la Basílica de Collemaggio | Italia | Academia | Monitoreo continuo de cinco años | Experiencia de campo | Hardware anterior | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Retardo de aplicación (ms) y cambio de frecuencias modales ante daño simulado
- **X:** Arquitectura 5G con cómputo en el borde y nivel de daño (10 % del módulo elástico)
- **Z (controles):** Intervalo de mensajes de 10 ms, ruido blanco, condiciones de borde
- **Datos:** Series generadas por un modelo de elementos finitos de un edificio de concreto (Coppito 1) y mediciones de red en un banco 5G
- **Método:** Simulación numérica y medición de retardo; aplicación de aprendizaje automático prototipo
- **Efecto reportado:** Retardo medio de 2,1 ms; reducción de frecuencias modales visible con 10 % de daño
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin sensibilidad al ruido, falsos positivos ni datos medidos

| Vacío | Tipo | Descripción |
|---|---|---|
| V-064-01 | TERR | L'Aquila (Italia), ciudad en reconstrucción tras el sismo de 2009 |
| V-064-02 | POBL | Un edificio de concreto armado; sin empresas ni habitantes |
| V-064-03 | TEMP | Milisegundos de red; series de segundos a minutos de vibración; sin evolución de la estructura |
| V-064-04 | MET | Datos sintéticos, un solo edificio, sin falsos positivos |
| V-064-05 | VAR | Faltan costos, temperatura, humedad, ruido real y tiempo de reocupación |
| V-064-06 | TEOR | Gemelo digital y SHM; sin teoría de recuperación económica |
| V-064-07 | CAUS | Efecto de la alerta sin evidencia |
