#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FPS2 import *



def copy( asd ) :
    # Copy list
    if type( asd ) == type( [] ) :
        tmp = []
        for e in asd :
            tmp.append( copy( e ) )
        return tmp
    # Copy Dict
    if type( asd ) == type( {} ) :
        tmp = {}
        keys = asd.keys()
        for key in keys :
            tmp[ key ] = copy( asd[ key ] )
        return tmp
    # Copy int
    if type( asd ) == type( 0 ) :
        return asd



def best_candidate( candidate_list, objson ) :
    bc = candidate_list[0]
    for sol in candidate_list :
        if hf( bc, objson ) > hf(sol, objson ) :
            bc = sol
    return bc



def hf( sol, objson ) :
    acum = 0

    profesores = {}
    grupos = {}
    practicas = []
    for i in range( len( sol ) ) :
        # Profesores con horario continuo de clases
        # Grupos con horario continuo de clases

        id_profesor = objson["metabounds"][i]["assignments"][0]["profesor_id"]
        id_grupo = objson["metabounds"][i]["assignments"][0]["grupo_id"]

        if not id_profesor in profesores :
            profesores[ id_profesor ] = []
        if not id_grupo in grupos :
            grupos[ id_grupo ] = []

        if "HG" in sol[i] :
            profesores[ id_profesor ].append( sol[i]["HG"][0] )
            grupos[ id_grupo ].append( sol[i]["HG"][0] )

            if len( objson["metabounds"][i]["practice"] ) > 0 :
                practicas.append( ( sol[i]["HG"][0], objson["metabounds"][i]["practice"][0]["d"] ) )

        if "HT" in sol[i] and "HT1" in sol[i]["HT"] :
            profesores[ id_profesor ].append( sol[i]["HT"]["HT1"][0] )
            profesores[ id_profesor ].append( sol[i]["HT"]["HT2"][0] )
            grupos[ id_grupo ].append( sol[i]["HT"]["HT1"][0] )
            grupos[ id_grupo ].append( sol[i]["HT"]["HT2"][0] )
        elif "HT" in sol[i] :
            profesores[ id_profesor ].append( sol[i]["HT"][0] )
            grupos[ id_grupo ].append( sol[i]["HT"][0] )
        elif "HT1" in sol[i] :
            profesores[ id_profesor ].append( sol[i]["HT1"][0] )
            profesores[ id_profesor ].append( sol[i]["HT2"][0] )
            grupos[ id_grupo ].append( sol[i]["HT1"][0] )
            grupos[ id_grupo ].append( sol[i]["HT2"][0] )

        if "HP" in sol[i] and "HP1" in sol[i]["HP"] :
            profesores[ id_profesor ].append( sol[i]["HP"]["HP1"][0] )
            profesores[ id_profesor ].append( sol[i]["HP"]["HP2"][0] )
            grupos[ id_grupo ].append( sol[i]["HP"]["HP1"][0] )
            grupos[ id_grupo ].append( sol[i]["HP"]["HP2"][0] )
            practicas.append( ( sol[i]["HP"]["HP1"][0], objson["metabounds"][i]["practice"][0]["d"] ) )
            practicas.append( ( sol[i]["HP"]["HP2"][0], objson["metabounds"][i]["practice"][1]["d"] ) )
        elif "HP" in sol[i] :
            profesores[ id_profesor ].append( sol[i]["HP"][0] )
            grupos[ id_grupo ].append( sol[i]["HP"][0] )
            practicas.append( ( sol[i]["HP"][0], objson["metabounds"][i]["practice"][0]["d"] ) )
        elif "HP1" in sol[i] :
            profesores[ id_profesor ].append( sol[i]["HP1"][0] )
            profesores[ id_profesor ].append( sol[i]["HP2"][0] )
            grupos[ id_grupo ].append( sol[i]["HP1"][0] )
            grupos[ id_grupo ].append( sol[i]["HP2"][0] )
            practicas.append( ( sol[i]["HP1"][0], objson["metabounds"][i]["practice"][0]["d"] ) )
            practicas.append( ( sol[i]["HP2"][0], objson["metabounds"][i]["practice"][1]["d"] ) )

    # Profesores con horario continuo de clases
    keys = profesores.keys()
    for key in keys :
        profesores[ key ].sort()
        if len( profesores[ key ] ) > 1 :
            for i in range( len( profesores[ key ] ) - 1 ) :
                # Horas en la mañana
                if profesores[ key ][i] < 14 and profesores[ key ][i+1] < 14 :
                    acum += profesores[ key ][i+1] - profesores[ key ][i] - 1
                # Horas en la tarde
                elif profesores[ key ][i] < 19 and profesores[ key ][i+1] < 19 :
                    acum += profesores[ key ][i+1] - profesores[ key ][i] - 1
                    # Cuenta horas continuas en tarde y mañana ?
                else :
                    acum += profesores[ key ][i+1] - profesores[ key ][i] - 3

    # Grupos con horario continuo de clases
    keys = grupos.keys()
    for key in keys :
        grupos[ key ].sort()
        manana = False
        tarde = False
        if len( grupos[ key ] ) > 1 :
            for i in range( len( grupos[ key ] ) - 1 ) :
                # Horas en la mañana
                if grupos[ key ][i] < 14 and grupos[ key ][i+1] < 14 :
                    manana = True
                    acum += grupos[ key ][i+1] - grupos[ key ][i] - 1
                # Horas en la tarde
                elif grupos[ key ][i] < 19 and grupos[ key ][i+1] < 19 :
                    tarde = True
                    acum += grupos[ key ][i+1] - grupos[ key ][i] - 1
                    # Cuenta horas continuas en tarde y mañana ?
                else :
                    acum += grupos[ key ][i+1] - grupos[ key ][i] - 3
            # Horario distribuido en todo el dia
            if not ( manana and tarde ) :
                    acum += 5

    # Prácticas fuera del horario habitual
    for practica in practicas :
        if practica[0] < 14 :
            if practica[0] + practica[1] > 14 :
                acum += 1
        elif practica[0] < 19 :
            if practica[0] + practica[1] > 19 :
                acum += 1

    return acum



