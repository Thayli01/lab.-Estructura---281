import numpy as np
from typing import Tuple

#ejercicios de laboratorio 3 y 4

# 01: Escribe una función recursiva que imprima los números pares del 1 al 100.
# Se define la función print_even_numbers usando "type hints"
def imprimir_numeros_pares(n: int = 1):
    if n == 100:
        # caso base: se detiene si n es 100
        return
    if n % 2 == 0:
        # imprime los números pares de 1 a 100
        print(n, end=" - ")
    # caso recursivo: llama a la función pasando como argumento el siguiente número
    imprimir_numeros_pares(n + 1)

# llamada de la función
imprimir_numeros_pares()


# ---------------------------------------------------------------------------------------

# 02: Escribe una función recursiva que imprima la suma de los números del 1 al n
def suma_recursiva(número_actual: int, número_final: int, suma_actual: int = 0):
    if número_actual > número_final:
        # caso base, termina con la ejecución
        return
    # almacena en current_sum la suma de current_sum + current_number
    número_actual: int =número_final+ suma_actual
    # imprime la suma actual
    print()
    # caso recursivo: llama a la función
    suma_recursiva(número_actual + 1, número_final, suma_actual)

# llamada de la función
suma_recursiva(1, 5)


# ---------------------------------------------------------------------------------------
# 03: Escribe una función recursiva que imprima la pirámide de números del 1 al n

def imprimir_piramide_numeros(n: int, fila_actual: int = 1):#funcion que Imprime la pirámide de números del 1 al n, parametro n =  número de filas de la pirámide 

    if fila_actual > n:
        # caso base: Se detiene si n es 100
        return
    # imprime espacios antes de los números de la fila actual
    print(" " * (n - fila_actual), end="")
    
    # imprime los números de la fila actual de manera ascendente
    for numero in range(1, fila_actual + 1):
        print(numero, end="")
    # imprime los números de la fila actual de manera descendente
    for num in range(fila_actual - 1, 0, -1):
        print(num, end="")
    # pasar a la siguiente línea después de imprimir la fila.
    print()

    # caso recursivo: imprime recursivamente la siguiente fila
    imprimir_piramide_numeros(n, fila_actual + 1)

# llamada de la función
imprimir_piramide_numeros(9)


# ---------------------------------------------------------------------------------------

# 04: Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n

def imprimir_piramide_numeros_invertido(n: int, fila_actual: int = 1) -> None:# funcion imprime la pirámide de números invertidos del 1 al n.
    if fila_actual> n:
        # caso base: Se detiene si current_row es mayor a n
        return
    # imprime espacios antes de los números invertidos de la fila actual
    print(" " * (n - fila_actual), end="")

    # imprime los números de la fila actual de manera descendente
    for numero in range(fila_actual, 0, -1):
        print(numero, end="")

    # imprime los números de la fila actual de manera ascendente
    for num in range(2, fila_actual + 1):
        print(num, end="")

    # pasar a la siguiente línea después de imprimir la fila.
    print()

    # caso recursivo: imprime recursivamente la siguiente fila
    imprimir_piramide_numeros_invertido(n, fila_actual= + 1)

# llamada de la función
imprimir_piramide_numeros_invertido(6)


# ---------------------------------------------------------------------------------------
# 05:  Escribe una función recursiva que imprima la tabla de multiplicar del n.
def tabla_multiplicar(n: int, multiplicador: int = 1) -> None: # la funcion mprime la tabla de multiplicar del n. tiene como parametro n el número para el cual se imprimirá la tabla de multiplicar y el multiplicador de la fila de la tabla

    if multiplicador > 12:
        # caso base: esta instrucción if verifica si el multiplicador es mayor que 10.
        return
    # esta variable almacena el producto de n y el multiplicador actual
    resultado = n * multiplicador
    # el resultado se imprime usando la sintaxis de format (f), \t: carácter de tabulación
    
    print(f"\t{n} x {multiplicador} = {resultado}")
    # caso recursivo: esta función se llama de forma recursiva para imprimir la siguiente fila
    tabla_multiplicar(n, multiplicador + 1)

# llamada de la función
tabla_multiplicar(5)

# ---------------------------------------------------------------------------------------
# Arreglos y Matrices
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------

# 06: Crea una matriz de números reales
# usando types hints (np.ndarray para matrizes)
def matriz_de_reales() -> np.ndarray:
    """
    Crea una matriz de números reales.

    Returns:
        np.ndarray: matriz de números reales.
    """
    return np.array([
        [7, 2, 5],
        [4, 5, 8],
        [6, 0, 9]
    ])

# llamada de la función
print(matriz_de_reales())


# ---------------------------------------------------------------------------------------

