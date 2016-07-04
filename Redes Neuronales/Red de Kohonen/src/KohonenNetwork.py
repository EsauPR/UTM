#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################################
##  Red Unidimencional de Kohonen						##
##                                                      ##
##  Peralta Rosales Oscar Esaú                          ##
##  esau.opr@gmail.com                                  ##
##########################################################

import sys;
import random
import numpy
import math
import myLib



def euclideanDistance( x, y ) :
	"""
	@brief      		{ Función de distancia Euclidina }
	param[in]	<x> 	{ Coeficiente del vector de entrada }
	param[in]	<y> 	{ Pesos de la neurona }
	@return     		{ Distancia }
	"""
	d = 0.0
	for i in range( len( x ) ) :
		d += ( x[i] - y[i] ) * ( x[i] - y[i] )
	return math.sqrt( d )



def manhattanDistance( x, y ) :
	"""
	@brief      		{ Funcion de distancia de Manhattan }
	param[in]	<x> 	{ Coeficiente del vector de entrada }
	param[in]	<y> 	{ Pesos de la neurona }
	@return     		{ Distancia }
	"""	
	d = 0.0
	for i in range( len( x ) ) :
		d += abs( x[i] - y[i] )
	return d



def distance( x, y, type ) :
	"""
	@brief      		{ Función de distancia }
	param[in]	<x> 	{ Coeficiente del vector de entrada }
	param[in]	<y> 	{ Pesos de la neurona }
	param[in]	<type> 	{ tipo de distancia }
	@return     		{ Distancia }
	"""
	if type == 0 :
		return euclideanDistance( x, y )
	else :
		return manhattanDistance( x, y )



def KohonenNetworkClassifier( W, m, distanceType ) :
	"""
	@brief      				{ Entrenamiento de la Red de Kohonen }
	param[in]	<W> 			{ Pesos de las neuronas }
	param[in]	<m> 			{ Número de neuronas }
	param[in]	<distanceType> 	{ Tipo de Distancia Euclidiana}
	@return     				{ Neurona ganadora }
	"""
	global basePath

	distributionClass = {}
	distributionClass2 = []
	for j in range( m ):
		distributionClass[ "Clase " + str(j) ] = 0
		distributionClass2.append(0)

	while True :

		path = myLib.nextImage( basePath )

		# No hay más imágenes
		if( path == "" ) :
			break

		X  = myLib.loadImage( path )
		minD = math.inf
		minN = -1

		for j in range( m ) :
			d = distance( X, W[j], distanceType )
			if minD > d :
				minD = d
				minN = j

		distributionClass[ "Clase " + str(minN) ] += 1
		distributionClass2[ minN ] += 1

		myLib.saveOImage( X, "representantes/" + "Clase " + str(minN) + "-" + str(minD) + ".jpg" )

	myLib.resetDirectory()
	print( distributionClass )
	print( distributionClass2 )



def phi( winnerNeuron, j, r ) :
	d = abs( winnerNeuron - j )

	if d > r :
		return 0
	
	if r == 0 :
		if d == 0 :
			return 1
		else :
			return 0;
	
	return 1.0 - d/r;



def trainKohonenNetowork1D( alfa, m, L, r, params ):
	"""
	@brief      			{ Entrenamiento de la Red de Kohonen }
	param[in]	<alfa> 		{ Coeficiente de aprendizaje }
	param[in]	<m> 		{ Número de neuronas }
	param[in]	<L> 		{ Número de presentaciones }
	param[in]	<params> 	{ [coficiente de aprendizaje, Tipo de inicialización de pesos, Tipo de Distancia Euclidiana] }
	param[in]	<r> 		{ Radio }
	@return     			{ Pesos de las neuronas }
	"""
	
	global basePath

	sizeVector = 784

	if params[1] == 1 :
		W = myLib.randomMatrix( m, sizeVector )
	else :
		W = myLib.constMatrix( m, sizeVector, 0.5 )

	for l in range( L ) :
		print("Presentación: ", l+1)

		if params[0] == -1 :
			alfa = 1.0 / ( l + 2 )

		while True :

			path = myLib.nextImage( basePath )

			# No hay más imágenes
			if( path == "" ) :
				break

			X  = myLib.loadImage( path )

			minD = math.inf
			minN = -1;

			# Obteniendo la j-esima neurona mas cercana a X
			for j in range( m ) :
				d = distance( X, W[j], params[2] )

				if minD > d :
					minD = d
					minN = j

			winnerNeuron = minN

			# No hay vecindarios, solo se actualiza la neurona ganadora
			for j in range( len( W ) ) :
				fphi = phi( winnerNeuron, j, r )
				if fphi != 0 :
					for i in range( len( W[j] ) ) :
						W[j][i] += alfa * ( X[i] - W[j][i] ) * fphi

		# Reiniciar parámetros de lectura de las imágenes
		myLib.resetDirectory()

	return W



def usage() :
	"""
	@brief      { Uso del programa }
	@return     { void }
	"""
	print("Argumentos inválidos:")
	print("Uso: \n\tpython retropropagation.py -training [carpeta]")
	#print("\tpython retropropagation.py -test [imagen]")
	sys.exit()



def main() :
	"""
	@brief      { Inicializa parámetros iniciales }
	@return     { void }
	"""
	global basePath

	if len( sys.argv ) != 3 :
		usage()

	if( sys.argv[1] == "-training" ) :

		basePath = sys.argv[2]

		params = myLib.loadConfig();

		W = trainKohonenNetowork1D( params[2], int( params[0] ), int( params[1] ), int( params[5] ),params[2:] )
		KohonenNetworkClassifier( W, len( W ), params[4] )
		myLib.cleanSavesDirectory( "images/" )
		myLib.saveImages( W, "images/" )

		myLib.cleanSavesDirectory( "neuronas/" )
		for i in range( len( W ) ):
			myLib.saveList( W[i], "neuronas/n" + str(i))

	else :
		usage()

if __name__ == '__main__':
	main()