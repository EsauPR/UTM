#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Oscar Esaú Peralta Rosales
# esau.opr@gmail.com

import sys;
import random
import json
from factibilidadIndividual import *
from factibilidadGlobal import *

def printPretty( objson ) :
    print json.dumps( objson, sort_keys=True, indent=2, separators=(',', ': ') )


def parserJson( fileName ) :
    f = open( fileName, "r" )
    objson = json.load( f )
    f.closed
    return objson

def permutation( bounds ) :
    lst = []
    for e in bounds :
        lst.append( e )
    for i in range( len( lst ) ):
        pos = random.randint(0, len(lst) -1)
        tmp = lst[pos]
        lst[pos] = lst[i]
        lst[i] = tmp
    return lst

def getTypeCurse( curso ) :
    options = [
        curso["tperm"],
        curso["pperm"],
        curso["gperm"],
        curso["tmhi"],
        curso["pmhi"],
        curso["gmhi"],
        curso["samehourtp"],
        len( curso["theory"] ),
        len( curso["practice"] )
    ]
    # Caso en el que no existe vector de dias ya que es en toda la semana
    if options == [ False, False, False, False, False, False, False, 1, 0 ] :
        return 1 # ET,HT
    # caso en el que se dan menos de 5 clases a la semana y se elige los dias con Tperm
    if options == [ True, False, False, False, False, False, False, 1, 0 ] :
        return 2 # ET,HT,DT
    # caso en el que no existe vector de dias ya que es en toda la semana
    if options == [ False, False, False, False, False, False, False, 0, 1 ] :
        return 3 # EP,HP
    # caso en el que se dan menos de 5 clases a la semana y se elige los dias con Pperm
    if options == [ False, True, False, False, False, False, False, 0, 1 ] :
        return 4 # EP,HP,DP
    # no existen vectores de dias cada clases es en los 5 dias en cualquier hora un vector de hora por cada clase
    if options == [ False, False, False, False, False, False, False, 2, 0 ] :
        return 5 # ET1,HT1,ET2,HT2
    # existe un vector de teoria repartido entre las dos clases con Tperm en cualquier hora  un vector de hora por cada clase
    if options == [ True, False, False, False, False, False, False, 2, 0 ] :
        return 6 # ET,HT[[HT1],[HT2]],DT[[DT1],[DT2]]
    # existe un vector de teoria repartido entre las dos clases con Tperm y a la misma hora de inicioTmhi un vector de horas por las dos clases
    if options == [ True, False, False, True, False, False, False, 2, 0 ] :
        return 7 # ET,HT,DT[[DT1],[DT2]]
    # no existen vectores de dias cada clases es en los 5 dias en cualquier hora  un vector de hora por cada clase
    if options == [ False, False, False, False, False, False, False, 0, 2 ] :
        return 8 # EP1,HP1,EP2,HP2
    # existe un vector de practica repartido entre las dos clases con Pperm en cualquier hora  un vector de hora por cada clase
    if options == [ False, True, False, False, False, False, False, 0, 2 ] :
        return 9 # EP,HP[[HP1],[HP2]],DP[[DP1],[DP2]]
    # existe un vector de practica repartido entre las dos clases con Pperm y a la misma hora de inicioPmhi un vector de horas por las dos clases
    if options == [ False, True, False, False, True, False, False, 0, 2 ] :
        return 10 # EP,HP,DP[[DP1],[DP2]]
    # caso en el queno existe vector de dias ya que tanto teoria y practica estaran en los 5 dias y no a la misma hora
    if options == [ False, False, False, False, False, False, False, 1, 1 ] :
        return 11 # ET,HT,EP,HP
    # existe vector de diasTeoria y vector de diasPractica y tienen una hora global de inicio
    if options == [ True, True, False, False, False, True, False, 1, 1 ] :
        return 12 # ET,EP,HG,DT,DP
    # existe vector de diasTeoria y vector de diasPractica y no esnecesario que tengan la miama hora (dos vectores de horas)
    if options == [ True, True, False, False, False, False, False, 1, 1 ] :
        return 13 # ET,HT,DT,EP,HP,DP
    # existe vector de diasTeoria y vector de diasPractica y la misma hora de inicio global pero ambos espacios disponibles por samehour
    if options == [ True, True, False, False, False, True, True, 1, 1 ] :
        return 14 # ET,EP,HG,DT,DP
    # Existe vector de dias global y la teoria y practica a la misma hora, ambos espacios disponibles pos samehour
    if options == [ False, False, True, False, False, True, True, 1, 1 ] :
        return 15 # ET,EP,HG,DG[[DT],[DP]]
    # Existe vector de dias global y la teoria y practica a la misma hora
    if options == [ False, False, True, False, False, True, False, 1, 1 ] :
        return 16 # ET,EP,HG,DG[[DT],[DP]]
    # Existe vector de dias global pero no necesariamente a la misma hora
    if options == [ False, False, True, False, False, False, False, 1, 1 ] :
        return 17 # ET,EP,HT,HP,DG[[DT],[DP]]
    # solo existe un vector de teoria y no hay vector practica(es toda la semana) no pueden tener misma hora de inicio
    if options == [ True, False, False, False, False, False, False, 1, 1 ] :
        return 18 # ET,HT,DT,EP,HP
    # solo existe un vector de practica y no hay vector teoria(es toda la semana) no pueden tener misma hora de inicio
    if options == [ False, True, False, False, False, False, False, 1, 1 ] :
        return 19 # ET,HT,EP,HP,DP
    # No existe vector de dias 2Teoria y practica se dan los 5 dias de la semana  un vector de hora por cada clase
    if options == [ False, False, False, False, False, False, False, 2, 1 ] :
        return 20 # ET1,HT1,ET2,HT2,EP,HP
    # vector de diasTeoria se divide entre las dos clases no existe vector diasPractica(es en todos los dias) no necesariamente misma hora,  un vector de hora por cada clase
    if options == [ True, False, False, False, False, False, False, 2, 1 ] :
        return 21 # ET1,HT1,ET2,HT2,EP,HP
    # vector diasTeoria y diasPractica, los dias de teoria se distrubuyen entre las dos de teoria  un vector de hora por cada clase
    if options == [ True, True, False, False, False, False, False, 2, 1 ] :
        return 22 # ET,HT[[HT1],[HT2]],DT[[DT1],[DT2]],EP,HP,DP
    # vector de dias global que se reparten entre las dos de teoria y la de practica,  un vector de hora por cada clase
    if options == [ False, False, True, False, False, False, False, 2, 1 ] :
        return 23 # ET,HT[[HT1],[HT2]],EP,HP,DG[[DT1],[DT2],[DP]]
    # no existe vector diasTeoria y si de diasPractica(realiza permutacion)  un vector de hora por cada clase
    if options == [ False, True, False, False, False, False, False, 2, 1 ] :
        return 24 # ET1,HT1,ET2,HT2,EP,HP,DP
    # un vector de diasTeoria que se reparte entre las dos clases no existe diasPractica(es en los 5 dias) y las horas de teorias a la misma hora
    if options == [ True, False, False, True, False, False, False, 2, 1 ] :
        return 25 # ET,HT,DT[[DT1],[DT2]],EP,HP
    # un vector de diasTeoria que se reparte entre las dos clases un vector diasPractica y las horas de teoria a la misma hora
    if options == [ True, True, False, True, False, False, False, 2, 1 ] :
        return 26 # ET,HT,DT[[DT1],[DT2]],EP,HP,DP
    # un vector de diasTeoria(repartidos en dos clases) un vector de diasPractica y todas a la misma hora solo si:  nDiasTeoria + ndiasPractica=5,  un vector de hora por cada clase de teoria
    if options == [ True, True, False, False, False, True, False, 2, 1 ] :
        return 27 # ET,EP,HG,DT[[DT1],[DT2]],DP
    # un vector de diasGlobal pero solo dias de teoria a la misma hora, un vector de hora por las dos clases de teoria
    if options == [ False, False, True, True, False, False, False, 2, 1 ] :
        return 28 # ET,HT,EP,HP,DG[[DT1],[DT2],[DP]]
    # un vector de diasGlobal y un vector de horasGlobales
    if options == [ False, False, True, False, False, True, False, 2, 1 ] :
        return 29 # ET,EP,HG,DG[[DT1],[DT2],[DP]]
    # un vector de diasTeoria(repartidos en dos clases) un vector de diasPractica y todas a la misma hora solo si: nDiasTeoria + ndiasPractica=5, dos espacios disponibles, un vectorGlobal de horas
    if options == [ True, True, False, False, False, True, True, 2, 1 ] :
        return 30 # ET,EP,HG,DT[[DT1],[DT2]],DP
    # un vector de diasGlobal y un vector de horasGlobales, dos espacios disponibles
    if options == [ False, False, True, False, False, True, True, 2, 1 ] :
        return 31 # ET,EP,HG,DG[[DT1],[DT2],[DP]]
    # No existe vector de dias 2Teoria y practica se dan los 5 dias de la semana ,  un vector de hora por cada clase
    if options == [ False, False, False, False, False, False, False, 1, 2 ] :
        return 32 # ET,HT,EP1,HP1,EP2,HP2
    # no existe vector de practica y si de diasTeoria(realiza permutacion),  un vector de hora por cada clase
    if options == [ True, False, False, False, False, False, False, 1, 2 ] :
        return 33 # ET,HT,DT,EP1,HP1,EP2,HP2
    # vector diasTeoria y diasPractica, los dias de practica se distrubuyen entre las dos de practica,  un vector de hora por cada clase
    if options == [ True, True, False, False, False, False, False, 1, 2 ] :
        return 34 # ET,HT,DT,EP,HP[[HP1],[HP2]],DP[[DP1],[DP2]]
    # vector de dias global que se reparten entre las dos de teoria y la de practica,  un vector de hora por cada clase
    if options == [ False, False, True, False, False, False, False, 1, 2 ] :
        return 35 # ET,HT,EP,HP[[HP1],[HP2]],DG[[DT],[DP1],[DP2]]
    # vector de diasPractica se divide entre las dos clases no existe vector diasTeoria(es en todos los dias) no necesariamente misma hora,  un vector de hora por cada clase
    if options == [ False, True, False, False, False, False, False, 1, 2 ] :
        return 36 # ET,HT,EP,HP[[HP1],[HP2]],DP[[DP1],[DP2]]
    # un vector de diasPractica que se reparten en dos clases un vector de diasTeoria y las horas de pradica a la misma hora
    if options == [ True, True, False, False, True, False, False, 1, 2 ] :
        return 37 # ET,HT,DT,EP,HP,DP[[DP1],[DP2]]
    # un vector de diasPractica(repartidos en dos clases) un vector de diasTeoria y todas a la misma hora solo si:  nDiasTeoria + ndiasPractica=5,un vector de horas por todas las clases
    if options == [ True, True, False, False, False, True, False, 1, 2 ] :
        return 38 # ET,EP,HG,DT,DP[[DP1],[DP2]]
    # un vector de diasPractica que se reparte en dos clases no existe diasTeoria(es en los 5 dias) y las horas de practica a la misma hora,  un vector de hora por cada clase de practica
    if options == [ False, True, False, False, True, False, False, 1, 2 ] :
        return 39 # ET,HT,EP,HP,DP[[DP1],[DP2]]
    # un vector de diasGlobales y un vector de horasGlobales
    if options == [ False, False, True, False, False, True, False, 1, 2 ] :
        return 40 # ET,EP,HG,DG[[DT],[DP1],[DP2]]
    # un vector de diasGlobales pero solo dias de practica a la misma hora
    if options == [ False, False, True, False, True, False, False, 1, 2 ] :
        return 41 # ET,HT,EP,HP,DG[[DT],[DP1],[DP2]]
    # un vector de diasPractica(Repartidos en dos clases) un vector de diasTeoria y todas a la misma hora solo si:  nDiasTeoria + ndiasPractica=5, dos espacios disponibles
    if options == [ True, True, False, False, False, True, True, 1, 2 ] :
        return 42 # ET,EP,HG,DT,DP[[DP1],[DP2]]
    # un vector de diasGlobal y un vector de horasGlobales, dos espacios disponibles
    if options == [ False, False, True, False, False, True, True, 1, 2 ] :
        return 43 # ET,EP,HG,DG[[DT1],[DT2],[DP]]
    # no existe vectores ni de teoria ni de practica todas las clases son en los 5 dias
    if options == [ False, False, False, False, False, False, False, 2, 2 ] :
        return 44 # ET1,HT1,DT1,ET2,HT2,DT2,EP1,HP1,DP1,EP2,HP2,DP2
    # existe un vector diasTeoria repartidos en dos clases y no existe diasPractica
    if options == [ True, False, False, False, False, False, False, 2, 2 ] :
        return 45 # ET,HT[[HT1],[HT2]],DT[[DT1],[DT2]],EP1,HP1,DP1,EP2,HP2,DP2
    # existe un vector diasPractica repartidos en dos clases y no existe diasTeoria
    if options == [ False, True, False, False, False, False, False, 2, 2 ] :
        return 46 # ET1,HT1,DT1,ET2,HT2,DT2,EP,HP[[HP1],[HP2]],DP[[DP1],[DP2]]
    # existe un vector global y los dias se reparten entre las 4 clases(puede haber dos clases o practica en un mismo dia) no hay restriccion en cuanto a la hora de inicio
    if options == [ False, False, True, False, False, False, False, 2, 2 ] :
        return 47 # ET,HT[[HT1],[HT2]],EP,HP[[HP1],[HP2]],DG[[DT1],[DT2],[DP1],[DP2]]
    # existe u vector diasTeoria repartidos en dos clases yun vector diasPractica repartidos en dos clases
    if options == [ True, True, False, False, False, False, False, 2, 2 ] :
        return 48 # ET,HT[[HT1],[HT2]],DT[[DT1],[DT2]],EP,HP[[HP1],[HP2]],DP[[DP1],[DP2]]
    # existe vector de diasTeoria repartidos en dos clases a la misma hora Tmhi y no existe vector de diasPractica las dos clases son toda la semana
    if options == [ True, False, False, True, False, False, False, 2, 2 ] :
        return 49 # ET,HT,DT[[DT1],[DT2]],EP1,HP1,DP1,EP2,HP2,DP2
    # existe vector de diasPractica repartidos en dos clases a la misma hora Pmhi y no existe vector de diasTeoria las dos clases son toda la semana
    if options == [ False, True, False, False, True, False, False, 2, 2 ] :
        return 50 # ET1,HT1,DT1,ET2,HT2,DT2,EP,HP,DP[[DP1],[DP2]]
    # existe solo un vector de dias global teoria a la misma hora
    if options == [ False, False, True, True, False, False, False, 2, 2 ] :
        return 51 # ET,HT,EP,HP[[HP1],[HP2]],DG[[DT1],[DT2],[DP1],[DP2]]
    # existe solo un vector de dias global practica a la misma hora
    if options == [ False, False, True, False, True, False, False, 2, 2 ] :
        return 52 # ET,HT[[HT1],[HT2]],EP,HP,DG[[DT1],[DT2],[DP1],[DP2]]
    # existe solo un vector de dias global y horas globales si y solo si ndiasteoria +ndiaspractica=5
    if options == [ False, False, True, False, False, True, False, 2, 2 ] :
        return 53 # ET,EP,HG,DG[[DT1],[DT2],[DP1],[DP2]]
    # un vector de diasTeoria repartidas en dos cursos, un vector de diasPractica repartidas en dos cursos, cursos teoria a la misma hora
    if options == [ True, True, False, True, False, False, False, 2, 2 ] :
        return 54 # ET,HT,DT[[DT1],[DT2]],EP,HP[[HP1],[HP2]],DP[[DP1],[DP2]]
    # un vector de diasTeoria repartidas en dos cursos, un vector de diasPractica repartidas en dos cursos, cursos practica a la misma hora
    if options == [ True, True, False, False, True, False, False, 2, 2 ] :
        return 55 # ET,HT[[HT1],[HT2]],DT[[DT1],[DT2]],EP,HP,DP[[DP1],[DP2]]
    # un vector de diasTeoria repartidas en dos cursos, un vector de diasPractica repartidas en dos cursos, cursos teoria a la misma hora y cursos practica a la misma hora
    if options == [ True, True, False, True, True, False, False, 2, 2 ] :
        return 56 # ET,HT,DT[[DT1],[DT2]],EP,HP,DP[[DP1],[DP2]]
    # un vector de diasGlobal y horaGlobales si y solo si nDiasTeoria+nDiasPractica=5, dos espacios dispoibles
    if options == [ False, False, True, False, False, True, True, 2, 2 ] :
        return 57 # ET,EP,HG,DG[[DT1],[DT2],[DP1],[DP2]]

