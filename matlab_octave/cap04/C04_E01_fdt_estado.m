% =====================================================================
% C04_E01 — FDT, espacio de estados y polos (MATLAB / Octave)
% =====================================================================
% Capitulo: 4 - Funciones de transferencia, Laplace y espacio de estados
% Origen UNIR: ejemplo_FDT.m, ejemplo_FDT-1.m, ejemplo_residuos.m,
%              ejemplo_TFI.m, Untitled.m, untitled2.m, Tema_3.m
% Notebook Python equivalente: python/cap04/C04_E01_fdt_estado_polos.ipynb
% Compatibilidad: MATLAB con Control System Toolbox; Octave con paquete control
% =====================================================================

clear; close all;
% pkg load control          % descomentar en Octave

% FDT en serie: planta + sensor
G = tf([1.0], [10.0, 1.0]);     % planta de primer orden
H = tf([1.0], [0.5, 1.0]);      % sensor con dinamica
L = G*H;

disp('Polos FDT:'); disp(pole(L));
disp('Ceros FDT:'); disp(zero(L));

% Conversion a espacio de estados
ss_sys = ss(L);
disp('Matriz A:'); disp(ss_sys.A);
disp('Autovalores de A:'); disp(eig(ss_sys.A));

% Mapa de polos y ceros
figure;
pzmap(L); grid on;
title('C04\_E01 - Mapa de polos y ceros de G*H');

% --- Apartado adicional: transformada inversa de Laplace (deriva de ejemplo_TFI.m)
% Solo MATLAB con Symbolic Math Toolbox o Octave con symbolic
if exist('syms', 'file') == 2
    syms s t
    X = 1/s * 1/(s^2 + 4*s + 3);
    x = ilaplace(X);
    disp('Transformada inversa simbolica:');
    pretty(x)
end

% --- Apartado adicional: residuos (deriva de ejemplo_residuos.m)
p_n = [1 -1];
p_d = [1 7 18 20 8];
[r, p, k] = residue(p_n, p_d);
disp('Residuos r:'); disp(r);
disp('Polos p:');    disp(p);
disp('Termino directo k:'); disp(k);
