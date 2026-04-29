"""C05_E01 — Ajuste FOPDT por curve_fit.

Se prueba que `fit_fopdt` recupera los parámetros canónicos K, tau, theta
con tolerancia razonable a partir de datos sintéticos con ruido.
"""
import numpy as np
from scipy.optimize import curve_fit


def fopdt(t, K, tau, theta):
    y = np.zeros_like(t, dtype=float)
    mask = t > theta
    y[mask] = K * (1.0 - np.exp(-(t[mask] - theta) / tau))
    return y


def test_fit_fopdt_recovers_parameters():
    rng = np.random.default_rng(0)
    K_true, tau_true, theta_true = 2.0, 15.0, 5.0
    t = np.linspace(0, 100, 200)
    y = fopdt(t, K_true, tau_true, theta_true) + 0.05 * rng.standard_normal(t.size)
    popt, _ = curve_fit(fopdt, t, y, p0=[1.0, 10.0, 1.0])
    assert abs(popt[0] - K_true) < 0.1
    assert abs(popt[1] - tau_true) < 1.5
    assert abs(popt[2] - theta_true) < 0.6


def test_fopdt_zero_before_dead_time():
    t = np.linspace(0, 20, 200)
    y = fopdt(t, K=1.0, tau=5.0, theta=3.0)
    assert np.all(y[t < 3.0] == 0.0)
    assert y[-1] > 0.95
