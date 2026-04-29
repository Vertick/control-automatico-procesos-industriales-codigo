"""Smoke tests sobre los modelos canónicos del libro.

Verifica que los modelos FOPDT, primer orden, integrador y los lazos
canónicos producen comportamiento dinámico esperado. No comprueba
implementaciones específicas de notebooks; comprueba el modelo en
abstracto.
"""
import numpy as np
from scipy.integrate import solve_ivp
import control as ct


def test_fopdt_step_response_reaches_K():
    """La respuesta a escalón unitario de un FOPDT alcanza ~K en t>>tau+theta."""
    K, tau, theta = 2.0, 5.0, 1.0
    G = ct.tf([K], [tau, 1.0])
    t = np.linspace(0, 5*tau + theta + 5, 500)
    _, y = ct.step_response(G, t)
    assert abs(y[-1] - K) < 0.01


def test_first_order_time_constant():
    """A los t=tau una respuesta de primer orden alcanza ~63% del valor final."""
    K, tau = 1.5, 4.0
    G = ct.tf([K], [tau, 1.0])
    t, y = ct.step_response(G, np.linspace(0, 4*tau, 400))
    idx = np.argmin(np.abs(t - tau))
    assert abs(y[idx] / K - (1 - np.exp(-1))) < 0.02


def test_integrator_grows_linearly():
    """Un integrador puro 1/s ante un escalón unitario crece linealmente con pendiente 1."""
    G = ct.tf([1.0], [1.0, 0.0])
    t, y = ct.step_response(G, np.linspace(0, 10, 200))
    # pendiente ≈ 1
    pendiente = (y[-1] - y[0]) / (t[-1] - t[0])
    assert abs(pendiente - 1.0) < 0.05


def test_pi_eliminates_steady_state_error():
    """Un PI sobre planta de primer orden da error en régimen ≈ 0."""
    G = ct.tf([1.0], [10.0, 1.0])
    PI = ct.tf([0.5*5.0, 0.5], [5.0, 0.0])
    T = ct.feedback(PI*G, 1)
    t, y = ct.step_response(T, np.linspace(0, 100, 500))
    assert abs(y[-1] - 1.0) < 0.01


def test_second_order_underdamped_overshoots():
    """Un sistema de 2º orden con zeta=0.5 sobredispara entre 10% y 25%."""
    wn = 1.0; zeta = 0.5
    G = ct.tf([wn**2], [1.0, 2*zeta*wn, wn**2])
    t, y = ct.step_response(G, np.linspace(0, 20, 1000))
    overshoot = (y.max() - 1.0) / 1.0
    assert 0.10 < overshoot < 0.25
