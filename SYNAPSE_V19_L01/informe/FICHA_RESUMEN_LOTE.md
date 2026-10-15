# FICHA_RESUMEN_LOTE — L01

`MODE=COMPUTE FILES=TRUE BATCH=L01 DOCS=101 STATUS=COMPLETE`

## 1. Identificación del lote
Lote L01 de SYNAPSE V19.0; repositorio `TejidoEmpresarial`; rama `claude/tejido-empresarial-synapse-rf1qle`; fecha de cierre 2026-10-15. Tema: tecnología, transferencia, gemelos digitales e IoT para la recuperación productiva y la resiliencia empresarial tras sismos.

## 2. Alcance y criterios de inclusión
Se incluyeron todos los documentos del repositorio: 103 archivos PDF, de los cuales 101 son únicos (dos duplicados por MD5). Sin filtro por relevancia; la relevancia se asigna después (núcleo, adyacente, periférico, ajeno).

## 3. Inventario y composición
Scopus 86 (D001–D086), SciELO 12 (D087–D098), Web of Science 1 (D099), síntesis de buscadores 2 (D100–D101). Idioma: 87 en inglés y 12 en español (dos sin dato). Años: 66 documentos de 2024 a 2026 y 12 de 2008.

## 4. Calidad de extracción
Texto completo de todos los documentos. Defectos documentados: tablas desalineadas (SciELO y otros), líneas duplicadas por dos columnas (D099), y recorte de listas de referencias en el texto limpio. Ninguna cifra se infirió de tablas ilegibles.

## 5. Distribución de relevancia
Núcleo 17; adyacente 50; periférico 23; ajeno 11. Recomendación: aceptar con reservas 91; rechazar como evidencia (usar solo como hipótesis) 10.

## 6. Madurez multinivel
Mediana TRL 4 (n = 84; 55 con TRL ≤ 4); BRL 2 (n = 83); IRL 3 (n = 80); DRL 3 (n = 77). MRL no aplica en prácticamente todo el lote (sin manufactura). SRL estimado en 79 documentos con la fórmula del analista.

## 7. Brechas y valles de la muerte
V1 66; V3 8; V2 7; V4 3; sin valle 17. Brecha dominante: tecnología e integración por delante del negocio y de la evidencia en operación real.

## 8. Síntesis dialéctica del lote
*Tesis.* Los gemelos digitales, el IoT y la inteligencia en el borde pueden acelerar la detección, la evaluación de daño y la coordinación tras un sismo, y mejorar la resiliencia organizacional. *Antítesis.* La evidencia es de laboratorio, simulación, encuesta transversal o caso único; no mide tiempo de reanudación, ingresos ni empleo de empresas; y la evidencia de recuperación empresarial está desconectada de la tecnológica. *Síntesis.* La tecnología es una condición necesaria para reducir las demoras de detección y evaluación, pero su efecto sobre la recuperación productiva es una hipótesis cuya prueba exige integrar los modelos de recuperación con los datos de los gemelos y evaluar la transferencia con empresas.

## 9. KPIs agregados
Se extrajeron 959 indicadores. Cifras de referencia del lote: 101 documentos; 362 relaciones tipificadas; 472,600 palabras en fichas; k-means con 101 documentos k = 2 (silueta 0.23) y sin SciELO k = 3 (silueta 0.06); 2962 citas Scopus en 86 documentos con dato.

