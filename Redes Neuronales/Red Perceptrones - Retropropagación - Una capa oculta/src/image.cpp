/*
    Extra functions to process Images gif

    @author Oscar Esaú Peralta Rosales
    @email esau.opr@gmail.com
*/

#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>

#define STR_DIMENSION 150

using namespace std;

void nextLine( FILE *file ) {
	while( getc(file) != '\n' );
}

double nextValue( FILE *file ) {
	int pos = 0;
    char token [STR_DIMENSION];

	while( ( token[pos] = getc(file) ) != EOF && token[pos++] != '\n' );
	token[pos-1] = '\0';

    return atof( token );
}

vector<double> readInput( char *fname ) {
	char str[STR_DIMENSION];
	int cont = 28*28;
	vector<double> X;

	FILE *file = NULL;
    file = fopen( fname, "r");

    /* Los valores de los pixeles de la imagen empiezan a partir de la linea 19 */
	for (int i = 0; i < 19; i++) {
		nextLine( file );
	}

	while( fgets( str, STR_DIMENSION, file ) != NULL && cont > 0) {
		X.push_back( atof( str ) / 256.0 );
		cont--;
	}

	fclose( file );
	return X;
}

vector<double> getImage( char *fname ) {
    char cmd[100] = "octave-cli image.m ";

    strcpy( cmd + strlen( cmd ), fname );
    system( cmd );
	
    return readInput( (char*)"img_tmp" );
}
