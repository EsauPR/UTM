/*
    Extra functions to process files into any directory

    @author Oscar Esaú Peralta Rosales
    @email esau.opr@gmail.com
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <dirent.h>

#define MAX_NUMBER_DIRECTORY 9

using namespace std;

DIR *dir = NULL; // Directorio actual
struct dirent *ent; // Archivo actual
int NDIR = 0; // Número que representa el nombre de la carpeta de imágenes

void error(const char *s) {
    perror (s);
    exit(EXIT_FAILURE);
}

/*
    Concatena el directorio base con la carpeta actual indicada por NDIR
    "baseDir/NDIR"
*/
void * nextDir(char *baseDir, char *uri, int NDIR) {
    int len = strlen( baseDir );

    strcpy( uri, baseDir );
    uri[ len ] = '/';
    uri[ len + 1 ] = '0' + NDIR;
    uri[ len + 2 ] = '\0';
}

/*
    Recibe el directorio base donde se encuentran las carpetas de imágenes
    numeradas del 0 al 9.
    A la carpeta base se le concatena NDIR, el cual indica la carpeta actual
    retorna el nombre del archivo encontrado en la carpeta.

    Si no hay más archivos incrementa NDIR para cambiar de carpeta
*/
char * nextFile( char *baseDir ) {
    char nameDir[100];

    nextDir( baseDir, nameDir, NDIR );

    if( dir == NULL ) {
        dir = opendir (nameDir);
        //printf("Abriendo del dir %s\n", nameDir );
    }

    ent = readdir (dir);
    /*
        No más archivos, pasar al siguiente directorio
    */
    if ( ent == NULL ) {
        if ( NDIR < MAX_NUMBER_DIRECTORY ) {
            NDIR ++;
            dir = NULL;
            closedir (dir);
            return nextFile( baseDir );
        }
        else {
            closedir (dir);
            return NULL;
        }
    }
    /*
        Evitar direcotrio actual y anterior
    */
    if( strcmp( ent->d_name, "." ) == 0 || strcmp( ent->d_name, ".." ) == 0 ) {
        return nextFile( baseDir );
    }

    return ent->d_name;
}

void concat( char *s1, char *s2, char *s ) {
    strcpy( s, s1 );
    strcpy( s + strlen(s1), s2 );
}

void pathComplete( char* baseDir, char *fileName, char *path ) {
    nextDir( baseDir, path, NDIR );
    concat( path, (char *)"/", path );
    concat( path, fileName, path );
}
