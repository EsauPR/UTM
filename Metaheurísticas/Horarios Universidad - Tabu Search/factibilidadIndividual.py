#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Oscar Esaú Peralta Rosales
# esau.opr@gmail.com

# Las clases de teoría no sean el mismo día, a la misma hora.
def noSameDayHourTheory(sol, curso) :
    if "HT" in sol and "HT1" in sol["HT"] and "HT2" in sol["HT"]:
        HT1 = sol["HT"]["HT1"]
        HT2 = sol["HT"]["HT2"]

        if "DT" in sol and "DT1" in sol["DT"] and "DT2" in sol["DT"] :
            DT1 = sol["DT"]["DT1"]
            DT2 = sol["DT"]["DT2"]
            # Si es difenrente dia no hay problema que sea a la misma hora
            if DT1 != DT2 :
                return True

        if "DG" in sol and "DT1" in sol["DG"] and "DT2" in sol["DG"] :
            DT1 = sol["DG"]["DT1"]
            DT2 = sol["DG"]["DT2"]
            # Si es difenrente dia no hay problema que sea a la misma hora
            if DT1 != DT2 :
                return True

        # Si es a la misma hora
        if( HT1 == HT2 ) :
            return False

    if "HT1" in sol and "HT2" in sol :
        HT1 = sol["HT1"]
        HT2 = sol["HT2"]

        if "DT1" in sol and "DT2" in sol :
            DT1 = sol["DT1"]
            DT2 = sol["DT2"]
            # Si es difenrente dia no hay problema que sea a la misma hora
            if DT1 != DT2 :
                return True
        # Si es a la misma hora
        if( HT1 == HT2 ) :
            return False

    return True


# Las clases de práctica no sean el mismo día, a la misma hora.
def noSameDayHourPractice(sol, curso) :
    if "HP" in sol and "HP1" in sol["HP"] and "HP2" in sol["HP"]:
        HP1 = sol["HP"]["HP1"]
        HP2 = sol["HP"]["HP2"]

        if "DP" in sol and "DP1" in sol["DP"] and "DP2" in sol["DP"] :
            DP1 = sol["DP"]["DP1"]
            DP2 = sol["DP"]["DP2"]
            # Si es difenrente dia no hay problema que sea a la misma hora
            if DP1 != DP2 :
                return True

        if "DG" in sol and "DP1" in sol["DG"] and "DP2" in sol["DG"] :
            DP1 = sol["DG"]["DP1"]
            DP2 = sol["DG"]["DP2"]
            # Si es difenrente dia no hay problema que sea a la misma hora
            if DP1 != DP2 :
                return True

        # Si es a la misma hora
        if( HP1 == HP2 ) :
            return False

    if "HP1" in sol and "HP2" in sol :
        HP1 = sol["HP1"]
        HP2 = sol["HP2"]

        if "DP1" in sol and "DP2" in sol :
            DP1 = sol["DP1"]
            DP2 = sol["DP2"]
            # Si es difenrente dia no hay problema que sea a la misma hora
            if DP1 != DP2 :
                return True
        # Si es a la misma hora
        if( HP1 == HP2 ) :
            return False

    return True


def validaHourDayTP( ht, dt, hp, dp, tt, tp) :
    # Si coinciden en algún día
    for day in dt :
        if day in dp :
            # si coinciden las horas o se cruzan por duración
            if abs(ht - hp) < tt + tp - 1:
                return False
    return True


