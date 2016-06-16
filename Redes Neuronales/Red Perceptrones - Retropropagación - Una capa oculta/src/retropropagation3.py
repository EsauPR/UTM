#!/usr/bin/env python
# -*- coding: utf-8 -*-

# retropropagación actualizar la capa de entrada - Multiples pesos

import sys;
import random
import numpy
import math
from os import listdir
from PIL import Image

NDIR = 0;
fileNames = [];
currentFile = 0;
Errors = []
Error = []
ents = [[],[],[]]

# Derivada de la función sigmoide
def Dg( z ) :
    return math.exp( -z ) / math.pow( ( 1.0 + math.exp( -z ) ) , 2.0 )
# Funcion sigmoide
def g( z ) :
    return 1.0 / ( 1.0 + math.exp( -z ) );

# Devuelve la ruta completa de la sieguiente imagen a leer dado el directorio
# baso donde se encuentran todas las carpetas de las imágenes
def nextImage( url ) :
    global NDIR;
    global fileNames;
    global currentFile;

    path = url + "/" + str( NDIR ) + "/";

    if fileNames == []:
        fileNames = listdir(path)
        currentFile = 0

    if( currentFile == len( fileNames ) ) :
        if( NDIR == 9 ) :
            return ""
        NDIR = NDIR + 1
        fileNames = []
        return nextImage( url )

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



# Propafacion de un vector a través de la red
def propagation( n1, n2, n3, W_input, W_hidden, W_output, X ) :
    global Errors
    global ents
    I = []
    a = []
    O = []

    # Capa de entrada
    for k in range( n1 ) :
        ent_k = 0.0
        for l in range( len(X) ) :
            ent_k += W_input[k][l] * X[l]
        I.append( g( ent_k ) )
        ents[0].append( ent_k )
    # Capa de oculta
    for j in range( n2 ) :
        ent_j = 0.0
        for k in range( n1 ) :
            ent_j += W_hidden[j][k] * I[k]
        a.append( g( ent_j ) )
        ents[1].append( ent_j )
    # Cada de salida
    for i in range( n3 ) :
        ent_i = 0.0
        for j in range( n2 ) :
            ent_i += W_output[i][j] * a[j]
        O.append( g( ent_i ) )
        ents[2].append( ent_i )

    # Calculando Error Global
    Err = 0.0
    for i in range( n3 ) :
        # Error entre salida esperada y proporcionada por la neurona
        Ti = (NDIR >> i) & 1
        Err += ( Ti - O[i] ) * ( Ti - O[i] )
    Err /= 4.0
    Errors.append( Err )

    return a,O


# Actualilzación de los pesos través de la red
def backpropagation( basePath, n1, n2, n3, L, miu ) :
    global NDIR
    global Errors
    global Error
    global ents
    W_hidden = randomMatrix( n2, n1 )
    W_output = randomMatrix( n3, n2 )
    W_input = randomMatrix( n1, 784 )

    for t in range( L ) :
        while True :

            path = nextImage( basePath )

            if( path == "" ) :
                break

            #print( path )

            X  = loadImage( path )
            #print( X )

            ents = [[],[],[]]
            a, O = propagation( n1, n2, n3, W_input, W_hidden, W_output, X )

            # Actalizando pesos de la i-ésima neurona de la capa de salida
            preDelta_i = []
            for i in range( n3 ) :
                # Error entre salida esperada y proporcionada por la neurona
                Ti = (NDIR >> i) & 1
                Err_i = Ti - O[i]
                # Cálculo de ent_i
                #ent_i = 0.0
                #for j in range( n2 ) :
                #   ent_i += W_output[i][j] * a[j]
                ent_i = ents[2][i]
                # Se obtiene Delta_i
                delta_i = Err_i * Dg( ent_i )
                preDelta_i.append( delta_i )
                # Se actualiza cada peso de la i-ésima neurona
                for j in range( n2 ) :
                    W_output[i][j] += miu * a[j] * delta_i

            # Actalizando pesos de la j-ésima neurona de la capa oculta
            preDelta_j = []
            for j in range( n2 ) :
                # Se calcula ent_j
                #ent_j = 0.0
                #for k in range( n1 ) :
                #    ent_j += W_hidden[j][k] * X[k]
                ent_j = ents[1][j]
                # Se calcula delta_j
                delta_j = 0.0
                for i in range( n3 ) :
                    delta_j += W_output[i][j] * preDelta_i[i]
                delta_j *= Dg( ent_j )
                preDelta_j.append( delta_j )
                # Se actualiza cada peso de la j-ésima neurona
                for k in range( n1 ) :
                    W_hidden[j][k] += miu * X[k] * delta_j


            # Actualizando pesos de la capa de entrada
            for k in range( n1 ) :
                # Se calcula ent_j
                #ent_k = 0.0
                #for l in range( len( X ) ) :
                #    ent_k += W_input[k][l] * X[l]
                ent_k = ents[0][k]
                # Se calcula delta_j
                delta_k = 0.0
                for j in range( n2 ) :
                    delta_k += W_hidden[j][k] * preDelta_j[j]
                delta_k *= Dg( ent_k )
                # Se actualiza cada peso de la j-ésima neurona
                for l in range( len( X ) ) :
                    W_input[k][l] += miu * X[l] * delta_k

        NDIR = 0
        miu /= 1.03
        tmp = 0.0
        for e in Errors :
            tmp += e
        Error.append(tmp * tmp)
        Errors = []
        print( t+1, "Errores =>" ,Error )

    return W_input, W_hidden, W_output


def usage() :
    print("Argumentos inválidos:")
    print("Uso: \n\tpython retropropagation.py -training [carpeta]")
    print("\tpython retropropagation.py -test [imagen]")
    sys.exit()



def main() :
    if len( sys.argv ) != 3 :
        usage()

    params = loadConfig()
    print( params )

    if( sys.argv[1] == "-training" ) :
        W_input, W_hidden, W_output = backpropagation( sys.argv[2], int( params[0] ), int( params[1] ), int( params[2] ), int( params[3] ), params[4] )

        # Guardando Errores
        outfile = open('Error.txt', 'w')
        for err in Error :
            outfile.write( str(err) + "\n"  )
        outfile.close()

        #Guardando configuración de las neuronas capa de salida
        outfile = open('CapaSalida.txt', 'w')
        for row in W_output :
            for w in row :
                outfile.write( str( w ) + " "  )
            outfile.write("\n")
        outfile.close()

        #Guardando configuración de las neuronas capa oculta
        outfile = open('CapaOculta.txt', 'w')
        for row in W_hidden :
            for w in row :
                outfile.write( str( w ) + " "  )
            outfile.write("\n")
        outfile.close()

        #Guardando configuración de las neuronas capa entrada
        outfile = open('CapaEntrada.txt', 'w')
        for row in W_input :
            for w in row :
                outfile.write( str( w ) + " "  )
            outfile.write("\n")
        outfile.close()

    elif( sys.argv[1] == "-test" ) :
        W_hidden = loadMatrix( "CapaOculta.txt" )
        W_output = loadMatrix( "CapaSalida.txt" )
        W_input = loadMatrix( "CapaEntrada.txt" )
        X = loadImage( sys.argv[2] )
        a, O = propagation( int( params[0] ), int( params[1] ), int( params[2] ), W_input, W_hidden, W_output, X )
        print(O)
        a = 0
        for i in range( int(params[2]) ) :
            a = a | ( int( O[i] + 0.5 ) << i )
        print(a)

    else :
        usage()


if __name__ == '__main__':
    main()
