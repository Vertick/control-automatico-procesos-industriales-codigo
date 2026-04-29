% =====================================================================
% C09_E01 — PID con saturacion y antiwindup (MATLAB / Octave)
% =====================================================================
% Capitulo: 9 - Control PID en la practica industrial
% Notebook Python equivalente: python/cap09/C09_E01_pid_antiwindup.ipynb
% Compatibilidad: MATLAB / Octave estandar (sin toolbox)
% =====================================================================

clear; close all;

% Planta primer orden discreto
K = 2.0; tau = 10.0;
% Parametros PID
Kp = 2.0; Ki = 0.5; Kd = 0.0;
% Limites del actuador
umin = 0; umax = 1.5;

T = 100; dt = 0.1; N = T/dt;
SP = 5.0;

% Simulacion con y sin antiwindup
ys = zeros(N, 2); us = zeros(N, 2);
for caso = 1:2
    antiwindup = (caso == 1);
    Tt = 1.0; if ~antiwindup, Tt = 1e9; end
    y = 0; e_prev = 0; I = 0;
    for k = 1:N
        e = SP - y;
        P = Kp*e;
        I = I + Ki*e*dt;
        D = Kd*(e - e_prev)/dt;
        u_unsat = P + I + D;
        u_sat = max(umin, min(umax, u_unsat));
        I = I + (u_sat - u_unsat)*dt/Tt;   % antiwindup back-calculation
        e_prev = e;
        y = y + dt*(K*u_sat - y)/tau;
        ys(k, caso) = y; us(k, caso) = u_sat;
    end
end

t = (0:N-1)*dt;
figure;
subplot(2,1,1);
plot(t, ys(:,1), 'DisplayName', 'Con antiwindup'); hold on;
plot(t, ys(:,2), '--', 'DisplayName', 'Sin antiwindup');
yline(SP, ':', 'DisplayName', 'Consigna');
ylabel('y'); legend; grid on;
title('C09\_E01 - PID con/sin antiwindup');

subplot(2,1,2);
plot(t, us(:,1), 'DisplayName', 'u (antiwindup)'); hold on;
plot(t, us(:,2), '--', 'DisplayName', 'u (sin antiwindup)');
yline(umax, ':', 'Color', 'r', 'DisplayName', 'Saturacion');
xlabel('t (s)'); ylabel('u'); legend; grid on;
