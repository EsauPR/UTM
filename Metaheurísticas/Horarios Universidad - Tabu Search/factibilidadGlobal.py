#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Oscar Esaú Peralta Rosales
# esau.opr@gmail.com

def cruceHorasDias( hrs1, days1, hrs2, days2, d1, d2 ) :
    if d1 != False and d2 != False :
        # si se traslanpan las horas
        if abs(hrs1[0] - hrs2[0]) < d1 + d2 - 1:
            # si coinciden en dias
            for day in days1 :
                if day in days2 :
                    return False
    return True

'''
 Dos o mas profesores no pueden estar en el mismo lugar a la misma hora
 el mismo dia, a menos que sea multiasignación
'''
def noSameEHD( sols, cursos ) :
    for i in range( len( sols ) - 1 ):
        for j in range( 1, len( sols ) ) :
            # ET, EP, HT1, HT2, HP1, HP2, DT1, DT2, DP1, DP2, dt1, dt2, dp1, dp2
            values1 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
            values2 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]

            # Espacios de teoria y práctica curso 1
            if "ET" in sols[i]:
                values1[0] = sols[i]["ET"]
            if "EP" in sols[i]:
                values1[1] = sols[i]["EP"]
            # Espacios de teoria y práctica curso 2
            if "ET" in sols[j]:
                values2[0] = sols[j]["ET"]
            if "EP" in sols[j]:
                values2[1] = sols[j]["EP"]


            # Días de teoria curso 1
            # {"DT" : {"DT1" : [], "DT2" : []}}
            if "DT" in sols[i] and "DT1" in sols[i]["DT"] :
                values1[6] = sols[i]["DT"]["DT1"]
                values1[7] = sols[i]["DT"]["DT2"]
            #{"DT" : []}
            elif "DT" in sols[i] :
                values1[6] = sols[i]["DT"]
            # {"DG" : {"DT1" : [], "DT2" : []}}
            elif "DG" in sols[i] and "DT1" in sols[i]["DG"] :
                values1[6] = sols[i]["DG"]["DT1"]
                values1[7] = sols[i]["DG"]["DT2"]
            # {"DT1" : [], "DT2" : []}
            elif "DT1" in sols[i] and "DT2" in sols[i] :
                values1[6] = sols[i]["DT1"]
                values1[7] = sols[i]["DT2"]

            # Días de práctica curso 1
            # {"DT" : {"DT1" : [], "DT2" : []}}
            if "DP" in sols[i] and "DP1" in sols[i]["DP"] :
                values1[8] = sols[i]["DP"]["DP1"]
                values1[9] = sols[i]["DP"]["DP2"]
            #{"DP" : []}
            elif "DP" in sols[i] :
                values1[8] = sols[i]["DP"]
            # {"DG" : {"DP1" : [], "DP2" : []}}
            elif "DG" in sols[i] and "DP1" in sols[i]["DG"] :
                values1[8] = sols[i]["DG"]["DP1"]
                values1[9] = sols[i]["DG"]["DP2"]
            # {"DP1" : [], "DP2" : []}
            elif "DP1" in sols[i] and "DP2" in sols[i] :
                values1[8] = sols[i]["DP1"]
                values1[9] = sols[i]["DP2"]

            # Días de teoria curso 2
            # {"DT" : {"DT1" : [], "DT2" : []}}
            if "DT" in sols[j] and "DT1" in sols[j]["DT"] :
                values2[6] = sols[j]["DT"]["DT1"]
                values2[7] = sols[j]["DT"]["DT2"]
            #{"DT" : []}
            elif "DT" in sols[j] :
                values2[6] = sols[j]["DT"]
            # {"DG" : {"DT1" : [], "DT2" : []}}
            elif "DG" in sols[j] and "DT1" in sols[j]["DG"] :
                values2[6] = sols[j]["DG"]["DT1"]
                values2[7] = sols[j]["DG"]["DT2"]
            # {"DT1" : [], "DT2" : []}
            elif "DT1" in sols[j] and "DT2" in sols[j] :
                values2[6] = sols[j]["DT1"]
                values2[7] = sols[j]["DT2"]

            # Días de práctica curso 2
            # {"DT" : {"DT1" : [], "DT2" : []}}
            if "DP" in sols[j] and "DP1" in sols[j]["DP"] :
                values2[8] = sols[j]["DP"]["DP1"]
                values2[9] = sols[j]["DP"]["DP2"]
            #{"DP" : []}
            elif "DP" in sols[j] :
                values2[8] = sols[j]["DP"]
            # {"DG" : {"DP1" : [], "DP2" : []}}
            elif "DG" in sols[j] and "DP1" in sols[j]["DG"] :
                values2[8] = sols[j]["DG"]["DP1"]
                values2[9] = sols[j]["DG"]["DP2"]
            # {"DP1" : [], "DP2" : []}
            elif "DP1" in sols[j] and "DP2" in sols[j] :
                values2[8] = sols[j]["DP1"]
                values2[9] = sols[j]["DP2"]


            # Horas para teoria curso 1
            # {"HT" : {"HT1" : []. "HT2": []}}
            if "HT" in sols[i] and "HT1" in sols[i]["HT"]:
                values1[2] = sols[i]["HT"]["HT1"]
                values1[3] = sols[i]["HT"]["HT2"]
            # {"HT" : []}
            elif "HT" in sols[i] :
                values1[2] = sols[i]["HT"]
            # {"HT1" : []. "HT2": []}
            elif "HT1" in sols[i] :
                values1[2] = sols[i]["HT1"]
                values1[3] = sols[i]["HT2"]
            elif "HG" in sols[i] :
                # Si no existe uno se valida al obtener la duración
                values1[2] = sols[i]["HG"]
                values1[3] = sols[i]["HG"]
            # Horas de práctica curso 1
            # {"HP" : {"HP1" : []. "HP2": []}}
            if "HP" in sols[i] and "HP1" in sols[i]["HP"]:
                values1[4] = sols[i]["HP"]["HP1"]
                values1[5] = sols[i]["HP"]["HP2"]
            # {"HP" : []}
            elif "HP" in sols[i] :
                values1[4] = sols[i]["HP"]
            # {"HP1" : []. "HP2": []}
            elif "HP1" in sols[i] :
                values1[4] = sols[i]["HP1"]
                values1[5] = sols[i]["HP2"]
            elif "HG" in sols[i] :
                # Si no existe uno se valida al obtener la duración
                values1[4] = sols[i]["HG"]
                values1[5] = sols[i]["HG"]

            # Horas para teoria curso 2
            # {"HT" : {"HT1" : []. "HT2": []}}
            if "HT" in sols[i] and "HT1" in sols[i]["HT"]:
                values2[2] = sols[j]["HT"]["HT1"]
                values2[3] = sols[j]["HT"]["HT2"]
            # {"HT" : []}
            elif "HT" in sols[j] :
                values2[2] = sols[j]["HT"]
            # {"HT1" : []. "HT2": []}
            elif "HT1" in sols[j] :
                values2[2] = sols[j]["HT1"]
                values2[3] = sols[j]["HT2"]
            elif "HG" in sols[j] :
                # Si no existe uno se valida al obtener la duración
                values2[2] = sols[j]["HG"]
                values2[3] = sols[j]["HG"]
            # Horas de práctica curso 2
            # {"HP" : {"HP1" : []. "HP2": []}}
            if "HP" in sols[j] and "HP1" in sols[j]["HP"]:
                values2[4] = sols[j]["HP"]["HP1"]
                values2[5] = sols[j]["HP"]["HP2"]
            # {"HP" : []}
            elif "HP" in sols[j] :
                values2[4] = sols[j]["HP"]
            # {"HP1" : []. "HP2": []}
            elif "HP1" in sols[j] :
                values2[4] = sols[j]["HP1"]
                values2[5] = sols[j]["HP2"]
            elif "HG" in sols[j] :
                # Si no existe uno se valida al obtener la duración
                values2[4] = sols[j]["HG"]
                values2[5] = sols[j]["HG"]

            # Duraciones de clases de Teoria y prática curso 1
            if( len( cursos[i]["theory"] ) > 0 ) :
                values1[10] == cursos[i]["theory"][0]["d"]
            if( len( cursos[i]["theory"] ) > 1 ) :
                values1[11] == cursos[i]["theory"][1]["d"]
            if( len( cursos[i]["practice"] ) > 0 ) :
                values1[12] == cursos[i]["practice"][0]["d"]
            if( len( cursos[i]["practice"] ) > 1 ) :
                values1[13] == cursos[i]["practice"][1]["d"]

            # Duraciones de clases de Teoria y prática curso 2
            if( len( cursos[j]["theory"] ) > 0 ) :
                values2[10] == cursos[j]["theory"][0]["d"]
            if( len( cursos[j]["theory"] ) > 1 ) :
                values2[11] == cursos[j]["theory"][1]["d"]
            if( len( cursos[j]["practice"] ) > 0 ) :
                values2[12] == cursos[j]["practice"][0]["d"]
            if( len( cursos[j]["practice"] ) > 1 ) :
                values2[13] == cursos[j]["practice"][1]["d"]

            check = True

            # Validación
            # ET == ET
            if values1[0] != False and values1[0] == values2[0] :
                # HT1 == HT1
                check = check and cruceHorasDias( values1[2], values1[6], values1[10], values2[2], values2[6], values1[10] )
                # HT1 == HT2
                check = check and cruceHorasDias( values1[2], values1[6], values1[10], values2[3], values2[7], values1[11] )
                # HT2 == HT1
                check = check and cruceHorasDias( values1[3], values1[7], values1[11], values2[2], values2[6], values1[10] )
                # HT2 == HT2
                check = check and cruceHorasDias( values1[3], values1[7], values1[11], values2[3], values2[7], values1[11] )

            # ET == EP
            if values1[0] != False and values1[0] == values2[1] :
                # HT1 == HP1
                check = check and cruceHorasDias( values1[2], values1[6], values1[10], values2[4], values2[8], values1[12] )
                # HT1 == HP2
                check = check and cruceHorasDias( values1[2], values1[6], values1[10], values2[5], values2[9], values1[13] )
                # HT2 == HP1
                check = check and cruceHorasDias( values1[3], values1[7], values1[11], values2[4], values2[8], values1[12] )
                # HT2 == HP2
                check = check and cruceHorasDias( values1[3], values1[7], values1[11], values2[5], values2[9], values1[13] )
            # EP == ET
            if values1[1] != False and values1[1] == values2[0] :
                # HP1 == HT1
                check = check and cruceHorasDias( values1[4], values1[8], values1[12], values2[2], values2[6], values1[10] )
                # HP1 == HT2
                check = check and cruceHorasDias( values1[4], values1[8], values1[12], values2[3], values2[7], values1[11] )
                # HP2 == HT1
                check = check and cruceHorasDias( values1[5], values1[9], values1[13], values2[2], values2[6], values1[10] )
                # HP2 == HT2
                check = check and cruceHorasDias( values1[5], values1[9], values1[13], values2[3], values2[7], values1[11] )

            # EP == EP
            if values1[1] != False and values1[1] == values2[1] :
                # HP1 == HP1
                check = check and cruceHorasDias( values1[4], values1[8], values1[12], values2[4], values2[8], values1[12] )
                # HP1 == HP2
                check = check and cruceHorasDias( values1[4], values1[8], values1[12], values2[5], values2[9], values1[13] )
                # HP2 == HP1
                check = check and cruceHorasDias( values1[5], values1[9], values1[13], values2[4], values2[8], values1[12] )
                # HP2 == HP2
                check = check and cruceHorasDias( values1[5], values1[9], values1[13], values2[5], values2[9], values1[13] )

            if check == False :
                return [i,j]

    return True



