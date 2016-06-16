#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mylib import *

Errors = []

# Propafacion de un vector a través de la red
def propagation( n1, n2, n3, W_hidden, W_output, X ) :
    global Errors
    I = []
    a = []
    O = []

    # Capa de entrada
    for k in range( n1 ) :
        I.append( X[k] )
    # Capa de oculta
    for j in range( n2 ) :
        ent_j = 0.0
        for k in range( n1 ) :
            ent_j += W_hidden[j][k] * I[k]
        a.append( g( ent_j ) )
    # Cada de salida
    for i in range( n3 ) :
        ent_i = 0.0
        for j in range( n2 ) :
            ent_i += W_output[i][j] * a[j]
        O.append( g( ent_i ) )

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
    W_hidden = randomMatrix( n2, n1 )
    W_output = randomMatrix( n3, n2 )

    for l in range( L ) :
        reset = True
        print(l)
        while True :
            path = nextImage( basePath, reset )
            reset = False

            if( path == "" ) :
                break

            #print( path )

            X  = loadImage( path )
            #print( X )

            a, O = propagation( n1, n2, n3, W_hidden, W_output, X )

            # Actalizando pesos de la i-ésima neurona de la capa de salida
            preDelta = []
            for i in range( n3 ) :
                # Error entre salida esperada y proporcionada por la neurona
                Ti = (NDIR >> i) & 1
                Err_i = Ti - O[i]
                # Cálculo de ent_i
                ent_i = 0.0
                for j in range( n2 ) :
                    ent_i += W_output[i][j] * a[j]
                # Se obtiene Delta_i
                delta_i = Err_i * Dg( ent_i )
                preDelta.append( delta_i )
                # Se actualiza cada peso de la i-ésima neurona
                for j in range( n2 ) :
                    W_output[i][j] += miu * a[j] * delta_i

            # Actalizando pesos de la j-ésima neurona de la capa oculta
            for j in range( n2 ) :
                # Se calcula ent_j
                ent_j = 0.0
                for k in range( n1 ) :
                    ent_j += W_hidden[j][k] * X[k]
                # Se calcula delta_j
                delta_j = 0.0
                for i in range( n3 ) :
                    delta_j += W_output[i][j] * preDelta[i]
                delta_j *= Dg( ent_j )
                # Se actualiza cada peso de la j-ésima neurona
                for k in range( n1 ) :
                    W_hidden[j][k] += miu * X[k] * delta_j

    return W_hidden, W_output



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

    if( sys.argv[1] == "-trainig" ) :
        W_hidden, W_output = backpropagation( sys.argv[2], int( params[0] ), int( params[1] ), int( params[2] ), int( params[3] ), params[4] )

        # Guardando Errores
        outfile = open('Error.txt', 'w')
        for err in Errors :
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

    elif( sys.argv[1] == "-test" ) :
        W_hidden = loadMatrix( "CapaOculta.txt" )
        W_output = loadMatrix( "CapaSalida.txt" )
        X = loadImage( sys.argv[2] )
        a, O = propagation( int( params[0] ), int( params[1] ), int( params[2] ), W_hidden, W_output, X )
        print( O )
    else :
        usage()



if __name__ == '__main__':
    main()
