import random

Aleatorio=random.randint(1,5)
Intentos=0
Vidas=6
Num=0

while(Intentos == Vidas):
    Intentos=Intentos+1
    print("ingrese un numero entre el 1 y 5 usted tendra 6 intentos")
    Num=int(input())
    if Num < Aleatorio:
        print("el numero ingresado es mayor, intente nuevamente")
    if Num > Aleatorio:
        print("el numero ingresado es menor, intente nuevamente")
    if Num == Aleatorio:
        print("felicitaciones, adivinaste el numero")
    else:
        print("se le acabaron los intentos")
        break
    