/*
    Extra functions to process data input

    @author Oscar Esaú Peralta Rosales
    @email esau.opr@gmail.com
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

#define STR_DIMENSION 150

using namespace std;

/*
 Process the input file
*/
double nextParam( FILE *file ) {
	int pos = 0;
    char token [STR_DIMENSION];

	/* Label */
	while( ( token[pos] = getc(file) ) != EOF && token[pos] != ':' );
	/* Value */
	while( ( token[pos] = getc(file) ) != EOF && token[pos++] != '\n' );

	token[pos-1] = '\0';
    return atof( token );
}

void printVec( vector<vector< double> > X ) {
    for (int i = 0; i < X.size() ; i++) {
        for (int j = 0; j < X[0].size(); j++) {
            printf("%.4lf ", X[i][j]);
        }
        puts("");
    }
    puts("");
}

void printVec( vector<double> X ) {
    for (int i = 0; i < X.size() ; i++) {
		printf("%.2lf ", X[i]);
    }
    puts("");
}

void printVecCF( vector< double> X ) {
	puts("Parámetros:");
    for (int i = 0; i < X.size() ; i++) {
		printf("A%d = %Lf ", i+1, X[i]);
    }
    puts("");
}

void printVecNF( vector< double> X ) {
    for (int i = 0; i < X.size() ; i++) {
		printf("%Lf\n",X[i]);
    }
    puts("");
}
