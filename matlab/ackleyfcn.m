function y = ackleyfcn(x)
    t1 = -20 * exp(-0.2 * sqrt(0.5 * (x(1)*x(1) + x(2)*x(2))));
    t2 = -exp(0.5 * (cos(2*pi*x(1)) + cos(2*pi*x(2))));
    y = t1 + t2 + exp(1) + 20;
end