# Análisis relacional inter-documental — Lote L01

`MODE=COMPUTE FILES=TRUE BATCH=L01 DOCS=101 STATUS=COMPLETE`

## 1. Alcance y método

Se tipificaron 362 relaciones dirigidas entre los 101 documentos (`csv/analisis_relacional.csv`). Hay seis tipos: CONFIRMA, CONTRADICE, COMPLEMENTA, EXTIENDE, DEPENDE_DE y PRECEDE. Cada relación tiene una base declarada: **citación verificada** (coincidencia de las primeras ocho palabras del título de un documento con la lista de referencias de otro; 114 aristas, de las cuales 86 parten de la síntesis D100), **autoría compartida** (calculada sobre los metadatos) y **juicio del analista** (relaciones sustantivas, con justificación). Las relaciones EXTIENDE y DEPENDE_DE tienen como inversa PRECEDE; las demás son simétricas. Por tipo: PRECEDE 118, DEPENDE_DE 107, COMPLEMENTA 66, CONFIRMA 56, EXTIENDE 11, CONTRADICE 4.

Excluyendo las síntesis D100 y D101, el grafo tiene 83 documentos conectados y 9 componentes conexos, de tamaños 41, 11, 9, 8, 5, 3, 2, 2, 2. Quedan sin relación sustantiva 16 documentos: cuatro periféricos (D038, D046, D057, D058), un adyacente (D083) y los once ajenos (D088–D098); D087 se vincula solo con D003.

## 2. Estructura del grafo

- **Componente 1 (41 documentos).** D003, D004, D005, D006, D007, D008, D012, D013, D014, D015, D016, D017, D020, D024, D026, D028, D029, D030, D034, D037, D043, D044, D047, D048, D050, D051, D056, D061, D064, D065, D066, D070, D072, D077, D078, D079, D080, D081, D082, D087, D099.
- **Componente 2 (11 documentos).** D001, D010, D019, D022, D031, D041, D042, D060, D062, D071, D076.
- **Componente 3 (9 documentos).** D009, D023, D032, D033, D035, D039, D068, D084, D086.
- **Componente 4 (8 documentos).** D002, D011, D027, D040, D053, D054, D067, D069.
- **Componente 5 (5 documentos).** D045, D049, D063, D073, D075.

Los componentes se interpretan así. El componente 1 reúne gemelos digitales de ciudad y comunitarios, revisiones, adopción organizacional del IoT y resiliencia de cadenas de suministro. El componente 2 agrupa el aprendizaje automático para alerta sísmica con UAV e IoT en gestión de desastres. El componente 3 contiene monitoreo estructural con IoT de bajo costo y gemelos de puentes. El componente 4 contiene los modelos de tiempo de recuperación de edificios y empresas y la economía del refuerzo sísmico. El componente 5 contiene la alerta sísmica de bajo costo, con arquitecturas descentralizadas.

Los documentos de mayor grado en la red de relaciones son: D013 (grado 10), D006 (grado 4), D048 (grado 4), D080 (grado 4), D017 (grado 4), D049 (grado 4), D040 (grado 4), D031 (grado 4). D013 (revisión de gemelos digitales posdesastre) es el nodo de mayor intermediación.

## 3. Hallazgos relacionales

### 3.1 Convergencias

Las relaciones CONFIRMA (56) se concentran en tres temas. (a) Las revisiones sobre gemelos digitales convergen en potencial alto e implementación incipiente (D004, D013, D028, D061, D079, D081, D099). (b) Los estudios de alerta sísmica con procesamiento en el nodo coinciden en reducir la latencia (D049, D073, D075, D064, D066). (c) Los estudios de encuesta organizacional coinciden en que el IoT y el gemelo digital mejoran la resiliencia operativa (D029, D030, D052, D085). De las 54 relaciones CONFIRMA entre documentos del lote (sin síntesis), 4 se apoyan en autoría compartida y no deben contarse como confirmaciones independientes.

### 3.2 Contradicciones y tensiones

