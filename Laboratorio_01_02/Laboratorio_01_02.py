import math
from typing import List

# --------------------------------------------------------------------------------
# 1. Realiza la suma, resta, multiplicación y división de dos números ingresados por el usuario
num1 = int(input("a:")) #solicitamos al usuario que ingrese dos numeros a y b
num2 = int(input("b:"))
print(f"a + b:{num1+num2}\na - b:{num1-num2}\na x b:{num1*num2}\na / b:{num1/num2}")#imprimimos la suma, resta, multiplicacion y division de a y b

# --------------------------------------------------------------------------------
# 2. Solicita un número al usuario y determina si es par o impar.
numero = int(input("numero:")) #solicitamos al usuario que ingrese un numero
if numero % 2 == 0: #verificamos: si el residuo al dividir el numero entre 2 es 0, el nuimero es par
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")# si es difereente de 0 es impar

# --------------------------------------------------------------------------------
# 3. Pide la base y la altura de un triángulo al usuario y calcula su área.

base = float(input("base:")) #solicitamos al ususario que ingrese la base y altutra de un triangulo
altura = float(input("altura:"))
area = base*altura # incilalizamos la variable area con el producto de base por altura
print(f"area del triangulo: {area}") # imprimimos el area del triangulo

# --------------------------------------------------------------------------------
# 4. Crea una función que calcule la factorial de un número.

def factorial (n):#definimos la funcion factorial que recibe como parametro n
    if n == 0:  ## verificamos si n es igual a 0, si es así, la funcion devuelve 1 (ya que el factorial de 0 es 1)
        return 1
    else:
        return n*factorial (n-1) # Si n no es igual a 0, devuelve n multiplicado por el factorial de n-1(por ejemplo si n
                                #   es 7 en la primera iteracion retorna 7 * factorial(6), en la segunda 7*6*factorial(5)...)
print(factorial(7))

# --------------------------------------------------------------------------------
# 5. Verifica si un número ingresado por el usuario es primo o no.
# Definición de una función llamada es_primo que verifica si un número n es primo
def es_primo(n):
   
    es_primo = True # Inicializamos una variable es_primo como True
    
    for i in range(2, n):# con for iteramos sobre todos los números desde 2 hasta n-1
        # con if verificamos si n es divisible por i
        if n % i == 0:
            # Si n es divisible por i, entonces n no es primo
            # Se establece la variable es_primo como False y se sale del bucle
            es_primo = False
            break
    # devuelve True si es_primo sigue siendo True, es decir, si n no es divisible por ningún número entre 2 y n-1
    return es_primo

# Solicitamos al usuario que ingrese un número
n = int(input("Ingrese un número: "))

# Llamamos a la función es_primo para verificar si el número ingresado es primo
es_primo = es_primo(n)

# se imprime el resultado dependiendo de si el número es primo o no
if es_primo:
   print(n, "es primo.")
else:
    print(n, "no es primo.")

# --------------------------------------------------------------------------------
# 6. Toma una cadena de texto y muestra su inversión.

def invertir_cadena(cadena):# Definimos una función llamada invertir_cadena 
    # Utiliza la técnica de rebanado de cadenas para invertir la cadena y la devuelve
    return cadena[::-1]


cadena = "Buenos dias!"# Cadena de texto inicial

# Llamamos a la función invertir_cadena para invertir la cadena y guarda el resultado en la variable cadena_invertida
cadena_invertida = invertir_cadena(cadena)

# Imprimimos la cadena original y la cadena invertida
print("La cadena original es:", cadena)
print("La cadena invertida es:", cadena_invertida)

# --------------------------------------------------------------------------------
# 7. Calcula la suma de los números pares en un rango especificado por el usuario.

def suma_pares(inicio, final):# se define la funcion suma_pares
    suma = 0                   #se iniclaiza la variable suma, a la cual se sumaras los pares que se encuentran dentro del rango que ingreso el usuario 
    for i in range(inicio, final + 1): # i toma los valores que se encuentran dentro del rango
        if i % 2 == 0: #si el residuo de dividir i entre 2 es cero es un numero par
            suma += i   #a la variable suma se le agrega i
    return suma         #la funcion retorna la suma de pares

def devolver_resutado():  #se define devolver resultado  solicita al usuario ingresar el inicio y el final del rango y devuelve la suma de los números pares dentro de ese rango 
    inicio = int(input("ingrese el inicio del rango: "))
    final = int(input("Ingrese el inicio del rango: "))
    return suma_pares(inicio, final)

print(suma_pares())

# --------------------------------------------------------------------------------
# 8. Crea una lista de los cuadrados de los primeros 10 números naturales
def arreglo_raiz_cuadrada(numero):
    arreglo_cuadrados: List[int] = []  # Se inicializa una lista vacía para almacenar los cuadrados
    for i in range(1, numero + 1):  # Itera desde 1 hasta numero + 1
        arreglo_cuadrados.append(i * i)  # Agrega el cuadrado del número actual a la lista

    return arreglo_cuadrados  # Devuelve la lista de cuadrados

print(arreglo_raiz_cuadrada(10))  # Imprime la lista de cuadrados de los números del 1 al 10

# --------------------------------------------------------------------------------
# 9. Cuenta el número de vocales en una cadena de texto.

