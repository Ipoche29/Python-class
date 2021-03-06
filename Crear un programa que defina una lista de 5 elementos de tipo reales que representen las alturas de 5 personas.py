estaturas = [5.3, 5.6, 5.9, 6.3, 6.7]
Altura_promedio = (estaturas [0] + estaturas [1] + estaturas [2] + estaturas [3] + estaturas [4]) / 5
personas_altas = 0
personas_bajas = 0
para i en rango (len (estaturas)):
    if float (estaturas [i])> Altura_promedio:
        personas_altas + = 1
    elif float (estaturas [i]) <Altura_promedio:
        personas_bajas + = 1
