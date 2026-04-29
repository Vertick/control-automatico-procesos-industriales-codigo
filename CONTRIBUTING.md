# Cómo contribuir

Gracias por considerar contribuir al repositorio. Sigue estas reglas básicas para mantener el repositorio coherente con el libro.

## Antes de abrir un issue o PR

1. Lee `docs/politica_uso_responsable.md`. El repositorio acompaña a un libro técnico; los principios editoriales (sobriedad, marcadores de madurez `[C]/[E]/[X]`, no hype de IA, no sustituir control clásico) son vinculantes.
2. Comprueba si tu propuesta encaja con la arquitectura de 17 capítulos del libro. Cambios estructurales requieren consenso con el autor.

## Tipos de contribución bienvenidas

- **Erratas en código** o en la documentación.
- **Mejoras de portabilidad** (tests adicionales, soporte ampliado para Octave o versiones de Python).
- **Variantes MATLAB/Octave** para los notebooks que aún no la tienen y proceda incluirla.
- **Datos sintéticos adicionales** con seeds explícitas en `data/synthetic/`.
- **Ejemplos industriales adicionales** que ilustren un capítulo, manteniendo la sobriedad del libro.

## Tipos de contribución que NO se aceptan

- Ejemplos con dependencias pesadas no justificadas (frameworks deep learning completos).
- Código que sustituya control clásico por capas modernas sin ingeniería de seguridad.
- Material promocional o afirmaciones sobre productos comerciales.
- Notebooks con datos reales no anonimizados.

## Convenciones

- Identificadores `CXX_EYY` para activos. `fig_CXX_FYY` para figuras.
- Notebooks Python con seed explícito (`numpy.random.seed(0)` o `default_rng(0)`).
- Cada notebook debe ejecutarse de inicio a fin sin manipulación manual.
- Tests pytest en `tests/` con docstring que cite el ID del notebook origen.
- Mensajes de commit: convencionales (`feat:`, `fix:`, `docs:`, `test:`, `ci:`, `chore:`).

## Flujo de trabajo

1. Fork del repositorio.
2. Rama temática (`feat/...`, `fix/...`).
3. Tests verdes (`pytest tests/`).
4. Pull request con descripción del cambio y referencia al capítulo afectado.

## Contacto

Pedro Plaza Merino — pplaza@plazarobotica.es
