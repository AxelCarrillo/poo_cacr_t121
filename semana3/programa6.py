
"""
Carlos Axel Carrillo Rocha
   Nombre. Axel CR
   Fecha: 31/01/2023
   Descripcion: Calcular el Area y Perimetro de triangulo
"""
print ("Area y Perimetro de un Triangulo")

base= float(input("Digita el tamaño de la base: ")) #Usuario Digitara el tamaño de la base
area= float(input("Digita el tamaño del lado: ")) #Usuario digitara el tamaño de los lados
altura= float(input("Digita el tamaño de la altura: ")) #Usuario Digitara la altura

area= (base*altura)/2 #Proceso para sacar el area con los datos ingresados de base y altura
peri = area*3 #Proceso para sacar el perimetro con los datos de el Area

print("El área del triangulo es: ", area) #Imprimira el Area, ya realizado el proceso anterior
print("El perímetro del triangulo es: ", peri) #Imprimira el Perimetro, ya realzado el proceso anterior