# 07: Crea una matriz de números complejos
def matriz_numeros_complejos() -> np.ndarray:
# se crea una matriz de números complejos utilizando np.array y especificando los valores directamente
    return np.array([
        [1 + 2j, 3 + 4j, 6 + 5j],
        [5 + 6j, 7 + 8j, 0],
        [9 + 1j, 2, 2j]
    ], dtype=complex)# se especifica el tipo de datos como complejo para que NumPy pueda interpretar los números correctamente


# llamada de la función
print(matriz_numeros_complejos())


# ---------------------------------------------------------------------------------------
# 08: Crea una matriz de matrices
def matriz_de_matrices() -> np.ndarray:
    return np.array([
        [8, 9, 3, 5],
        [9, 4, 0, 2],
        [0, 5, 2, 1],
        [7, 8, 9, 0]
    ])

# llamada de la función
print(matriz_de_matrices())

# la función lambda para crear matrices aleatorias, recibe 2 parametros, el número de filas y el número de columnas.
generador_matrices_aleatorias: np.ndarray = lambda filas, columnas: np.random.randint(1, 10, size=(filas, columnas))


# ---------------------------------------------------------------------------------------
# 09: Accede al elemento central de una matriz
def acceder_elemento_central_matriz(matriz: np.ndarray) -> np.ndarray: # funcion que accede al elemento central de una matrizrecibe como paarmetro una Matriz

    if matriz.shape[0] != matriz.shape[1]:
        # Verifica que sea una matriz cuadrada
        return 'matriz de dimensiones incorrectas'
    return matriz[int(matriz.shape[0] / 2)][int(matriz.shape[1] / 2)]

# creando la matriz A con la función random_matrix_generator
A: np.ndarray = generador_matrices_aleatorias(5, 5)
# la matriz A
print(f"La matriz A es:\n{A}\n")
# llamada de la función
num_central: int = acceder_elemento_central_matriz(A)
print(f'El elemento central de la matriz A es: {num_central}')



# --------------------------------------------------------------------------------------

# 10:  Suma dos matrices de diferentes tamaños.

def suma_matrices(A: np.ndarray, B: np.ndarray) -> np.ndarray: # la funcion suma dos matrices de diferentes tamaños, recibe dos matrices a y b

    # Usamos concatenate() de numpy para concatenar matrices de diferentes tamaños.
    matriz_suma: np.ndarray = A + B
    return matriz_suma

# creando la matriz A, B con la función random_matrix_generator
A: np.ndarray = generador_matrices_aleatorias(3, 3)
# la matriz A
print(f"La matriz A es:\n{A}\n")
# la matriz B
B: np.ndarray = generador_matrices_aleatorias(3, 3)
print(f"La matriz B es:\n{B}\n")
# llamada de la función, pasandole como arguemnto la matriz A y la matriz B
matriz_suma: np.ndarray = suma_matrices(A, B)
print(f'Suma de las matrices es:\n{matriz_suma}')


# ---------------------------------------------------------------------------------------

# 11: Multiplica una matriz por un número.

def multiplicar_matriz_por_escalar(matriz: np.ndarray, escalar: int) -> np.ndarray:
 
    #la funcion multiplica una matriz por un número.parametros: Matriz y escalar numero entero, retorna matriz multiplicada por el número
    return matriz * escalar

# creamos la matriz X, hacemos uso de la función multiply_matrix_by_scalar
X: np.ndarray = generador_matrices_aleatorias(3, 3)
print(f'la matriz X es:\n{X}\n')

producto: np.ndarray = multiplicar_matriz_por_escalar(X, 6)
print(f'La matriz multiplicada por 6 es:\n{producto}\n')#se imprime el producto de la matriz por el escala


# ---------------------------------------------------------------------------------------
# 12:  Calcula la media de los elementos de una matriz

def  Calcular_media_elementos_matriz(matriz: np.ndarray): #parametro matriz
    
    return np.mean(matriz)# con el metodo mean se calcula la media de los elementos de la matriz y retorna el resultado

# usamos la matriz X anteriormente creada, hacemos uso de la funcion Calcular_media_elementos_matriz
media_matriz = Calcular_media_elementos_matriz(X)
print(f'La media de la matriz es: {media_matriz}\n')


# =======================================================================================
# Exercises part II
# =======================================================================================

# ---------------------------------------------------------------------------------------
# 01: Crea una matriz de números aleatorios de tamaño 100x100
def matriz_numeros_aleatorios() -> np.ndarray:
    # crea una matriz de números aleatorios de tamaño 100 x 100
    return np.random.rand(100, 100)

# llamada de la función
matriz_aleatoria: np.ndarray = matriz_numeros_aleatorios()
print(f'matriz aleatoria de tamaño 100x100 es:\n{matriz_aleatoria}')


