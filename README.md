# Control Automático y de Procesos Industriales — código

Repositorio de **código fuente** asociado al libro:

> **Control Automático y de Procesos Industriales — Fundamentos, criterio y casos industriales didácticos con Python**
> Pedro Plaza Merino, 2026.

## Propósito

Este repositorio contiene los notebooks Python y las variantes MATLAB/Octave equivalentes a los ejemplos del libro. El libro muestra fragmentos mínimos para no interrumpir el hilo conceptual; aquí vive la versión reproducible.

> **El libro se entiende sin ejecutar código.** Este repositorio es un complemento opcional que permite reproducir las figuras, ejecutar los ejemplos numéricos y comparar implementaciones MATLAB/Octave con sus equivalentes Python.
>
> **Los ejemplos son didácticos, no código de producción ni recomendación directa para planta.** Cualquier traslado a operación real exige validación, gestión del cambio y supervisión humana.

## Instalación

### Opción A — pip + venv (Python 3.10 oficial)

```bash
python3.10 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

### Opción B — conda / mamba

```bash
conda env create -f environment.yml
conda activate control-libro
jupyter lab
```

### Opción C — MATLAB / Octave (opcional)

Las variantes MATLAB/Octave están en `matlab_octave/`. Funcionan en MATLAB R2022a+ con Control System Toolbox o en Octave 7+ con paquete `control`.

## Estructura

```
control-automatico-procesos-industriales-codigo/
├── README.md
├── LICENSE
├── CITATION.cff
├── CONTRIBUTING.md
├── requirements.txt        # dependencias pip
├── environment.yml         # entorno conda
├── .gitignore
├── .github/workflows/ci.yml
├── python/
│   ├── README.md
│   ├── cap01/  ...  cap17/   # 31 notebooks + pseudocódigo de C17
├── matlab_octave/
│   ├── README.md
│   ├── cap03/ cap04/ cap07/ cap09/ cap10/ cap11/   # 6 scripts equivalentes
├── tests/                   # pytest suite
├── data/
│   ├── synthetic/           # placeholders para datos sintéticos
│   └── examples/
└── docs/
    ├── guia_instalacion.md
    ├── mapa_ejemplos.md
    ├── equivalencias_matlab_python.md
    └── uso_responsable.md
```

## Cómo ejecutar los notebooks

Cada capítulo tiene su carpeta dentro de `python/`. Por ejemplo, para reproducir el ejemplo `C09_E01` (PID con antiwindup):

```bash
jupyter lab python/cap09/C09_E01_pid_antiwindup.ipynb
```

Pulsa **Run All** o ejecuta celda a celda. Los notebooks generan datos sintéticos internamente con `numpy.random.seed` explícito para reproducibilidad estricta. Las figuras se guardan opcionalmente en `figures/generated/` si decides crearla; no se incluyen por defecto en el repositorio.

## Cómo ejecutar los tests

```bash
pip install pytest
pytest -v
```

Cobertura: importaciones, modelos básicos, CUSUM, ajuste FOPDT, PID antiwindup, sensibilidades S/T, sintonías Z-N/Lambda/SIMC, datasets sintéticos.

GitHub Actions ejecuta el suite completo en cada push (Python 3.10).

## Tabla de capítulos y notebooks

| Cap | Notebooks Python | Script MATLAB/Octave |
|---|---|---|
| 1 | C01_E01_lazo_abierto_cerrado | — |
| 2 | C02_E01_senales_canonicas | — |
| 3 | C03_E01_linealizacion_sympy, C03_E02_ajuste_fopdt | C03_E02_fopdt.m |
| 4 | C04_E01_fdt_estado_polos | C04_E01_fdt_estado.m |
| 5 | C05_E01_curve_fit_fopdt, C05_E02_sensibilidades_S_T | — |
| 6 | C06_E01_bode_nyquist_margenes | — |
| 7 | C07_E01_root_locus | C07_E01_rlocus.m |
| 8 | C08_E01_cinco_lazos_canonicos | — |
| 9 | C09_E01_pid_antiwindup, C09_E02_paralelo_vs_isa | C09_E01_pid_antiwindup.m |
| 10 | C10_E01_sintonias_zn_lambda_simc, C10_E02_diagnostico_oscilacion | C10_E01_zn.m |
| 11 | C11_E01_c2d_tustin_zoh, C11_E02_pid_discreto_incremental | C11_E02_pid_discreto.m |
| 12 | C12_E01_cascada_intercambiador, C12_E02_feedforward, C12_E03_mpc_minimo | — |
| 13 | C13_E01_gain_scheduling_pH, C13_E02_str_rls | — |
| 14 | C14_E01_pseudo_plc_pid, C14_E02_mqtt_demo, C14_E03_grafcet_conceptual | — |
| 15 | C15_E01_cusum_drift, C15_E02_modelo_hibrido, C15_E03_sandbox_sintonia | — |
| 16 | C16_E01_soft_sensor_pls, C16_E02_detector_stiction, C16_E03_anomalias_isolation_forest, C16_E04_edge_ai_inferencia | — |
| 17 | C17_E01_patron_asistente.md (pseudocódigo) | — |

Tabla completa en `docs/mapa_ejemplos.md`.

## Cómo comparar MATLAB y Python

Para los ejemplos con variante MATLAB/Octave, ejecuta primero el notebook Python y luego el script MATLAB equivalente. Los resultados numéricos deben coincidir dentro de la tolerancia esperada. Las figuras pueden diferir estéticamente; los valores no.

Equivalencias completas en `docs/equivalencias_matlab_python.md`.

## Uso responsable

Antes de adaptar cualquier ejemplo a planta, lee `docs/uso_responsable.md`. Resumen:

- **No usar en planta sin validación independiente.** Los ejemplos son didácticos.
- **No tomar parámetros de sintonía como recetas universales.** Cada lazo requiere identificación y validación.
- **No usar los ejemplos de control adaptativo, MPC, gemelos digitales, ML o agentes en lazos críticos sin envoltorio de seguridad y supervisión humana.**

## Licencia

- **Código** (notebooks, scripts, configuración, tests): BSD-3-Clause.
- **Textos derivados** (README, documentos en `docs/`): CC BY-NC 4.0.

Ver `LICENSE` para el texto completo.

## Cómo citar

Ver `CITATION.cff`. Cita sugerida:

> Plaza Merino, P. (2026). *Control Automático y de Procesos Industriales: Fundamentos, criterio y casos industriales didácticos con Python.*
> Repositorio de código: https://github.com/<usuario>/control-automatico-procesos-industriales-codigo

## Estado

Versión asociada a la **primera edición del libro**. Las correcciones menores se documentan en `CHANGELOG.md` cuando se generen.

## Contacto

Pedro Plaza Merino — pplaza@plazarobotica.es
