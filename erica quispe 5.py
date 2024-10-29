
def cifrar(texto,desplazamiento):
    resultado=""
    for i in (texto):
        letra=ord(i) + desplazamiento
        if letra > ord('Z'):
            letra=letra-26
            
        if letra < ord('A'):
            letra=letra+26
            
        else:chr(letra)
            
        resultado=resultado + chr(letra)
    return resultado
        
texto=""
desplazamiento=0
print("ingrese el texto a cifrar")
texto=input()
texto=texto.upper()
print("ingrese el desplazamiento")
desplazamiento=int(input())
mensaje_cifrado=cifrar(texto,desplazamiento)
print(mensaje_cifrado)

