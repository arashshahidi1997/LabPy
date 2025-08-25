% Generate a noisy sinusoid and plot it

% Parameters
fs = 1000;           % Sampling frequency (Hz)
t = 0:1/fs:1;        % Time vector (1 second)
f = 5;               % Frequency of sinusoid (Hz)
A = 1;               % Amplitude

% Generate clean sinusoid
y_clean = A * sin(2*pi*f*t);

% Add Gaussian noise
noise_level = 0.3;   % Adjust noise amplitude
y_noisy = y_clean + noise_level * randn(size(t));

% Plot
figure;
plot(t, y_noisy, 'b');
hold on;
plot(t, y_clean, 'r--', 'LineWidth', 1);
xlabel('Time (s)');
ylabel('Amplitude');
title('Noisy Sinusoid');
legend('Noisy Signal', 'Clean Sinusoid');
grid on;