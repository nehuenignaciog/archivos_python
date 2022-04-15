# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    suma = 0
    with open ('stock.csv') as csvfile:
        movimientos_stock = list(csv.DictReader(csvfile))
    
    for movimiento in movimientos_stock:
        for producto, cantidad in movimiento.items():
            if producto == 'tornillos':
                suma += int(cantidad)
    print ("Stock total Tornillos:", suma)




def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    cantidad_2a = 0
    cantidad_3a = 0

    with open('propiedades.csv') as csvfile:
        lista_departamentos = list (csv.DictReader(csvfile))
    
    for departamento in lista_departamentos:
        for caracteristica, valor in departamento.items():
            if caracteristica == 'ambientes':
                try:
                    valor = int(valor)
                    if valor == 2 :
                        cantidad_2a += 1
                    elif valor == 3:
                        cantidad_3a += 1
                except:
                    print("Valor invalido ({}) en fila {}".format(departamento.get('ambientes'),departamento.get('')) )
            
    print ("Cantidad de Dptos. con 2 Ambientes: ", cantidad_2a)
    print ("Cantidad de Dptos. con 3 Ambientes: ", cantidad_3a)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
