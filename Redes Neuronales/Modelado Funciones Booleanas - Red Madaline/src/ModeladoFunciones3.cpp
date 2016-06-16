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

// Show the program help
void help() {
    printf("\nHow to use:\n");
    printf("\n\tSteepestDescent [file_input]\n" );
}

vector<double> nextVector( int num, int tam) {
    vector<double> xi;
    xi.push_back(1.0);
    for(int i = 0; i < tam; i++ ) {
        double t = (double)(num & 1);
        num = num >> 1;
        xi.push_back(t);
    }
    return xi;
}

// Adjusting weights by steepest Descent
vector<double> steepestDescent( vector<vector<double> > X, int T, int N, int P, double miu, int nNeu, bool autogen = false) {
    vector<double> W; // Solution weights

    W.resize( P );
    for (int i = 0; i < P; i++) {
        //W[i] = 2 - ( ( rand() % 2 ) == 0 ) ? 1 : -1;
        W[i] = 1 - (long double)( rand() % 11 ) / 5.0;
    }

    for (int t = 0; t < T; t++) {
    	double mse = 0.0;

        for (int m = 0; m < N; m++) {
            // Getting the error of each xi

            double error = 0.0;
            if ( autogen == false ) {
            	for (int i = 0; i < P; i++) {
                	error += W[i] * X[m][i];
            	}	
            }
            else {
            	vector<double> xt = nextVector( m, P -1 );
            	for (int i = 0; i < P; i++) {
                	error += W[i] * xt[i];
            	}	
            }
            
            if( m == nNeu ) {
            	//printf("%d\n", m );
            	//vector<double> xt = nextVector( m, P -1 );
            	//printVecNF( xt );
            	if( autogen == false ) {
            		error = 1.0 - error;
            	}
            	else {
            		error = -1.0 - error;	
            	}
            }
            else {
            	if( autogen == false ) {
            		error = -1.0 - error;
            	}
            	else {
            		error = 1.0 - error;
            	}
            }
            mse += error * error / 2.0;
            // Computing the gradient
            vector<double> D_Wm;
            D_Wm.resize( P );
            for (int i = 0; i < P; i++) {
            	if ( autogen == false ) {
            		D_Wm[i] = 2 * error * X[m][i] * miu;	
            	}
            	else {
            		vector<double> xt = nextVector( m, P -1 );
            		D_Wm[i] = 2 * error * xt[i] * miu;
            	}
                
                W[i] += D_Wm[i];
            }
        }
        miu /= 1.001;
        printf("%lf\n", mse );
    }
    puts("");

    return W;
}

double evalua( vector<double> W, vector<double> xi ) {
    double sum = 0.0;
    for (int i = 0; i < W.size(); i++) {
        sum += W[i] * xi[i];
    }
    return sum;
}

int main(int argc, char const *argv[])
{
	int T, P, N;
	int nNeu = 0;
	double miu;

	vector<vector<double> > X; // Data input, the las element of the each row i represents the value di
    vector<double> W; // Weights
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
    P = X[0].size() - 1;
    N = X.size();

    printf("Número de Presentaciones: %d, Factor escalamiento: %lf\n", T, miu );
    printf("P = %d, N =  %d\n", P, N );
    printVec(X);

    for (int i = 0; i < N; i++) {
    	if( X[i][P] == 1 ) {
    		printf("Error Neurona %d\n", nNeu+1);
    		W = steepestDescent( X, T, N, P, miu, i );
    		cIn.push_back( W );
    		nNeu++;
    	}
    }

    // Capa de Entrada
    puts("Capa de Entrada");
    for (int k = 0; k < nNeu; k++){
    	printf("Neurona %d:\n", k+1);
    	printVec(cIn[k]);
    	vector<double> xt;
	    for (int i = 0; i < N; i++) {
	    	for (int j = 1; j < P ; j++) {
	    		printf("%2d ", (int)X[i][j]);
	    	}
	    	double z = evalua( cIn[k], X[i] );
	    	printf("=> %lf\n", z );
	    }
    }
    
    // Capa de Salida
    puts("\nCapa de Salida");
    int Ns = (int)pow( 2, nNeu );
    printf("Error Neurona %d:\n", nNeu + 1);
    cOut = steepestDescent( X, T, Ns, nNeu + 1, miu, 0, true );

    printf("Neurona %d:\n", nNeu + 1);
    printVec( cOut );
    
    vector<double> vZ;
    for ( int i = 0; i < N; i++ ) {

    	vZ.clear();
    	vZ.push_back(1.0);
    	for(int j = 0; j < nNeu; j++ ) {
    		vZ.push_back( evalua( cIn[j], X[i] ) );
    		
    		if ( vZ[ vZ.size() - 1 ] > 0 ) {
    			vZ[ vZ.size() - 1 ] = 1.0;
    		}
    		else {
    			vZ[ vZ.size() - 1 ] = -1.0;	
    		}
    		//printf("%2d ", (int)vZ[ vZ.size() - 1 ]);
    	}
    	for (int j = 1; j < P ; j++) {
	    		printf("%2d ", (int)X[i][j]);
	    }
    	printf("=> %lf\n", evalua( cOut, vZ ) );
    }


	return 0;
}