## 10. Triangulación
- T01: El procesamiento en el nodo o en el borde reduce la latencia de alerta y actualización frente a arquitecturas centralizadas — **Triangulado con reservas** (6 documentos, 4 grupos independientes).
- T02: La interoperabilidad y la calidad de datos son la barrera técnica principal de los gemelos digitales y del IoT en desastres — **Triangulado** (10 documentos, 10 grupos independientes).
- T03: Los gemelos digitales y el IoT mejoran la resiliencia organizacional y la eficiencia operativa — **En tensión** (6 documentos, 6 grupos independientes).
- T04: El tiempo de reparación del edificio no basta como medida de recuperación empresarial; deben modelarse demoras e inactividad por tipo — **Triangulado con reservas** (5 documentos, 4 grupos independientes).
- T05: Incluir pérdidas indirectas y recuperación cambia la decisión de refuerzo sísmico — **Parcial** (3 documentos, 3 grupos independientes).
- T06: Los gemelos digitales urbanos estiman daño y necesidades de respuesta en escenarios sísmicos — **Parcial** (6 documentos, 5 grupos independientes).
- T07: Las revisiones de gemelos digitales concluyen potencial alto con implementación incipiente — **Triangulado** (7 documentos, 7 grupos independientes).
- T08: Los efectos digitales sobre la resiliencia de cadenas de suministro son mayores en preparación y respuesta que en recuperación — **Parcial** (3 documentos, 3 grupos independientes).
- T09: Los costos bajos del monitoreo estructural con IoT se demuestran solo en laboratorio o en estructuras individuales — **Triangulado** (5 documentos, 4 grupos independientes).
- T10: El orden de desempeño entre algoritmos de aprendizaje automático para alerta sísmica no es transferible entre estudios — **En tensión** (3 documentos, 3 grupos independientes).
- T11: UAV e IoT permiten restablecer comunicaciones y acelerar la evaluación de daños — **Parcial** (5 documentos, 5 grupos independientes).
- T12: La adopción del IoT y del gemelo digital depende de liderazgo, habilidades y aceptación de las partes interesadas — **Triangulado con reservas** (6 documentos, 6 grupos independientes).
- T13: La prefabricación y la robótica contribuyen a la recuperación posdesastre — **Fuente única** (1 documentos, 1 grupos independientes).
- T14: La transferencia tecnológica como mecanismo tiene evidencia empírica en recuperación posterremoto — **Sin evidencia primaria** (2 documentos, 2 grupos independientes).

## 11. Patrones y tensiones
- P01 (patrón): Madurez tecnológica baja y homogénea: la mediana de TRL es 4 en 84 documentos técnicos con TRL asignado (55 con TRL ≤ 4, 65 %); la mediana de BRL es 2 y la de IRL es 3.
- P02 (patrón): BRL ≤ 2 en 62 de 83 documentos con BRL asignado (75 %): casi ningún estudio presenta costos, modelos de negocio o análisis de adopción empresarial.
- P09 (tensión): Resiliencia organizacional como mediador lineal (D030) frente a propiedad emergente (D082).
- P10 (tensión): Orden de desempeño de algoritmos de alerta sísmica contradictorio entre estudios (XGBoost mejor en D060; red neuronal mejor que XGBoost en D041).
- P13 (anomalía): La síntesis D100 incluye como referencias a los 86 documentos D001-D086 (86 de 93 referencias); el corpus Scopus del lote coincide con su lista.
- P14 (anomalía): D100 declara alcance 2020-2024 pero 49 de 93 referencias son de 2025-2026 y hay referencias de 2013 y 2015.
- P16 (patrón): Ausencia explícita de métricas de recuperación o continuidad empresarial en 32 de 87 documentos técnicos (el vacío VAR lo declara de forma explícita).
- P19 (tensión): Mayor robustez argumentativa en los documentos ajenos al tema (media 3,84 de 10 en el bloque SciELO frente a 3,19 en núcleo y 3,13 en adyacentes).

## 12. Competidores y actores
Los competidores registrados (`csv/competidores.csv`) son enfoques alternativos y grupos de investigación citados en los documentos: sistemas centralizados frente a descentralizados de alerta, métodos clásicos frente a aprendizaje automático, ecuaciones de refuerzo y herramientas comerciales, y los dos asistentes de IA (Scopus AI y Web of Science Research Assistant). No hay competidores de mercado empresarial documentados con cuota o precio.

