#Problema 1
""
def mayor (num1,num2):
    result=None
    if num1>num2:
        result=num1

    elif num2>num1:
        result=num2

    return result #Guarda los datos y los regresa ya para imprimir el correcto en este caso el correcto

print (mayor(2,1)) #Prueba 1 e imprime lo correcto
print (mayor(1,2)) #Prueba 2
print (mayor(50,15)) #Prueba 3
print (mayor(-2,-4)) #Prueba 4
print (mayor(-8,8)) #Prueba 5
print (mayor(2.2,2.1)) #Prueba 6
print (mayor(-2.1,-2.2)) #Prueba 7
print (mayor(50.6,21.2)) #Prueba 8
""

#Problema 2
def mayor (num1:int,num2:int)->int|None:
    result=None
    if num1>num2:
        result=num1

    elif num2>num1:
        result=num2
    return result 

print (mayor(2,1))
print (mayor(1,2))
print (mayor(50,15))
print (mayor(-2,-4))
print (mayor(-8,8))
print (mayor(2.2,2.1))
print (mayor(-2.1,-2.2))
print (mayor(50.6,21.2))