Hay 2 contradicciones simétricas registradas. (i) Resiliencia organizacional como variable mediadora lineal (D030) frente a propiedad emergente de mecanismos colectivos, adaptativos y dinámicos (D082): implica diseños de evaluación distintos. (ii) Orden de desempeño de algoritmos de aprendizaje automático para alerta sísmica: XGBoost mejor en intensidad (D060) frente a una red neuronal mejor que XGBoost en magnitud (D041); las tareas y datos difieren, de modo que no hay contradicción empírica directa sino imposibilidad de transferir el orden. Se añade una tensión de alcance: D100 declara 2020-2024 pero incluye 49 referencias de 2025-2026 y no declara protocolo, mientras D099 cubre hasta junio de 2021 con protocolo PRISMA.

### 3.3 Dependencias y precedencias

Entre documentos del lote se verificaron 18 dependencias por citación. Las cadenas más claras son: D006 → D013 → D078 (gemelos de ciudad y comunitarios), D006/D048/D072 → D080, D045 → D049 → D075 (alerta sísmica de bajo costo) y D054/D002 → D040 (economía del refuerzo). D100 depende de 86 documentos del lote (referencia por referencia) y D101 de D099, D070 y D080.

### 3.4 Lectura por componente

**Componente de gemelos digitales, IoT y organización (41 documentos).** Es el más heterogéneo. Reúne tres líneas que apenas se conectan entre sí: gemelos urbanos y comunitarios para desastres (D006, D013, D034, D048, D070, D072, D078, D080), adopción organizacional e IoT en cadenas de suministro (D005, D007, D016, D017, D029, D030, D037, D051, D081, D082) y arquitecturas de borde y federadas con validación simulada (D043, D064, D065, D066). La unión entre ellas es D013 por su intermediación y las revisiones de gemelos. La consecuencia es que las afirmaciones sobre resiliencia organizacional no se apoyan en los estudios de desempeño técnico de los gemelos, y estos tampoco incorporan variables organizacionales.

**Componente de aprendizaje automático, UAV e IoT en desastres (11 documentos).** Agrupa estimación de magnitud e intensidad, restablecimiento de comunicaciones y evaluación de daño con imágenes (D001, D010, D019, D022, D031, D041, D042, D060, D062, D071, D076). Las relaciones son de complementariedad y de tensión de desempeño entre algoritmos; la evidencia es de simulación y de datos históricos, con una prueba de campo (D062).

**Componente de monitoreo estructural con IoT de bajo costo (9 documentos).** Reúne gemelos de puentes y nodos de bajo costo (D009, D023, D032, D033, D035, D039, D068, D084, D086). Se confirma que la evaluación en campo es excepcional (D023) y que dos documentos comparten autoría (D039, D086). La calidad del dato (D033, D039, D086) aparece como condición común.

**Componente de recuperación y economía del refuerzo (8 documentos).** Incluye modelos de tiempo de recuperación de empresas y edificios (D011, D053), análisis costo-beneficio con pérdidas indirectas y resiliencia (D040, D054, D069) y refuerzos específicos (D002, D027, D067). Es el único componente con modelos que predicen tiempos de cierre o de recuperación, y no tiene relaciones con tecnologías digitales; las citaciones verificadas lo confirman (D040 cita a D002 y D054; no hay citas hacia documentos de gemelos o IoT).

**Componente de alerta sísmica de bajo costo (5 documentos).** Contiene D045, D049, D063, D073 y D075. Tres de ellos comparten autoría, y los tres ofrecen una misma tesis: el procesamiento en el nodo reduce la latencia. D073 la apoya de forma independiente con datos de un sismo de magnitud 5,4.

### 3.5 Lectura de las síntesis automáticas

D100 se relaciona con 86 documentos del lote por citación y D101 con tres (uno de ellos, D099, ausente de la lista de D100). Las relaciones de D100 con el lote son de dependencia y no de confirmación: el contenido de D100 procede de lo que Scopus AI recuperó, y el lote contiene esos mismos documentos. Por ello la coincidencia de la conclusión de D100 con la de las revisiones del lote (potencial alto, evidencia empírica escasa) debe leerse como una consecuencia de la fuente común. La diferencia útil entre ambas síntesis es de cobertura: D100 recupera 93 referencias, de las cuales 49 son de 2025 y 2026, y D101 recupera solo tres. Ninguna de las dos informa la cadena de búsqueda, los criterios de inclusión ni el número de registros examinados, por lo que no se puede evaluar sensibilidad ni precisión de la recuperación.