def getDays( daysCurses, restrictions ) :
    tmp = []
    curse = 0
    inicio = 0
    N=1
    dayDic = {}
    if "DT" in daysCurses :
        if restrictions["tperm"]:
            perm = permutation( daysCurses["DT"] )
            if len(restrictions["theory"])>1:
                for x in range(len(restrictions["theory"])):
                    tmpDays = []

                    for y in range(inicio,inicio+restrictions["theory"][curse]["n"]):
                        tmpDays.append( perm[y] )
                    dayDic["DT"+str(N)] = tmpDays
                    inicio = restrictions["theory"][curse]["n"]
                    N += 1
                    curse += 1
                #tmp.append( dayDic )
                tmp = dayDic
            else :
                for y in range(restrictions["theory"][curse]["n"]):
                    tmp.append( perm[y] )
            return tmp

    if "DP" in daysCurses :
        if restrictions["pperm"]:
            perm = permutation( daysCurses["DP"] )
            if len(restrictions["practice"])>1:
                for x in range(len(restrictions["practice"])):
                    tmpDays = []
                    for y in range(inicio,inicio+restrictions["practice"][curse]["n"]):
                        tmpDays.append( perm[y] )
                    dayDic["DP"+str(N)] = tmpDays
                    inicio = restrictions["practice"][curse]["n"]
                    N += 1
                    curse += 1
                #tmp.append( dayDic )
                tmp = dayDic
            else :
                for y in range(restrictions["practice"][curse]["n"]):
                    tmp.append( perm[y] )
            return tmp

    if "DG" in daysCurses :
        perm = permutation( daysCurses["DG"] )
        if len(restrictions["theory"])>1:
            for x in range(len(restrictions["theory"])):
                tmpDays = []
                for y in range(inicio,inicio+restrictions["theory"][curse]["n"]):
                    tmpDays.append( perm[y] )
                dayDic["DT"+str(N)] = tmpDays
                inicio = restrictions["theory"][curse]["n"]
                N += 1
                curse += 1
            #tmp.append( dayDic )
            tmp = dayDic
        else :
            tmpDays = []
            for y in range(restrictions["theory"][curse]["n"]):
                tmpDays.append(perm[y])
            dayDic["DT"] = tmpDays
            #tmp.append( dayDic )
        curse = 0
        N=1
        if len(restrictions["practice"])>1:
            for x in range(len(restrictions["practice"])):
                tmpDays = []
                for y in range(restrictions["theory"][curse]["n"],restrictions["theory"][curse]["n"]+restrictions["practice"][curse]["n"]):
                    tmpDays.append( perm[y] )
                dayDic["DP"+str(N)] = tmpDays
                inicio = restrictions["practice"][curse]["n"]
                N += 1
                curse += 1
            #tmp.append( dayDic )
        else :
            tmpDays = []
            for y in range(restrictions["theory"][curse]["n"],restrictions["theory"][curse]["n"]+restrictions["practice"][curse]["n"]):
                tmpDays.append(perm[y])
            dayDic["DP"] = tmpDays
            #tmp.append( dayDic )
            tmp = dayDic
        return tmp

    if "DT1" in daysCurses :
        perm = permutation( daysCurses["DT1"] )
        for x in range(len(restrictions["theory"])):
            tmpDays = []
            for y in range(restrictions["theory"][curse]["n"]):
                tmpDays.append( perm[y] )
            #tmp.append( tmpDays )
            tmp = dayDic
            curse += 1
        return tmp
    if "DT2" in daysCurses :
        perm = permutation( daysCurses["DT2"] )
        for x in range(len(restrictions["theory"])):
            tmpDays = []
            for y in range(restrictions["theory"][curse]["n"]):
                tmpDays.append( perm[y] )
            #tmp.append( tmpDays )
            tmp = dayDic
            curse += 1
        return tmp
    if "DP1" in daysCurses :
        perm = permutation( daysCurses["DP1"] )
        for x in range(len(restrictions["practice"])):
            tmpDays = []
            for y in range(restrictions["practice"][curse]["n"]):
                tmpDays.append( perm[y] )
            #tmp.append( tmpDays )
            tmp = dayDic
            curse += 1
        return tmp
    if "DP2" in daysCurses :
        perm = permutation( daysCurses["DP2"] )
        for x in range(len(restrictions["practice"])):
            tmpDays = []
            for y in range(restrictions["practice"][curse]["n"]):
                tmpDays.append( perm[y] )
            tmp.append( tmpDays )
            curse += 1
        return tmp


