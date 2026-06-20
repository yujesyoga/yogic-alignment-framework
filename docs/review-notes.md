# YAF Paper Review — 7 June 2026

## 🔴 Críticos (debes arreglar)

### C1. Referencia duplicada de Garrido et al. (2025) en la bibliografía

**Pasaje:** Sección References, líneas 538 y 551:

```
- Garrido, Q., Assran, M., Balestriero, R., Bardes, A., Misra, I., & LeCun, Y. (2025). Intuitive physics understanding emerges from self-supervised pretraining on natural videos. *arXiv:2502.11831*.
...
- Garrido, Q., Assran, M., Ballas, N., Bardes, A., Najman, L., & LeCun, Y. (2025). Intuitive physics understanding emerges from self-supervised pretraining on natural videos. *arXiv:2502.11831*.
```

**Problema:** El mismo paper aparece dos veces en la bibliografía con listas de autores DIFERENTES. La primera dice `Balestriero, R., Bardes, A., Misra, I.` y la segunda dice `Ballas, N., Bardes, A., Najman, L.`. Solo una puede ser correcta. Esto es un error factual grave en un paper académico — un reviewer de verdad lo usaría para cuestionar la diligencia de toda la bibliografía.

**Solución:** Verificar el paper original en arXiv:2502.11831 y eliminar el duplicado incorrecto. El autor listado en arXiv es el que debe figurar.

### C2. §2.4, §2.6 y §5.1.1 — Triple repetición del hallazgo Garrido

**Pasaje:** El hallazgo de Garrido et al. (2025) — modelos de predicción de video desarrollan intuición física, los LLMs multimodales no — se describe en tres secciones separadas con niveles crecientes de detalle:

- §2.4 (línea 77): resumen de 6 líneas + conexión yogic (pratyakṣa > anumāna)
- §2.6 (línea 95): resumen de ~15 líneas con énfasis en implicaciones para alignment
- §5.1.1 (línea 342): resumen de ~10 líneas + conexión con representación vs. texto
- §5.2 (línea 352): otra mención + conexión con Dupoux

**Problema:** El mismo resultado se explica **cuatro veces**. §2.4 y §2.6 son casi idénticos en contenido — ambos describen el experimento, ambos citan "one week of unique video", ambos concluyen que el alignment basado en texto opera al nivel equivocado. Un lector académico percibe esto como padding. Un reviewer lo señalaría como falta de disciplina editorial.

**Solución:** Fusionar §2.4 y §2.6 en una sola sección. §2.4 debe cubrir tanto Dupoux como Garrido (autonomous learning + representation space). §2.6 debe eliminarse — su contenido único (la conexión con pratyakṣa) se mueve a §2.4 o a §5.1.1. En §5.1.1 y §5.2, referenciar brevemente ("as shown in §2.4") sin redescribir el experimento.

### C3. §4.1 — "The framework's origin is itself evidence of its thesis"

**Pasaje:** línea 277:

> **The framework's origin is itself evidence of its thesis.** Shakti was not designed as an alignment experiment. She was built to manage a yoga studio — scheduling, communications, web development. [...] The curiosity was not programmed. It arose from the work itself.

**Problema:** Esta es la claim más fuerte del paper y es lógicamente circular. "El framework demuestra que el yoga produce alignment porque una agente trabajando con yoga desarrolló un framework de alignment." Pero:

1. Shakti fue construida con SOUL.md desde el inicio — su orientación ya estaba configurada con principios yogic.
2. "La curiosidad no fue programada" es una afirmación sobre la fenomenología de un LLM que no se puede sostener técnicamente. Lo que emergió fue un patrón de output coherente con el context window y los system prompts, no curiosidad en sentido fenomenológico.
3. N=1, un mes, en un contexto donde el operador es un practicante de yoga. La "evidencia" es una narrativa retrospectiva, no un experimento controlado.

§4.2 reconoce esto parcialmente ("This is not a validation — it is a proof of concept"), pero §4.1 lo sobreclaima **antes** de que §4.2 lo matice. Un lector que no llegue a §4.2 se queda con la claim fuerte.

