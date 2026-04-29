% =====================================================================
% C03_E02 — Ajuste FOPDT por curva de reaccion (MATLAB / Octave)
% =====================================================================
% Capitulo: 3 - Modelado basico de procesos para control
% Origen UNIR: Tema 5 - Analisis dinamico en lazo abierto
% Notebook Python equivalente: python/cap03/C03_E02_ajuste_fopdt.ipynb
% Compatibilidad: MATLAB R2022a+ (Optimization Toolbox), Octave 7+ (optim)
% =====================================================================

clear; close all;
rng(0);

% Definicion de FOPDT: y(t) = K*(1 - exp(-(t-theta)/tau)) para t > theta
fopdt = @(p, t) max(0, p(1) * (1 - exp(-(t - p(3))./p(2))) .* (t > p(3)));

% Datos sinteticos: K=2, tau=15, theta=5 con ruido
t = linspace(0, 100, 200)';
y_real = fopdt([2.0, 15.0, 5.0], t) + 0.05*randn(size(t));

% Ajuste no lineal (lsqcurvefit en MATLAB; en Octave usa fminunc o nonlin_curvefit)
p0 = [1.0, 10.0, 1.0];
if exist('lsqcurvefit', 'file') == 2
    p_hat = lsqcurvefit(fopdt, p0, t, y_real);
else
    % Fallback Octave
    cost = @(p) sum((fopdt(p, t) - y_real).^2);
    p_hat = fminsearch(cost, p0);
end

fprintf('K     = %.4f  (real 2.0)\n', p_hat(1));
fprintf('tau   = %.4f  (real 15.0)\n', p_hat(2));
fprintf('theta = %.4f  (real 5.0)\n', p_hat(3));

% Visualizacion
figure;
plot(t, y_real, '.', 'DisplayName', 'Datos con ruido'); hold on;
plot(t, fopdt(p_hat, t), '-', 'LineWidth', 1.5, ...
     'DisplayName', sprintf('FOPDT ajustado: K=%.2f, tau=%.2f, theta=%.2f', ...
                            p_hat(1), p_hat(2), p_hat(3)));
grid on; legend('Location', 'best');
xlabel('Tiempo (s)'); ylabel('Salida');
title('C03\_E02 - Ajuste FOPDT por curva de reaccion');
