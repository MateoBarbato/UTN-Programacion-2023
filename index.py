import math as math
import os as os

listaFunciones= ['1)Area Circulo','2)Par o Impar','3)Sumar Todo','4)Maximo entre 3','5)Invertir Cadena','6)Ordenar Lista','7)Potencia al exponente','8)Filtrar A Impares','9)Producto De Lista','10)Validar Palindromo']

def areaCiculo (radio:int) -> int:
    """
    Calcula el area de un circulo con el radio del mismo

    Argumentos: Radio del circulo

    Devuelve el area del circulo
    """
    result = math.pi * radio**2
    return result
def parOImpar (numero:float) -> float:
   """
   Imprime en consola si el numero es par o impar

   Argumentos: el numero a validar 

   Devuelve si es par o impar
   """
   if (numero%2 == 0):
      print('El numero es par')
   else:
      print('El numero es impar')
def sumarTodo (listaNumeros:list)->int:
    """
    Calcula la suma de todos los valores de una lista

    Argumentos: Lista de numeros

    Devuelve la suma de todos los valores de la lista
    """
    total=0
    for lista in listaNumeros:
        total = total + lista
    return total
def maxEntre3 (listaNumeros:list)->int:
    """
    Encuentra en maximo entre 3 numeros

    Argumentos: Lista con los 3 numeros

    Devuelve el numero mayor encontrado
    """
    a = listaNumeros[0]
    b = listaNumeros[1]
    c = listaNumeros[2]

    maxNum=0
    if(a > b and a > c):
        maxNum = a
    elif(b>a and b>c):
        maxNum = b
    else:
        maxNum = c
    return maxNum
def cadenaInvetida (string:str) -> str:
    """
    Invierte una cadena de texto

    Argumentos: Cadena de texto a invertir

    Devuelve la cadena de texto invertida
    """
    return string[::-1]
def listaOrdenada (listaPalabras:list) -> list:
    """
    Ordena una lista de valores ( con sorted )

    Argumentos: Lista a ordenar

    Devuelve la lista ordenada
    """
    return sorted(listaPalabras)
def potencia(base:float,exponente:float) -> int:
    """
    Potencia la base por el exponente

    Argumentos:
        base (float): base de la potencia
        exponente (float): exponenente de la potencia

    Devuelve:
        float: el numero resultante de potenciar el argumente base por el argumento exponente
    """
    return base ** exponente
def filtrarAPares(listaNumeros:list) -> list:
    """
    Filtra los impares de la lista ingresada

    Argumentos: Cantidad de numeros a pedir

    Devuelve la suma de todos los valores de la lista
    """
    numeros_impares = [numero for numero in listaNumeros if numero % 2 == 0]
    return numeros_impares
def productoTodosEnLista(listaNumeros:list)->list:
    """
    Calcula el producto entre todos numeros de una lista

    Argumentos: Lista de numeros (numero,numero,...)

    Devuelve el producto de todos los valores de la lista
    """
    total = 1
    for numero in listaNumeros:
        total = total *numero
    return total
def palindromo(str:str):
    """
    Funcion para saber si es palindromo o no

    Argumentos:Una cadena de texto

    Devuelve:
        print en consola con el resultado (true/false)
    """
    if(str == str[::-1]):
        print('Es palindromo')
    else :
        print('No es palindromo')



# FUNCIONES DE AYUDA PARA EL MENU

def imprimirLista():
    """
    Imprime el menu de opciones
    """
    print("<============ Menu de funciones ===========>")
    for funciones in listaFunciones:
        print(funciones)

def validarNumeroIngresado():
    """
    Valida si el dato ingresado es un numero

    Devuelve:
        float: Numero ingresado validado.
    """
    while True:
        try:
            numero_ingresado = input("Ingrese un numero: ")
            numero = float(numero_ingresado)
            return numero
        except:
            print("Numero ingresado invalido. Ingrese un numero valido. ")

def validarStringIngresado():
    """
    Valida si el dato ingresado es un string

    Devuelve:
        float: String ingresado validado.
    """
    while True:
        try:
            stringresado = input('Ingrese una cadena de texto: ')
            if bool(stringresado):
                return stringresado
        except:
            print('La cadena ingresada es invalida, porfavor ingresar un cadena de texto str')


def ingresarLista(numIteraciones=None):
    """
    Pide ingresar una lista de valores (numero,numero,...)

    Argumentos: Cantidad de veces que pide numero(optional)

    Devuelve la suma de todos los valores de la lista
    """
    contador = 0
    listaNum = []

    while True:
        valorIngresada = validarNumeroIngresado()
        listaNum.append(valorIngresada)
        contador += 1
        seguirAgregando = input('Quiere seguir agregando numeros? s/n')
        if(seguirAgregando!='s' or (numIteraciones == contador and numIteraciones!=None)):
            break
    return listaNum
  
def ingresarListaStr():
    listaStr = []

    while True:
        try:
            valorIngresada = validarNumeroIngresado()
            if valorIngresada.isalpha():
                listaStr.append(valorIngresada)
                seguirAgregando = input('Quiere seguir agregando palabras? s/n')
                if(seguirAgregando!='s' ):
                    break
        except:
            print('Ingresa un dato que sea str.')
    return listaStr