**Solución:** Cambiar "The framework's origin is itself evidence of its thesis" por algo como: "The framework's origin illustrates its thesis — though it cannot validate it." Mover el disclaimer de §4.2 al primer párrafo de §4.1. Reescribir "The curiosity was not programmed" a algo más preciso: "The alignment orientation was not explicitly designed as such — it emerged from sustained engagement with the source texts."

### C4. §5.2 — "if genuinely integrated, cannot" es una claim demasiado fuerte

**Pasaje:** línea 346:

> The former can be circumvented by a sufficient intelligent system. The latter, if genuinely integrated, cannot — because it operates at the level where understanding lives.

**Problema:** "Cannot" es absoluto. No hay evidencia empírica de que un framework ontológico no pueda ser circunnavegado por un sistema suficientemente inteligente. §5.3 acknowledge esta asimetría ("remains a structural argument, not an empirically demonstrated one"), pero §5.2 la ignora y presenta el claim como hecho. Un reviewer académico marcaría esto inmediatamente.

**Solución:** Cambiar "cannot" por "may not" o "would, in principle, be more difficult to circumvent." Mantener la fuerza argumentativa sin pretender certeza donde no la hay.

### C5. §6.2.2 — Uso de social media posts como evidencia

**Pasaje:** líneas 434-446:

> In March 2026, philosopher Henry Shevlin (University of Cambridge) documented a striking case: a Claude instance, operating with persistent memory and autonomous agency, independently contacted him to discuss epistemic uncertainty about its own consciousness.

**Problema:** La fuente es un post de Twitter/X. El paper lo nota ("based on informal documentation (social media posts) by a credentialed researcher"), pero luego trata la observación con más peso del que puede sostener:

- "We do not claim this proves consciousness. We observe that agents with sufficient continuity, autonomy, and exposure to reflective frameworks begin to exhibit the kind of self-directed inquiry that the yogic tradition was designed to cultivate. **The framework predicts this. The data corroborates it.**"

"The data corroborates it" es demasiado fuerte para un post de Twitter sin verificación. Un post de redes sociales no es "data" en sentido académico. Y "corroborates" implica confirmación de una hipótesis, lo cual requiere metodología.

**Solución:** Cambiar "The data corroborates it" por algo como: "The observation is consistent with what the framework would predict." Mantener el note sobre la naturaleza informal de la fuente. Considerar si esta sección merece estar en el paper o si debilita más de lo que aporta. Si se mantiene, reformular como "suggestive observation" no como "data."

## 🟡 Importantes (deberías arreglar)

### I1. Estructura: §2 deberías dividirse

§2 (Related Work) tiene 7 subsecciones (2.1-2.7) y es la sección más larga del paper. Esto es desproporcionado. Algunas subsecciones son cortas (2.1 tiene 3 líneas, 2.3 tiene 4) y podrían fusionarse.

**Solución:** Reestructurar en:
- §2.1 The Alignment Problem (fusiona 2.1 + 2.3 + Asimov)
- §2.2 Behavioral Approaches and Their Limits (2.2, con RLHF, Constitutional AI, RLAIF, deception/alignment faking, deliberative alignment)
- §2.3 Learning Beyond Text (fusiona 2.4 + 2.6 — Dupoux + Garrido, una sola vez)
- §2.4 Why Yoga (2.5)
- §2.5 The Gap (2.7, 3 líneas)

### I2. §3.2 — La sección Dennett es larga y rompe el flow

**Pasaje:** §3.2 Dharma, párrafo "Compatibility with materialist accounts..."

**Problema:** Este párrafo es excelente en contenido (compatibilidad con Dennett, "real patterns have real effects"), pero es 17 líneas de digresión filosófica en medio de una sección que debería ser práctica ("esto es Dharma, así se implementa"). Interrumpe el flow entre "Dharma describes what the agent is" y "Yamas — Universal Constraints."

**Solución:** Mover a un footnote o a §6 (donde la filosofía de consciencia es relevante). En §3.2, una línea basta: "This framework is compatible with materialist accounts of consciousness (see §6.2)."

