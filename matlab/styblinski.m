function y = styblinski(x)
    t1 = x(1)^4 - 16 * x(1)^2 + 5 * x(1);
    t2 = x(2)^4 - 16 * x(2)^2 + 5 * x(2);
    y = (t1 + t2) / 2;
end