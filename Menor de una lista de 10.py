lista = []
cantidad = int(input("cantidad:"))
menor = 0
i = 1

while(cantidad > 0) :
    numero = float(input("numero #" + str(i) + ": "))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad - 1


menor = min(lista)

print("Lista:", lista)
print("Menor:", menor)
