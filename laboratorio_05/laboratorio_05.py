# -------------------------------------------------------------------------------------------------------
# 1. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos.

def imprimir_conjunto_numeros_primos(conjunto_numeros):
    # Define un conjunto vacío para almacenar los números primos encontrados
    conjunto_numeros_primos = set()

    # Itera sobre cada número en el conjunto dado
    for numero in conjunto_numeros:
        divisores = 0
        # Itera sobre cada número desde 1 hasta el número actual
        for i in range(1, numero + 1):
            # Si el número actual es divisible exactamente por i, incrementa el contador de divisores
            if numero % i == 0:
                divisores += 1
        # Si el número tiene exactamente 2 divisores (1 y el número en sí), entonces es primo
        if divisores == 2:
            # Agrega el número primo al conjunto de números primos
            conjunto_numeros_primos.add(numero)

    # Devuelve el conjunto de números primos, ordenado
    return sorted(conjunto_numeros_primos)

#ejemplo
conjunto_numeros = {7,8,9,1,3,11,5,6,8,20,47}
print(imprimir_conjunto_numeros_primos(conjunto_numeros))

# print (imprimir_conjunto_numeros_primos(conjunto_numeros ))

# -------------------------------------------------------------------------------------------------------
# 2. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las
# palabras que comienzan con una letra determinada.


def palabras_letra_determinada(conjunto_palabra):
    # Define un conjunto vacío para almacenar las palabras que comienzan con la letra especificada
    palabras_inicial_iguales = set()
    letra = input("Ingrese una letra: ")  # Solicita al usuario que ingrese una letra

    # Itera sobre cada palabra en el conjunto de palabras dado
    for palabra in conjunto_palabra:
        # Comprueba si la primera letra de la palabra coincide con la letra especificada por el usuario
        if letra == palabra[0]:
            # Si la primera letra coincide, agrega la palabra al conjunto de palabras encontradas
            palabras_inicial_iguales.add(palabra)

    # Devuelve el conjunto de palabras que comienzan con la letra especificada
    return palabras_inicial_iguales

palabras = ["mora", "cereza", "ciruela", "coco"]
conjunto_palabra = set(palabras)
print (palabras_letra_determinada(conjunto_palabra))

# -------------------------------------------------------------------------------------------------------
# 3. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son
# divisibles por un número determinado.

def conjunto_numeros(numeros):
    # Define un conjunto vacío para almacenar los números divisibles
    numeros_divisibles = set()
    numero = int(input("Ingrese un número: "))  # Solicita al usuario que ingrese un número

    # Itera sobre cada número en el conjunto dado
    for i in numeros:
        # Comprueba si el número actual es divisible por el número especificado por el usuario
        if i % numero == 0:
            # Si es divisible, agrega el número al conjunto de números divisibles
            numeros_divisibles.add(i)

    # Devuelve el conjunto de números divisibles
    return numeros_divisibles

#ejemplo
numeros = {1, 2, 3, 4, 5, 6}
print(conjunto_numeros(numeros))

# -------------------------------------------------------------------------------------------------------
# 4. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están
# en ambos conjuntos.

def mostar_conjunto_interseccion(conjunto1, conjunto2):
    # la funcion encuentra la intersección entre conjunto1 y conjunto2, recibe como parametros dos conjuntos
    interseccion = conjunto1.intersection(conjunto2)
    # Devuelve los elementos de la intersección, ordenados
    return sorted(interseccion)

# La función devuelve los elementos comunes entre conjunto1 y conjunto2
conjunto1 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
conjunto2 = {23, 11, 17, 13, 2, 7, 5, 3}
print(mostar_conjunto_interseccion(conjunto1, conjunto2))


# -------------------------------------------------------------------------------------------------------
# 5. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están
# en el primer conjunto pero no en el segundo.

def mostar_diferencia_conjuntos(conjunto1, conjunto2):
    # la funcion encuentra los elementos en conjunto1 que no están en conjunto2, utilizando el metodo diference
    conjunto_diferencia = conjunto1.difference(conjunto2)
    # Devuelve los elementos de la diferencia (elementos están en el conjunto1 pero no en el conjunto2), ordenados
    return sorted(conjunto_diferencia)

#ejemplo
conjunto1 = {3, 4, 5, 13, 24, 56, 2, 6, 7}
conjunto2 = {5, 3, 11, 7, 9, 8, 2, 6, 23, 13}
print(mostar_diferencia_conjuntos(conjunto1, conjunto2))

# -------------------------------------------------------------------------------------------------------
# 6. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están
# en el segundo conjunto pero no en el primero.

