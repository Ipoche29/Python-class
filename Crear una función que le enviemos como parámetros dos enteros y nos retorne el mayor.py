empleado1 = input ('Escriba el nombre del empleado:')
empleado2 = input ('Escriba el nombre del segundo empleado:')
empleado3 = input ('Escriba el nombre del tercer empleado:')
empleado4 = input ('Escriba el nombre del cuarto empleado:')
empleado5 = input ('Escriba el nombre del quinto empleado:')
sueldos = (15000, 24000, 45000, 85789, 47839)
sueldo1, sueldo2, sueldo3, sueldo4, sueldo5 = sueldos
if sueldo1> sueldo2 and sueldo1> sueldo3 and sueldo1> sueldo4 and sueldo1> sueldo5:
    print (empleado1, 'logro obtener un total de', sueldo1, 'en los ultimos tres meses y fue el que mas gano')
elif sueldo2> sueldo1 and sueldo2> sueldo3 and sueldo2> sueldo4 and sueldo1> sueldo5:
    print (empleado2, 'logro obtener un total de', sueldo2, 'en los ultimos tres meses y fue el que mas gano')
elif sueldo3> sueldo1 and sueldo3> sueldo2 and sueldo3> sueldo4 and sueldo3> sueldo5:
    print (empleado3, 'logro obtener un total de', sueldo3, 'en los ultimos tres meses y fue el que mas gano \ n ')
elif sueldo4> sueldo1 and sueldo4> sueldo2 and sueldo4> sueldo3 and sueldo4> sueldo5:
    print (empleado4, 'logro obtener un total de', sueldo4, 'en los ultimos tres meses y fue el que mas gano')
elif sueldo5> sueldo1 and sueldo5> sueldo2 and sueldo5> sueldo3 and sueldo5> sueldo4:
    print (empleado5, 'logro obtener un total de', sueldo5, 'en los ultimos tres meses y fue el que mas gano')
print ('sueldo obtenido de cada uno en general \ n ')
print('********************')
print ('******************** \ n ')
print (empleado1, sueldo1)
print (empleado2, sueldo2)
print (empleado3, sueldo3)
print (empleado4, sueldo4)
print (empleado5, sueldo5)
print('********************')
print('********************')