def get_neighbor( sol, objson, boundsSol ) :
    percent_cursos = 40
    percent_keys = 40

    neighbor = copy( sol )
    # Numero de cursos a cambiar
    num_cursos = random.randint( 1, 1 + len(neighbor) * percent_cursos / 100 )

    sol_tmp = getSolution( objson, boundsSol )
    #print "nuevo vecino", num_cursos, range(  )
    #print sol
    #print "-----"
    #print neighbor
    #print "-----"
    for i in range( num_cursos ) :
        #print "ok"
        pos = random.randint( 0, len(neighbor) - 1 )
        keys = sol_tmp[pos].keys()
        #print "keys: ",keys
        # Numero de atributos del curso a cambiar
        num_keys  = random.randint( 1, 1 + len( keys ) * percent_keys / 100)
        for j in range( num_keys ) :
            #print "D: ",sol_tmp[pos] , sol[pos]
            # Un elemenot random EP, ET, HT, ...
            key = keys[ random.randint( 0, num_keys - 1 ) ]
            try :
                neighbor[pos][key] = sol_tmp[pos][key]
                break
            except Exception :
                pass
                #printPretty(sol_tmp)
                #print "-----"
                #printPretty(sol)
                #print "-----"
                #printPretty( boundsSol[pos] )
                #exit(0)

    #print sol
    #print "-----"
    #print neighbor
    #print "-----\n"
    return neighbor



def contains_tabu_list( sol, TABU_LIST ) :
    for curso in sol :
        if curso in TABU_LIST :
            return True
    return False



def features_tabu( sol, objson, TABU_LIST ) :
    index = noSameEHD( sol, objson["metabounds"] )

    if index != True :
        TABU_LIST.append( copy( sol[ index[0] ]) )
        TABU_LIST.append( copy( sol[ index[1] ]) )

    index = noSamePEHD( sol, objson["metabounds"] )

    if index != True :
        TABU_LIST.append( copy( sol[ index[0] ] ) )
        TABU_LIST.append( copy( sol[ index[1] ] ) )




def tabuSearch( sol, objson, boundsSol ) :
    # Parámetros
    MAX_ITERATIONS = 1000
    NUM_NEIGHBOR = 50
    MAXTABU_SIZE = 200

    TIME_LAST_BEST = 0
    MAX_TIME_CHANGE_BEST = 50


    print sol
    print "HF = ", hf( sol, objson )

    # Lista tabú
    TABU_LIST = []

    # Solución incial
    S = sol
    SBest = copy(sol)

    for i in range( MAX_ITERATIONS ) :
    #for i in range( 1 ) :
        candidate_list = []
        neighborhood = []

        # Obtener vecindario
        for j in range( NUM_NEIGHBOR ) :
            neighbor = get_neighbor( SBest, objson, boundsSol )
            neighborhood.append( neighbor )
        #printPretty(neighborhood)

        # Candidatos = vecinos sin características tabú
        for j in range( NUM_NEIGHBOR ) :
            if not contains_tabu_list( neighborhood[ j ], TABU_LIST ) :
                candidate_list.append( neighborhood[ j ] )

        S = best_candidate( candidate_list, objson )

        if hf( S, objson ) < hf( SBest, objson ) :
            TIME_LAST_BEST  = i
            # Ingresamos caracteristicas tabú de la solución a la lista
            features_tabu( S, objson, TABU_LIST )

            # Eliminar características tabú demasiado antiguas
            if len( TABU_LIST ) == MAXTABU_SIZE :
                TABU_LIST.remove( TABU_LIST[0] )

            # Actualizar la mejor solución
            SBest = copy( S )

        if i - TIME_LAST_BEST > MAX_TIME_CHANGE_BEST :
            TIME_LAST_BEST = i
            #print "Tiempo sin cambios, haciendo ajustes..."
            num_elements = random.randint( 0, len( TABU_LIST ) * random.randint( 1, 99 ) / 100 )
            for j in range( num_elements ) :
                TABU_LIST.remove( TABU_LIST[0] )

        #print S
        #print SBest
        #print ""
        #print hf( S, objson )
        #print hf( SBest, objson )

    print SBest
    print "HF = ", hf( SBest, objson )


def main( ) :
    if len( sys.argv ) != 2 :
        print "Argumentos inválidos, especifique un archivo como argumento"
        sys.exit()

    objson = parserJson( sys.argv[1] )
    [boundsSol, sol] = process_solution( objson )
    tabuSearch( sol, objson, boundsSol )



if __name__ == "__main__":
    main()
