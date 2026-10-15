# FB-L01-002 | D002 — Optimal seismic retrofitting of reinforced concrete buildings by steel-jacketing using a genetic algorithm-based framework

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/1-s2.0-S0141029619348746-main.pdf` · 14 páginas · Relevancia para el eje del corpus: **Adyacente** (Reforzamiento sísmico (mitigación previa al evento) con optimización de costos; conecta con el análisis costo-beneficio de la resiliencia pero no modela interrupción empresarial.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-002 / D002
- **Tipo de recurso:** Artículo científico (journal peer-reviewed)
- **Referencia APA 7:** Di Trapani, F., Malavisi, M., Marano, G. C., Sberna, A. P., & Greco, R. (2020). Optimal seismic retrofitting of reinforced concrete buildings by steel-jacketing using a genetic algorithm-based framework. *Engineering Structures*, *219*, Article 110864. https://doi.org/10.1016/j.engstruct.2020.110864
- **Autores:** Di Trapani, Fabio (55428171100); Malavisi, Marzia (56642866900); Marano, Giuseppe Carlo (57382102800); Sberna, Antonio Pio (57217025383); Greco, Rita (7103137160)
- **Afiliaciones:** Dipartimento di Ingegneria Strutturale, Edile e Geotecnica, Politecnico di Torino, Corso Duca degli Abruzzi 24, Turin, 10129, Italy; Dipartimento di Ingegneria Civile, Ambientale, del Territorio, Edile e di Chimica, Politecnico di Bari, Italy
- **Fecha de publicación:** 2020
- **Fuente/contenedor:** Engineering Structures · vol. 219
- **Identificador persistente:** DOI 10.1016/j.engstruct.2020.110864 · ISSN 01410296
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85085841651&doi=10.1016%2fj.engstruct.2020.110864&partnerID=40&md5=2167b28f33b9ea81d5a798087d0e0eb6
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 87

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Formular un marco de optimización que minimice el costo de reforzar con camisas de acero (ángulos y pletinas) las columnas de edificios porticados de concreto reforzado no diseñados para cargas sísmicas, decidiendo la ubicación de las columnas reforzadas (optimización topológica) y el espaciamiento de las pletinas, de modo que cada solución cumpla un nivel de seguridad especificado por el proyectista y se reduzcan tanto los costos de obra como el tiempo de inhabilitación del inmueble, medido con la razón entre ductilidad de capacidad y de demanda obtenida del análisis estático no lineal.

**Pregunta de investigación.** [INFERIDA] ¿Es posible reducir el costo directo del reforzamiento con camisas de acero sin perder el nivel de seguridad sísmico exigido, si la selección de columnas y el espaciamiento de pletinas se determinan mediante un algoritmo genético acoplado a un modelo de fibras?

**Marco teórico.** El trabajo se ubica en la ingeniería sísmica basada en desempeño y en la optimización estructural. Usa el método N2 de Fajfar (2000), adoptado por el Eurocódigo 8, para convertir curvas pushover en razones de ductilidad capacidad/demanda; el confinamiento del concreto se modela con las expresiones de Razvi y Saatcioglu (1992) combinadas con el enfoque de Montuori y Piluso (2009) y los resultados experimentales de Campione et al. (2017). La optimización se enmarca en la computación evolutiva (algoritmos genéticos) y en la tradición de diseño sísmico óptimo de Liu, Zou y Mitropoulou. El paradigma es determinista y positivista: la seguridad se expresa como una restricción de desempeño y el costo como función objetivo con penalización.

**Metodología.** Se conecta la herramienta de algoritmo genético de Matlab con un modelo tridimensional de fibras en OpenSees, con elementos de plasticidad distribuida basados en fuerza y cinco puntos de Gauss-Lobatto, concreto Concrete02 con límite de aplastamiento MinMax a 30 % de pérdida de resistencia y acero Steel02. Cada individuo codifica un vector de 17 variables: 16 variables binarias que indican si se refuerza cada columna de los dos primeros niveles (excepto las centrales, siempre reforzadas) y un espaciamiento común de pletinas entre 150 y 400 mm. La factibilidad se evalúa con un pushover (perfil uniforme) y la razón ξμ = μc/μd; la función objetivo suma un costo fijo por columna (2.000 EUR, demolición y reposición de revestimientos y mampostería) y el costo del acero (4,5 EUR/kg), con penalización cúbica sobre Cmax para soluciones infactibles. Población de 50 individuos (tres veces el vector de diseño), cruce disperso y mutación gaussiana. El caso es un pórtico de cinco niveles y dos vanos en Cosenza (Italia), suelo tipo C, vida nominal de 100 años y periodo de retorno de 975 años, con concreto de 20 MPa; se prueban una configuración regular y otra irregular con mampostería de relleno en un solo pórtico.

**Resultados principales.** La estructura sin refuerzo presenta ξμ = 0,792 y el colapso de la columna central. Entre las cinco configuraciones preliminares, solo reforzar los 18 pilares de los dos primeros niveles con pletinas a 150 mm (51.578,33 EUR, ξμ = 1,722) y el patrón de la prueba 5 (10 columnas, pletinas a 250 mm, 27.170,98 EUR, ξμ = 1,030) cumplen la verificación. El algoritmo converge tras unas 870 evaluaciones; el óptimo para una dirección aparece en la iteración 821 con cuatro columnas reforzadas, pletinas a 250 mm, ξμ = 1,014 y 10.868,39 EUR. Al extenderlo a todas las direcciones por simetría, el diseño final refuerza seis columnas, con ξμ = 1,010 y 16.302,59 EUR, es decir, 40 % menos que la prueba 5, con una diferencia de ξμ de 2 %. Con mampostería de relleno, la estructura sin refuerzo cae a ξμ = 0,535 en la dirección Z; el óptimo (columnas 6, 9 y 4 del primer nivel, sb = 250 mm) alcanza ξμ = 1,015 con 13.585,49 EUR, y el diseño final en ambas direcciones cuesta 16.302,59 EUR con ξμ = 1,095 en X. Cada pushover tarda unos 0,5 min y la optimización total, unas 8 horas. El cálculo del analista a partir de los costos reportados indica que el acero aporta cerca de 717 EUR por columna con pletinas a 250 mm, frente a 2.000 EUR del costo fijo por columna.

**Discusión y contribución.** Los autores concluyen que el marco reduce los costos de reforzamiento y de tiempo fuera de servicio controlando el nivel de seguridad; que menor cantidad de acero no implica menor seguridad si la ubicación es adecuada; que el procedimiento funciona con irregularidades; y que, para estructuras simétricas, basta optimizar un número reducido de direcciones y extender el resultado. Insisten en que el resultado es una sugerencia al proyectista, quien conserva el criterio final, y que el corte por cortante de columnas y nudos no se modeló. La contribución es la primera aplicación de optimización al refuerzo con camisas de acero, que en la literatura se había optimizado para FRP, amortiguadores y arriostramientos. La discusión no cuantifica el tiempo fuera de servicio que el resumen y la introducción presentan como motivación del trabajo.

**Limitaciones declaradas.** No hay sección formal de limitaciones. Se declaran: pushover con perfil uniforme y una dirección para el caso simétrico, modelo sin comportamiento no lineal del nudo, sin falla por cortante, un solo tipo de camisa con espaciamiento uniforme y casos de pórtico sencillo.

**Trabajo futuro.** Desarrollo de algoritmos de optimización para múltiples técnicas de reforzamiento y de técnicas efectivas de restricción del espacio de diseño para reducir el esfuerzo computacional en edificios complejos.

**Palabras clave.** Declaradas: Genetic algorithm; Optimization; Pushover; Retrofitting; Steel jacketing | Inferidas: camisas de acero, pushover, método N2, ductilidad, OpenSees, optimización topológica, costo de reforzamiento, edificios de concreto reforzado, mampostería de relleno

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un algoritmo genético acoplado a un modelo de fibras puede encontrar configuraciones de reforzamiento con camisas de acero que cumplen la seguridad exigida con un costo 40 % menor que las soluciones heurísticas de ingeniería, incluso en estructuras con irregularidades.

**Antítesis identificada.** El óptimo se ubica en el borde de la restricción (ξμ de 1,010 a 1,015), de modo que no queda margen frente a la variabilidad de materiales, del modelo de mampostería o de la acción sísmica; una restricción determinista de capacidad igual a demanda para un único periodo de retorno equivale, en términos de confiabilidad, a una probabilidad de falla cercana a la incertidumbre del modelo. Además, el objetivo es dominado por un costo fijo por columna (2.000 EUR frente a unos 717 EUR de acero), por lo que el algoritmo esencialmente minimiza el número de columnas y casi no optimiza el espaciamiento. La referencia de comparación es una configuración preliminar elaborada por los propios autores, no una práctica de diseño documentada, y el tiempo fuera de servicio, que motiva el estudio, no forma parte de la función objetivo.

**Síntesis propuesta.** El artículo demuestra que el desempeño sísmico puede traducirse en una restricción computable dentro de un lazo de optimización, y que la ubicación de los refuerzos importa más que su cantidad. Para que el hallazgo sea utilizable en decisiones de recuperación productiva, debe extenderse con restricciones probabilistas, con márgenes de seguridad explícitos y con un término de pérdida de actividad económica durante la obra y tras el sismo. Así, el marco pasa de minimizar el costo de obra a minimizar el costo esperado del ciclo de vida de la edificación y de las empresas que la ocupan, lo que alinea la ingeniería estructural con los objetivos de continuidad de actividad.

**Áreas grises detectadas.**

1. Costo del 'tiempo fuera de servicio': el resumen y la introducción lo citan como motivación, pero la función objetivo (Ecs. 24-25) solo incluye material, mano de obra y un monto fijo de 2.000 EUR por columna para demolición y reposición; no hay modelo de interrupción de uso ni de ingresos.
2. Línea base de ahorro: la reducción de 40 % se calcula frente a la Prueba 5, diseñada por los autores con criterio heurístico, y no frente a una práctica profesional documentada ni frente a un método alternativo de optimización o de diseño por capacidad.
3. Seguridad en el límite: ξμ = 1,010 a 1,015 significa capacidad igual a demanda para un solo espectro (TR = 975 años) y un único perfil de carga lateral uniforme; no se presenta análisis de sensibilidad a la resistencia del concreto (20 MPa), al modelo de nudo omitido ni a la variabilidad de la mampostería.
4. Generalización: las conclusiones sobre 'estructuras más grandes' se proyectan desde dos pórticos de cinco niveles y dos vanos; el tamaño del espacio de diseño (17 variables) y las 8 horas de cómputo sugieren que el escalamiento a edificios reales no está resuelto.

**Puntos oscuros aclarados.** El texto afirma que reducir columnas o acero no reduce necesariamente la seguridad, y sus pruebas lo respaldan, pero la razón es que la Prueba 3, con 10 columnas a 150 mm, falla por la ubicación (ξμ = 0,931) mientras la Prueba 5, con 10 columnas a 250 mm, cumple. El mecanismo es la protección de las columnas que más gravedad portan (centrales y del eje 2-8), no la cantidad de refuerzo. La relación costo-seguridad no es monótona porque el modo de falla gobernante es el colapso de la columna central por pérdida de capacidad axial y de ductilidad. Esta explicación, sugerida por los autores al comentar las columnas 2 y 8, indica que la optimización converge a un patrón físico reconocible, y que un criterio de diseño por capacidad podría obtenerlo sin algoritmo genético. La evidencia faltante es una comparación contra ese criterio simple, aplicada al mismo edificio y con el mismo modelo de costos.

**Ideas propositivas novedosas.**

1. Función objetivo con pérdida de actividad económica: añadir al costo de obra un término de interrupción proporcional al número de columnas intervenidas, a la superficie afectada y a los ingresos por día de la actividad alojada, más el costo esperado de interrupción tras el sismo derivado de curvas de fragilidad. Fundamento: el propio artículo identifica el tiempo fuera de servicio como motivación y las tablas muestran que el costo fijo por columna domina. Verificabilidad: aplicar el marco a edificios con locales comerciales o industriales y comparar la configuración óptima con y sin el término. Utilidad: vincula el reforzamiento con la resiliencia empresarial y orienta incentivos públicos para pymes ubicadas en edificaciones antiguas de zonas sísmicas.
2. Optimización con restricción de confiabilidad: reemplazar ξμ ≥ 1 por una restricción de probabilidad máxima de falla estimada con muestreo (concreto, acero, relleno y espectro) y reportar el costo del margen de seguridad. Fundamento: los óptimos encontrados están al 1-1,5 % de la frontera. Verificabilidad: simulaciones de Monte Carlo con los mismos modelos de OpenSees y comparación del costo entre diseño determinista y confiable. Utilidad: evita optimizar hacia diseños frágiles y permite negociar el nivel de riesgo aceptable con aseguradoras y propietarios, además de justificar tarifas de seguro diferenciadas según el margen de seguridad adoptado.

**Relaciones poco exploradas.**

1. Razón de costos fijo/variable (demolición por columna frente a acero por kilogramo) (determina) la topología óptima: si el costo fijo crece, el óptimo reduce columnas; si baja, optimiza el espaciamiento. Merece un análisis de sensibilidad paramétrico.
2. Excentricidad entre centro de rigidez y de masa inducida por mampostería (determina) las columnas que se refuerzan (6 y 9 del lado opuesto) por demanda torsional: relación poco explorada entre índice de irregularidad en planta y patrón óptimo de refuerzo.

**Robustez argumentativa:** 5.8/10 (ponderación 30/30/25/15) — consistencia lógica 7/10; calidad de la evidencia 6/10; validez de inferencias causales 5/10; generalizabilidad 4/10.

**Valor estratégico:** 5/10 — El artículo aporta un procedimiento replicable de optimización del reforzamiento, con datos económicos explícitos y un resultado claro de que la posición supera a la cantidad. Su valor para el eje del corpus es moderado, porque conecta la mitigación estructural con costos pero no con la continuidad de la actividad productiva; sirve como base cuantitativa para integrar interrupción empresarial en decisiones de adaptación.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Hombre de paja (Comparación del 40 % contra la 'prueba 5' creada por los autores (Sec. 5.2, p. 10)); Generalización apresurada (Dos pórticos regular e irregular de 5 niveles y 2 vanos se proyectan a 'larger RC structures' (Sec. 7, p. 14)); Falsa dicotomía (Se presenta costo frente a seguridad sin considerar el costo de interrupción como tercer criterio (Resumen, p. 1))
- **Bradford-Hill:** Aplica solo a relaciones mecánicas: ubicación de refuerzo y ductilidad muestran plausibilidad y coherencia con mecánica estructural; faltan experimento propio, replicación y análisis de sensibilidad para consistencia y fuerza.
- **TRL asignado:** 4 — 'The procedure was tested on a 5-storey 2-bays reinforced concrete structure' (p. 14)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto con ecuaciones fragmentadas por la extracción, pero tablas y resultados legibles. La lista de referencias quedó intercalada en el cuerpo (columna) y no afecta el análisis.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un algoritmo genético acoplado a un modelo de fibras puede encontrar configuraciones de reforzamiento con camisas de acero que cumplen la seguridad exigida con un costo 40 % menor que las soluciones heurísticas de ingeniería, incluso en estructuras con irregularidades.  | El óptimo se ubica en el borde de la restricción (ξμ de 1,010 a 1,015), de modo que no queda margen frente a la variabilidad de materiales, del modelo de mampostería o de la acción sísmica; una restricción determinista de capacidad igual a demanda para un único periodo de retorno equivale, en términos de confiabilidad, a una probabilidad de falla cercana a la incertidumbre del modelo. Además, el objetivo es dominado por un costo fijo por columna (2.000 EUR frente a unos 717 EUR de acero), por lo que el algoritmo esencialmente minimiza el número de columnas y casi no optimiza el espaciamiento. La referencia de comparación es una configuración preliminar elaborada por los propios autores, no una práctica de diseño documentada, y el tiempo fuera de servicio, que motiva el estudio, no forma parte de la función objetivo.  | El artículo demuestra que el desempeño sísmico puede traducirse en una restricción computable dentro de un lazo de optimización, y que la ubicación de los refuerzos importa más que su cantidad. Para que el hallazgo sea utilizable en decisiones de recuperación productiva, debe extenderse con restricciones probabilistas, con márgenes de seguridad explícitos y con un término de pérdida de actividad económica durante la obra y tras el sismo. Así, el marco pasa de minimizar el costo de obra a minimizar el costo esperado del ciclo de vida de la edificación y de las empresas que la ocupan, lo que alinea la ingeniería estructural con los objetivos de continuidad de actividad.  | 5.8/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Seguridad' se define como ξμ = μc/μd ≥ 1 en el método N2; 'costo' como mano de obra, material y un monto fijo por columna; 'óptimo' como el mínimo de F = C + penalización.
- **P2 Supuestos:** Supone espaciamiento uniforme de pletinas, perfil de carga uniforme, simetría polar para extender resultados, ausencia de falla por cortante y un modelo de confinamiento uniforme en la sección; supone también que el costo fijo de 2.000 EUR por columna es independiente del contexto.
- **P3 Evidencia:** La evidencia es numérica (OpenSees) sin validación experimental propia en el artículo; el modelo de camisas se apoya en ensayos previos (Campione et al., 2017).
- **P4 Consecuencias:** Si es cierto, proyectistas pueden reducir cerca de 40 % el costo directo manteniendo la seguridad; si el margen es insuficiente, las estructuras optimizadas quedarían sin reserva ante variabilidad real.
- **P5 Contraejemplos:** Estructuras con falla por cortante o con nudos débiles, o con irregularidades mayores que la mampostería en un pórtico, pueden invalidar el patrón encontrado.
- **P6 Alternativas:** Alternativas: diseño por capacidad con criterios de jerarquía, optimización multiobjetivo con tiempo fuera de servicio, otras técnicas (FRP, disipadores, arriostramientos) y optimización bajo incertidumbre.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Razón ξμ de la estructura sin refuerzo (regular) | 0.792 | adimensional | Prueba 1, as-built | Tabla 3, p. 10 | Tabla | Alta | Un solo perfil de carga |
| Costo del refuerzo total (18 columnas, sb=150 mm) | 51578.33 | EUR | Prueba 2 | Tabla 3, p. 10 | Tabla | Alta | Modelo de costo simplificado |
| Costo de la prueba 5 (10 columnas, sb=250 mm) | 27170.98 | EUR | Mejor solución preliminar | Tabla 3, p. 10 | Tabla | Alta | Línea base elegida por los autores |
| Razón ξμ de la prueba 5 | 1.030 | adimensional | Mejor solución preliminar | Tabla 3, p. 10 | Tabla | Alta | Sin margen explícito |
| Costo óptimo una dirección (4 columnas) | 10868.39 | EUR | Dirección Z+, sb=250 mm | Tabla 4, p. 10 | Tabla | Alta | Simplificación por simetría |
| Costo óptimo todas las direcciones (6 columnas) | 16302.59 | EUR | Diseño final regular | Tabla 4, p. 10 | Tabla | Alta | Extendido por simetría y no reoptimizado |
| Razón ξμ final regular | 1.010 | adimensional | Todas las direcciones | Tabla 4, p. 10 | Tabla | Alta | Margen de 1 % |
| Reducción de costo frente a prueba 5 | 40 | % | Diseño final frente a mejor solución preliminar | Sec. 5.2, p. 10 | Texto | Media | La línea base es heurística de los autores |
| Diferencia de ξμ frente a prueba 5 | 2 | % | 1,01 frente a 1,03 | Sec. 5.2, p. 10 | Texto | Alta | Sin análisis de incertidumbre |
| Evaluaciones hasta estabilizar el óptimo | 870 | evaluaciones | Convergencia del AG, caso regular | Sec. 5.2, p. 9 | Texto | Alta | Una sola corrida reportada |
| Iteración del óptimo (una dirección) | 821 | iteración | Caso regular | Sec. 5.2, p. 9 | Texto | Alta | Sin repeticiones con semillas distintas |
| Tiempo de pushover por individuo | 0.5 | min | Costo computacional | Sec. 5.2, p. 10 | Texto | Alta | Modelo simple de pórtico |
| Tiempo total de optimización | 8 | horas | Caso regular | Sec. 5.2, p. 10 | Texto | Alta | Escalamiento no analizado |
| Razón ξμ sin refuerzo con mampostería (dirección Z) | 0.535 | adimensional | Pórtico irregular as-built | Sec. 6, p. 11 | Texto | Alta | Modelo de puntal equivalente |
| Costo final con mampostería (todas las direcciones) | 16302.59 | EUR | Misma suma que el caso regular | Tabla 6, p. 12 | Tabla | Alta | Coincidencia con el caso regular |
| Costo fijo por columna / costo del acero | 2000 / 4.5 | EUR/columna; EUR/kg | Parámetros del modelo de costo | Sec. 3.6, p. 6 | Texto | Alta | Valores supuestos, sin fuente de mercado citada |
| Periodo de retorno y vida nominal | 975; 100 | años | Acción sísmica de diseño en Cosenza, suelo C | Sec. 4, p. 7 | Texto | Alta | Un solo nivel de peligro |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'The procedure was tested on a 5-storey 2-bays reinforced concrete structure' (p. 14) | Marco de software validado en entorno de laboratorio computacional con casos sintéticos; sin edificio real ni herramienta liberada (TRL 4 NASA). |
| MRL | N/A | No | No aplica | Los costos remiten a ejecución de obra y no a procesos de manufactura. |
| BRL | 2 | Sí | 'cost of each solution... fixed amount (cm) of 2000 € per reinforced column' (p. 6) | Existe un análisis preliminar de costos unitarios pero sin mercado, clientes ni modelo de negocio. |
| IRL | 4 | Sí | 'automatically interfaced with the 3D model of the building realized in OpenSees' (p. 2) | Integración demostrada entre Matlab AG y OpenSees en entorno de laboratorio. |
| DRL | N/A | No | No aplica |  |
| SRL | 3.33 | Sí | Componentes: Modelo de fibras OpenSees con método N2 (TRL 6), Optimizador genético Matlab (TRL 9) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 30.0; ÷9 → 3.33; nivel acotado a [1,9] = 3.33 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | N/A | N/A |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Baja · TRL 4 con BRL 2: herramienta sin ruta de adopción, sin colaboración con firmas de ingeniería y sin validación en edificio real. · Estrategia de salida: Validar con un edificio existente, liberar el código y comparar contra práctica de diseño documentada.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Hombre de paja | Comparación del 40 % contra la 'prueba 5' creada por los autores (Sec. 5.2, p. 10) | Sobrestima la mejora frente a la práctica profesional |
| Generalización apresurada | Dos pórticos regular e irregular de 5 niveles y 2 vanos se proyectan a 'larger RC structures' (Sec. 7, p. 14) | Limita la validez externa |
| Falsa dicotomía | Se presenta costo frente a seguridad sin considerar el costo de interrupción como tercer criterio (Resumen, p. 1) | Deja fuera una dimensión relevante para la recuperación productiva |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Posición de columnas reforzadas → ratio ξμ | Pruebas 1-5 y óptimos | Plausibilidad, gradiente, coherencia, temporalidad | Experimento, consistencia, especificidad | Modelo de nudo omitido; perfil de carga único | 6 | Causal (mecánica simulada) |
| Espaciamiento de pletinas → costo | Función de costo explícita | Especificidad, plausibilidad | Experimento | Costo fijo dominante | 7 | Causal (aritmética del modelo) |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Tecnológico | Incorporar tiempo fuera de servicio y pérdida de ingresos como objetivos junto con el costo de obra | Crítico | Alta | 9 |
| Metodológico | Optimización bajo incertidumbre con restricción de confiabilidad | Significativo | Media | 8 |
| Conocimiento | Validación contra edificios reales y contra criterios de diseño por capacidad | Significativo | Media | 7 |
| Mercado | Sin datos de adopción por propietarios ni de costos de mercado latinoamericanos | Moderado | Media | 5 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Column steel-jacketing arrangements | Esquema | Cajas con y sin conexión resistente a momento | No aplica | Media |
| Fig. 5 | Flowchart of the optimization process | Diagrama | Lazo de AG con OpenSees y verificación pushover | No aplica | Alta |
| Fig. 8 | Penalty function | Gráfico | Penalización cúbica en función de 1/ξ | No aplica | Media |
| Fig. 9 | Case study structure | Esquema | Pórtico de 5 niveles y 2 vanos con simetría polar | No aplica | Media |
| Fig. 16 | Convergence history of the cost | Gráfico | Convergencia del costo tras unas 870 evaluaciones | No tabulados | Alta |
| Fig. 17 | History of the capacity/demand ratio | Gráfico | ξμ promedio factible tras 600 iteraciones y cercano a 1 | No tabulados | Media |
| Tabla 3 | Results of preliminary tests | Tabla | Cinco pruebas con ξμ, sb, nc y costo | ξμ 0,792-1,722; costo 27.170,98-51.578,33 EUR | Alta |
| Tabla 4 | Results of the optimization | Tabla | Óptimo una dirección y todas las direcciones | 10.868,39 y 16.302,59 EUR | Alta |
| Tabla 6 | Results for the infilled frame | Tabla | Óptimo con mampostería | 13.585,49 y 16.302,59 EUR | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Optimización de chaquetas FRP (Chisari y Bedon, 2016) | No especificado en documento | Grupo de investigación | FRP | Menor peso añadido | Costo y durabilidad del material | Creciendo |
| Optimización de amortiguadores viscosos (Pollini et al., 2017) | No especificado en documento | Grupo de investigación | Disipación pasiva | Reduce demanda sin modificar la columna | Requiere elementos de soporte | Estable |
| Optimización de arriostramientos disipativos (Braga et al., 2019) | Italia | Grupo de investigación | Contravientos | Control de costo de intervención | Intrusivo en fachadas | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Costo directo de reforzamiento (EUR) sujeto a ξμ ≥ 1
- **X:** Número y posición de columnas reforzadas; espaciamiento de pletinas
- **Z (controles):** Geometría y materiales del pórtico, peligro sísmico (TR = 975 años), costos unitarios
- **Datos:** Dos modelos numéricos sintéticos (corte transversal); sin datos de campo
- **Método:** Algoritmo genético + pushover N2 + función de penalización
- **Efecto reportado:** Reducción de 40 % del costo frente a la prueba 5 con ξμ de 1,01
- **Endogeneidad tratada:** No - es un problema de optimización, no de inferencia causal
- **Instrumento:** No aplica
- **Robustez reportada:** Caso con mampostería irregular; sin sensibilidad a parámetros de costo

| Vacío | Tipo | Descripción |
|---|---|---|
| V-002-01 | TERR | Sin aplicación a edificios de América Latina ni a regiones con normativas distintas del Eurocódigo 8 |
| V-002-02 | POBL | No se considera el tipo de ocupación (comercial, industrial) ni su vulnerabilidad económica |
| V-002-03 | MET | Falta optimización multiobjetivo, bajo incertidumbre y con criterios alternativos de diseño por capacidad |
| V-002-04 | VAR | Ausencia de variables de interrupción de uso, ingresos perdidos y emisiones |
| V-002-05 | TEOR | No se vincula con teoría de resiliencia comunitaria o empresarial |
| V-002-06 | CAUS | No se estima efecto causal del reforzamiento sobre pérdidas reales ni sobre recuperación |