def getHours( hoursCurses, restrictions ) :
    tmp = []
    dicTmp = {}
    vecAux = []
    N = 1
    if "HT" in hoursCurses :
        nCurseT = len(restrictions["theory"])
        if nCurseT == 2 and restrictions["tmhi"]==False:
            for x in range(nCurseT):
                dicTmp["HT"+str(N)] = permutation( hoursCurses["HT"] )[0]
                N+=1
            tmp.append(dicTmp)
        if nCurseT == 1 or (nCurseT == 2 and restrictions["tmhi"]==True):
            tmp.append(permutation( hoursCurses["HT"] )[0])
        return tmp
    if "HP" in hoursCurses :
        nCurseP = len(restrictions["practice"])
        if nCurseP == 2 and restrictions["pmhi"]==False:
            for x in range(nCurseP):
                dicTmp["HP"+str(N)] = permutation( hoursCurses["HP"] )[0]
                N+=1
            tmp.append(dicTmp)
        if nCurseP == 1 or (nCurseP == 2 and restrictions["pmhi"]==True):
            tmp.append(permutation( hoursCurses["HP"] )[0])
        return tmp
    if "HG" in hoursCurses :
        tmp.append(permutation( hoursCurses["HG"] )[0])
        return tmp
    if "HT1" in hoursCurses :
        tmp.append(permutation( hoursCurses["HT1"] )[0])
        return tmp
    if "HT2" in hoursCurses :
        tmp.append(permutation( hoursCurses["HT2"] )[0])
        return tmp
    if "HP1" in hoursCurses :
        tmp.append(permutation( hoursCurses["HP1"] )[0])
        return tmp
    if "HP2" in hoursCurses :
        tmp.append(permutation( hoursCurses["HP2"] )[0])
        return tmp

