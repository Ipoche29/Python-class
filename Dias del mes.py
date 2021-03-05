def cantidad_dias(mes):
    if mes.lower() in ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"):
        return '31'
    elif mes.lower() == "febrero":
        return "28"
    


nombre_mes = input('Ingrese el nombre del mes:')

print(cantidad_dias(nombre_mes))