## 13. Variables econométricas y vacíos
Los estudios con modelos estructurales (D029, D030, D052, D085) usan percepciones como variable dependiente; los demás reportan resultados técnicos. Vacíos más frecuentes: territorial (sin América Latina en 33 de 87 documentos técnicos), de variables (sin métricas de recuperación en al menos 32) y causal (sin identificación). Total de vacíos registrados: 694.

## 14. ML/NLP y sensibilidad
TF-IDF (unigramas y bigramas), k-means, Ward, DBSCAN, LDA (6 temas), PCA, t-SNE, redes de co-palabras y de coautoría. Con SciELO la estructura se reduce a dos bloques (idioma y dominio); sin SciELO, la silueta es 0.06 (difusa). ARI entre particiones con y sin SciELO a k = 3: 0.58. Los resultados descriptivos de madurez no dependen del bloque SciELO.

## 15. Riesgos y premortem
Riesgos principales: usar proxies técnicos como beneficio empresarial; usar D100 o D101 como evidencia; extrapolar evidencia organizacional no sísmica; sobreponderar la cantidad de revisiones; ignorar la dependencia de pocos grupos de autores. Contingencia: pilotos con métricas de recuperación, ponderación por grupo de autoría y verificación contra las fuentes.

## 16. Recomendaciones, valor estratégico y próximos pasos
1. Conectar los parámetros de los gemelos digitales con los componentes de demora de los modelos de recuperación (proposición P-E1).
2. Diseñar un estudio empírico de transferencia tecnológica con empresas afectadas por sismos, con capacidad de absorción como moderador (P-E5).
3. Usar D100 y D101 solo como mapas de búsqueda y registrar una búsqueda propia con doble revisión.
4. Ponderar la evidencia por grupo de autoría y exigir intervalos de confianza y validación externa.
5. Ampliar el módulo de patentes: 11 patentes analizadas con lectura parcial (`patentes/`); faltan lectura completa, estado legal y búsqueda sistemática.

**Valor estratégico.** Fija qué evidencia puede sustentar decisiones de inversión y cuál es una hipótesis, y señala el vacío central del corpus.

**¿Qué se me escapa?** Lectura completa y estado legal de las 11 patentes, búsqueda sistemática de patentes, registros de Scopus sin PDF y siete referencias de D100 fuera del lote, literatura regional en español, datos empresariales de cierre e ingresos, y una verificación entre revisores de los juicios de madurez.

**Documentos núcleo de mayor valor estratégico:** D011 (8/10); D053 (8/10); D081 (8/10); D004 (7/10); D005 (7/10); D013 (7/10); D048 (7/10); D064 (7/10).

**Prioridades de brecha:** D101: Falta de evidencia sobre empresas y transferencia tecnológica en recuperación posterior a  (prioridad 9); D016: Literatura de IoT en cadena de suministro orientada a interrupciones, desastres naturales  (prioridad 9); D084: Repeticiones, sensibilidad a daño incipiente, falsos positivos y efectos ambientales (prioridad 9); D083: Resiliencia operativa del IoT industrial ante interrupciones y dimensión social con datos (prioridad 9); D082: Pruebas longitudinales y cuantitativas de configuraciones y revisión sin umbral de citació (prioridad 9); D082: Resiliencia de pymes durante y después de desastres físicos, con medición de la recuperaci (prioridad 9); D017: Evidencia empírica de efecto del IoT sobre resiliencia y recuperación ante desastres natur (prioridad 9); D078: Interrupción empresarial, cadenas de suministro y recuperación económica en la plataforma (prioridad 9)

---
Archivos: `informe/informe_lote.md`, `informe/analisis_relacional.md`, `informe/bibliografia_APA.md`, `informe/tabla_control.md`, `informe/checklist_validacion.md`, `informe/diagramas_mermaid.md`, `csv/`, `figuras/`, `fichas/`.
