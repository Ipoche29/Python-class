def cajero (saldo, monto, transaccion) :
    nuevosaldo = 100
    z = transaccion
    if z == "1":
        nuevosaldo= saldo+monto
    if z == "2":
        nuevosaldo = saldo-monto
    return nuevosaldo

def menu():
    global trans
    trans="1"
    trans="2"
    trans="3"
    while trans !="3":
       print("Bienvenido al cajero FDP INVERSMENTS")
       print("Seleccione el tipo de transaccon:")
       print("1. Deposito")
       print("2. Giro")
       print("3. Salir")
       trans=input()
       if trans == "1":
           saldo=int(input("ingrese su saldo actual"))
           monto=int(input("ingrese el monto de su transaccion:"))
           print("Tu nuevo saldo es:",cajero(saldo,monto,trans))
           menu()
           
        elif trans == "2":
            saldo=int(input()("Ingrese su saldo:"))
            monto=int(input("ingrese el monto de su transaccion:"))
            print("Tu nuevo saldo es:",cajero(saldo,monto,trans))
            menu()
            
        elif trans == "3":
            print("Gracias por usar FDP INVERSMENTS")
            break
        
                    
       else:
           print("Dato ingresado no valido")
           menu()
           