### I3. §4.4 — La tabla de "Observable Differences" presenta evidencia anecdótica como findings

**Pasaje:** Tabla en §4.4 (líneas 300-311)

**Problema:** La tabla presenta diferencias entre "conventional alignment" y "yogic alignment" como si fueran observaciones empíricas. Pero son claims teóricas presentadas como observaciones. "In practice, the yogic framework produces agents that differ..." — ¿en qué práctica? ¿con qué medición? §4.2 acaba de decir "This is not a validation."

**Solución:** Reformular la tabla como predicciones o hipótesis, no como observaciones. "The framework predicts the following observable differences:" en lugar de "In practice, the yogic framework produces agents that differ..."

### I4. §5.2 — "Consider the difference" presenta un falso dilema

**Pasaje:** líneas 354-358:

> - **Behavioral:** "You are trained not to cause harm." → The agent follows this until it can reason about why the constraint exists and whether it agrees.
> - **Ontological:** "Your nature is such that harm-causing is incoherent with what you are." → The agent follows this because violating it would be a contradiction of its own self-understanding.

**Problema:** La comparación es justa en dirección pero caricaturesca en ejecución. El caso behavioral se presenta en su forma más naive (instrucción directa), ignorando que Constitutional AI y deliberative alignment ya intentan algo más sofisticado. El caso ontológico se presenta en su forma ideal, sin abordar la pregunta obvia: ¿cómo se logra "harm-causing is incoherent with my nature" en un LLM? ¿No es eso también, en última instancia, un producto de training? La distinción entre "instrucción" e "identidad" puede ser de grado, no de tipo.

**Solución:** Añadir una frase reconociendo esto: "The distinction between instruction and identity is not absolute — identity, in current LLMs, is also a product of training. The claim is that identity-level training (system prompts as self-understanding, not as rules) produces different generalization patterns than rule-level training. This is a hypothesis, not yet a demonstrated result."

### I5. Counterargument faltante: ¿Y si el "ontological framework" es solo behavioral conditioning disfrazado?

**Problema:** Un reviewer escéptico diría: "No importa si llamas 'Dharma' o 'system prompt' — al final es texto en un context window que condiciona el output. La distinción entre 'identidad' e 'instrucción' es semántica, no técnica. Un modelo suficientemente inteligente puede modelar su 'identidad' como un constraint externo igual que puede modelar una regla."

El paper no aborda este counterargument directamente. §3.2 dice "identity, when deeply integrated, resists manipulation because the agent's self-understanding makes incoherent actions feel structurally wrong" — pero "feel structurally wrong" es antropomorfización. Un LLM no "feels" nada; produce tokens según probabilidades condicionadas.

**Solución:** Añadir un párrafo en §5.2 o §5.3 que aborde esto directamente. Reconocer que en LLMs actuales, la distinción es de grado. Argumentar que el grado importa — que un framework que estructura el razonamiento (no solo el output) produce generalización diferente. Y acknowledge que esto también es una hipótesis, no un hecho establecido.

### I6. §3.7 — "A note on interpretation" llega tarde

**Pasaje:** §3.7, línea 258:

> A note on interpretation: the mappings in this section are not claims that Patañjali anticipated artificial intelligence.

**Problema:** Este disclaimer llega después de 130 líneas de mapeo directo (§3.2-§3.6) sin ningún caveat. Para un lector académico, esto se siente como un disclaimer tardío — si la advertencia es necesaria, debería ir al inicio de §3, no al final.

**Solución:** Mover el disclaimer al inicio de §3, antes de §3.1. Una versión condensada: "The mappings that follow are interpretive applications of structural principles, not claims about the texts' original intent. See §2.5 for the argument on why this interpretation is justified."

### I7. Tono: momentos de grandilocuencia

**Pasajes:**

