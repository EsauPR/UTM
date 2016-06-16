#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################################
##  Retropropagación 									##
##  Funciones extra			                            ##
##                                                      ##
##  Peralta Rosales Oscar Esaú                          ##
##  esau.opr@gmail.com                                  ##
##########################################################

import sys;
import random
import numpy
import math
import os
from PIL import Image

NDIR = 0;
fileNames = [];
currentFile = 0;

# Devuelve la ruta completa de la sieguiente imagen a leer dado el directorio
# baso donde se encuentran todas las carpetas de las imágenes
def nextImage( url ) :
	global NDIR;
	global fileNames;
	global currentFile;

	path = url + "/" + str( NDIR ) + "/";

	if fileNames == []:
		fileNames = os.listdir(path)
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
def loadMatrix( fileName  ) :
	W = []
	infile = open( fileName, 'r')
	for line in infile:
		W.append( [] )
		numbers = line.split( " " )
		numbers.pop( len( numbers ) - 1 )
		for num in numbers :
			W[ len( W ) -1 ].append( float(num) )

	infile.close()
	return W



# Guarda una matrix en un archivo
def saveMatrix( fileName, W ) :
	outfile = open( fileName , 'w')
	
	for row in W :
		for w in row :
			outfile.write( str( w ) + " "  )
		outfile.write("\n")
	
	outfile.close()



# Guarda una matrix en un archivo
def saveList( fileName, W ) :
	outfile = open( fileName , 'w')
	
	for w in W :
		outfile.write( str( w ) + "\n"  )
	
	outfile.close()



# Retorna una Matriz de N x M con valores aleatoreos entre -1.0 y 1.0
def randomMatrix( n, m ) :
	W = []
	for i in range( n ) :
		W.append( [] )
		for j in range( m ) :
			W[i].append( random.uniform(-1, 1) )
	return W



# Retorna uatriz multidimencional
def randomMultiMatrix( p, n ) :
	W = []
	for i in range( len( n ) ) :
		if i == 0 :
			W.append( randomMatrix(n[i], p) )
		else :
			W.append( randomMatrix(n[i], n[i-1]) )
	return W



# Carga las configuraciones desde el archivo config
def loadConfig() :
	archivo = open("config", "r")
	params = []
	contLine = 0
	for line in archivo :
		numbers = line.split( ":" )[1].split(' ')
		numbers.remove('')
		if contLine == 1 :
			tmp = []
			for number in numbers :
				tmp.append( int( number ) )
			params.append( tmp )
		else :
			params.append( float( numbers[0] ) )
		contLine += 1

	return params



# Retorna el valor que representa la imagen actual 
def getExpectedValue() :
	return NDIR



# Reinicia la lectura de las imagenes
def resetDirectory() :
	global NDIR
	global fileNames
	global currentFile

	NDIR = 0;
	fileNames = [];
	currentFile = 0;



# Borra los archivos con los pesos de cada nuerona de cada capa
def cleanSavesDirectory() :
	fileNames = os.listdir("Capas")
	for file in fileNames :
		os.remove("Capas/" + file)