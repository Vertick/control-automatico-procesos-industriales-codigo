# data/

Esta carpeta es el lugar canónico para datos sintéticos y datos de ejemplo del repositorio.

## Política

- **`synthetic/`** — datos generados por scripts deterministas (con `numpy.random.seed` o `default_rng(seed=…)` explícitos). En este repositorio, **los notebooks generan los datos en línea** dentro del propio cuaderno; esta subcarpeta queda preparada para que los lectores que prefieran exportar los datos a CSV los depositen aquí.
- **`examples/`** — datos de ejemplo anonimizados (no procedentes de planta). Vacío en la entrega del Lote 4: si en lotes posteriores se incorporan datos reales anonimizados, se documentan aquí (origen, fecha, columnas, unidades, política de uso).

## Reproducibilidad

Si un notebook lee de `data/` (no es el caso en el Lote 4), debe documentar:

1. Ruta exacta del archivo dentro del repo.
2. Origen (sintético determinista, derivado de un dataset público, o anonimizado).
3. Columnas y unidades.
4. Seed o semilla usada en la generación.
5. Advertencia explícita de "datos sintéticos" en la celda inicial.

## Uso responsable

Los datos depositados aquí son didácticos. No representan operación real de planta. Cualquier inferencia que el lector haga sobre comportamiento industrial debe validarse contra datos reales propios y bajo política de uso responsable (ver `docs/politica_uso_responsable.md`).
