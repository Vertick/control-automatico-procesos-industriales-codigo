% =====================================================================
% C11_E02 — PID discreto incremental (MATLAB / Octave)
% =====================================================================
% Capitulo: 11 - Control digital, muestreo e implementacion en PLC/DCS
% Notebook Python equivalente: python/cap11/C11_E02_pid_discreto_incremental.ipynb
% Compatibilidad: MATLAB / Octave estandar (sin toolbox)
% =====================================================================

clear; close all;

% Parametros
Kp = 0.6; Ti = 10.0; Td = 0.0; Ts = 0.2;
umin = 0; umax = 4.0;
K_p = 2.0; tau = 10.0;
SP = 5.0; T = 60.0; N = round(T/Ts);

y = 0; e1 = 0; e2 = 0; u = 0;
ys = zeros(N, 1); us = zeros(N, 1);
for k = 1:N
    e = SP - y;
    du = Kp * ((e - e1) + (Ts/Ti)*e + (Td/Ts)*(e - 2*e1 + e2));
    u_new = u + du;
    u = max(umin, min(umax, u_new));
    e2 = e1; e1 = e;
    y = y + Ts*(K_p*u - y)/tau;
    ys(k) = y; us(k) = u;
end

t = (0:N-1)*Ts;
figure;
subplot(2,1,1); plot(t, ys); yline(SP, '--');
ylabel('y'); grid on;
title('C11\_E02 - PID discreto incremental');
subplot(2,1,2); stairs(t, us);
xlabel('t (s)'); ylabel('u (saturada)'); grid on;