### 3.6 Lectura de los vínculos con el bloque SciELO

Los documentos D088 a D098 no tienen vínculo temático con el eje y su única relación es la pertenencia al mismo número de la revista *Biomédica* (volumen 28, número 3, 2008). D087, un editorial sobre la política de ciencia, tecnología e innovación, se relaciona con D003 como contexto institucional. El bloque sirvió como control negativo: en las pruebas de similitud forma un grupo propio y su exclusión no altera los resultados descriptivos de madurez.

## 4. Proposiciones emergentes

Las proposiciones surgen de la comparación entre documentos y no figuran en ninguno de ellos. Son hipótesis del analista, con la evidencia que las sustenta y la prueba que las falsearía.

**P-E1. Los parámetros que mejoran los gemelos digitales y el IoT corresponden a componentes de demora de los modelos de recuperación empresarial, y ningún documento los conecta.**
*Evidencia.* El componente de modelos de recuperación (D011, D053; también D040, D054, D069) está desconectado del componente de gemelos e IoT. D011 modela varios tipos de inactividad y tácticas de mitigación y D053 modela demoras impedientes con distribuciones de valor extremo; los estudios de gemelos y de alerta sísmica reducen el tiempo de detección, de evaluación de daño y de comunicación (D034, D048, D064, D049, D076). *Hipótesis.* Sustituir en los modelos de recuperación el tiempo de evaluación de daño por el de un gemelo digital con sensores reduce la mediana del tiempo de cierre; la magnitud depende de la fracción del tiempo total que ocupan las demoras de inspección. *Falsación.* Si en datos observados de sismos la demora de evaluación representa menos de una fracción pequeña del tiempo de cierre, la mejora es marginal. *Valor.* Permite estimar un efecto de la tecnología sobre el resultado de interés con datos existentes antes de financiar pilotos.

**P-E2. El «potencial alto» de las revisiones y la «implementación incipiente» son la misma observación y no dos hallazgos independientes.**
*Evidencia.* Siete revisiones convergen (T07), pero dependen de una base común de estudios con TRL mediano 4 y comparten sesgo de publicación; D100 incluye 86 de los documentos del lote. *Hipótesis.* El número de revisiones que concluyen potencial no aumenta la confianza en el efecto; el peso efectivo corresponde al número de estudios empíricos independientes con desenlaces medidos, que en el lote es cercano a cero para empresas. *Falsación.* Un metaanálisis de los estudios de base con desenlaces cuantificados que muestre efectos consistentes. *Valor.* Evita sobreponderar la cantidad de revisiones en decisiones de política.

**P-E3. La independencia efectiva de la evidencia es menor que el número de documentos.**
*Evidencia.* Cinco agrupamientos de autoría (Prasanna: D045, D049, D075; Yu-Fu-Cui: D039, D086; Galasso: D040, D053; Korkmaz-Demirkesen: D048, D080; Abdalzaher-Krichen: D019, D060) reducen los grupos independientes en afirmaciones como la de latencia en alerta (seis documentos, cuatro grupos). *Hipótesis.* Una ponderación por grupo de autoría cambia el veredicto de al menos una afirmación de triangulada a parcial. *Falsación.* Un recálculo con réplica por grupos distintos que mantenga la convergencia. *Valor.* Mejora la calibración de la confianza.

**P-E4. La calidad de reporte estadístico se asocia inversamente con la relevancia temática.**
*Evidencia.* La robustez media del bloque ajeno (3.84) supera a la de núcleo (3.19) y adyacentes (3.13); los estudios biomédicos reportan intervalos de confianza, controles de calidad externos y límites, y los tecnológicos suelen presentar una sola partición o simulación. *Hipótesis.* La adopción de guías de reporte en el campo tecnológico elevaría la robustez en más de un punto sin cambiar la tecnología. *Falsación.* Una evaluación de estudios tecnológicos recientes que ya cumpla esas guías sin mejorar la robustez. *Valor.* Es una intervención de bajo costo sobre la calidad de la evidencia.

