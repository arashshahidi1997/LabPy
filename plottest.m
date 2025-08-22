% plottest.m
% Simple test plot in MATLAB

x = linspace(0, 2*pi, 100);
y = sin(x);

figure;
plot(x, y, 'b-', 'LineWidth', 2);
xlabel('x');
ylabel('sin(x)');
title('Test Plot of sin(x)');
grid on;