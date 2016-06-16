/*
    Adjusting weights for Adaline Neuron by steepest Descent
    Multiple Inputs - One Output

    @author Oscar Esaú Peralta Rosales
    @email esau.opr@gmail.com
*/

#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string.h>
#include <time.h>
#include "processInput.cpp"

using namespace std;

void readParams( int *T, long double *miu, int *factorMiu, int *M ); // Read algorithm parameters
void help();  // Show the program help

vector<long double> autoregressiveParameters( vector<vector<long double> > X ); // Adjusting weights by steepest Descent

int main(int argc, char const *argv[]) {

    vector<vector<long double> > X; // Data input, the las element of the each row i represents the value di
    vector<long double> A; // Weights
    if ( argc < 2 ) {
        printf("Error: Enter a input file as argument\n");
        help();
        exit( EXIT_FAILURE );
    }

    srand(time(NULL));
    X = readInput( argv[1]);
    //printf("n = %d,  p = %d\n", n, p );
    //printVec( X );

    A = autoregressiveParameters( X );

    vector<long double> NV;
    for (int n = 1 ; n < X.size(); n++ ) {
        long double x = 0.0;

        if( n < A.size() ) {
            NV.push_back( X[n][1] );
        }
        else {
            for (int k = 0; k < A.size(); k++) {
                x += A[k] * X[n-k][1];
            }
            NV.push_back( x );
        }
    }

    puts("Solución");
    printVecCF( A );
    printVecNF(NV);

    exit(EXIT_SUCCESS);
}

// Adjusting weights by steepest Descent
vector<long double> autoregressiveParameters( vector<vector<long double> > X ) {
    int T, M; // Number of presentations, model order
    int N = X.size(), P = X[0].size() - 1;
    long double miu;
    int factorMiu;
    vector<long double> A; // Solution weights
    vector<long double> MSE;

    readParams( &T, &miu, &factorMiu, &M );
    printf("T = %d, miu = %lf, factorMiu = %d, M = %d\n", T, miu, factorMiu, M );

    A.resize( M );
    for (int i = 0; i < M; i++) {
        A[i] = 2 - (long double)( rand() % 10 ) / 5.0;
    }

    puts("Solución inicial");
    printVecCF( A );
    //printVec( X );

    for (int i = 0; i < T; i++) {
        for (int n = M ; n < N; n++ ) {

            long double x = 0.0;

            for (int k = 0; k < M; k++) {
                x += A[k] * X[n-k][1];
            }
            long double error = X[n][1] - x;

            //printf("%lf - %lf\n", X[n][1] , x );

            vector<long double> D_A;
            D_A.resize( M );

            for (int k = 0; k < M; k++) {
                D_A[k] = 2 * miu * error * X[n-k][1];
                A[k] += D_A[k];
            }

            //printVec( A );

            if ( n % factorMiu == 0) {
                miu /= 1.01;
            }

        }

        long double mse = 0.0;
        for (int n = M ; n < N; n++ ) {
            long double x = 0.0;

            for (int k = 0; k < M; k++) {
                x += A[k] * X[n-k][1];
            }
            long double error = X[n][1] - x;
            mse += error * error;
        }

        mse /= N - M;
        printf("%Lf\n", mse );
    }
    //printVecNF(MSE);

    return A;
}

// Reading parameters
void readParams( int *T, long double *miu, int *factorMiu, int *M ) {
    FILE *file = NULL;

    file = fopen( "config", "r" );
    if( file == NULL ) {
		printf("Error: The config file does not exist\n");
		exit(EXIT_FAILURE);
	}

    *miu = nextParam( file );
    *factorMiu = (int)nextParam( file );
    *T = (int) nextParam( file );
    *M = (int) nextParam( file );

    fclose( file );
}

// Show the program help
void help() {
    printf("\nHow to use:\n");
    printf("\n\tAutoregressiveParameters [file_input]\n" );
}