**P-E5. La transferencia tecnológica es el vínculo ausente entre ambas subliteraturas, y su única mención empírica proviene de contextos no sísmicos.**
*Evidencia.* D100 reconoce que faltan marcos y evidencia empírica; sus referencias sobre factores humanos y organizacionales (D029, D007, D085 y estudios de mantenimiento y construcción) no son sísmicas; D003 y D012 señalan equidad y gestión del conocimiento. *Hipótesis.* La capacidad de absorción de la empresa modera el efecto de la tecnología sobre el tiempo de recuperación: en empresas con baja capacidad, la tecnología no reduce el tiempo. *Falsación.* Un estudio con empresas afectadas por un sismo que no encuentre moderación. *Valor.* Orienta el diseño de programas de transferencia hacia capacidades, no solo hacia equipos.

## 5. Puntaje de integración relacional

Se define un índice del analista, transparente y reproducible: **S = 10 × (C + I + K) / 3**, donde C es la cobertura relacional (proporción de los 87 documentos técnicos con al menos una relación sustantiva = 0.94), I es la independencia de las convergencias (proporción de relaciones CONFIRMA sin autoría compartida = 0.93) y K es la conectividad (tamaño del mayor componente sobre el número de documentos técnicos = 0.47).

**S = 7.8 sobre 10.** La interpretación es que la cobertura y la independencia son altas, pero la conectividad es baja: el campo está fragmentado en subliteraturas sin vínculos y, en particular, los modelos de recuperación empresarial no se relacionan con los gemelos digitales. El puntaje no mide calidad de los documentos, solo la integración de la red construida.

## 6. Limitaciones del análisis relacional

- Las relaciones sustantivas son juicio del analista; otro analista podría registrar relaciones adicionales, y la desconexión de componentes depende en parte de ese registro. Se contrastó con la estructura de TF-IDF: el grupo de refuerzo sísmico y recuperación también se separa en k-means (k = 3).
- La detección de citaciones se limita a documentos presentes en el lote y a coincidencia de títulos; puede omitir citas con títulos abreviados.
- Las síntesis D100 y D101 no son fuentes independientes y se excluyeron del cálculo de componentes.
- Los documentos del bloque ajeno no se relacionan con el eje y no entran en el índice.

## 7. Valor estratégico

El análisis relacional permite priorizar investigaciones que conectan modelos de recuperación con datos de gemelos digitales (P-E1) y pruebas de capacidad de absorción (P-E5), y establece que la cantidad de revisiones no equivale a evidencia (P-E2). Para quien decide la inversión, el principal riesgo es confundir potencial con efecto medido.

## 8. Anexo A. Relaciones sustantivas de confirmación, contradicción y extensión (sin síntesis de buscadores)

Cada fila se lista una vez (origen < destino para relaciones simétricas). La base indica si hay citación verificada o autoría compartida.

