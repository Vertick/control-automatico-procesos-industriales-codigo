# C17_E01 — Patrón asistente con verificación humana (pseudocódigo)

**Capítulo:** 17 — Control cognitivo, agentes, copilotos de ingeniería y gobernanza de IA en control industrial
**Identificador:** `C17_E01`
**Tipo:** Pseudocódigo. **No ejecutable.** No depende de servicios externos.

---

## Contexto

Este patrón documenta cómo se integra un copiloto LLM en sala de control sin actuar sobre planta y manteniendo la decisión humana y la trazabilidad. Es el patrón mínimo razonable; en planta, la implementación real depende del sistema DCS, del proveedor de IA y de la política interna de la organización.

## Pseudocódigo

```python
def patron_asistente(pregunta_operador, contexto_planta):
    # 1. Sistema de IA propone respuesta o acción
    sugerencia = llm.consultar(pregunta_operador, contexto_planta)
    log.registrar({
        "prompt": pregunta_operador,
        "respuesta_ia": sugerencia,
        "modelo": llm.version,
        "timestamp": ahora_iso8601(),
    })

    # 2. Verificación humana obligatoria
    decision = operador.revisar(sugerencia)
    log.registrar({"decision_humana": decision})

    # 3. Si la decisión implica acción sobre planta:
    if decision.aplicar:
        # 3a. Gating de seguridad: rangos, límites SIL, ventana operativa
        if not gating_seguridad(decision.accion):
            log.registrar({"gating": "rechazado", "motivo": gating_motivo()})
            alertar_operador("Acción rechazada por gating de seguridad")
            return None
        # 3b. Ejecución con registro
        ejecutar_accion(decision.accion)
        log.registrar({
            "accion_ejecutada": decision.accion,
            "operador": operador.id,
            "ts": ahora_iso8601(),
        })

    return decision
```

## Reglas obligatorias

1. **Sin acción autónoma sobre planta crítica.** El sistema solo propone; el operador decide.
2. **Trazabilidad completa.** Cada interacción (prompt, respuesta del modelo, decisión humana, acción ejecutada) queda registrada con identificador de operador, modelo y timestamp.
3. **Gating de seguridad antes de ejecutar.** El sistema valida que la acción propuesta cae dentro de rangos seguros, ventanas operativas, y respeta funciones de seguridad SIL.
4. **Plan de rollback.** Toda acción aplicable debe tener procedimiento de reversión documentado.
5. **Auditoría periódica.** Tasa de aceptación, frecuencia de gating rechazado, incidentes asociados a propuestas del sistema.

## Por qué no se ejecuta

Un notebook ejecutable de copiloto LLM dependería de un servicio externo (API de modelo) cuyo coste, latencia, política de privacidad y licencia exceden el alcance de este libro. La política responsable es documentar el patrón conceptualmente y dejar la integración real a la organización que despliegue el sistema, con su propia política de gobernanza.

## Referencias normativas

- NIST AI Risk Management Framework (AI RMF 1.0).
- IEC 62443 (ciberseguridad industrial).
- IEC 61508 / IEC 61511 (seguridad funcional).
- ISO/IEC 23894 (gestión de riesgo de IA).
