#include <math.h>


int rastrigini(float* x, float* y){
    float t1 = x[0] * x[0] - 10 * cos(2 * M_PI * x[0]);
    float t2 = x[1] * x[1] - 10 * cos(2 * M_PI * x[1]);
    *y = t1 + t2 + 20;

    return 0;
}