def getPlaces( placesCurses, restrictions ) :
    #if "ET" in placesCurses :
    if "ET" in placesCurses:
        return permutation( placesCurses["ET"] )[0]
    elif "EP" in placesCurses:
        return permutation( placesCurses["EP"] )[0]
    elif "ET1" in placesCurses:
        return permutation( placesCurses["ET1"] )[0]
    elif "EP1" in placesCurses:
        return permutation( placesCurses["EP1"] )[0]
    elif "ET2" in placesCurses:
        return permutation( placesCurses["ET2"] )[0]
    elif "EP2" in placesCurses:
        return permutation( placesCurses["EP2"] )[0]

def getSolution( objson, boundsCurse ) :
    sols = []
    #print boundsCurse
    for curso in range( len( boundsCurse ) ) :
        tmp = {}
        ## Obtencion de Espacios
        if "ET" in  boundsCurse[curso] :
            tmp["ET"] = getPlaces( {"ET" : boundsCurse[curso]["ET"]}, objson["metabounds"][curso] )
        if "EP" in  boundsCurse[curso] :
            tmp["EP"] = getPlaces( {"EP" : boundsCurse[curso]["EP"]}, objson["metabounds"][curso] )
        if "ET1" in  boundsCurse[curso] :
            tmp["ET1"] = getPlaces( {"ET1" : boundsCurse[curso]["ET1"]}, objson["metabounds"][curso] )
        if "ET2" in  boundsCurse[curso] :
            tmp["ET2"] = getPlaces( {"ET2" : boundsCurse[curso]["ET2"]}, objson["metabounds"][curso] )
        if "EP1" in  boundsCurse[curso] :
            tmp["EP1"] = getPlaces( {"EP1" : boundsCurse[curso]["EP1"]}, objson["metabounds"][curso] )
        if "EP1" in  boundsCurse[curso] :
            tmp["EP1"] = getPlaces( {"EP1" : boundsCurse[curso]["EP1"]}, objson["metabounds"][curso] )

        ## Obtencio de horas
        if "HT" in  boundsCurse[curso] :
            tmp["HT"] = getHours( {"HT" : boundsCurse[curso]["HT"]}, objson["metabounds"][curso] )
        if "HP" in  boundsCurse[curso] :
            tmp["HP"] = getHours( {"HP" : boundsCurse[curso]["HP"]}, objson["metabounds"][curso] )
        if "HG" in  boundsCurse[curso] :
            tmp["HG"] = getHours( {"HG" : boundsCurse[curso]["HG"]}, objson["metabounds"][curso] )
        if "HT1" in  boundsCurse[curso] :
            tmp["HT1"] = getHours( {"HT1" : boundsCurse[curso]["HT1"]}, objson["metabounds"][curso] )
        if "HT2" in  boundsCurse[curso] :
            tmp["HT2"] = getHours( {"HT2" : boundsCurse[curso]["HT2"]}, objson["metabounds"][curso] )
        if "HP1" in  boundsCurse[curso] :
            tmp["HP1"] = getHours( {"HP1" : boundsCurse[curso]["HP1"]}, objson["metabounds"][curso] )
        if "HP2" in  boundsCurse[curso] :
            tmp["HP2"] = getHours( {"HP2" : boundsCurse[curso]["HP2"]}, objson["metabounds"][curso] )

        ## Obtencio de DIAS
        if "DT" in  boundsCurse[curso] :
            tmp["DT"] = getDays( {"DT" : boundsCurse[curso]["DT"]}, objson["metabounds"][curso] )
        if "DP" in  boundsCurse[curso] :
            tmp["DP"] = getDays( {"DP" : boundsCurse[curso]["DP"]}, objson["metabounds"][curso] )
        if "DG" in  boundsCurse[curso] :
            tmp["DG"] = getDays( {"DG" : boundsCurse[curso]["DG"]}, objson["metabounds"][curso] )
        if "DT1" in  boundsCurse[curso] :
            tmp["DT1"] = getDays( {"DT1" : boundsCurse[curso]["DT1"]}, objson["metabounds"][curso] )
        if "DT2" in  boundsCurse[curso] :
            tmp["DT2"] = getDays( {"DT2" : boundsCurse[curso]["DT2"]}, objson["metabounds"][curso] )
        if "DP1" in  boundsCurse[curso] :
            tmp["DP1"] = getDays( {"DP1" : boundsCurse[curso]["DP1"]}, objson["metabounds"][curso] )
        if "DP2" in  boundsCurse[curso] :
            tmp["DP2"] = getDays( {"DP2" : boundsCurse[curso]["DP2"]}, objson["metabounds"][curso] )
        sols.append( tmp )
        #print boundsCurse[curso]
        #print tmp
    return sols

