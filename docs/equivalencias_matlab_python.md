# Equivalencias MATLAB ↔ Python

Tabla de equivalencias para los ejemplos de control. Python (con `python-control`, `scipy.signal`, `sympy`) cubre la mayor parte de la API de MATLAB Control System Toolbox.

## Funciones más usadas

| MATLAB / Control Toolbox | Python | Librería | Notas |
|--------------------------|--------|----------|-------|
| `tf(num, den)` | `control.tf(num, den)` | python-control | API casi idéntica |
| `ss(A, B, C, D)` | `control.ss(A, B, C, D)` | python-control | Equivalente directo |
| `feedback(G, H)` | `control.feedback(G, H)` | python-control | Realimentación negativa por defecto |
| `series(G1, G2)` o `G1*G2` | `control.series(G1, G2)` o `G1*G2` | python-control | Operador `*` sobrecargado |
| `parallel(G1, G2)` | `control.parallel(G1, G2)` o `G1+G2` | python-control | Operador `+` sobrecargado |
| `step(G)` | `control.step_response(G)` | python-control | Devuelve `(t, y)` |
| `lsim(G, u, t)` | `control.forced_response(G, t, u)` o `scipy.signal.lsim` | python-control / scipy | **Atención al orden de argumentos** |
| `bode(G)` | `control.bode_plot(G, dB=True, deg=True)` | python-control | Argumentos para coincidir con MATLAB |
| `nyquist(G)` | `control.nyquist_plot(G)` | python-control | API similar |
| `margin(G)` | `control.margin(G)` | python-control | Devuelve `(gm, pm, wcg, wcp)` |
| `rlocus(G)` | `control.root_locus(G)` | python-control | Devuelve `(rlist, klist)` |
| `zpk(z, p, k)` | `control.zpk(z, p, k)` | python-control | Equivalente directo |
| `c2d(G, Ts, method)` | `control.c2d(G, Ts, method)` | python-control | Métodos: `tustin`, `zoh`, `matched`, `bilinear` |
| `residue(num, den)` | `scipy.signal.residue(num, den)` | scipy.signal | Devuelve `(r, p, k)` |
| `ilaplace(F)` | `sympy.inverse_laplace_transform(F, s, t)` | sympy | Resultado simbólico |
| `laplace(f)` | `sympy.laplace_transform(f, t, s)` | sympy | Devuelve `(F, a, cond)` |
| `roots(p)` | `numpy.roots(p)` | numpy | Equivalente; orden no garantizado |
| `poles(G)` | `control.poles(G)` | python-control | Equivalente |
| `zero(G)` | `control.zeros(G)` | python-control | Equivalente |
| `lqr(A,B,Q,R)` | `control.lqr(A,B,Q,R)` | python-control | API muy similar |
| `kalman(...)` | `control.lqe(...)` o `filterpy` | python-control / filterpy | python-control cubre lqe |
| `ss2tf, tf2ss` | `control.ss2tf, control.tf2ss` | python-control | Conversión directa |
| `simulink` | — | — | Sin equivalente directo; construir con `control` + `scipy` |

## Ejemplos MATLAB de los materiales UNIR

| Archivo MATLAB | Tema UNIR | Capítulo libro | Notebook Python equivalente |
|----------------|-----------|----------------|------------------------------|
| ejemplo_TFI.m | T3 | C4 | python/cap04/C04_E01.ipynb (sección Laplace inversa) |
| ejemplo_residuos.m | T3 | C4 | python/cap04/C04_E01.ipynb (sección residuos) |
| ejemplo_FDT.m | T4 | C4 | python/cap04/C04_E01.ipynb |
| ejemplo_FDT-1.m | T4 | C4 | python/cap04/C04_E01.ipynb |
| ejemplo_rootlocus-2.m | T7 | C7 | python/cap07/C07_E01.ipynb |
| ejemplo_optimizacion_PID.m | T8 | C10 | python/cap10/C10_E01.ipynb |
| Untitled.m | T4 | C4 | python/cap04/C04_E01.ipynb |
| untitled2.m | T4 | C4 | python/cap04/C04_E01.ipynb |
| Tema_3.m | T3 | C4 | python/cap04/C04_E01.ipynb (sección sympy) |
| Actividad_grupal.mlx | T3-T8 | C3-C10 | troceado en varios notebooks |