def contador_vocales(texto):
    contador = 0  # Se inicializa el contador de vocales
    for caracter in texto:  # Se itera sobre cada caracter en el texto
        if caracter in "aeiouAEIOUáéíóúÁÉÍÓÚ":  # con se verifica si el caracter es una vocal
            contador += 1  # si es una vocal el contador incrementa en 1
    return contador  # la funcion devuelve el total de vocales encontradas

print(contador_vocales("Un texto es una composición de signos codificados en un sistema")) 
# --------------------------------------------------------------------------------
# 10. Genera los primeros 10 números de la serie Fibonacci.

def fibonacci(numero): #Función recursiva para calcular el número de Fibonacci para un número dado
    
    if numero <= 1:  # Caso base: cuando el número es 0 o 1, devuelve el número mismo
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)  # Llamada recursiva para calcular el número de Fibonacci

def arreglo_fibonacci(numero):# la funcion Genera un arreglo de números de fibonacci hasta el número especificado.
    arreglo = []  # se inicializa un arreglo vacío para almacenar la serie de los números de Fibonacci
    for i in range(numero):  # se itera desde 0 hasta el número especificado
        arreglo.append(fibonacci(i))  # se agrega al arreglo el número de fibonacci en la posición actual 
    return arreglo  # la funcion retorna el arreglo de números de fibonacci

print(arreglo_fibonacci(10))  # se imprime un arreglo de los 10 primeros números de la serie Fibonacci
# --------------------------------------------------------------------------------

# 11. Ordena una lista de números ingresados por el usuario de menor a mayor.
def arreglo_ordenado_numeros():
    arreglo_numeros = []  # Inicializa una lista vacía para almacenar los números
    for i in range(int(input("¿Cuántos numeros quieres ingresar? "))): # se solicita al usuario la cantidad de números que desea ingresar y recorre ese rango
        # Solicita al usuario que ingrese cada número y lo agrega a la lista
        arreglo_numeros.append(int(input(f"Numero {i + 1}: ")))

    arreglo_numeros.sort()  # se ordena la lista de números de forma ascendente

    return arreglo_numeros  # Devuelve la lista de números ordenados

print(arreglo_ordenado_numeros())  # se imprime la lista de números ordenados

# --------------------------------------------------------------------------------
# 12. Verifica si una palabra ingresada por el usuario es un palíndromo.
def palindromo(palabra: str):
    longitud: int = len(palabra)  # se obtiene la longitud de la palabra
    mitad: int = longitud // 2  # se calcula la mitad de la longitud de la palabra
    # Iteramos sobre la primera mitad de la palabra
    for i in range(0, mitad):
        # se compara los caracteres de la primera mitad con sus correspondientes en la segunda mitad
        if palabra[i] != palabra[longitud - i - 1]:
            return False  # Si hay alguna diferencia, la funcion retorna falso, no es palindromo
    return True  # Si no hay diferencias, retorna true, es palindromo
# se solicita al usuario ingresar una palabra
palabra: str = input("Ingrese una palabra: ")
# Llamada a la función palindromo() y se le pasa como paarmetro la palabra ingresada por el usuario para verificar si la palabra es un palíndromo
palabra_palindromo = palindromo(palabra)

if palabra_palindromo:# Imprime el resultado dependiendo de si la palabra es un palíndromo o no
    print(palabra, "es un palíndromo.")
else:
    print(palabra, "no es un palíndromo.")

# --------------------------------------------------------------------------------
# 13. Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario
def tabla_multiplicacion():
    # Definición de la función que generara la tabla de multiplicar

    numero: int = int(input("Ingresa un número para generar tu tabla de multiplicar: "))
    # se solicita al usuario que ingrese un número y lo convierte a un entero

    for i in range(1, 11):
        # Inicia un bucle que va desde 1 hasta 10
        resultado: int = numero * i # Calcula el resultado de la multiplicación entre el número ingresado y el multiplicador actual
        print(f"{numero} x {i} = {resultado}")
        # Imprime la multiplicación en formato "número x multiplicador = resultado"

tabla_multiplicacion()# se llama a la función para generar la tabla de multiplicar

# --------------------------------------------------------------------------------

# 14. Pide el radio de un círculo al usuario y calcula su área.

def area_circunferencia(): # función para calcular el área de la circunferencia

    radio = float(input("Ingrese el radio de la circunferencia: ")) # se solicita al usuario que ingrese el radio de la circunferencia y lo almacena como un número flotante

    area = math.pi * pow(radio, 2) # Calculamos el área de la circunferencia utilizando la fórmula π * radio^2
    return f"Área de la circunferencia: {area}"
    # Devuelve el resultado del área de la circunferencia 
print(area_circunferencia()) # Imprime el resultado del cálculo del área de la circunferencia

# --------------------------------------------------------------------------------

# 15. Toma un número entero y calcula la suma de sus dígitos.
def suma_digitos(numero: int):# función para calcular la suma de los dígitos de un número entero
    suma: int = 0 # Inicializa la variable suma para almacenar la suma de los dígitos
    for i in numero:
        # Iteramos sobre cada dígito del número 
        suma = suma + i
        # cada dígito se suma a la variable suma
    return suma
    # la funcion retorna el resultado de la suma de los dígitos

print(suma_digitos(565))
# Llamamos a la función suma_digitos() con el número 565 y no imprime 16