def mostar_diferencia_conjuntos(conjunto1,conjunto2):
    # la funcion encuentra los elementos en conjunto1 que no están en conjunto2, utilizando el metodo diference
    conjunto3 = conjunto2.difference(conjunto1)
    # Devuelve los elementos de la diferencia (elementos están en el conjunto2 pero no en el conjunto1), ordenados
    return sorted(conjunto3)


conjunto1 = {3,4,5,13,24,56,2,6,7}
conjunto2 = {5,3,11,7,9,8,2,6,23,13}

print(mostar_diferencia_conjuntos(conjunto1,conjunto2))


# -------------------------------------------------------------------------------------------------------
# 7. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
# son anagramas.
def son_anagramas(palabra1, palabra2):
    # la funcion comprueba si dos palabras son anagramas comparando si sus letras ordenadas son iguales
    return sorted(palabra1) == sorted(palabra2)

def encontrar_anagramas(conjunto_palabras):
    anagramas_dict = {}

    for palabra in conjunto_palabras:
        # Busca anagramas existentes en el diccionario
        anagramas = [key for key in anagramas_dict if son_anagramas(palabra, key)]

        if anagramas:
            # Si se encuentra un anagrama, se agrega la palabra al conjunto de anagramas
            anagramas_dict[anagramas[0]].add(palabra)
        else:
            # Si no se encuentra un anagrama, se crea un nuevo conjunto con la palabra
            anagramas_dict[palabra] = {palabra}

    # Filtra los conjuntos de anagramas para obtener aquellos con más de una palabra
    anagramas_resultado = {tuple(val) for val in anagramas_dict.values() if len(val) > 1}

    return anagramas_resultado

# Conjunto de palabras para buscar anagramas
conjunto_palabras = {"amor", "roma", "carro", "arco", "delira", "ramo", "lidera"}

# Encuentra y almacena los anagramas en el conjunto de palabras dado
resultado = encontrar_anagramas(conjunto_palabras)
print(resultado)

# -------------------------------------------------------------------------------------------------------
# 8. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos.
def palabras_palindromo(palabras):
    # la funcion define un conjunto vacío para almacenar las palabras palíndromas
    conjunto_palabras_palindromo = set()
    # Itera sobre cada palabra en el conjunto de palabras dado
    for palabra in palabras:
        # Comprueba si la palabra es igual a su reverso (es decir, si es un palíndromo)
        if palabra == palabra[::-1]:
            # Si la palabra es un palíndromo, agrégala al conjunto de palabras palíndromas
            conjunto_palabras_palindromo.add(palabra)
    
    # Devuelve el conjunto de palabras palíndromas encontradas
    return conjunto_palabras_palindromo

# Conjunto de palabras para buscar palíndromos
palabras = {"oso", "radar", "casa", "reconocer"}

# Encuentra y almacena las palabras palíndromas en el conjunto de palabras dado
resultado = palabras_palindromo(palabras)
print(resultado)

# -------------------------------------------------------------------------------------------------------
# 9. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada.

def palabras_tamaños_iguales(palabras):
    # la funcion define un conjunto vacío para almacenar las palabras con el mismo tamaño
    palabras_tamaño_igual = set()
    
    # Solicita al usuario que ingrese el tamaño deseado para las palabras
    tamaño = int(input("Ingrese el tamaño deseado para las palabras: "))
    
    # Itera sobre cada palabra en el conjunto de palabras dado
    for i in palabras:
        # Comprueba si la longitud de la palabra es igual al tamaño especificado por el usuario
        if len(i) == tamaño:
            # Si la longitud de la palabra coincide con el tamaño especificado, agrégala al conjunto
            palabras_tamaño_igual.add(i)
    
    # Devuelve el conjunto de palabras con el mismo tamaño especificado
    return palabras_tamaño_igual

# Conjunto de palabras para buscar palabras con el mismo tamaño
animales = {"mapache", "cebra", "escarabajo", "ballena", "merluza", "bisonte", "mariposa", "flamenco"}

# Encuentra y almacena las palabras con el mismo tamaño especificado en el conjunto dado
resultado = palabras_tamaños_iguales(animales)
print(resultado)

# -------------------------------------------------------------------------------------------------------
# 10. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada.
def palabras(conjunto_palabras):
    # Se define un conjunto vacío para almacenar las palabras que contienen la letra específica
    palabras_letra_determinada = set()
    
    # Solicita al usuario que ingrese la letra que desea buscar en las palabras
    letra = input("Ingrese la letra que desea buscar en las palabras: ")
    
    # Itera sobre cada palabra en el conjunto dado
    for palabra in conjunto_palabras:
        # Comprueba si la letra especificada está presente en la palabra actual
        if letra in palabra:
            # Si la letra está presente, agrega la palabra al conjunto de palabras encontradas
            palabras_letra_determinada.add(palabra)
    
    # Devuelve el conjunto de palabras que contienen la letra especificada
    return palabras_letra_determinada

