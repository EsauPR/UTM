#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################################
##  Retropropagación sin actualizar la capa de entrada  ##
##  Múltiples Capas Ocultas                             ##
##                                                      ##
##  Peralta Rosales Oscar Esaú                          ##
##  esau.opr@gmail.com                                  ##
##########################################################

import sys;
import random
import numpy
import math
import myLib


ents = []
Errors = []
Error = []

# Derivada de la función sigmoide
def Dg( z ) :
	return math.exp( -z ) / math.pow( ( 1.0 + math.exp( -z ) ) , 2.0 )



# Función sigmoide
def g( z ) :
	return 1.0 / ( 1.0 + math.exp( -z ) );



# Propagación de un vector a través de la red
# p = número de neuronas capa de entrada
# q = número de neuronas en la capa de salida
# n[] = número de neuronas en las capas ocultas
def propagation( p, n, q, W_hiddens, W_output, X ) :
	global Errors
	global ents
	
	# Número de capas ocultas
	m = len( n )

	I = [] # Salida de las neuronas de la capa de entrada
	a = [] # Salida de las neuronas de la capa de salida
	O = [] # Salida de las neuronas de las capas ocultas

	# Capa de entrada
	ents_k = []
	for k in range( p ) :
		I.append( X[k] )
		ents_k.append( X[k] )
	ents.append( ents_k )
	
	# Capas de ocultas
	for i in range( m ) :
		a_tmp = []
		ents_j = []
		# Para cada neurona 
		for j in range( n[i] ) :
			ent_j = 0.0
			# Primer capa oculta
			if i == 0 :
				for k in range( p ) :
					ent_j += W_hiddens[i][j][k] * I[k]
			# Demás capas ocultas
			else :
				for k in range( n[i-1] ) :
					ent_j += W_hiddens[i][j][k] * a[i-1][k]
			a_tmp.append( g( ent_j ) )
			# Guardar el valor de la sumatoria sin función de activación 
			# para evitar doble cálculo en la función de retropropagación
			ents_j.append( ent_j )
		ents.append( ents_j )
		a.append( a_tmp )
	
	# Capa de salida
	ents_i = []
	for i in range( q ) :
		ent_i = 0.0
		for j in range( n[m-1] ) :
			ent_i += W_output[i][j] * a[m-1][j]
		O.append( g( ent_i ) )
		ents_i.append( ent_i )
	ents.append( ents_i )

	# Calculando Error de aprendizaje de la imagen
	Err = 0.0
	for i in range( q ) :
		# Error entre salida esperada y proporcionada por la neurona
		ev = myLib.getExpectedValue()
		Ti = (ev >> i) & 1
		Err += ( Ti - O[i] ) * ( Ti - O[i] )
	Err /= 4.0
	Errors.append( Err )

	return a,O



