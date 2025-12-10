import math
import random


#ejercicio 1
for n in range(0,101,1):
    print(n)


#ejercicio 2

numero = int(input("ingresar numero entero = "))

contarDigitos = len(str(numero))
print(f"la cantidad de digitos es = {contarDigitos}")


#ejercicio 3

valor1 = int(input("ingrese el primer numero = "))
valor2 = int(input("ingrese el segundo valor = "))
suma = 0
for numeros in range(valor1 + 1,valor2,1):
    suma += numeros
    print(suma)
    

#ejercicio 4
numero = int(input("ingrese numero entero = "))
sumar = 0
while numero != 0:
    sumar += numero 
    numero = int(input("ingrese numero entero = "))
    
print(sumar)


#ejercicio 5
numero = int(input("ingrese un numero entre el 0 y el 9 = "))
numeroElegido = random.randint(0, 9)
intentos = 0
while numero != numeroElegido:
    print("numero incorrecto, intente nuevamente")
    numero = int(input("ingrese un numero entre el 0 y el 9 = "))
    intentos += 1
print("numero correcto")
print(f"la cantidad de intentos fue de = {intentos}")


#ejercicio 6
for n in range(100,-1,-2):
    print(n)
    
    
#ejercicio 7
a = 0
contador = 0
numero = int(input("ingrese un numero positivo =  "))
for i in range(a, numero + 1):
    contador += i
print(contador)


#ejercicio 8
    
pares = 0
impares = 0 
positivos = 0
negativos = 0
for n in range(1,101):
    numero = int(input("ingrese 100 numeros para clasificarlos = "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")



#ejercicio 9
suma = 0
media = 0
for n in range(1,101):
    numero = int(input("ingrese 100 numeros para calcular la media = "))
    suma += numero
    media = suma / 100
print(f"La media de los números ingresados es: {media}")



#ejercicio 10
numero = int(input("Ingrese un número entero positivo: "))
numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10
print(f"El número invertido es: {numero_invertido}")

