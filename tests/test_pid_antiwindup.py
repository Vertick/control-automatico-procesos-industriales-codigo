"""C09_E01 — PID con saturación y antiwindup back-calculation.

Verifica que el antiwindup reduce el sobredisparo cuando se aplica un
escalón ambicioso pero alcanzable (SP < K·u_max para que el lazo pueda
estabilizarse en consigna).
"""
import numpy as np


def planta(y, u, dt, K=2.0, tau=10.0):
    return y + dt * (K * u - y) / tau


def pid_step(state, e, Kp, Ki, Kd, dt, umin, umax, Tt=1.0):
    P = Kp * e
    state["I"] += Ki * e * dt
    D = Kd * (e - state["e_prev"]) / dt
    u_unsat = P + state["I"] + D
    u_sat = float(np.clip(u_unsat, umin, umax))
    state["I"] += (u_sat - u_unsat) * dt / Tt
    state["e_prev"] = e
    return u_sat, state


def simular(antiwindup=True, T=80.0, dt=0.05, SP=2.5, umax=1.5,
            Kp=2.0, Ki=0.5):
    """K·u_max = 2·1.5 = 3.0 > SP=2.5 (consigna alcanzable)."""
    t = np.arange(0, T, dt)
    Tt = 1.0 if antiwindup else 1e9
    y = 0.0
    st = {"I": 0.0, "e_prev": 0.0}
    ys = []
    for _ in t:
        e = SP - y
        u, st = pid_step(st, e, Kp, Ki, 0.0, dt, 0.0, umax, Tt=Tt)
        y = planta(y, u, dt)
        ys.append(y)
    return np.array(ys)


def test_antiwindup_reduces_overshoot():
    SP = 2.5
    y_aw = simular(antiwindup=True, SP=SP)
    y_no = simular(antiwindup=False, SP=SP)
    over_aw = max(0.0, y_aw.max() - SP)
    over_no = max(0.0, y_no.max() - SP)
    # Con antiwindup el sobredisparo es estrictamente menor
    assert over_aw < over_no
    # Y la reducción es significativa (al menos 25%)
    assert over_aw < 0.75 * over_no


def test_pid_reaches_setpoint():
    SP = 2.5
    y = simular(antiwindup=True, T=200.0, SP=SP)
    assert abs(y[-1] - SP) < 0.05
