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
#include <math.h>
#include "processInput.cpp"

using namespace std;

void readParams( int *T, double *miu ); // Read algorithm parameters
void help();  // Show the program help

vector<double> steepestDescent( vector<vector<double> > X, int T, int N, int P, double miu, int pos, int level); // Adjusting weights by steepest Descent
double evalua( vector<double> W, vector<double> xi );
bool evaluaRed( vector<vector<double> > cIn, vector<double> cOut, vector<double> xi );

vector<double> nextVector( int num, int tam) {
    vector<double> xi;
    xi.push_back(1.0);
    for(int i = 0; i < tam; i++ ) {
        double t = (double)(num & 1);
        num = num >> 1;
        xi.push_back(t);
    }
    printVecNF(xi);
    return xi;
}

int main(int argc, char const *argv[]) {

    int nCin = 0;
    int T,P;
    double miu = 0.05;
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
    readParams(&T, &miu);
    printf("Número de Presentaciones: %d, Factor escalamiento: %lf\n", T, miu );
    printVec(X);

    P = X[0].size() - 1;
    // Capa de entrada
    for (int i = 0; i < X.size(); i++) {
        if( X[i][P] == 1.0 ) {
            nCin ++;
            W = steepestDescent( X, 100, X.size(), P, miu, i, -1 );
            cIn.push_back( W );
        }
    }

    //*
    for( int k=0; k < cIn.size(); k++ ) {
        for (int i = 0; i < X.size(); i++) {
            //printVec(cIn[0]);
            printVecNF( X[i] );
            printf("sol = %lf\n\n", evalua( cIn[k], X[i] ) );
        }
        puts("---------------");
    }
    
    //*/
    //return 0;
    //Capa de Salida
    cOut = steepestDescent( X, T, (int)pow(2.0, nCin), nCin+1, miu, 0, 1 );

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
        //printVecNF(X[i]);
        evaluaRed(cIn, cOut, X[i]);
    }

    exit(EXIT_SUCCESS);
}

// Adjusting weights by steepest Descent
vector<double> steepestDescent( vector<vector<double> > X, int T, int N, int P, double miu, int pos, int level) {
    
    vector<double> W; // Solution weights

    W.resize( P );
    for (int i = 0; i < P; i++) {
        //W[i] = 2 - ( ( rand() % 2 ) == 0 ) ? 1 : -1;
        W[i] = 2 - (long double)( rand() % 10 ) / 5.0;
    }

    for (int t = 0; t < T; t++) {
        double mse = 0.0;
        for (int m = 0; m < N; m++) {
            // Getting the error of each xi
            double error = 0.0;
            if ( level == -1 ) {
                for (int i = 0; i < P; i++) {
                    error += W[i] * X[m][i];
                }
            }
            else {
                vector<double> xt = nextVector(m, P - 1);
                for (int i = 0; i < P; i++) {
                    error += W[i] * xt[i];
                }   
            }
            
            if( m == pos ) {
                error = 1.0 - error;
            }
            else {
                error = -1.0 - error;
            }
            mse += error * error / 2.0;
            // Computing the gradient
            vector<double> D_Wm;
            D_Wm.resize( P );
            for (int i = 0; i < P; i++) {
                D_Wm[i] = 2 * error * X[m][i] * miu;
                W[i] += D_Wm[i];
            }

            miu /= 1.01;
        }
        printf("e = %lf\n", mse);
    }
    puts("-----------");

    return W;
}

double evalua( vector<double> W, vector<double> xi ) {
    double sum = 0.0;
    //printVecNF(W);
    for (int i = 0; i < W.size(); i++) {
        sum += W[i] * xi[i];
       // printf(" + %lf * %lf\n", W[i], xi[i] );
    }
    //puts("");
    return sum;
}

bool evaluaRed( vector<vector<double> > cIn, vector<double> cOut, vector<double> xi ) {
    vector<double> xn;
    xn.push_back( 1.0 );

    for (int i = 0; i < cIn.size(); i++) {
        double sum = evalua( cIn[i], xi);
        //printVec(xi);
        printf("Neu %d:  %lf\n", i+1, sum );
        if ( sum > 0 ) {
            xn.push_back( 1.0 );
        }
        else {
            xn.push_back( -1.0 );   
        }
    }

    double sum = evalua( cOut, xn );
    printf("Neu %d:  %lf\n", cIn.size() + 1, sum );

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

// Reading parameters
void readParams( int *T, double *miu ) {
    FILE *file = NULL;

    file = fopen( "config", "r" );
    if( file == NULL ) {
        printf("Error: The config file does not exist\n");
        exit(EXIT_FAILURE);
    }

    *T = (int) nextParam( file );
    *miu = nextParam( file );

    fclose( file );
}