# Conjunto de palabras para buscar palabras que contienen una letra específica
utensilios_cocina = {"cuchillo", "olla", "sartén", "espátula", "cucharón", "tenedor", "colador"}

# llamar a la función palabras() para encontrar palabras que contienen una letra específica e imprimir el conjunto con las palabras que contienen una letra determinada
print(palabras(utensilios_cocina))

# 11. Escriba una función que reciba un conjunto de números y devuelva un conjunto con
#  los números que están ordenados de menor a mayor.
def order_numbers(numbers):
  numbers = list(numbers)
  numbers.sort()
  return set(numbers)


numbers = {6, 2, 3, 4, 2, 3}
ordered_numbers = order_numbers(numbers)
print(ordered_numbers)


# ------------------------------------------------------------------------------------
# 12. Función que devuelve un conjunto con los números ordenados de mayor a menor.
def numeros_ordenados_de_mayor_a_menor(conjunto):
    # Convertimos el conjunto a una lista y la ordenamos de mayor a menor
    lista_ordenada = sorted(conjunto, reverse=True)
    # Convertimos la lista ordenada de nuevo a un conjunto y la retornamos
    return set(lista_ordenada)

# conjunto = {3, 6, 1, 9, 4}
# resultado = numeros_ordenados_de_mayor_a_menor(conjunto)
# print(resultado) 


# ------------------------------------------------------------------------------------
# 13. Función que devuelve un conjunto con los números duplicados en el conjunto dado.
def numeros_duplicados(conjunto):
    # Creamos un conjunto vacío para almacenar los números duplicados
    duplicados = set()
    # Creamos un conjunto para almacenar los números únicos mientras recorremos el conjunto dado
    numeros_unicos = set()
    # Iteramos sobre cada número en el conjunto dado
    for numero in conjunto:
        # Si el número ya está en el conjunto de números únicos, significa que es duplicado
        if numero in numeros_unicos:
            duplicados.add(numero)  # Agregamos el número duplicado al conjunto de duplicados
        else:
            numeros_unicos.add(numero)  # Agregamos el número único al conjunto de números únicos
    # Retornamos el conjunto de números duplicados
    return duplicados

# conjunto = {3, 6, 1, 9, 4, 6, 2, 3}
# resultado = numeros_duplicados(conjunto)
# print(resultado) 


# ------------------------------------------------------------------------------------
# 14. Función que devuelve un conjunto con los números no duplicados en el conjunto dado.
def numeros_no_duplicados(conjunto):
    # Creamos un conjunto vacío para almacenar los números no duplicados
    no_duplicados = set()
    # Creamos un conjunto para almacenar los números duplicados mientras recorremos el conjunto dado
    duplicados = set()
    # Iteramos sobre cada número en el conjunto dado
    for numero in conjunto:
        # Si el número ya está en el conjunto de números duplicados, lo ignoramos
        if numero in duplicados:
            continue
        # Si el número ya está en el conjunto de números no duplicados, lo movemos al conjunto de duplicados
        elif numero in no_duplicados:
            no_duplicados.remove(numero)
            duplicados.add(numero)
        # Si el número no está en ninguno de los conjuntos, lo agregamos al conjunto de no duplicados
        else:
            no_duplicados.add(numero)
    # Retornamos el conjunto de números no duplicados
    return no_duplicados

# conjunto = {3, 6, 1, 9, 4, 6, 2, 3}
# resultado = numeros_no_duplicados(conjunto)
# print(resultado)

# ------------------------------------------------------------------------------------
# 15. Escriba una función que reciba un conjunto de números y devuelva un conjunto con
#  los números que son primos y están ordenados de menor a mayor.
def es_primo(numero):
    """
    Función que verifica si un número es primo.
    """
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Verifica si el número es divisible por algún número entre 2 y su raíz cuadrada
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False  # Si es divisible, el número no es primo

    return True  # Si no es divisible por ningún número, el número es primo

def primos(numeros):
    """
    Función que devuelve un conjunto de números primos de un conjunto dado.
    """
    primos_encontrados = set()
    for numero in numeros:
        # Verifica si el número es primo utilizando la función es_primo
        if es_primo(numero):
            primos_encontrados.add(numero)  # Agrega el número al conjunto de primos
    return sorted(primos_encontrados)  # Devuelve los números primos ordenados

# Conjunto de números para encontrar los primos
numeros = {23, 3, 5, 7, 13, 11, 19, 17, 2}

