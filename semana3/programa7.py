"""
   programa7.py
   Nombre. Axel CR
   Fecha: 31/01/2023
   Descripcion: Calcular el Area y Perimetro de un circulo y Cuadrado
"""

#---------------------------------------AREA Y PERIMETRO DEL CIRCULO--------------------------------------------
print ("Area y Perimetro de un Circulo") #Imprime un texto para el usuario
print("") #ESPACIO POR ESTETICA
diametro= float(input("Digita el diametro de tu circulo: ")) #AREA Y PERIMETRO DEL CIRCULO
radio= diametro/2 #Proceso para el radio del circulo
area_cir= 3.1416*radio**2 #Proceso para el area del circulo
peri_cir = 2*3.1416*radio #Proceso para el perimetro del circulo
print ("El area de un circulo de {} de radio es {}".format(diametro,area_cir)) #Imprime el area del Circulo, realizando el proceso anterior 
print ("El perimetro de un circulo de {} de radio es {}".format(diametro,peri_cir)) #Imprime el perimetro del Circulo, realizando el proceso anterior

print("") #ESPACIO POR ESTETICA
print("") #ESPACIO POR ESTETICA

#-----------------------------------------AREA Y PERIMETRO CUADRADO---------------------------------------------
print ("Area y Perimetro de un Cuadrado") #Imprime un texto para el Usuario
print("") #ESPACIO POR ESTETICA
lado= float(input("Digita la medida de los lados del cuadrado: ")) #Ingresa datos de los lados del cuadrado
area_cua= lado**2 #Proceso para el area del cuadrado
peri_cua= lado*4 #Proceso para el area del cuadrado
print ("El area de un cuadrado de {}cm es: {}".format(lado,area_cua)) #Imprime el area del cuadrado, realizando el proceso anterior
print ("El perimetro de un cuadrado de {}cm es: {}".format(lado,peri_cua)) #Imprime el perimetro del cuadrado, realizando el proceso anterior



"""
print("El numero {} / {} es {} ".format(num1,num2,num1/num2)) #Anotacion para guiarme
"""