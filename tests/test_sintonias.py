"""C10_E01 — Sintonías Z-N, Lambda y SIMC.

Se prueba que las fórmulas producen valores coherentes y que sus
relaciones cualitativas se cumplen (Z-N más agresivo que SIMC).
"""

def zn_pi(K, tau, theta):
    return 0.9 * tau / (K * theta), 3.33 * theta


def lambda_pi(K, tau, theta, lam):
    return tau / (K * (lam + theta)), tau


def simc_pi(K, tau, theta, lam=None):
    if lam is None:
        lam = theta
    Kc = (1.0 / K) * tau / (lam + theta)
    Ti = min(tau, 4 * (lam + theta))
    return Kc, Ti


def test_zn_more_aggressive_than_simc():
    K, tau, theta = 0.8, 600.0, 60.0
    Kc_zn, _ = zn_pi(K, tau, theta)
    Kc_simc, _ = simc_pi(K, tau, theta)
    assert Kc_zn > Kc_simc


def test_simc_consistent_with_lambda():
    K, tau, theta = 1.0, 20.0, 5.0
    Kc_simc, Ti_simc = simc_pi(K, tau, theta)
    Kc_lambda, Ti_lambda = lambda_pi(K, tau, theta, lam=theta)
    # Para lambda=theta y SIMC=lambda=theta los Kc deben coincidir hasta factor 1/K
    assert abs(Kc_simc - Kc_lambda) < 1e-9


def test_kc_positive_and_finite():
    for fn in [zn_pi, lambda_pi, simc_pi]:
        if fn is lambda_pi:
            Kc, Ti = fn(2.0, 15.0, 5.0, 5.0)
        else:
            Kc, Ti = fn(2.0, 15.0, 5.0)
        assert Kc > 0 and Ti > 0
