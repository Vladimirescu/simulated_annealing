function t = tempHandle(optimValues, options)
    t = options.InitialTemperature .* 0.997.^optimValues.k;
end