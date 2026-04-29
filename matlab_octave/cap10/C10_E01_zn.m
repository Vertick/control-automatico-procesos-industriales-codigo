% =====================================================================
% C10_E01 — Sintonias Z-N, Lambda, SIMC sobre el mismo FOPDT
% =====================================================================
% Capitulo: 10 - Sintonia de PID y diagnostico de lazos
% Origen UNIR: ejemplo_optimizacion_PID.m
% Notebook Python equivalente: python/cap10/C10_E01_sintonias_zn_lambda_simc.ipynb
% Compatibilidad: MATLAB con Control System Toolbox; Octave con control
% =====================================================================

clear; close all;
% pkg load control          % Octave

K = 0.8; tau = 600; theta = 60;

% Z-N por curva de reaccion (PI)
Kc_zn = 0.9*tau/(K*theta); Ti_zn = 3.33*theta;
% Lambda con lambda = theta
lam = theta; Kc_l = tau/(K*(lam+theta)); Ti_l = tau;
% SIMC con lambda = theta
Kc_s = (1/K)*tau/(theta + theta); Ti_s = min(tau, 4*(theta+theta));

fprintf('Z-N:    Kc=%.3f, Ti=%.1f\n', Kc_zn, Ti_zn);
fprintf('Lambda: Kc=%.3f, Ti=%.1f\n', Kc_l, Ti_l);
fprintf('SIMC:   Kc=%.3f, Ti=%.1f\n', Kc_s, Ti_s);

% Aproximacion Pade del retardo
[num_pade, den_pade] = pade(theta, 1);
G = tf([K], [tau, 1]) * tf(num_pade, den_pade);

t = linspace(0, 4000, 1500);
figure; hold on;
sets = {Kc_zn, Ti_zn, 'Z-N';
        Kc_l,  Ti_l,  'Lambda';
        Kc_s,  Ti_s,  'SIMC'};
for i = 1:size(sets, 1)
    Kc = sets{i,1}; Ti = sets{i,2};
    PI = tf([Kc*Ti, Kc], [Ti, 0]);
    Tcl = feedback(PI*G, 1);
    y = step(Tcl, t);
    iae = trapz(t, abs(1 - y));
    plot(t, y, 'DisplayName', sprintf('%s (IAE=%.0f)', sets{i,3}, iae));
end
yline(1.0, '--', 'Color', [0.5 0.5 0.5]);
xlabel('t (s)'); ylabel('y/SP');
legend; grid on;
title('C10\_E01 - Z-N vs Lambda vs SIMC');
