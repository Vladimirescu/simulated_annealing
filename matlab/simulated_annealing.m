clear all; clc; 

N = 100;
x_optim = [0 0];
T = zeros(1, N);
d = zeros(1, N);

options = optimoptions('simulannealbnd', ...
    'Initialtemperature', 1000, ...
    'TemperatureFcn', @tempHandle, ...
    'AnnealingFcn', @generatePoints);

for i=1:N
    x0 = [unifrnd(-5, 5) unifrnd(-5, 5)];
    tic
    x = simulannealbnd(@rastrigini, x0, -5, 5, options);
    T(i) = toc;
    d(i) = sqrt(sum((x - x_optim).^2));
end

disp('Medie timp');
disp(mean(T));
disp("Dispersie timp");
disp(std(T));
disp("Distanta medie");
disp(mean(d));