def noSamePEHD( sols, cursos ) :
    for i in range( len( sols ) ):
        for j in range( len( sols ) ) :
            if cursos[j]["assignments"][0]["profesor_id"] == cursos[i]["assignments"][0]["profesor_id"]:
                # ET, EP, HT1, HT2, HP1, HP2, DT1, DT2, DP1, DP2, dt1, dt2, dp1, dp2
                values1 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
                values2 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]

                # Espacios de teoria y práctica curso 1
                if "ET" in sols[i]:
                    values1[0] = sols[i]["ET"]
                if "EP" in sols[i]:
                    values1[1] = sols[i]["EP"]
                # Espacios de teoria y práctica curso 2
                if "ET" in sols[j]:
                    values2[0] = sols[j]["ET"]
                if "EP" in sols[j]:
                    values2[1] = sols[j]["EP"]


                # Días de teoria curso 1
                # {"DT" : {"DT1" : [], "DT2" : []}}
                if "DT" in sols[i] and "DT1" in sols[i]["DT"] :
                    values1[6] = sols[i]["DT"]["DT1"]
                    values1[7] = sols[i]["DT"]["DT2"]
                #{"DT" : []}
                elif "DT" in sols[i] :
                    values1[6] = sols[i]["DT"]
                # {"DG" : {"DT1" : [], "DT2" : []}}
                elif "DG" in sols[i] and "DT1" in sols[i]["DG"] :
                    values1[6] = sols[i]["DG"]["DT1"]
                    values1[7] = sols[i]["DG"]["DT2"]
                # {"DT1" : [], "DT2" : []}
                elif "DT1" in sols[i] and "DT2" in sols[i] :
                    values1[6] = sols[i]["DT1"]
                    values1[7] = sols[i]["DT2"]

                # Días de práctica curso 1
                # {"DT" : {"DT1" : [], "DT2" : []}}
                if "DP" in sols[i] and "DP1" in sols[i]["DP"] :
                    values1[8] = sols[i]["DP"]["DP1"]
                    values1[9] = sols[i]["DP"]["DP2"]
                #{"DP" : []}
                elif "DP" in sols[i] :
                    values1[8] = sols[i]["DP"]
                # {"DG" : {"DP1" : [], "DP2" : []}}
                elif "DG" in sols[i] and "DP1" in sols[i]["DG"] :
                    values1[8] = sols[i]["DG"]["DP1"]
                    values1[9] = sols[i]["DG"]["DP2"]
                # {"DP1" : [], "DP2" : []}
                elif "DP1" in sols[i] and "DP2" in sols[i] :
                    values1[8] = sols[i]["DP1"]
                    values1[9] = sols[i]["DP2"]

                # Días de teoria curso 2
                # {"DT" : {"DT1" : [], "DT2" : []}}
                if "DT" in sols[j] and "DT1" in sols[j]["DT"] :
                    values2[6] = sols[j]["DT"]["DT1"]
                    values2[7] = sols[j]["DT"]["DT2"]
                #{"DT" : []}
                elif "DT" in sols[j] :
                    values2[6] = sols[j]["DT"]
                # {"DG" : {"DT1" : [], "DT2" : []}}
                elif "DG" in sols[j] and "DT1" in sols[j]["DG"] :
                    values2[6] = sols[j]["DG"]["DT1"]
                    values2[7] = sols[j]["DG"]["DT2"]
                # {"DT1" : [], "DT2" : []}
                elif "DT1" in sols[j] and "DT2" in sols[j] :
                    values2[6] = sols[j]["DT1"]
                    values2[7] = sols[j]["DT2"]

                # Días de práctica curso 2
                # {"DT" : {"DT1" : [], "DT2" : []}}
                if "DP" in sols[j] and "DP1" in sols[j]["DP"] :
                    values2[8] = sols[j]["DP"]["DP1"]
                    values2[9] = sols[j]["DP"]["DP2"]
                #{"DP" : []}
                elif "DP" in sols[j] :
                    values2[8] = sols[j]["DP"]
                # {"DG" : {"DP1" : [], "DP2" : []}}
                elif "DG" in sols[j] and "DP1" in sols[j]["DG"] :
                    values2[8] = sols[j]["DG"]["DP1"]
                    values2[9] = sols[j]["DG"]["DP2"]
                # {"DP1" : [], "DP2" : []}
                elif "DP1" in sols[j] and "DP2" in sols[j] :
                    values2[8] = sols[j]["DP1"]
                    values2[9] = sols[j]["DP2"]


                # Horas para teoria curso 1
                # {"HT" : {"HT1" : []. "HT2": []}}
                if "HT" in sols[i] and "HT1" in sols[i]["HT"]:
                    values1[2] = sols[i]["HT"]["HT1"]
                    values1[3] = sols[i]["HT"]["HT2"]
                # {"HT" : []}
                elif "HT" in sols[i] :
                    values1[2] = sols[i]["HT"]
                # {"HT1" : []. "HT2": []}
                elif "HT1" in sols[i] :
                    values1[2] = sols[i]["HT1"]
                    values1[3] = sols[i]["HT2"]
                elif "HG" in sols[i] :
                    # Si no existe uno se valida al obtener la duración
                    values1[2] = sols[i]["HG"]
                    values1[3] = sols[i]["HG"]
                # Horas de práctica curso 1
                # {"HP" : {"HP1" : []. "HP2": []}}
                if "HP" in sols[i] and "HP1" in sols[i]["HP"]:
                    values1[4] = sols[i]["HP"]["HP1"]
                    values1[5] = sols[i]["HP"]["HP2"]
                # {"HP" : []}
                elif "HP" in sols[i] :
                    values1[4] = sols[i]["HP"]
                # {"HP1" : []. "HP2": []}
                elif "HP1" in sols[i] :
                    values1[4] = sols[i]["HP1"]
                    values1[5] = sols[i]["HP2"]
                elif "HG" in sols[i] :
                    # Si no existe uno se valida al obtener la duración
                    values1[4] = sols[i]["HG"]
                    values1[5] = sols[i]["HG"]

                # Horas para teoria curso 2
                # {"HT" : {"HT1" : []. "HT2": []}}
                if "HT" in sols[i] and "HT1" in sols[i]["HT"]:
                    values2[2] = sols[j]["HT"]["HT1"]
                    values2[3] = sols[j]["HT"]["HT2"]
                # {"HT" : []}
                elif "HT" in sols[j] :
                    values2[2] = sols[j]["HT"]
                # {"HT1" : []. "HT2": []}
                elif "HT1" in sols[j] :
                    values2[2] = sols[j]["HT1"]
                    values2[3] = sols[j]["HT2"]
                elif "HG" in sols[j] :
                    # Si no existe uno se valida al obtener la duración
                    values2[2] = sols[j]["HG"]
                    values2[3] = sols[j]["HG"]
                # Horas de práctica curso 2
                # {"HP" : {"HP1" : []. "HP2": []}}
                if "HP" in sols[j] and "HP1" in sols[j]["HP"]:
                    values2[4] = sols[j]["HP"]["HP1"]
                    values2[5] = sols[j]["HP"]["HP2"]
                # {"HP" : []}
                elif "HP" in sols[j] :
                    values2[4] = sols[j]["HP"]
                # {"HP1" : []. "HP2": []}
                elif "HP1" in sols[j] :
                    values2[4] = sols[j]["HP1"]
                    values2[5] = sols[j]["HP2"]
                elif "HG" in sols[j] :
                    # Si no existe uno se valida al obtener la duración
                    values2[4] = sols[j]["HG"]
                    values2[5] = sols[j]["HG"]

                # Duraciones de clases de Teoria y prática curso 1
                if( len( cursos[i]["theory"] ) > 0 ) :
                    values1[10] == cursos[i]["theory"][0]["d"]
                if( len( cursos[i]["theory"] ) > 1 ) :
                    values1[11] == cursos[i]["theory"][1]["d"]
                if( len( cursos[i]["practice"] ) > 0 ) :
                    values1[12] == cursos[i]["practice"][0]["d"]
                if( len( cursos[i]["practice"] ) > 1 ) :
                    values1[13] == cursos[i]["practice"][1]["d"]

                # Duraciones de clases de Teoria y prática curso 2
                if( len( cursos[j]["theory"] ) > 0 ) :
                    values2[10] == cursos[j]["theory"][0]["d"]
                if( len( cursos[j]["theory"] ) > 1 ) :
                    values2[11] == cursos[j]["theory"][1]["d"]
                if( len( cursos[j]["practice"] ) > 0 ) :
                    values2[12] == cursos[j]["practice"][0]["d"]
                if( len( cursos[j]["practice"] ) > 1 ) :
                    values2[13] == cursos[j]["practice"][1]["d"]

                check = True

                # Validación
                # ET == ET
                if values1[0] != False and values1[0] == values2[0] :
                    # HT1 == HT1
                    check = check and cruceHorasDias( values1[2], values1[6], values1[10], values2[2], values2[6], values1[10] )
                    # HT1 == HT2
                    check = check and cruceHorasDias( values1[2], values1[6], values1[10], values2[3], values2[7], values1[11] )
                    # HT2 == HT1
                    check = check and cruceHorasDias( values1[3], values1[7], values1[11], values2[2], values2[6], values1[10] )
                    # HT2 == HT2
                    check = check and cruceHorasDias( values1[3], values1[7], values1[11], values2[3], values2[7], values1[11] )

                # ET == EP
                if values1[0] != False and values1[0] == values2[1] :
                    # HT1 == HP1
                    check = check and cruceHorasDias( values1[2], values1[6], values1[10], values2[4], values2[8], values1[12] )
                    # HT1 == HP2
                    check = check and cruceHorasDias( values1[2], values1[6], values1[10], values2[5], values2[9], values1[13] )
                    # HT2 == HP1
                    check = check and cruceHorasDias( values1[3], values1[7], values1[11], values2[4], values2[8], values1[12] )
                    # HT2 == HP2
                    check = check and cruceHorasDias( values1[3], values1[7], values1[11], values2[5], values2[9], values1[13] )
                # EP == ET
                if values1[1] != False and values1[1] == values2[0] :
                    # HP1 == HT1
                    check = check and cruceHorasDias( values1[4], values1[8], values1[12], values2[2], values2[6], values1[10] )
                    # HP1 == HT2
                    check = check and cruceHorasDias( values1[4], values1[8], values1[12], values2[3], values2[7], values1[11] )
                    # HP2 == HT1
                    check = check and cruceHorasDias( values1[5], values1[9], values1[13], values2[2], values2[6], values1[10] )
                    # HP2 == HT2
                    check = check and cruceHorasDias( values1[5], values1[9], values1[13], values2[3], values2[7], values1[11] )

                # EP == EP
                if values1[1] != False and values1[1] == values2[1] :
                    # HP1 == HP1
                    check = check and cruceHorasDias( values1[4], values1[8], values1[12], values2[4], values2[8], values1[12] )
                    # HP1 == HP2
                    check = check and cruceHorasDias( values1[4], values1[8], values1[12], values2[5], values2[9], values1[13] )
                    # HP2 == HP1
                    check = check and cruceHorasDias( values1[5], values1[9], values1[13], values2[4], values2[8], values1[12] )
                    # HP2 == HP2
                    check = check and cruceHorasDias( values1[5], values1[9], values1[13], values2[5], values2[9], values1[13] )

                if check == False :
                    return [i,j]

    return True