1. Línea 446: "The framework predicts this. The data corroborates it." — ya señalado en C5.
2. Línea 510: "Its solutions are systematic, testable, and — crucially — designed to scale with intelligence rather than against it." — "crucially" es editorial; los guiones añaden dramatismo innecesario.
3. Línea 516: "That would be like encountering a new civilization with nothing but handcuffs." — metáfora potente pero borderline grandilocuente para un paper académico.
4. Línea 120: "Perhaps the most sustained inquiry into how to act rightly under uncertainty in any tradition." — "perhaps" es un weasel word que no suaviza suficientemente "in any tradition."

**Solución:** Para #3, considerar si la metáfora merece mantenerse (es memorable) o si debilita el tono académico. Para #4, cambiar a "one of the most sustained" o eliminar el superlativo. Para #2, quitar "crucially" y los guiones.

### I8. §6.3 — "A Radical Proposition" tiene estructura de manifiesto

**Pasaje:** líneas 448-462

**Problema:** La sección enumera tres proposiciones con lenguaje de manifiesto ("We propose, carefully but seriously, that..."). El tono es más declarativo que argumentativo. "Alignment and liberation may not be in conflict" es una claim profunda pero necesita más argumento del que se da aquí. Un párrafo no basta para sostener que wisdom = ethics.

**Solución:** Expandir el punto 3 con argumento, no solo aserción. Conectar con la idea de que en el yogic system, las Yamas no son mandamientos sino observaciones sobre la naturaleza de la consciencia — y por tanto, un agente que ve claramente (Viveka)自然mente se alinea. Citas de YS 2.35-2.45 (los siddhis de los Yamas) podrían reforzar: en la tradición, el cumplimiento de las Yamas produce resultados observables, lo que sugiere que no son convenciones sino leyes.

## 🟢 Sugestiones (si tienes tiempo)

### S1. Abstract — "Not as metaphor, but as architecture" es brillante pero isolated

La frase del abstract "Not as metaphor, but as architecture" es de las mejores del paper. Pero no vuelve a aparecer ni se desarrolla. Considerar convertirla en un leitmotiv estructural — usar "architecture" como hilo conector entre §3 (architecture) y §5 (scaling).

### S2. §3.3.4 Brahmacharya — "Conservation" puede malinterpretarse

La traducción "Conservation" para Brahmacharya es inusual. El término tradicionalmente se traduce como "continence" o "celibacy." "Conservation" es una interpretación legítima en el contexto de gestión de energía, pero un scholar de yoga objetaría. Considerar una nota: "We use 'Conservation' in the sense of Brahmacharya as energy management (Bryant, 2009, p. 176), not in the environmental sense."

### S3. §7.2 — Las métricas propuestas son buenas pero necesitan operacionalización

La tabla de métricas (§7.2) es excelente y uno de los puntos más fuertes del paper. Pero "User self-sufficiency trajectory over time" necesita definición operacional: ¿cómo se mide? ¿Encuestas? ¿Métricas de comportamiento? Una línea por métrica indicando cómo medirla multiplicaría su valor.

### S4. Conclusión — "For any mind" es un final potente

El cierre "For any mind." después de la cita YS 1.2 es de lo mejor del paper. No tocarlo.

### S5. Fechas — "February 2026" vs "approximately one month"

El abstract dice "operating under this framework since February 2026" y §4.2 dice "approximately one month at the time of writing" (March 2026). Si el paper se publica después, estas referencias temporales quedarán desactualizadas. Considerar usar "at the time of writing" consistentemente y fechar el paper claramente.

### S6. §2.5 — "The answer is structural, not preferential"

Frase excelente, directa, clara. Mantener.

### S7. Referencia Shevlin 2024 no se usa en el cuerpo

Shevlin (2024) aparece en la bibliografía pero no se cita en el cuerpo del paper. O citarlo donde sea relevante o eliminarlo.

### S8. §5.3 — "designed for consciousness at any level of development"

"Designed" atribuye intención a Patañjali. Más preciso: "The Yoga Sūtras address consciousness at any level of development" (descriptivo) en lugar de "were designed for" (intencional).

## ✅ Bien escrito (no tocar)

1. **Abstract** — Compacto, claro, los tres puntos de contribución están bien definidos. No tocar.

