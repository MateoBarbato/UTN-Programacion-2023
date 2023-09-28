from index import * 
flagMenu = True
while True:
    
    if(flagMenu):
        imprimirLista()
    numero = input('Elija entre las funciones:')

    if numero.isdigit():
        numero = int(numero)
        if numero <= 10 and numero >= 0:
            break
        else:
            flagMenu=False
            print("Opcion invalida. Ingrese un numero entre 0 y 10.")
    else:
        print("Opcion invalida. Ingrese un numero valido.")

match numero:
    case 1:
        numParametro = validarNumeroIngresado()
        print(numParametro)
        if numParametro > 0:
            area = areaCiculo(numParametro)
            print(f"El area de un ciruclo con radio {numParametro} es: {area}")
                
        else:
            print('Ingrese un numero entero posiivo')        
    case 2:
        numeroIngresado = validarNumeroIngresado()
        resultado = parOImpar(numeroIngresado)
    case 3:
        listaIngresada = ingresarLista()
        total = sumarTodo(listaIngresada)
        print(f'El total sumado es:{total}')
    case 4:
        listaIngresada = ingresarLista(3)
        total = maxEntre3(listaIngresada)
        print(f'El numero maximo entre los 3 ingreados es: {total}')
    case 5:
        textoIngresado = validarStringIngresado()
        resultadoInvertido = cadenaInvetida(textoIngresado)
        print(f'El invertido del texto ingresado es: {resultadoInvertido}')
    case 6:
        lista = ingresarLista()
        print(f'la lisa ordenada es:{listaOrdenada(lista)}')
    case 7:
        print('Base :')
        base = validarNumeroIngresado()
        print('Exponencial:')
        exponente = validarNumeroIngresado()

        total = potencia(base,exponente)
        print(f'El resultado de la potencia de {base} por {exponente} es: {total}')
    case 8:
        listaNum = ingresarLista()
        listaFiltrada = filtrarAPares(listaNum)
        print(f'La lista filtrada queda asi: {listaFiltrada}' )
    case 9:
        listaNum = ingresarLista()
        listaTotal = productoTodosEnLista(listaNum)
        print(f'El total del producto de todos los valores de la lista es: {listaTotal}')
    case 10:
        str = validarStringIngresado()
        palindromo(str)
    case _:
        print("Opcion invalida. Vuelva a ingresa una opcion.")