# Actualilzación de los pesos través de la red
# p = número de neuronas capa de entrada
# q = número de neuronas en la capa de salida
# n[] = número de neuronas en las capas ocultas
# T = número de presentaciones
# miu = Factor de actualización
def backpropagation( basePath, p, n, q, T, miu ) :
	global NDIR
	global Error
	global Errors
	global ents
	
	# Número de capas ocultas
	m = len( n )

	W_hiddens = myLib.randomMultiMatrix( p, n )
	W_output = myLib.randomMatrix( q, n[m-1] )

	for t in range( T ) :
		print( "Presentación ", t+1 )
		while True :

			path = myLib.nextImage( basePath )

			# No hay más imágenes
			if( path == "" ) :
				break

			X  = myLib.loadImage( path )

			# Valores de las sumatorias de cada capa sin función de activación
			ents = []
			a, O = propagation( p, n, q, W_hiddens, W_output, X )

			# Actalizando pesos de la i-ésima neurona de la capa de salida
			preDelta = []
			# Para cada neurona de la capa de salida
			for i in range( q ) :
				# Error entre salida esperada y proporcionada por la neurona
				ev = myLib.getExpectedValue()
				Ti = (ev >> i) & 1
				Err_i = Ti - O[i]
				# Sumatoria de salida para la i-ésima neurona de la capa de salida
				ent_i = ents[ len(ents) - 1 ][i]
				# Se obtiene Delta_i
				delta_i = Err_i * Dg( ent_i )
				preDelta.append( delta_i )
				# Se actualiza cada peso de la i-ésima neurona
				for j in range( n[m-1] ) :
					W_output[i][j] += miu * a[m-1][j] * delta_i

			# Para cada capa oculta
			for l in range( m ) :
				if l != 0 :
					preDelta = actDelta
				actDelta = []
				# Actalizando pesos de la j-ésima neurona de la l-ésima capa oculta
				for j in range( n[ m-l-1 ] ) :
					# Sumatoria de salida para la i-ésima neurona de la l-ésima capa oculta
					ent_j = ents[m-l][j]
					# Se calcula delta_j
					delta_j = 0.0
					# Última capa oculta
					if l == 0 :
						for i in range( q ) :
							delta_j += W_output[i][j] * preDelta[i]
					# Capas intermedias
					else :
						for i in range( n[m-l] ) :
							delta_j += W_hiddens[m-l][i][j] * preDelta[i]

					delta_j *= Dg( ent_j )
					actDelta.append( delta_j )
					# Se actualiza cada peso de la j-ésima neurona de la l-ésima capa oculta
					# Para la primer capa oculta
					if l == m-1 :
						for k in range( p ) :
							W_hiddens[0][j][k] += miu * X[k] * delta_j
					# Para la capas ocultas intermedias
					else :
						for k in range( n[m-l-1] ) :
							W_hiddens[m-l-1][j][k] += miu * a[m-l-2][k] * delta_j

		# Calculando el error global por presentación del conjunto de imágenes
		tmp = 0.0
		for e in Errors :
			tmp += e
		Error.append( tmp )
		Errors = []
		print( "Error =>" , Error[-1] )

		# Reiniciar parámetros de lectura de las imágenes
		myLib.resetDirectory()

	return W_hiddens, W_output



# Clasifica una imagen
def test( filename, p, n, q ) :
	W_output = myLib.loadMatrix("Capas/CapaSalida")
	W_hiddens = []
	for i in range( len( n ) ) :
		W_hiddens.append( myLib.loadMatrix( "Capas/CapaOculta" + str(i+1)) )
	
	X = myLib.loadImage( filename )
	a, O = propagation( p, n, q, W_hiddens, W_output, X )

	print(O)
	for num in O :
		print( int(num+0.5) )
	out = 0
	for i in range( q ) :
		out = out | ( int( O[i] + 0.5 ) << i )
	print("Valor proporcionado por la red: ", out)
	



# Ayuda de uso del programa
def usage() :
	print("Argumentos inválidos:")
	print("Uso: \n\tpython retropropagation.py -training [carpeta]")
	print("\tpython retropropagation.py -test [imagen]")
	sys.exit()



def main() :
	if len( sys.argv ) != 3 :
		usage()

	params = myLib.loadConfig()
	print("Parámetros [p, n, q, T, miu, g]: ", params )
	
	if( sys.argv[1] == "-training" ) :
		W_hiddens, W_output = backpropagation( sys.argv[2], int( params[0] ), params[1], int( params[2] ), int( params[3] ), params[4] )

		# Guardando Parámetros de las neuronas de cada capa
		myLib.cleanSavesDirectory()
		myLib.saveMatrix("Capas/CapaSalida", W_output)
		for i in range( len( W_hiddens ) ) :
			myLib.saveMatrix( "Capas/CapaOculta" + str(i+1), W_hiddens[i] )

		# Guardando Errores globales de cada presentación
		myLib.saveList("Error.txt", Error)

	elif( sys.argv[1] == "-test" ) :
		test( sys.argv[2], int( params[0] ), params[1], int( params[2] ) )

	else :
		usage()



if __name__ == '__main__':
	main()