# Imprime los números primos encontrados en el conjunto dado
print(primos(numeros))

# ------------------------------------------------------------------------------------
# 16. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con
#  las palabras que son palíndromos y están ordenadas de menor a mayor.
def palindromos(palabras):
    """
    Función que encuentra los palíndromos en un conjunto de palabras.
    """
    palindromos_encontrados = set()
    for palabra in palabras:
        # Verifica si la palabra es igual a su reverso, lo que indica que es un palíndromo
        if palabra == palabra[::-1]:
            palindromos_encontrados.add(palabra)  # Agrega el palíndromo al conjunto
    return sorted(palindromos_encontrados)  # Devuelve los palíndromos ordenados

# Conjunto de palabras para buscar palíndromos
palabras = {"xyzyx", "elefante", "abcdcba", "pqrqp", "abcba", "abcde"}

# Imprime los palíndromos encontrados en el conjunto dado
# print(palindromos(palabras))

# ------------------------------------------------------------------------------------
# 17. Escriba  una  función  que  reciba  un  conjunto  de  palabras  y  devuelva  un
#  conjunto  con  las  palabras  que tienen una longitud determinada y están ordenadas de menor a mayor.
def palabras_con_longitud(palabras, longitud):
    """
    Función que encuentra palabras en un conjunto con una longitud específica.
    """
    palabras_con_longitud = set()
    for palabra in palabras:
        # Verifica si la longitud de la palabra es igual a la longitud especificada
        if len(palabra) == longitud:
            palabras_con_longitud.add(palabra)  # Agrega la palabra al conjunto
    return sorted(palabras_con_longitud)  # Devuelve las palabras encontradas, ordenadas

# Conjunto de palabras para buscar palabras con una longitud específica
palabras = {"pqrst", "abcd", "xyz", "xxyyz", "adxc", "xd", "abcde"}
longitud = 5

# Imprime las palabras encontradas en el conjunto dado con la longitud especificada
# print(palabras_con_longitud(palabras, longitud))

# ------------------------------------------------------------------------------------
# 18. Escriba  una  función  que  reciba  un  conjunto  de  palabras  y  devuelva  un
#  conjunto  con  las  palabras  que contienen una letra determinada y están ordenadas de mayor a menor.
def palabras_con_letra(palabras, letra):
    """
    Función que encuentra palabras en un conjunto que contienen una letra específica.
    """
    palabras_con_letra = set()
    for palabra in palabras:
        # Verifica si la letra especificada está presente en la palabra actual
        if letra in palabra:
            palabras_con_letra.add(palabra)  # Agrega la palabra al conjunto
    return sorted(palabras_con_letra, reverse=True)  # Devuelve las palabras encontradas, ordenadas de forma inversa

# Conjunto de palabras para buscar palabras que contienen una letra específica
palabras = {"abcd", "mknf", "xdda", "xyza"}
letra = "a"

# Imprime las palabras encontradas en el conjunto dado que contienen la letra especificada
# print(palabras_con_letra(palabras, letra))

# ------------------------------------------------------------------------------------
# 19. Escriba una función que reciba un conjunto de números y devuelva un conjunto con

#  los números que están ordenados de menor a mayor y que no están duplicados.
def unique_sorted_numbers(numbers):
    """
    Función que debería devolver un conjunto de números únicos ordenados.
    """
    return numbers  # Devuelve el conjunto de números sin realizar cambios

# Conjunto de números para procesar
numbers = {8, 1, 2, 3, 1, 2, 3, 4, 5, 6}

# Imprime el conjunto de números original y el resultado de la función unique_sorted_numbers
print(numbers)
print(unique_sorted_numbers(numbers))


# ------------------------------------------------------------------------------------
# 20.  Escriba una función que reciba un conjunto de palabras y devuelva un conjunto
# con las palabras que son palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor.
def palindromos(palabras, longitud):
    """
    Función que encuentra palíndromos en un conjunto de palabras con una longitud específica.
    """
    palindromos_encontrados = set()
    for palabra in palabras:
        # Verifica si la palabra tiene la longitud especificada y es igual a su reverso
        if len(palabra) == longitud and palabra == palabra[::-1]:
            palindromos_encontrados.add(palabra)  # Agrega el palíndromo al conjunto
    return sorted(palindromos_encontrados)  # Devuelve los palíndromos encontrados, ordenados

# Conjunto de palabras para buscar palíndromos con una longitud específica
palabras = {"xyzyx", "elefante", "abcdcba", "pqrqp", "abcba", "abcde"}
longitud = 5

# Imprime los palíndromos encontrados en el conjunto dado con la longitud especificada
print(palindromos(palabras, longitud))