# ---------------------------------------------------------------------------------------
# 02: Calcula la media, la mediana y la desviación estándar de los elementos de una matriz
def calculate_statistics(matrix: np.ndarray) -> Tuple[float, float, float]:
    """
    Calcula la media, mediana y desviación estándar de los elementos de una matriz

    Parameters:
        matrix (np.ndarray): Matriz

    Returns:
        Tuple[float, float, float]: Una tupla que contiene la media, la mediana y la desviación estándar
    """
    # calcula la media
    valor_medio = np.mean(matrix)
    # llama la función generador_matrices_aleatorias para obtener la media de la matriz
    median_value = Calcular_media_elementos_matriz(matrix)
    # calcula la desviación estándar
    desviacion_estandar = np.std(matrix)

    return valor_medio, median_value, desviacion_estandar

# creamos la matriz A, llamamos a la función calculate_statistics
# A: np.ndarray = random_matrix_generator(5, 5)
# print(f"La matriz A es:\n{A}\n")
# usando la asignación múltiple o desempaquetado de tuplas en Python tenemos:
# mean_value, median_value, std_deviation = calculate_statistics(A)
# print(mean_value, median_value, std_deviation)

# ---------------------------------------------------------------------------------------
# 03: Escribe una función que encuentre el elemento máximo de una matriz
def elemento_maximo_matriz(matriz: np.ndarray):
    """
    Encuentra el elemento máximo de una matriz

    Parametros:
        matrix (np.ndarray): Matriz

    Retorna:
        float: El elemento máximo de la matriz
    """
    # calcula el máximo elemento de la matriz
    return np.max(matriz)

# creamos la matriz B, llamamos a la función calculate_statistics
B: np.ndarray = generador_matrices_aleatorias(5, 5)
max_elemento: float = elemento_maximo_matriz(B)
print(f"Matriz B:\n{B}")
print(f"Elemento máximo: {max_elemento}")


# ---------------------------------------------------------------------------------------
# 04: Escribe una función que encuentre la submatriz de mayor suma de una matriz
def find_submatrix_max(matriz: np.ndarray, contador: int): # type: ignore
    """
    Encuentra la submatriz de mayor suma de una matriz

    Parameters:
        matriz (np.ndarray): Matriz
        contadoe (int): Número de elementos a obtener

    Retorna:
        Tupla[np.ndarray, int]: Una tupla que contiene la submatriz de mayor suma y el valor de la suma
    """
    # convertirmos la matriz en un arreglo
    arreglo_numeros = np.array(matriz).flatten()

    if contador <= 0:
        # Si contador es 0 o negativo, retornar un arreglo vacío
        return []

    # Ordenar el arreglo en orden descendente
    arreglo_ordenado = sorted(arreglo_numeros, reverso=True)
    # Obtener los primeros count elementos
    arreglo_resultado = arreglo_ordenado[:contador]

    # Obtener la suma
    arreglo_suma= sum(arreglo_resultado)

    return arreglo_resultado, arreglo_suma


# Creamos una matriz de 5 x 5 con generador_matrices_aleatorias
matriz: np.ndarray = generador_matrices_aleatorias(5, 5)
print(f"Matriz:\n{matriz}\n")
# usamos asignación múltiple para alamcenar los valores que nos retorna la función
submatriz, sum = find_submatrix_max(matriz, matriz.shape[0])
print(f"submatriz: {submatriz} y la suma: {sum}")


# ---------------------------------------------------------------------------------------
# 05: Escribe una función que encuentre la matriz de covarianza de dos matrices
def matriz_covarianza(matriz_A: np.ndarray, matriz_B: np.ndarray):

    if matriz_A.shape != matriz_B.shape:
        raise ValueError("Las matrices deben tener la misma forma para el cálculo de la covarianza.")
    # Apilar las matrices para obtener una matriz combinada
    matriz_combinada = np.vstack((matriz_A, matriz_B))

    # calculamos la matriz de covarianza
    # rowvar=False se utiliza para tratar cada columna como una variable y cada fila como una observación
    matriz_de_covarianza = np.cov(matriz_combinada, rowvar=False)

    return matriz_de_covarianza

# creamos matrices: X e Y, llamamos a la función covariance_matrix
X: np.ndarray = generador_matrices_aleatorias(5, 5)
Y: np.ndarray = generador_matrices_aleatorias(5, 5)
matriz_cov: np.ndarray = matriz_covarianza(X, Y) # inializamos la variable matriz_cov llamando la funcion matriz_covarianza
print(f"Matriz A:\n{X}\n") #se imprime la matriz X e Y, y la matriz de covarianza
print(f"Matriz B:\n{Y}\n")
print(f'Matriz de covarianza:\n{matriz_cov}\n') 