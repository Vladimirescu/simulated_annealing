function y = rastrigini(x)
    t1 = x(1)^2 - 10 * cos(2 * pi * x(1));
    t2 = x(2)^2 - 10 * cos(2 * pi * x(2));
    y = t1 + t2 + 20;
end