% =====================================================================
% C07_E01 — Lugar de raices (MATLAB / Octave)
% =====================================================================
% Capitulo: 7 - Lugar de raices y diseno clasico
% Origen UNIR: ejemplo_rootlocus-2.m
% Notebook Python equivalente: python/cap07/C07_E01_root_locus.ipynb
% Compatibilidad: MATLAB con Control System Toolbox; Octave con paquete control
% =====================================================================

clear; close all;
% pkg load control          % descomentar en Octave

% Planta de segundo orden (consistente con notebook Python)
G = tf([0.5], [20.0, 12.0, 1.0]);

% Trazado del LDR
figure;
rlocus(G); grid on;
title('C07\_E01 - Lugar de raices de G(s)');

% Diseno: encontrar Kc para zeta objetivo
zeta_target = 0.7;
[Kc_target, ~] = rlocfind(G, complex(-1, 1));   % interactivo en MATLAB
% Alternativa no interactiva: barrido
kvect = linspace(0.1, 20, 200);
roots_all = rlocus(G, kvect);
% Buscar el Kc cuyo polo dominante complejo tenga zeta mas cercano a 0.7
zeta_dom = NaN(size(kvect));
for i = 1:length(kvect)
    rs = roots_all(:, i);
    rs_complex = rs(imag(rs) ~= 0);
    if ~isempty(rs_complex)
        [~, idx] = min(abs(imag(rs_complex)));
        r = rs_complex(idx);
        wn = abs(r);
        zeta_dom(i) = -real(r)/wn;
    end
end
[~, idx_target] = min(abs(zeta_dom - zeta_target));
fprintf('Kc para zeta=0.7: %.3f\n', kvect(idx_target));
