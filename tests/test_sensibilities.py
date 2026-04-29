"""C05_E02 — Sensibilidades S, T, KS, SG.

Verifica la identidad S+T=1 en frecuencias de prueba (no en s=0 exacto,
porque el integrador del PI hace divergir 1+L allí) y los rangos
operativos esperados.
"""
import numpy as np
import control as ct


def _S_T(K=2.0, tau=15.0, lam=15.0):
    G = ct.tf([K], [tau, 1.0])
    Kc = tau / (K * lam); Ti = tau
    PI = ct.tf([Kc * Ti, Kc], [Ti, 0.0])
    L = PI * G
    S = 1.0 / (1.0 + L)
    T = L / (1.0 + L)
    return S, T, L


def test_S_plus_T_equals_one_at_low_freq():
    """Identidad S+T=1 cumplida en cualquier punto fuera del polo en 0."""
    S, T, _ = _S_T()
    for w in [1e-3, 1e-2, 1e-1, 1.0, 10.0]:
        s_val = complex(ct.evalfr(S, 1j * w))
        t_val = complex(ct.evalfr(T, 1j * w))
        assert abs((s_val + t_val) - 1.0) < 1e-6, f"falla en w={w}"


def test_T_high_at_low_freq_and_S_high_at_high_freq():
    S, T, _ = _S_T()
    # Baja frecuencia (ω pequeña, no 0): T≈1, S≈0
    w_lo = 1e-4
    assert abs(np.abs(ct.evalfr(T, 1j * w_lo)) - 1.0) < 0.05
    assert np.abs(ct.evalfr(S, 1j * w_lo)) < 0.05
    # Alta frecuencia: T→0, S→1
    w_hi = 1e3
    assert np.abs(ct.evalfr(T, 1j * w_hi)) < 0.1
    assert np.abs(ct.evalfr(S, 1j * w_hi)) > 0.9