def getBoundsCurse( objson ) :
    indexBounds = 0
    sol = []

    for curse in objson["metabounds"] :
        sol_tmp = {}
        opcion = getTypeCurse( curse )
        ## La entrada comienza con vector Espacio de Teoria
        if (opcion in [1,2,6,7,11,12,13,14,15,16,17,18,19,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,47,48,49,51,52,53,54,55,56,57]):
            sol_tmp["ET"] = objson["bounds"][ indexBounds ]
            indexBounds += 1

            ## seundo vector
            if (opcion in [1,2,6,7,11,13,17,18,19,22,23,25,26,28,32,33,34,35,36,37,39,41,45,47,48,49,51,52,54,55,56]):
                if (opcion in [6]):
                    sol_tmp["HT1"] = objson["bounds"][ indexBounds ]
                    indexBounds += 1
                    sol_tmp["HT2"] = objson["bounds"][ indexBounds ]
                    indexBounds += 1
                else:
                    sol_tmp["HT"] = objson["bounds"][ indexBounds ]
                    indexBounds += 1
                ## tercer vector
                if (opcion in [2,6,7,13,18,22,25,26,33,34,37,45,48,49,54,55,56]):
                    sol_tmp["DT"] = objson["bounds"][ indexBounds ]
                    indexBounds += 1
                    ## cuarto vector
                    if (opcion in [13,18,22,25,26,34,37,48,54,55,56]):
                        sol_tmp["EP"] = objson["bounds"][ indexBounds ]
                        indexBounds += 1
                        sol_tmp["HP"] = objson["bounds"][ indexBounds ]
                        indexBounds += 1
                        ## quinto vector
                        if (opcion in [13,22,26,34,37,48,54,55,56]):
                            sol_tmp["DP"] = objson["bounds"][ indexBounds ]
                            indexBounds += 1
                    ## cuarto vector
                    if (opcion in [33,45,49]):
                        idP = 0
                        for x in range(len( curso["practice"] )):
                            sol_tmp["EP"+idP] = objson["bounds"][ indexBounds ]
                            indexBounds += 1
                            sol_tmp["HP"+idP] = objson["bounds"][ indexBounds ]
                            indexBounds += 1
                            if (opcion in [45,49]):
                                sol_tmp["DP"+idP] = objson["bounds"][ indexBounds ]
                                indexBounds += 1
                            idP +=1
                ## tercer vector
                if (opcion in [11,17,19,23,28,32,35,36,39,41,47,51,52]):
                    sol_tmp["EP"] = objson["bounds"][ indexBounds ]
                    indexBounds += 1
                    ## cuarto vector
                    if (opcion in [11,17,19,23,28,35,36,39,41,47,51,52]):
                        sol_tmp["HP"] = objson["bounds"][ indexBounds ]
                        indexBounds += 1
                        ## quinto vector
                        if (opcion in [19,36,39]):
                            sol_tmp["DP"] = objson["bounds"][ indexBounds ]
                            indexBounds += 1
                        ## quinto vector
                        if (opcion in [17,23,28,35,41,47,51,52]):
                            sol_tmp["DG"] = objson["bounds"][ indexBounds ]
                            indexBounds += 1
                ## tercer vector
                if (opcion in [32]):
                    idP = 0
                    for x in range(len( curso["practice"] )):
                        sol_tmp["EP"+idP] = objson["bounds"][ indexBounds ]
                        indexBounds += 1
                        sol_tmp["HP"+idP] = objson["bounds"][ indexBounds ]
                        indexBounds += 1
                        idP +=1

            ## seundo vector
            if (opcion in [12,14,15,16,27,29,30,31,38,40,42,43,53,57]):
                sol_tmp["EP"] = objson["bounds"][ indexBounds ]
                indexBounds += 1
                ## tercer vector
                if (opcion in [12,14,15,16,27,29,30,31,38,40,42,43,53,57]):
                    sol_tmp["HG"] = objson["bounds"][ indexBounds ]
                    indexBounds += 1
                    ## cuarto vector
                    if (opcion in [12,14,27,30,38,42]):
                        sol_tmp["DT"] = objson["bounds"][ indexBounds ]
                        indexBounds += 1
                        sol_tmp["DP"] = objson["bounds"][ indexBounds ]
                        indexBounds += 1
                    ## cuarto vector
                    if (opcion in [15,16,29,31,40,43,53,57]):
                        sol_tmp["DG"] = objson["bounds"][ indexBounds ]
                        indexBounds += 1
        ## La entrada comienza con vector Espacio de Practica
        if (opcion in [3,4,9,10]):
            sol_tmp["EP"] = objson["bounds"][ indexBounds ]
            indexBounds += 1
            if (opcion in [9]):
                sol_tmp["HP1"] = objson["bounds"][ indexBounds ]
                indexBounds += 1
                sol_tmp["HP2"] = objson["bounds"][ indexBounds ]
                indexBounds += 1
            else:
                sol_tmp["HP"] = objson["bounds"][ indexBounds ]
                indexBounds += 1
            if (opcion in [4,9,10]):
                sol_tmp["DP"] = objson["bounds"][ indexBounds ]
                indexBounds += 1

        if ( opcion in [8]) :
            idP = 1
            for x in range(len( curso["practice"] )):
                sol_tmp["EP"+idP] = objson["bounds"][ indexBounds ]
                indexBounds += 1
                sol_tmp["HP"+idP] = objson["bounds"][ indexBounds ]
                indexBounds += 1
                idP +=1

        if ( opcion in [5,20,21,24,44,46,50]) :
            idT = 1
            for x in range(len( curso["theory"] )):
                sol_tmp["ET"+idT] = objson["bounds"][ indexBounds ]
                indexBounds += 1
                sol_tmp["HT"+idT] = objson["bounds"][ indexBounds ]
                indexBounds += 1
                idT +=1
                if (opcion in [44,46,50]):
                    sol_tmp["DT"+idT] = objson["bounds"][ indexBounds ]
                    indexBounds += 1

            if ( opcion in [44]) :
                idP = 1
                for x in range(len( curso["practice"] )):
                    sol_tmp["EP"+idP] = objson["bounds"][ indexBounds ]
                    indexBounds += 1
                    sol_tmp["HP"+idP] = objson["bounds"][ indexBounds ]
                    indexBounds += 1
                    sol_tmp["DP"+idP] = objson["bounds"][ indexBounds ]
                    indexBounds += 1
                    idP +=1

            if ( opcion in [20,21,24,46,50]) :
                sol_tmp["EP"] = objson["bounds"][ indexBounds ]
                indexBounds += 1
                sol_tmp["HP"] = objson["bounds"][ indexBounds ]
                indexBounds += 1
                if ( opcion in [24,46,50]) :
                    sol_tmp["DP"] = objson["bounds"][ indexBounds ]
                    indexBounds += 1
        sol.append(sol_tmp)
        #print sol_tmp
    return sol