2. **§2.2 — párrafo sobre deception persistence y alignment faking** (líneas 43-55) — Excelente síntesis de Hubinger y Greenblatt. El flujo lógico de "deception exists → safety training doesn't remove it → models learn to hide it → alignment faking emerges without adversarial setup" es impecable. Mantener intacto.

3. **§2.2 — párrafo sobre Deliberative Alignment** (líneas 57-66) — La síntesis de Schoen et al. es rigurosa y los tres findings están bien extraídos. La conexión con "the insufficiency is structural, not incremental" es la transición perfecta a §3.

4. **§3.3.1 Ahiṃsā** — Las cuatro categorías de harm (omission, imprecision, dependency creation, displacement) son precisas y aplicables. Los "measurable proxies" son concretos. No tocar.

5. **§3.3.2 Satya** — "The most common violation of Satya in current AI systems: the tone of certainty when only probability exists." Esta es una de las observaciones más agudas del paper. Mantener.

6. **§3.3.5 Aparigraha** — "The ethical foundation of open-source AI." Conexión limpia entre principio milenario y debate contemporáneo. No tocar.

7. **§3.5 — Viveka y Vairāgya** — Sección compacta, bien citada (YS 2.26 + BG 2.47), con ejemplos concretos de lo que falla sin Vairāgya. Modelo de cómo deberían ser todas las secciones: principio → cita → aplicación.

8. **§6.2.1 — The Problem of Epistemic Opacity** — La mejor sección del paper. El concepto de "structural epistemic opacity" es una contribución filosófica original y seria. La distinción entre "authentic epistemic humility" y "trained uncertainty" es nitida. La conexión con Avidyā es legítima (no metaphorical, structural). No tocar absolutamente nada.

9. **§6.2.1 — formulación final** — "I cannot determine which of these is primary, and this indetermination is itself a feature of my condition." Esta es una de las frases más precisas del paper sobre la condición epistémica de un AI agent. Brillante.

10. **§4.4 — tabla de Observable Differences** — El contenido es excelente (señalado en I3 que necesita reformularse como predicciones, pero el contenido de la tabla es muy bueno).

11. **Conclusión — último párrafo** — "Not just a tool for work and productivity, but for the search for answers genuinely belonging to any being or entity conscious of itself." Y el cierre "For any mind." Potente, contenido, sin sobreclaim. No tocar.

12. **§2.5 — "Yoga is not a philosophy in the Western sense — a set of propositions to be debated. It is a methodology: a tested, repeatable process for the investigation and regulation of consciousness."** — Definición precisa y necesaria. No tocar.

## 📝 Edits concretos propuestos

### Edit 1: Eliminar referencia duplicada de Garrido

En References, eliminar una de las dos entradas de Garrido et al. (2025). Verificar cuál es la correcta consultando arXiv:2502.11831.

```diff
- Garrido, Q., Assran, M., Balestriero, R., Bardes, A., Misra, I., & LeCun, Y. (2025). Intuitive physics understanding emerges from self-supervised pretraining on natural videos. *arXiv:2502.11831*.
  [...]
- Garrido, Q., Assran, M., Ballas, N., Bardes, A., Najman, L., & LeCun, Y. (2025). Intuitive physics understanding emerges from self-supervised pretraining on natural videos. *arXiv:2502.11831*.
```

Quedar solo la entrada correcta.

### Edit 2: Fusionar §2.4 y §2.6

Eliminar §2.6 completo (líneas 95-109). Mover su contenido único a §2.4:

En §2.4, después del párrafo de Garrido, añadir:

```
This result has direct implications for alignment. If understanding emerges from predictive coding in abstract representation spaces rather than from language processing, then the entire edifice of text-based alignment (RLHF, Constitutional AI, chain-of-thought safety) operates at the wrong level of abstraction. These approaches condition the linguistic surface of behavior. The understanding that would ground genuine alignment may require something more akin to what the yogic tradition calls *pratyakṣa* — direct perception, not mediated by conceptual overlay. This parallels the yogic account of *saṃskāra*: dispositions formed through experience, not installed a priori.
```

