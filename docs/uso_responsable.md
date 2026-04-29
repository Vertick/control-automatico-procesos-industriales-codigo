# Política de uso responsable

Este repositorio contiene ejemplos didácticos asociados al libro Control Automático y de Procesos Industriales. La política de uso responsable es parte integral del repositorio: cualquier usuario que ejecute, modifique o derive trabajo del código aquí incluido la acepta.

## Principios

1. **Los ejemplos son didácticos.** No son código de producción. No están diseñados para soportar lazos de planta sin adaptación, validación y supervisión.
2. **La validación es responsabilidad del usuario.** Cualquier implementación real requiere validación independiente. El autor no se responsabiliza del uso del código en planta.
3. **Las técnicas avanzadas tienen requisitos.** Control adaptativo, MPC, gemelos digitales, ML aplicado, agentes y copilotos LLM requieren ingeniería de seguridad explícita: barreras de seguridad, supervisión humana, trazabilidad, validación, plan de rollback.
4. **No usar RL ni agentes en lazo cerrado en planta crítica.** El estado del arte no proporciona garantías formales suficientes para sustituir lazos PID, MPC o adaptativos validados en lazos críticos. Cualquier despliegue de este tipo es responsabilidad exclusiva del implementador.
5. **No tomar parámetros de sintonía como recetas universales.** Cada lazo requiere identificación de proceso y validación de la sintonía propuesta.
6. **Ciberseguridad.** Cualquier despliegue que conecte el algoritmo con planta (IIoT, gemelos, copilotos) debe respetar segmentación OT/IT, autenticación, cifrado, registro y referencias normativas (IEC 62443, NIST AI RMF).

## Uso recomendado

- **Estudiantes**: ejecutar los notebooks, modificar parámetros, observar el comportamiento, hacer los ejercicios del libro.
- **Profesionales**: usar los ejemplos como punto de partida para razonar sobre lazos propios; replicar la metodología, no los parámetros.
- **Docentes**: usar los notebooks en clase, citando la fuente. Los notebooks son CC BY-NC 4.0; el uso comercial requiere acuerdo explícito.

## Lo que NO debe hacerse

- Aplicar parámetros de sintonía aquí publicados a un lazo en planta sin validación previa.
- Usar el patrón asistente (C17_E01) sin gating humano explícito y sin trazabilidad.
- Desplegar gemelos digitales sin protocolo de calibración y validación.
- Desplegar soft-sensors sin calibración periódica contra sensor físico.
- Desplegar detectores de anomalías sin métricas operativas honestas (tasa de falsos positivos / negativos).
- Usar RL o agentes autónomos en lazo cerrado sobre planta crítica.

## Reportar problemas

Errores en el código, bugs, sugerencias: usar issues de GitHub. Cuestiones sobre uso en planta crítica: solicitar consultoría profesional independiente; el autor no responde consultas operativas individuales.
