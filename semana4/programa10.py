"""
   programa9.py
   Nombre. Axel CR
   Fecha: 02/02/2023
   Descripcion: Comparacion de 2 numeros y si son iguales que lo imprima
"""
n1= int(input("Digita un numero: "))
n2= int(input("Digita un segundo numero: ")) 

#Forma 1
if n1>n2:
    print(n1)
if n2>n1:
    print(n1)
if n1 == n2:
    print (None)

#Forma 2
if n2>n1:
    print(n2)
if n1>n2:
    print(n1)
else:
    print (None)

#Forma 3
if n1 > n2:
    print (n1)
elif n2 > n1:
    print (n2)
else:
    print (None)

#Forma 4
if n1==n2:
    print (None)
elif n1>n2:
    print (n1)
elif n2>n1:
    print (n2)

#Forma 5
if n1<n2:
    print(n2)
if n2<n1:
    print (n1)
if n1==n2:
    print (None)

#Forma 6
if n2>n1:
    if n2<n1:
        print (n1)
else:
    print (None)

#Forma 7
if (n2<n1>n2):
    print (n1)
elif (n1<n2>n1):
    print (n2)
else:
    print (None)

#Forma 8
if n1<=n2:
    if n1==n2:
        print (None)
    else:
        print (n2)
else:
    print (n1)

#Forma 9
if 