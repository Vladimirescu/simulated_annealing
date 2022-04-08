function y = generatePoints(optimValues, problem)
    x_now = optimValues.x;
    y = x_now + randn(1, length(x_now));
    y(y > problem.ub(1)) = problem.ub(1);
    y(y < problem.lb(1)) = problem.lb(1);
end