import random
LI=1 #LI: Limite Inferior
LS=0 #LS: Limite Superior
opcion=0
print("ingrese una opcion 1 para nivel facil y 2 para dificil")
opcion=int(input())
if opcion==1:
    Intentos=0
    Vidas=6
    Num=0
    LS=20
if opcion==2:
    Intentos=0
    Vidas=7
    Num=0
    LS=200
    
Aleatorio=random.randint(LI,LS)
  
print("secreto:" , Aleatorio)

while(Intentos < Vidas):
    Intentos=Intentos+1
    print("ingrese un numero entre el" , LI ," y " , LS , "usted tendra" , Vidas , "intentos")
    Num=int(input())
    if Num < Aleatorio:
        print("el numero ingresado es menor, intente nuevamente")
    if Num > Aleatorio:
        print("el numero ingresado es mayor, intente nuevamente")
    if Num == Aleatorio:
        print("felicitaciones, adivinaste el numero")
        break
if Intentos == Vidas:
    print("se le acabaron los intentos")
        
    