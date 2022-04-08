#include <iostream>
#include <cmath>
#include <random>
#include <chrono>
#include <thread>
#include <windows.h>
#include <time.h>
using namespace std;

// global random generators
unsigned seed1 = std::chrono::system_clock::now().time_since_epoch().count();
default_random_engine gen(seed1);
default_random_engine generator;
normal_distribution<double> normal(0.0, 1.0);
uniform_real_distribution<double> uniform_01(0.0, 1.0);
uniform_real_distribution<double> uniform_distribution(-5, 5);

// constants
const int n_dims = 2;
const double bounds[][2] = {{-5, 5}, {-5, 5}};


double himmelblau(double x[2]){

    double t1 = pow(pow(x[0], 2) + x[1] - 11, 2);
    double t2 = pow(x[0] + pow(x[1], 2) - 7, 2);
    return t1 + t2;

}

double ackley(double x[2]){
    double t1 = -20 * exp(-0.2 * sqrt(0.5 * (pow(x[0], 2) + pow(x[1], 2))));
    double t2 = -exp(0.5 * (cos(2 * M_PI * x[0]) + cos(2 * M_PI * x[1])));
    return t1 + t2 + exp(1.0) + 20;
}

double styblinski_tang(double x[2]){
    double t1 = pow(x[0], 4) - 16 * x[0] * x[0] + 5 * x[0];
    double t2 = pow(x[1], 4) - 16 * x[1] * x[1] + 5 * x[1];
    return (t1 + t2) / 2.0;
}

double rastrigini(double x[2]){
    double t1 = x[0]*x[0] - 10 * cos(2 * M_PI * x[0]);
    double t2 = x[1]*x[1] - 10 * cos(2 * M_PI * x[1]);
    return t1 + t2 + 20;
}

double quadratic(double x[2]){
    return pow(x[0], 2) + pow(x[1], 2);
}


void get_neighbour(double x[n_dims], double* v){

    double g;
    for(int i=0; i<n_dims; i++){
        g = normal(generator) + x[i];
        if(g < bounds[i][0]) g = bounds[i][0];
        if(g > bounds[i][1]) g = bounds[i][1];
        v[i] = g;
    }
}

void SA(double (*func)(double*), double T0, int iters_T, double solution[2]){

    double x[n_dims];
    for(int i=0; i<n_dims; i++){
        x[i] = uniform_distribution(generator);
    }

    double T = T0;
    int k = 1;
    double yk[n_dims];
    double p, r;

    while(T >= 1e-3){
        for(int i=0; i<iters_T; i++){
            get_neighbour(x, yk);

            if(func(yk) < func(x)){
                for(int j=0; j<n_dims; j++) x[j] = yk[j];
            }else{
                r = uniform_01(generator);
                if(exp(-(func(yk) - func(x)) / T) > r){
                    for(int j=0; j<n_dims; j++) x[j] = yk[j];
                }
            }
        }
        T = T0 * pow(0.997, k);
        k += 1;
    }

    for(int i=0; i<n_dims; i++) solution[i] = x[i];


    // cout << "Final solution: ";
    // for(int j=0; j<n_dims; j++) cout << x[j] << " ";
    // cout << "Final value: " << func(x) << " Final Temperature: " << T << endl;

}

int main(){

    //double T = 1;
    int N = 100;
    double T_max = 1000;
    double x[2];
    double distance_sum = 0;

    for(int i=0; i<N; i++){
        auto t1 = chrono::high_resolution_clock::now();
        SA(&rastrigini, T_max, 10, x);
        auto t2 = chrono::high_resolution_clock::now();

        //distance_sum += sqrt(x[0] * x[0] + x[1] * x[1]);

        cout << chrono::duration_cast<chrono::milliseconds>(t2 - t1).count() / 1000.0 << endl;;
    }

    cout << "Mean distance: " << distance_sum / N << endl;

    return 0;
}
