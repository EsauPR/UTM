/*
    Retropropagación

    @author Oscar Esaú Peralta Rosales
    @email esau.opr@gmail.com
*/

#include <math.h>
#include <time.h>
#include <vector>
#include "dir.cpp"
#include "image.cpp"
#include "processInput.cpp"

using namespace std;

void help();  // Show the program help
void backpropagation( char * baseDir );
void propagation(int n1, int n2, int n3, vector<vector<double> > W_hidden, vector<vector<double> > W_output, vector<double> X, double *a, double *O, int gcase);
void getParams( int *n1, int *n2, int *n3, double *miu, int *L, int *gcase ); // Obtiene parámetros de Entrenamiento
double g( double z, int gcase ); // functiones de activacion
double Dg( double z, int gcase ); // Derivada de la función de activación
vector<vector< double > > initWeight( int n, int m ); // Inicializa una matriz de pesos

int main(int argc, char const *argv[]) {

    if ( argc < 2 ) {
        printf("Error: Enter a input file as argument\n");
        help();
        exit( EXIT_FAILURE );
    }

    srand(time(NULL));

    backpropagation( (char*)argv[1] );
    puts("passF");

    return 0;
}

void propagation(int n1, int n2, int n3, vector<vector<double> > W_hidden, vector<vector<double> > W_output, vector<double> X, double *a, double *O, int gcase) {
    double I[n1];

    // Capa de entrada
    for (int k = 0; k < n1; k++) {
        I[k] = X[k];
    }


    for (int j = 0; j < n2; j++) {
        double ent_j = 0;
        for (int k = 0; k < n1; k++){
            ent_j += W_hidden[j][k] * I[k];
        }
        //a[j] = g( ent_j, gcase );
        a[j] = ent_j;
    }

    // Capa de Salida
    for (int i = 0; i < n3; i++) {
        double ent_i = 0;
        for (int j = 0; j < n2; j++) {
            ent_i += W_output[i][j] * a[j];
        }
        //O[i] = g( ent_i, gcase );
        O[i] = ent_i;
    }
}

void backpropagation( char * baseDir ) {
    int n1, n2, n3, EValue, L, gcase;
    double miu;
    double I[n1], a[n2], O[n3]; // Valores de la sumatoria de salida

    getParams( &n1, &n2, &n3, &miu, &L, &gcase );
    //printf("%d %d %d %lf %d\n",n1, n2,n3,miu,L );

    vector<vector<double> > W_hidden, W_output; //Pesos capa oculta y capa de salida
    W_hidden = initWeight( n2, n1 );
    W_output = initWeight( n3, n2 );

    char *nameFile, path[100];
    vector<double> X;

    /*
        Mientras encuentre archivos
    */
    for (int l = 0; l < L; l++) {

        while( ( nameFile = nextFile( baseDir ) ) != NULL ) {

            pathComplete( baseDir, nameFile, path );
            X = getImage( path );
            EValue = NDIR;
            printf("Loading image: %s -> Valor: %d \n", path, EValue );
            printVec(X);
            printVec(X);
            printVec(X);
            printVec(X);
            printVec(X);
            printVec(X);
            printVec(X);
            
            puts("pass");

            //propagation( n1, n2, n3, W_hidden, W_output, X, a, O, gcase );
            puts("pass1");
            /*
            // Calculando el error de la capa de Salida
            double ErrG = 0;
            for (int i = 0; i < n3; i++) {
                double Ti = (double)( ( EValue >> i ) & 1 );
                Err[ i ] = Ti - O[i];
                ErrG += Err[i] * Err[i];
                //printf("%lf ", Err[i] );
            }
            ErrG /= n3;

            printf("ErrG %lf\n", ErrG );
            */
        }
        NDIR = 0;
    }
}

void getParams( int *n1, int *n2, int *n3, double *miu, int *L, int *gcase ) {
    FILE *config = NULL;
    config = fopen("config", "r");

    if ( config == NULL ) {
        error("Config file is missing");
    }

    *n1 = (int) nextParam( config );
    *n2 = (int) nextParam( config );
    *n3 = (int) nextParam( config );
    *miu = nextParam( config );
    *L = (int) nextParam( config );
    *gcase = (int) nextParam( config );

    fclose( config );
}

double g( double z, int gcase ) {
    switch ( gcase ) {
        case 1:
            //printf("Exp %lf %lf %lf\n", exp(-z), z, 1.0 / ( 1.0 + exp( -z ) ) );
            return 1.0 / ( 1.0 + exp( -z ) );

        case 2:
            return exp( 2.0 * z ) / ( 1.0 + exp( 2.0 * z ) );
    }
}

double Dg( double z, int gcase ) {
    switch ( gcase ) {
        case 1:
            return exp( -z ) / pow( ( 1.0 + exp( -z ) ) , 2.0 );
        case 2:
            return 2 * exp( 2.0 * z  ) / pow( 1.0 + exp( 2.0 * z ), 2 );
    }
}

vector<vector< double > > initWeight( int n, int m ) {
    vector<vector< double > > W;

    for (int i = 0; i < n; i++) {
        vector<double> wi;
        for (int j = 0; j < m; j++) {
            double t = 1.0 - (double)( rand() % 10 ) / 5.0;
            wi.push_back( t );
        }
        W.push_back( wi );
    }

    return W;
}

// Show the program help
void help() {
    printf("\nHow to use:\n");
    printf("\n\tAutoregressiveParameters [file_input]\n" );
}
