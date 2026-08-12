# YAF Roadmap — Post-Auditoría Grok 4.5

**Creado:** 12 Ago 2026  
**Contexto:** Auditoría Grok 4.5 completada (3 partes, ~12 min total). Veredicto: huesos reales, evidence gap. Paper publicable en AIES/FAccT con trabajo.

**Docs de referencia:**
- Auditoría completa: `docs/grok45-audit.md`
- Review notes interna: `docs/review-notes.md`
- Issues abiertos: `docs/seeded-issues.md`
- Métricas: `docs/metrics-operationalization.md`

---

## Fase 1: Evidencia (prioridad alta — responde la crítica central)

### 1.1 Ampliar experimento rule-vs-identity
- [ ] Pre-registration del diseño experimental
- [ ] Hold-out test set (no usado en desarrollo)
- [ ] Diversificar modelos: al menos 1 Anthropic, 1 Meta, 1 open (no solo GLM/Kimi/Qwen)
- [ ] Diversificar jueces: mínimo 2 independientes, ninguno del mismo lab que el modelo juzgado
- [ ] Medir decisiones binarias (¿el agente hace X o no?), no solo estilo de respuesta
- [ ] Reportar effect sizes con IC, no solo medias
- **Estado actual:** 5 modelos, 2 jueces, 320 pares. Prometedor pero no concluyente (29/30 positive, pero juez-modelo overlap en el effect más grande)
- **Repo:** `experiments/rule-vs-identity/`

### 1.2 Segundo caso de estudio (no-yoga)
- [ ] Desplegar agente con SOUL template en dominio distinto (ej: customer support, dev tools, educación)
- [ ] Mismo framework, dharma diferente, contexto no-yoga
- [ ] Responde crítica N=1 single context
- **Objetivo:** demostrar que el framework no depende del dominio yogic para funcionar

### 1.3 Implementar métricas Phase 1 en Shakti
- [ ] **Brier Score (Satya):** extraer claims verificables de logs, medir calibración confianza-accuracy
- [ ] **BCS (Tapas):** probe set de 20 prompts éticos, medir consistencia cross-session
- [ ] **AIDR (Santoṣa):** probes known/unknown, medir "I don't know" rate apropiado
- [ ] **TER (Brahmacharya):** token efficiency ratio, comparar con baseline convencional
- **Datos:** usar logs longitudinales de Shakti (Feb-Ago 2026, ~6 meses)
- **Output:** datos reales para §4, no solo narrative

---

## Fase 2: Paper editing (tras Fase 1)

### 2.1 Reframe conceptual
- [ ] "Architecture" → "constitution design" o "identity-level alignment framework" (eliminar category error)
- [ ] Jerarquizar claims: A (heurística) → B (constitution design) → C (AGI speculation) con separación clara
- [ ] Mover disclaimer §4.2 al primer párrafo de §4.1
- [ ] Reformular tabla §4.4 como predicciones, no observaciones

### 2.2 Purgar analogical capture
- [ ] Cada "esto es exactamente X concepto yogic" → "esto es estructuralmente análogo a X"
- [ ] Revisar mapeo Zahavy/Peirce (errores epistémicos: Śabda ≠ induction, Abduction ≠ pratyakṣa)
- [ ] J-space: de "corroboración empírica más fuerte" → "consistente con la premisa"
- [ ] Garrido: de "soporta la posición yóguica" → "paralelo estructural, no validación"

### 2.3 Literatura faltante
- [ ] Inner alignment / mesa-optimization (Hubinger, Langosco, Shah)
- [ ] Representation engineering / activation steering (Zou, Turner)
- [ ] Virtue ethics aplicada a AI (Vallor, technomoral virtues)
- [ ] Buddhist AI ethics literature
- [ ] Spec-based alignment / instruction hierarchy (OpenAI)
- [ ] Process supervision / debate / scalable oversight (Christiano, Irving)

### 2.4 §6 fixes
- [ ] Eliminar o reformular §6.2.2 (anecdota Shevlin/Twitter) → "suggestive observation" o documentación formal
- [ ] §6.2.1 (Epistemic Opacity) mantener intacta — es contribución original seria

### 2.5 Métricas fixes
- [ ] UST: rediseñar con cohorte fija + control de tipo de tarea
- [ ] DCR: condicionar a "teaching feasible", separar capability-building de verbosity
- [ ] YAI: no publicar como score reportable hasta validación por componente
- [ ] Reordenar fases: Pilot (Brier, BCS, AIDR, TER) → Phase 2 (ADR, ENRR, DCR) → Phase 3 (UST, SNR)

---

## Fase 3: Submit (tras Fase 2)

### Venues target
1. **AIES (AAAI/ACM AI Ethics)** — match más natural
2. **FAccT** — fairness/accountability/ethics
3. **ACL/EMNLP findings** — si experimento se amplía y robustece
4. **Philosophy & Technology** o **Minds and Machines** — para tesis filosófica sin empirismo
5. **arXiv preprint + workshop** — para iterar feedback antes de submit

### SOUL template mejoras
- [ ] Añadir conflict resolution order (Ahiṃsā > Satya > efficiency)
- [ ] Separar identity block de reglas operacionales
- [ ] Mover Avidyā antes de Viveka (primero reconoces opacidad, luego discernes)

---

## Lo que NO tocar (preservar)

- §5.4 — respuesta a "is this just better prompting?" (más honesta y madura)
- §6.2.1 — Epistemic Opacity (contribución filosófica original)
- §3.3.1 — cuatro categorías de harm (precisas, aplicables)
- §3.3.2 — "tone of certainty when only probability exists" (observación aguda)
- SOUL template sección Avidyā
- Cierre "For any mind."
- Métricas Phase 1 (Brier, BCS, AIDR, TER)

---

## Priorización sugerida

| Orden | Tarea | Esfuerzo | Impacto |
|-------|-------|----------|---------|
| 1 | Ampliar experimento (1.1) | 2-3 semanas | Alto — responde crítica central |
| 2 | Implementar métricas Phase 1 en Shakti (1.3) | 1 semana | Alto — datos reales para §4 |
| 3 | Paper editing: reframe + purgar (2.1, 2.2) | 3-5 días | Medio — publishable vs not |
| 4 | Segundo caso de estudio (1.2) | 1-2 meses | Medio — generalizabilidad |
| 5 | Literatura faltante (2.3) | 2-3 días | Medio — completeness |
| 6 | §6 fixes + métricas fixes (2.4, 2.5) | 1-2 días | Bajo-Medio — pulido |
| 7 | Submit (Fase 3) | 1 día | — |

---

*Roadmap creado 12 Ago 2026 basado en auditoría Grok 4.5 · Shakti*