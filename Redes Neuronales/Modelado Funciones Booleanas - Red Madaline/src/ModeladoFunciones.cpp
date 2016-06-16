/*
    Modelado de Funciones Booleanas

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

void readParams( int *T, double *miu, double *factorMiu ); // Read algorithm parameters
void help();  // Show the program help

vector<double> steepestDescent( vector<vector<double> > X, int T, int N, int P, double miu ); // Adjusting weights by steepest Descent
vector<vector<double> > construcPoints( vector<double> a );
vector<double> orientacion( vector<double> W, vector<double> xi, int ori );
double evalua( vector<double> W, vector<double> xi );
bool evaluaRed( vector<vector<double> > cIn, vector<double> cOut, vector<double> xi );


int main(int argc, char const *argv[]) {

    int nCin = 0;
    int P;
    double miu = 0.000005;
    vector<vector<double> > X; // Data input, the las element of the each row i represents the value di
    vector<double> W; // Weights
    vector<vector<double> > points;
    vector<vector<double> > cIn;
    vector<double> cOut;

    if ( argc < 2 ) {
        printf("Error: Enter a input file as argument\n");
        help();
        exit( EXIT_FAILURE );
    }
    
    srand(time(NULL));
    X = readInput( argv[1]);
    printVec(X);

    P = X[0].size() - 1;
    // Capa de entrada
    for (int i = 0; i < X.size(); i++) {
        if( X[i][P] == 1.0 ) {
            nCin ++;
            points = construcPoints( X[i] );
            puts("Puntos");
            printVec( points );
            W = steepestDescent( points, 1, points.size(), P, miu );
            W = orientacion( W, X[i], 1 );
            cIn.push_back( W );
        }
    }

    // Capa de Salida
    vector<double> xi;
    xi.push_back(1);
    for (int i = 1; i < P ; i++) {
        xi.push_back( -1.0 );
    }
    xi.push_back(1);

    points = construcPoints( xi );
    puts("Puntos");
    printVec( points );
    cOut = steepestDescent( points, 1, 1, P, miu );
    cOut = orientacion( cOut, xi, -1 );


    // Imprimiendo Solución
    puts("Capa de entrada:");
    printf("Número de Neuronas: %d\n", cIn.size() );
    for (int i = 0; i < cIn.size(); i++) {
        printf("Neurona %i:\n", i+1);
        printVec( cIn[i] );
    }

    puts("\nCapa de Salida:");
    printf("Neurona 1:\n");
    printVec( cOut );

    puts("\nEvaluación de la Red");

    for (int i = 0; i < X.size(); i++) {
        evaluaRed(cIn, cOut, X[i]);
    }
    
    exit(EXIT_SUCCESS);
}

// Adjusting weights by steepest Descent
vector<double> steepestDescent( vector<vector<double> > X, int T, int N, int P, double miu ) {
    
    vector<double> W; // Solution weights

    W.resize( P );
    for (int i = 0; i < P; i++) {
        //W[i] = 2 - ( ( rand() % 2 ) == 0 ) ? 1 : -1;
        W[i] = 2 - (long double)( rand() % 10 ) / 5.0;
    }

    for (int t = 0; t < T; t++) {
        for (int m = 0; m < N; m++) {
            // Getting the error of each xi
            double error = 0.0;
            for (int i = 0; i < P; i++) {
                error += W[i] * X[m][i];
            }
            // The las element of the each row of X represents the value di
            error = X[m][P] - error;

            // Computing the gradient
            vector<double> D_Wm;
            D_Wm.resize( P );
            for (int i = 0; i < P; i++) {
                D_Wm[i] = 2 * error * X[m][i] * miu;
            }
            for (int i = 0; i < P; i++) {
                W[i] += D_Wm[i];
            }
        }
    }

    return W;
}

vector<vector<double> > construcPoints( vector<double> a ) {
    vector<vector<double> > X;

    int d = a.size();
    a[d-1] = 0;
    double inc;
    for (int i = 1; i < d - 1; i++) {
        if ( a[i] == -1.0 ) {
            inc = 1;
        }
        else {
            inc = -1;   
        }

        a[i] += inc;
        X.push_back( a );
        a[i] -= inc;
    }

    return X;
}

double evalua( vector<double> W, vector<double> xi ) {
    double sum = 0.0;
    for (int i = 0; i < W.size(); i++) {
        sum += W[i] * xi[i];
    }
    return sum;
}

vector<double> orientacion( vector<double> W, vector<double> xi, int ori ) {
    double sum = evalua( W, xi );

    if( ori == 1 && sum < 0 || ori == -1 && sum > 0 ) {
        for (int i = 0; i < W.size(); i++) {
            W[i] *= -1;
        }        
    }
    return W;
}

bool evaluaRed( vector<vector<double> > cIn, vector<double> cOut, vector<double> xi ) {
    vector<double> xn;
    xn.push_back( 1.0 );

    for (int i = 0; i < cIn.size(); i++) {
        double sum = evalua( cIn[i], xi);
        //printVec(xi);
        //printf("Sum %d:  %lf\n", i+1, sum );
        if ( sum > 0 ) {
            xn.push_back( 1.0 );
        }
        else {
            xn.push_back( -1.0 );   
        }
    }

    double sum = evalua( cOut, xn );

    for (int j = 1; j < xi.size() - 1; j++) {
        printf("%2d ", (int)xi[j] );
    }

    if( sum > 0 ) {
        printf("=>  1\n");
    }
    else {
        printf("=> -1\n");
    }

}

// Show the program help
void help() {
    printf("\nHow to use:\n");
    printf("\n\tSteepestDescent [file_input]\n" );
}
