#include <math.h>

int himmelblau(float* x, float* y){

    float t1 = pow(x[0] * x[0] + x[1] - 11, 2);
    float t2 = pow(x[0] + x[1] * x[1] - 7, 2);
    *y = t1 + t2;

    return 0;
}