| Origen | Tipo | Destino | Justificación | Base |
|---|---|---|---|---|
| D013 | EXTIENDE | D006 | propone un marco integral de gemelo digital posdesastre (IA explicable, dinámica social, sistemas interconectados) que desarrolla la visión de ciudad-gemelo en desastre de D006; ambos son propuestas conceptuales sin validación operativa | juicio del analista; citación verificada de D013 a D006 |
| D048 | EXTIENDE | D072 | usa el gemelo digital como imagen operativa común para estimar daños y necesidades de rescate, apoyado en el antecedente de modelado híbrido físico-datos de D072 | juicio del analista; citación verificada de D048 a D072 |
| D080 | EXTIENDE | D048 | replica la lógica de imagen operativa común en un distrito industrial con sensores IoT y arquitectura híbrida; comparte autoría (Korkmaz, Demirkesen) con D048, por lo que no es una confirmación independiente | juicio del analista; citación verificada de D080 a D048; autoría compartida |
| D078 | EXTIENDE | D013 | construye un gemelo comunitario con datos públicos reales que operacionaliza parte del marco posdesastre de D013, con validación todavía simulada | juicio del analista; citación verificada de D078 a D013 |
| D034 | CONFIRMA | D048 | ambos estiman daño por edificio y necesidades de respuesta con gemelos urbanos y escenarios sísmicos; proceden de contextos y grupos distintos (Ningxia, China, y Kocaeli, Türkiye) | juicio del analista |
| D004 | CONFIRMA | D028 | ambas revisiones concluyen que los gemelos digitales tienen potencial pero la implementación real es incipiente y depende de integración de datos, escalabilidad e inversión | juicio del analista |
| D028 | CONFIRMA | D079 | ambas revisiones señalan interoperabilidad, calidad de datos y escalabilidad como barreras y escasa validación en operación real | juicio del analista |
| D004 | CONFIRMA | D013 | relación inversa de D013 CONFIRMA D004: coinciden en que la literatura de gemelos digitales es fragmentada e incipiente y en que faltan marcos integrados | juicio del analista |
| D013 | CONFIRMA | D061 | relación inversa de D061 CONFIRMA D013: la revisión PRISMA de gemelos para inundaciones urbanas (85 estudios) reporta mejoras de pronóstico y respuesta y coincide en la necesidad de integrar | juicio del analista; citación verificada de D061 a D013 |
| D037 | CONFIRMA | D081 | relación inversa de D081 CONFIRMA D037: ambos hallan efectos por etapa de la disrupción, mayores en preparación y respuesta que en recuperación (D037 r=0,331 global y r=0,273 en recuperación | juicio del analista |
| D016 | CONFIRMA | D017 | relación inversa de D017 CONFIRMA D016: ambos describen crecimiento de la literatura de IoT en cadenas de suministro desde 2017-2018 y concentración en blockchain, aprendizaje automático y I | juicio del analista |
| D007 | EXTIENDE | D005 | D007 refina la tesis de D005 (los beneficios del IoT dependen de condiciones institucionales) con aceptación de partes interesadas, liderazgo digital y opacidad parcial; D007 cita a D005 | juicio del analista; citación verificada de D007 a D005 |
| D005 | CONFIRMA | D007 | relación inversa de D007 CONFIRMA D005: ambos concluyen que la adopción del IoT es un proceso organizacional y no solo técnico, con consecuencias estructurales | juicio del analista; citación verificada de D007 a D005 |
| D029 | CONFIRMA | D030 | relación inversa de D030 CONFIRMA D029: ambos muestran con encuestas que IoT y gemelo digital mejoran la resiliencia organizacional operativa mediante capacidades; ambos son transversales y | juicio del analista |
| D030 | CONTRADICE | D082 | relación inversa de D082 CONTRADICE D030: D082 concibe la resiliencia organizacional como propiedad emergente de mecanismos colectivos, adaptativos y dinámicos, mientras D030 la trata como var | juicio del analista |
| D052 | CONFIRMA | D085 | relación inversa de D085 CONFIRMA D052: coinciden en que el valor del gemelo digital en construcción pasa por el intercambio de información y la decisión colaborativa, no por la tecnología p | juicio del analista |
| D005 | CONFIRMA | D029 | relación inversa de D029 CONFIRMA D005: la capacidad de absorción de conocimiento como condición de beneficio refuerza la tesis de D005 sobre condiciones institucionales de la adopción | juicio del analista |
| D003 | CONFIRMA | D012 | relación inversa de D012 CONFIRMA D003: ambos señalan que las soluciones tecnológicas dominan la literatura de desastres con integración débil de conocimiento, equidad y factores humanos | juicio del analista |
| D003 | CONFIRMA | D099 | relación inversa de D099 CONFIRMA D003: coinciden en que la evidencia es fragmentada y en que faltan estudios sobre las condiciones de adopción tecnológica en desastres (barreras y factores | juicio del analista |
| D050 | CONFIRMA | D099 | relación inversa de D099 CONFIRMA D050: ambos identifican el IoT como núcleo de la gestión de desastres con beneficios de monitoreo y comunicación y con desafíos de confiabilidad | juicio del analista |
| D040 | EXTIENDE | D054 | D040 incorpora pérdidas indirectas y carbono del ciclo de vida al análisis costo-beneficio de refuerzo que D054 desarrolla con víctimas y reparaciones; D040 cita a D054 | juicio del analista; citación verificada de D040 a D054 |
| D040 | CONFIRMA | D069 | ambos muestran que incluir recuperación, tiempo de inhabilitación y pérdidas indirectas cambia la medida preferida de refuerzo frente a considerar solo pérdidas directas | juicio del analista |
| D011 | CONFIRMA | D053 | relación inversa de D053 CONFIRMA D011: ambos muestran que el tiempo de reparación del edificio no basta como medida de recuperación y que las demoras y la inactividad deben modelarse; D011 | juicio del analista |
| D053 | EXTIENDE | D011 | relación inversa de D011 PRECEDE D053: el marco analítico de D011 (varios tipos de inactividad y tácticas de mitigación) antecede a los modelos de simulación de alta fidelidad de D053 | juicio del analista |
| D075 | EXTIENDE | D045 | D075 lleva la alerta sísmica de bajo costo a una red LoRa multisalto descentralizada; D045 revisa sensores MEMS de bajo costo y cita a D049; D075 cita a D045; comparten autoría (Prasanna) | juicio del analista; citación verificada de D075 a D045; autoría compartida |
| D049 | CONFIRMA | D073 | ambos muestran que detectar y generar la alerta en el nodo reduce la latencia frente a arquitecturas centralizadas (D049 1,24 a 2,88 s; D073 localización más temprana en sismo de magnitud 5,4), con evidencia de simulación o datos históricos | juicio del analista |
| D049 | CONFIRMA | D075 | relación inversa de D075 CONFIRMA D049: comparten autoría (Prasanna, Holden): la arquitectura descentralizada reduce la latencia; la concordancia procede del mismo grupo | juicio del analista; autoría compartida |
| D041 | CONTRADICE | D060 | relación inversa de D060 CONTRADICE D041: D060 reporta que XGBoost supera a otros algoritmos en intensidad sísmica (99,05 %) y D041 que una red neuronal supera a XGBoost en magnitud; las tarea | juicio del analista |
| D019 | CONFIRMA | D042 | ambas revisiones integran IoT, UAV, comunicaciones y aprendizaje automático en el ciclo del terremoto y concluyen que la integración mejora la conciencia situacional con validación real escasa | juicio del analista; citación verificada de D042 a D019 |
| D071 | EXTIENDE | D031 | D071 desarrolla la semántica de IoT para detección sísmica (ontología SSN/SOSA y clasificador profundo) que D031 planteaba como arquitectura de alerta temprana | juicio del analista |
| D064 | CONFIRMA | D066 | ambos sostienen que el cómputo en el borde reduce la latencia (D064 retardo medio de 2,1 ms; D066 mejora en simulación); D066 no tiene despliegue real | juicio del analista |
| D065 | CONFIRMA | D066 | relación inversa de D066 CONFIRMA D065: ambos son propuestas de asignación descentralizada de recursos en el borde validadas solo por simulación | juicio del analista |
| D043 | CONFIRMA | D065 | validación únicamente simulada de marcos descentralizados con tecnologías de borde y aprendizaje federado | juicio del analista |
| D039 | CONFIRMA | D086 | relación inversa de D086 CONFIRMA D039: comparten autoría (Yu, Fu, Cui): resuelven calidad de datos y sincronización en redes inalámbricas de monitoreo estructural; no son confirmaciones ind | juicio del analista; autoría compartida |
| D068 | CONFIRMA | D084 | relación inversa de D084 CONFIRMA D068: ambos demuestran monitoreo estructural con IoT de bajo costo solo en laboratorio (modelo a escala o viga), con TRL 4 y sin pruebas de campo | juicio del analista |
| D009 | CONFIRMA | D035 | ambos reconstruyen el comportamiento dinámico de puentes con modelos actualizados por datos con errores de hasta 5 % (D009: 1 % a 5 %; D035: menos de 5 % en frecuencias) | juicio del analista |
| D015 | EXTIENDE | D020 | D015 modela de forma conjunta la incertidumbre del sensado y el cumplimiento normativo con un modelo bayesiano ordinal y cita a D020, que asocia componentes de IoT con la resiliencia sísmica mediante una encuesta | juicio del analista; citación verificada de D015 a D020 |
| D044 | CONFIRMA | D050 | ambos informan beneficios del IoT en respuesta a emergencias y gestión de desastres, con ejemplos descriptivos | juicio del analista |
| D050 | CONFIRMA | D056 | relación inversa de D056 CONFIRMA D050: ambos describen mejoras del IoT en alerta temprana, monitoreo y comunicación para desastres naturales con evidencia mayormente descriptiva | juicio del analista |

## 9. Anexo B. Relaciones de complementariedad

| Origen | Destino | Justificación |
|---|---|---|
| D070 | D079 | D079 revisa gemelos urbanos con IoT e IA en ciudades inteligentes y D070 los aplica al caso de terremotos fuertes y a los ODS; ambos concluyen potencial con evidencia empírica escasa |
| D034 | D064 | D034 modela intensidad y daño por edificio con actualización por sensores; D064 aporta la arquitectura 5G y de borde para actualizar gemelos con baja latencia |
| D008 | D064 | D008 resuelve la interoperabilidad entre simulaciones (ficha BSIC) y D064 la latencia de actualización; los dos desafíos coinciden con los identificados por D100 como barreras centrales |
| D021 | D025 | D021 integra datos heterogéneos con repositorio BIM y web semántica para gestión de activos; D025 sincroniza BIM, inspecciones y sensores con identificadores persistentes alineados con IFC 4.3 |
| D013 | D081 | relación inversa de D081 COMPLEMENTA D013: D081 estudia el efecto del gemelo sobre la resiliencia de cadenas de suministro por etapas y D013 sobre la gestión posdesastre; ambas mezclan evidenci |
| D017 | D037 | relación inversa de D037 COMPLEMENTA D017: D037 mide asociación entre tecnologías digitales y resiliencia de cadena de suministro con metaanálisis y D017 describe la evolución y barreras del Io |
| D017 | D051 | relación inversa de D051 COMPLEMENTA D017: D051 clasifica 92 desafíos en 16 categorías y D017 sintetiza barreras (seguridad, interoperabilidad) para IoT en cadenas de suministro |
| D016 | D024 | relación inversa de D024 COMPLEMENTA D016: D024 trata cadenas de alimentos y D016 logística general; ambos son revisiones bibliométricas de periferia temática con IoT |
| D037 | D077 | relación inversa de D077 COMPLEMENTA D037: D077 propone un marco conceptual ilustrado con datos abiertos de compras en línea durante la pandemia en Australia, sin medir resiliencia; D037 cuanti |
| D029 | D082 | relación inversa de D082 COMPLEMENTA D029: D082 ofrece el marco de mecanismos y D029 aporta evidencia sobre capacidad de absorción y turbulencia tecnológica como moderador |
| D052 | D085 | D052 identifica la transparencia de la información como mediador del efecto del gemelo en la eficiencia (0,749); D085 identifica factores de oficina, obra e interfaz; ambos usan encuestas de percepción en construcción |
| D013 | D099 | relación inversa de D099 COMPLEMENTA D013: D099 mapea seis familias de Industria 4.0 en gestión de riesgo de desastres y D013 se centra en gemelos posdesastre; ambos reconocen un campo incipien |
| D003 | D087 | relación inversa de D087 COMPLEMENTA D003: ambos son editoriales de política sin datos propios: D087 sobre el sistema de ciencia, tecnología e innovación de Colombia (2008) y D003 sobre tecnolo |
| D054 | D069 | relación inversa de D069 COMPLEMENTA D054: D054 valora la reducción de víctimas y D069 la ganancia de funcionalidad; ambos contribuyen a justificar el refuerzo más allá de las reparaciones |
| D040 | D053 | relación inversa de D053 COMPLEMENTA D040: comparten autoría (Galasso): D053 aporta modelos de consecuencia de tiempo de recuperación y D040 los usa en decisiones de refuerzo; no son confirmaci |
| D002 | D067 | D002 optimiza camisas de acero con algoritmo genético (costo 40 % menor) y D067 evalúa camisas de concreto con fibras de acero (capacidad cortante hasta 39 % mayor); ambos son estudios de caso en estructuras específicas |
| D002 | D027 | relación inversa de D027 COMPLEMENTA D002: D027 compara fibras de vidrio y carbono por rentabilidad del confinamiento y D002 el costo de camisas de acero; ambos priorizan costo con evidencia de |
| D049 | D063 | relación inversa de D063 COMPLEMENTA D049: ambos aplican el principio PLUM: D063 a ferrocarriles de alta velocidad con arquitectura jerárquica y D049 de forma modificada en sensores MEMS de baj |
| D010 | D041 | ambos estiman magnitud con aprendizaje automático; D010 corrige el desbalance de eventos grandes con datos sintéticos (CTGAN) y D041 compara modelos con datos históricos de California |
| D019 | D060 | comparten autoría (Abdalzaher, Krichen): D019 revisa tecnologías emergentes y D060 aplica aprendizaje automático a intensidad sísmica en sitio |
| D018 | D055 | D018 integra agentes de IA y gemelos digitales (demostración por simulación de una red eléctrica genérica) y D055 modela gemelos como agentes BDI; ambos son propuestas de baja madurez |
| D018 | D059 | relación inversa de D059 COMPLEMENTA D018: D059 redefine el gemelo como motor de datos con modelo grande como motor de inteligencia y D018 usa el gemelo como entorno de simulación de agentes; a |
| D039 | D084 | relación inversa de D084 COMPLEMENTA D039: D084 sincroniza nodos por hardware (error de 50 microsegundos) y D039 corrige retardos por aprendizaje profundo; son soluciones alternativas al mismo |
| D023 | D084 | relación inversa de D084 COMPLEMENTA D023: D084 valida nodos en laboratorio y D023 opera un gemelo con LoRaWAN en un puente ferroviario en servicio, lo que muestra la brecha entre prototipo y c |
| D023 | D035 | D023 mantiene medición continua con LoRaWAN y D035 actualiza el modelo por algoritmo genético en el puente de acero; ambos aportan a gemelos de puentes |
| D014 | D020 | D014 define dónde instalar sensores en un edificio patrimonial y D020 asocia componentes de IoT con resiliencia sísmica; ambos de ingeniería de edificios con IoT |
| D009 | D032 | relación inversa de D032 COMPLEMENTA D009: D032 mapea la literatura de gemelos con IA para SHM y D009 es un ejemplo de gemelo con monitoreo híbrido de modelo y datos |
| D022 | D062 | relación inversa de D062 COMPLEMENTA D022: D062 planifica trayectorias de AAV con LoRa por aprendizaje por refuerzo y D022 revisa UAV como estaciones base aéreas para restablecer comunicaciones |
| D001 | D062 | D001 optimiza la ruta y la energía de un UAV para recolectar datos y D062 la trayectoria y la conectividad; ambos con simulación |
| D042 | D076 | relación inversa de D076 COMPLEMENTA D042: D076 clasifica daño posterremoto en imágenes de UAV con aprendizaje profundo ligero y D042 revisa IoT y UAV en la gestión del terremoto |
| D026 | D048 | D026 caracteriza las soluciones digitales tras el terremoto de 2023 en Türkiye (plataformas web de proveedores privados) y D048 modela un gemelo para una respuesta en Kocaeli; ambos con Türkiye como referencia territorial |
| D026 | D047 | relación inversa de D047 COMPLEMENTA D026: D047 revisa SIG en la gestión del transporte posterremoto y D026 las soluciones digitales de respuesta y recuperación; ambos con evidencia mayormente |