def process_solution( objson ):
    boundsCurse = getBoundsCurse( objson )
    #print "_____________________________Solucion________________________________"
    solution = getSolution( objson, boundsCurse )
    indVal = 0

    for solCurse in range(len(solution)):
        nHTP = noHoursTP(solution[solCurse],objson["metabounds"][indVal])
        nDTP = noDaysTP(solution[solCurse],objson["metabounds"][indVal])
        nSDHTP = noSameDayHourTP(solution[solCurse],objson["metabounds"][indVal])
        nSDHP = noSameDayHourPractice(solution[solCurse],objson["metabounds"][indVal])
        nSDHT = noSameDayHourTheory(solution[solCurse],objson["metabounds"][indVal])
        #print indVal, " ==> ", nHTP, nDTP, nSDHTP, nSDHP, nSDHT
        while False in [nHTP, nDTP, nSDHTP, nSDHP, nSDHT]:
            #print " hola"
            solution[indVal] = getSolution({"metabounds":[objson["metabounds"][indVal]]},[boundsCurse[solCurse]])
            nHTP = noHoursTP(solution[solCurse],objson["metabounds"][indVal])
            nDTP = noDaysTP(solution[solCurse],objson["metabounds"][indVal])
            nSDHTP = noSameDayHourTP(solution[solCurse],objson["metabounds"][indVal])
            nSDHP = noSameDayHourPractice(solution[solCurse],objson["metabounds"][indVal])
            nSDHT = noSameDayHourTheory(solution[solCurse],objson["metabounds"][indVal])
            #print indVal, " ==> ", nHTP, nDTP, nSDHTP, nSDHP, nSDHT
        indVal+=1

    #print "_____________________________________________________________________________________"
    #print "factibilidadGlobal 1"
    index = noSameEHD( solution, objson["metabounds"] )
    '''
    if index != True :
        print "Error en las soluciones"
        print solution[ index[0] ]
        print solution[ index[1] ]
    else :
        print "Todo bien"
    '''
    #print "_____________________________________________________________________________________"
    #print "factibilidadGlobal 2"
    index = noSamePEHD( solution, objson["metabounds"] )
    '''
    if index != True :
        #print "Error en las soluciones"
        #print solution[ index[0] ]
        #print solution[ index[1] ]
    else :
        #print "Todo bien"
    '''
    return [boundsCurse, solution]
