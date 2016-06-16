#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys;
import random
import numpy
import math
from os import listdir
from PIL import Image

NDIR = 0;
fileNames = [];
currentFile = 0;

# Derivada de la función sigmoide
def Dg( z ) :
    return math.exp( -z ) / math.pow( ( 1.0 + math.exp( -z ) ) , 2.0 )
# Funcion sigmoide
def g( z ) :
    return 1.0 / ( 1.0 + math.exp( -z ) );

# Devuelve la ruta completa de la sieguiente imagen a leer dado el directorio
# baso donde se encuentran todas las carpetas de las imágenes
def nextImage( url, reset ) :
    global NDIR;
    global fileNames;
    global currentFile;

    if( reset == True ) :
        NDIR = 0

    path = url + "/" + str( NDIR ) + "/";
    print( NDIR, path )

    if fileNames == []:
        fileNames = listdir(path)
        currentFile = 0

    if( currentFile == len( fileNames ) ) :
        if( NDIR == 9 ) :
            return ""
        NDIR = NDIR + 1
        fileNames = []
        return nextImage( url, reset )

    path =  path + fileNames[ currentFile ]
    currentFile += 1

    return path


# Carga la una imagen y devuelve una lista con los pixeles de la imagen
def loadImage( path ) :
    f = Image.open( path )
    m = A = numpy.squeeze( numpy.asarray( f ) )
    X = []

    for array in m :
        X = X + array.tolist()

    for i in range( len(X) ) :
        X[i] /= 256

    return X


# Retorna una Matriz de N x M con valores aleatoreos entre -1.0 y 1.0
def randomMatrix( n, m ) :
    W = []
    for i in range( n ) :
        W.append( [] )
        for j in range( m ) :
            W[i].append( random.uniform(-1, 1) )
    return W



# Carga las configuraciones desde el archivo config
def loadConfig() :
    archivo = open("config", "r")
    params = []

    for line in archivo :
        params.append( float( line.split( ":" )[1] ) )

    return params

# Carga una matriz desde un archivo
def loadMatrix( filename  ) :
    W = []
    infile = open( filename, 'r')
    for line in infile:
        W.append( [] )
        numbers = line.split( " " )
        numbers.pop( len( numbers ) - 1 )
        for num in numbers :
            W[ len( W ) -1 ].append( float(num) )

    infile.close()
    return W
