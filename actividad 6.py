suma=0
contrasuma=0
contramulti=1
multi=1
matriz=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

for i in range (len(matriz)):
    for j in range (len(matriz)):
        (matriz[i][j])
        if ([i]==[j]):
            suma=suma + matriz[i][j]
            multi=multi * matriz[i][j]
        if(j==3-i):
            contrasuma=contrasuma + matriz[i][j]
            contramulti=contramulti * matriz[i][j]
print(matriz)
print(suma)
print(multi)
print("la suma de la diagonal es" , suma , "y la multiplicacion" , multi)
print(contrasuma)
print(contramulti)
print("la contra suma es" , contrasuma , "y la contra multiplicacion es" , contramulti)
                