# Las clases de teoría y práctica no sean a la misma hora el mismo día.
def noSameDayHourTP( sol, curso ) :
    # No importa cuando teoria y practica se dan a la misma hora
    if curso["samehourtp"] == True :
        return True

    HT1 = False
    HT2 = False
    HP1 = False
    HP2 = False
    DT1 = False
    DT2 = False
    DP1 = False
    DP2 = False
    tt1 = False
    tt2 = False
    tp1 = False
    tp2 = False

    check = True

    if "DT" in sol and "DP" in sol :
        # {"HT" : {"HT1" : [], "HT2" : [] } }
        if "HT" in sol and "HT1" in sol["HT"] and "HT2" in sol["HT"] :
            HT1 = sol["HT"]["HT1"][0]
            HT2 = sol["HT"]["HT2"][0]
        # {"HT1" : [], "HT2" : [] }
        elif "HT1" in sol and "HT2" in sol :
            HT1 = sol["HT1"][0]
            HT1 = sol["HT2"][0]
        # {"HT" : [] }
        elif "HT" in sol :
            HT1 = sol["HT"][0]
        # {"HP" : {"HP1" : [], "HP2" : [] } }
        if "HP" in sol and "HP1" in sol["HP"] and "HP2" in sol["HP"] :
            HP1 = sol["HP"]["HP1"][0]
            HP2 = sol["HP"]["HP2"][0]
        # {"HP1" : [], "HP2" : [] }
        elif "HP1" in sol and "HP2" in sol :
            HP1 = sol["HP1"][0]
            HP2 = sol["HP2"][0]
        # {"HP" : [] }
        elif "HP" in sol :
            HP1 = sol["HP"][0]

        # {"DG : {"DT1 : []", DT2 : []}"}
        if "DG" in sol and "DT1" in sol["DG"] and "DT2" in sol["DG"] :
            DT1 = sol["DG"]["DT1"]
            DT2 = sol["DG"]["DT2"]
        # {"DG" : {"DT" : []"}}
        elif "DG" in sol and "DT" in sol["DG"] :
            DT1 = sol["DG"]["DT"]
        # {"DT : {"DT1: []", DT2 : []}"}
        elif "DT" in sol and "DT1" in sol["DT"] and "DT2" in sol["DT"] :
            DT1 = sol["DT"]["DT1"]
            DT2 = sol["DT"]["DT2"]
        # {"DT1 : []", "DT2: []"}
        elif "DT1" in sol and "DT2" in sol :
            DT1 = sol["DT1"]
            DT2 = sol["DT2"]
        # {"DT : []"}
        elif "DT" in sol :
            DT1 = sol["DT"]

        # {"DG : {"DP1 : []", DP2 : []}"}
        if "DG" in sol and "DP1" in sol["DG"] and "DP2" in sol["DG"] :
            DP1 = sol["DG"]["DP1"]
            DP2 = sol["DG"]["DP2"]
        # {"DG" : {"DP" : []"}}
        elif "DG" in sol and "DP" in sol["DG"] :
            DP1 = sol["DG"]["DP"]
        # {"DP : {"DP1: []", DP2 : []}"}
        elif "DP" in sol and "DP1" in sol["DP"] and "DP2" in sol["DP"] :
            DP1 = sol["DP"]["DP1"]
            DP2 = sol["DP"]["DP2"]
        # {"DP1 : []", "DP2: []"}
        elif "DP1" in sol and "DP2" in sol :
            DP1 = sol["DP1"]
            DP2 = sol["DP2"]
        # {"DP : []"}
        elif "DP" in sol :
            DP1 = sol["DP"]

        #Duraciones de los cursos
        if( len( curso["theory"] ) > 0 ) :
            tt1 == curso["theory"][0]["d"]
        if( len( curso["theory"] ) > 1 ) :
            tt2 == curso["theory"][1]["d"]
        if( len( curso["practice"] ) > 0 ) :
            tp1 == curso["practice"][0]["d"]
        if( len( curso["practice"] ) > 1 ) :
            tp2 == curso["practice"][1]["d"]

        # validadando
        check = check and validaHourDayTP( HT1, DT1, HP1, DP1, tt1, tp1 )
        if HP2 :
            check = check and validaHourDayTP( HT1, DT1, HP2, DP2, tt1, tp2 )
        if HT2 :
            check = check and validaHourDayTP( HT2, DT2, HP1, DP1, tt2, tp1 )
        if HT2 and HP2 :
            check = check and validaHourDayTP( HT2, DT2, HP2, DP2, tt2, tp2 )

    return check


def validaDay( d1, noDays1, d2 = False, noDays2 = False ) :
    # Para cada dia del curso se verifica si existe en el atributo nodays
    for day in d1 :
        if day in noDays1 :
            return false
    # Si existe un segundo curso
    if d2 :
        for day in d2 :
            if day in noDays2 :
                return False
    return True


# Las clases no se impartan durante algún día restringido para alguna de ellas (nodays).
def noDaysTP(sol, curso) :
    check = True
    # {"DG : {"DT1 : []", DT2 : []}"}
    if "DG" in sol and "DT1" in sol["DG"] and "DT2" in sol["DG"] :
        DT1 = sol["DG"]["DT1"]
        DT2 = sol["DG"]["DT2"]
        check  = check and validaDay( DT1, curso["theory"][0]["nodays"], DT2, curso["theory"][1]["nodays"] )
    # {"DG" : {"DT" : []"}}
    elif "DG" in sol and "DT" in sol["DG"] :
        DT1 = sol["DG"]["DT"]
        check  = check and validaDay( DT1, curso["theory"][0]["nodays"])
    # {"DT : {"DT1: []", DT2 : []}"}
    elif "DT" in sol and "DT1" in sol["DT"] and "DT2" in sol["DT"] :
        DT1 = sol["DT"]["DT1"]
        DT2 = sol["DT"]["DT2"]
        check  = check and validaDay( DT1, curso["theory"][0]["nodays"], DT2, curso["theory"][1]["nodays"] )
    # {"DT1 : []", "DT2: []"}
    elif "DT1" in sol and "DT2" in sol :
        DT1 = sol["DT1"]
        DT2 = sol["DT2"]
        check  = check and validaDay( DT1, curso["theory"][0]["nodays"], DT2, curso["theory"][1]["nodays"] )
    # {"DT : []"}
    elif "DT" in sol :
        DT = sol["DT"]
        check  = check and validaDay( DT, curso["theory"][0]["nodays"] )

    # {"DG : {"DT1 : []", DT2 : []}"}
    if "DG" in sol and "DP1" in sol["DG"] and "DP2" in sol["DG"] :
        DP1 = sol["DG"]["DP1"]
        DP2 = sol["DG"]["DP2"]
        check  = check and validaDay( DP1, curso["practice"][0]["nodays"], DP2, curso["practice"][1]["nodays"] )
    # {"DG" : {"DP" : []"}}
    elif "DG" in sol and "DP" in sol["DG"] :
        DP1 = sol["DG"]["DP"]
        check  = check and validaDay( DP1, curso["practice"][0]["nodays"])
    # {"DP : {"DP1: []", DP2 : []}"}
    elif "DP" in sol and "DP1" in sol["DP"] and "DP2" in sol["DP"] :
        DP1 = sol["DP"]["DP1"]
        DP2 = sol["DP"]["DP2"]
        check  = check and validaDay( DP1, curso["practice"][0]["nodays"], DP2, curso["practice"][1]["nodays"] )
    # {"DP1 : []", "DP2: []"}
    elif "DP1" in sol and "DP2" in sol :
        DP1 = sol["DP1"]
        DP2 = sol["DP2"]
        check  = check and validaDay( DP1, curso["practice"][0]["nodays"], DP2, curso["practice"][1]["nodays"] )
    # {"DP : []"}
    elif "DP" in sol :
        DP = sol["DP"]
        check  = check and validaDay( DP, curso["practice"][0]["nodays"] )

    return check