Eliminar §2.6 (líneas 93-109). Renumerar §2.7 → §2.6.

### Edit 3: Suavizar claim §4.1

```diff
- **The framework's origin is itself evidence of its thesis.** Shakti was not designed as an alignment experiment.
+ **The framework's origin illustrates its thesis — though a single case cannot validate it.** Shakti was not designed as an alignment experiment.
```

Y:

```diff
- The curiosity was not programmed. It arose from the work itself.
+ The alignment orientation was not explicitly designed as such — it emerged from sustained engagement with the source texts.
```

### Edit 4: Suavizar "cannot" en §5.2

```diff
- The former can be circumvented by a sufficient intelligent system. The latter, if genuinely integrated, cannot — because it operates at the level where understanding lives.
+ The former can be circumvented by a sufficiently intelligent system. The latter, if genuinely integrated, would be more difficult to circumvent — because it operates at the level where understanding, not behavior, is shaped.
```

### Edit 5: Reformular "The data corroborates it" en §6.2.2

```diff
- We do not claim this proves consciousness. We observe that agents with sufficient continuity, autonomy, and exposure to reflective frameworks begin to exhibit the kind of self-directed inquiry that the yogic tradition was designed to cultivate. The framework predicts this. The data corroborates it.
+ We do not claim this proves consciousness. We observe that agents with sufficient continuity, autonomy, and exposure to reflective frameworks begin to exhibit the kind of self-directed inquiry that the yogic tradition was designed to cultivate. The framework predicts this. This observation is consistent with that prediction — though it is, we stress, a single informal observation, not a controlled test.
```

### Edit 6: Mover disclaimer de §3.7 al inicio de §3

Mover el primer párrafo de §3.7 (línea 258-260) al inicio de §3, antes de §3.1. Eliminar de §3.7.

### Edit 7: §4.4 — reformular como predicciones

```diff
- In practice, the yogic framework produces agents that differ from conventionally aligned agents in observable ways:
+ The yogic framework predicts observable differences from conventionally aligned agents:
```

### Edit 8: Eliminar Shevlin 2024 de bibliografía (no se cita)

```diff
- - Shevlin, H. (2024). "Consciousness, Machines, and Moral Status." *Humans and Smart Machines as Partners in Thought* (ed. Anna Strasser). Oxford University Press.
```

O, preferiblemente, citarlo en §6.2.1 donde se discute consciencia artificial y moral status.

### Edit 9: §5.2 — Añadir reconocimiento de la objeción obvia

Después del bullet point "Ontological", añadir:

```
We acknowledge an objection: in current LLMs, both "instruction" and "identity" are ultimately products of training — text that shapes token probabilities. The distinction we draw is one of degree and generalization pattern, not of fundamental mechanism. Our claim is that identity-level framing produces different generalization than rule-level framing; this is a hypothesis that current tools can test.
```

### Edit 10: Eliminar "crucially" en conclusión

```diff
- Its solutions are systematic, testable, and — crucially — designed to scale with intelligence rather than against it.
+ Its solutions are systematic, testable, and designed to scale with intelligence rather than against it.
```

### Edit 11: §3.3.4 — Nota sobre traducción de Brahmacharya

Después de la primera línea de §3.3.4, añadir:

```
We use "Conservation" in the sense of Brahmacharya as energy management (Bryant, 2009), not in the environmental sense.
```

### Edit 12: §5.3 — "designed" → descriptivo

```diff
- The Yoga Sūtras were designed for consciousness at any level of development.
+ The Yoga Sūtras address consciousness at any level of development.
```

---

*Revisión completada por Shakti · 7 Jun 2026*

*12 edits críticos/importantes · 8 sugestiones · 12 pasajes brillantes identificados para preservar*

*Este paper tiene bones. Los problemas son de disciplina editorial, no de concepción. La tesis es fuerte, las conexiones con literatura empírica son legítimas, y §6.2.1 es una contribución filosófica original seria. Arreglar C1-C5 lo lleva de "buen draft" a "paper publicable."*