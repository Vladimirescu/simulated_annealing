#include <math.h>


int styblinski_tang(float* x, float* y){
    float t1 = pow(x[0], 4) - 16 * x[0] * x[0] + 5 * x[0];
    float t2 = pow(x[1], 4) - 16 * x[1] * x[1] + 5 * x[1];
    *y = (t1 + t2) / 2.0;

    return 0;
}