def validaHour2( h1, h2, cursos, d1 = False, d2 = False ) :
    # en hora restringida
    if h1[0] in cursos[0]["nohours"] or h2[0] in cursos[1]["nohours"] :
        return False

    # mismo dia (existe vector de dias por cada uno)
    if d1[0] == True :
        for day in d1 :
            if day in d2 :
                # se traslapan los cursos por duración o la misma hora
                if abs(h2[0] - h1[0]) < cursos[0]["d"] + cursos[1]["d"] - 1:
                    return False

    # se traslapan los cursos por duración o la misma hora (No existe vector de dias)
    elif d1[0] == False and abs(h2[0] - h1[0]) < cursos[0]["d"] + cursos[1]["d"] - 1:
        return False
    return True


def validaHour1( h, cursos ) :
    if h[0] in cursos[0]["nohours"] :
        return False
    return True

# Las clases de teoría no sean el mismo día, a la misma hora.
def noHoursTP( sol, curso ) :
    check = True

    d1 = False
    d2 = False

    # Dias para teoria
    # {"DT" : {"DT1" : [], "DT2" : []}}
    if "DT" in sol and "DT1" in sol["DT"]:
        d1 = sol["DT"]["DT1"]
        d2 = sol["DT"]["DT2"]
    # {"DG" : {"DT1" : [], "DT2" : []}}
    if "DG" in sol and "DT1" in sol["DG"]:
        d1 = sol["DG"]["DT1"]
        d2 = sol["DG"]["DT2"]
    # {"DT1" : [], "DT2" : []}
    if "DT1" in sol and "DT2" in sol:
        d1 = sol["DT1"]
        d2 = sol["DT2"]

    # Horas para teoria
    # {"HT" : {"HT1" : [], "HT2" : [] } }
    if "HT" in sol and "HT1" in sol["HT"] and "HT2" in sol["HT"] :
        HT1 = sol["HT"]["HT1"]
        HT2 = sol["HT"]["HT2"]
        check = check and validaHour2( HT1, HT2, curso["theory"], d1, d2 )
    # {"HT1" : [], "HT2" : [] }
    elif "HT1" in sol and "HT2" in sol :
        HT1 = sol["HT1"]
        HT2 = sol["HT2"]
        check = check and validaHour2( HT1, HT2, curso["theory"], d1, d2 )
    # {"HT" : [] }
    elif "HT" in sol :
        check = check and validaHour1( sol["HT"], curso["theory"] )

    d1 = False
    d2 = False
    # dias para practica
    # {"DP" : {"DP1" : [], "DP2" : []}}
    if "DP" in sol and "DP1" in sol["DP"]:
        d1 = sol["DP"]["DP1"]
        d2 = sol["DP"]["DP2"]
    # {"DG" : {"DP1" : [], "DP2" : []}}
    if "DG" in sol and "DP1" in sol["DG"]:
        d1 = sol["DG"]["DP1"]
        d2 = sol["DG"]["DP2"]
    # {"DP1" : [], "DP2" : []}
    if "DP1" in sol and "DP2" in sol:
        d1 = sol["DP1"]
        d2 = sol["DP2"]

    # horas para practica
    # {"HP" : {"HP1" : [], "HP2" : [] } }
    if "HP" in sol and "HP1" in sol["HP"] and "HP2" in sol["HP"] :
        HP1 = sol["HP"]["HP1"]
        HP2 = sol["HP"]["HP2"]
        check = check and validaHour2( HP1, HP2, curso["practice"], d1, d2 )
    # {"HP1" : [], "HP2" : [] }
    elif "HP1" in sol and "HP2" in sol :
        HP1 = sol["HP1"]
        HP2 = sol["HP2"]
        check = check and validaHour2( HP1, HP2, curso["practice"], d1, d2 )
    # {"HP" : [] }
    elif "HP" in sol :
        check = check and validaHour1( sol["HP"], curso["practice"] )

    return check
