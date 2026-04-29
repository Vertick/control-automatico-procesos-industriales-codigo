# MATLAB / Octave — variantes de equivalencia docente

Esta carpeta contiene los scripts MATLAB/Octave equivalentes a los ejemplos de Python que provienen de los materiales originales de la asignatura UNIR Introducción al Control Automático y de Procesos.

## Compatibilidad

- **MATLAB** R2022a+ con Control System Toolbox.
- **Octave** 7+ con paquete `control` (`pkg install -forge control`).

## Capítulos cubiertos

| Capítulo | Script | Origen UNIR |
|----------|--------|-------------|
| C3 | C03_E02_fopdt.m | Tema 5 (curva de reacción) |
| C4 | C04_E01_fdt_estado.m | ejemplo_FDT.m, ejemplo_residuos.m, ejemplo_TFI.m, Untitled.m, untitled2.m, Tema_3.m |
| C7 | C07_E01_rlocus.m | ejemplo_rootlocus-2.m |
| C9 | C09_E01_pid_antiwindup.m | — (nuevo) |
| C10 | C10_E01_zn.m | ejemplo_optimizacion_PID.m |
| C11 | C11_E02_pid_discreto.m | — (nuevo) |

## Notas de portabilidad

- En Octave, sustituir funciones específicas de MATLAB por equivalentes (`tic/toc` funcionan en ambos; `evalin` no).
- Las figuras pueden diferir estéticamente de las generadas por matplotlib en Python; los valores numéricos coinciden.

## Trazabilidad

Cada script incluye un encabezado con:
- Capítulo del libro asociado.
- Identificador del ejemplo (CXX_EYY).
- Origen UNIR si procede.
- Equivalente en notebook Python.
