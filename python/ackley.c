#include <math.h>
//extern "C"

int ackley(float* x, float* y){
    float t1 = -20 * exp(-0.2 * sqrt(0.5 * (x[0] * x[0] + x[1] * x[1])));
    float t2 = -exp(0.5 * (cos(2 * M_PI * x[0]) + cos(2 * M_PI * x[1])));
    //return t1 + t2 + exp(1.0) + 20;
    *y = t1 + t2 + exp(1.0) + 20;

    return 0;
}
