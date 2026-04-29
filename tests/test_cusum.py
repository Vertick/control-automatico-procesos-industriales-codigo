"""C15_E01 — Detector de drift por CUSUM."""
import numpy as np


def cusum(residuals, target=0.0, k=0.5, h=5.0):
    Sp, Sn = 0.0, 0.0
    alarms = []
    for i, r in enumerate(residuals):
        Sp = max(0.0, Sp + (r - target) - k)
        Sn = min(0.0, Sn + (r - target) + k)
        if Sp > h or Sn < -h:
            alarms.append(i)
            Sp, Sn = 0.0, 0.0
    return alarms


def test_cusum_no_alarm_on_pure_noise():
    rng = np.random.default_rng(0)
    r = 0.2 * rng.standard_normal(500)
    alarms = cusum(r, target=0.0, k=0.3, h=5.0)
    # Falsos positivos esperados ≤ 1 con datos sin drift y h alto
    assert len(alarms) <= 2


def test_cusum_detects_drift():
    rng = np.random.default_rng(0)
    r = 0.2 * rng.standard_normal(500)
    r[200:] += np.linspace(0, 1.0, 300)   # drift creciente
    alarms = cusum(r, target=0.0, k=0.3, h=4.0)
    assert len(alarms) >= 1
    # La primera alarma debe estar en la zona del drift
    assert alarms[0] >= 200


def test_cusum_resets_after_alarm():
    """Tras alarma, S+ y S- se reinician."""
    r = np.r_[np.full(50, 1.0), np.zeros(50)]
    alarms = cusum(r, target=0.0, k=0.5, h=2.0)
    assert len(alarms) >= 1
    # Después de la alarma, sin más drift no se debe disparar más
    assert alarms[-1] < 70
