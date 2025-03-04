__autor__ = "Ezequeil Suarez"

"""
Desarrollar un programa que permita cargar por teclado un texto
completo en una variable de tipo caracter. 

Usuario cargara un punto para indicar el final del texto y que
cada palabra de ese texto esta sépara de los demás por un
espacio en blanco. 

El programa pide:
Punto 1 - Determinar cuántas palabras tienen 3, 5 o 7 letras.

Punto 2 - Determinar la cantidad de palabras con más de tres letras
que tengan solo una vocal o dos vocales sobre el total de
palabras del texto.

Punto 3 - Determiar la cantidad de palabras que contienen más de una
silaba 'pe'.
"""

# Funciones Globales
def porcentaje_calcular(valor, total):
    if total > 0:
        return round(valor * 100 / total, 2)
    return 0

def es_vocal(letra):
    vocales = 'aeiouáéíóúÁÉÍÓÚAEIOU'
    return letra in vocales
# Función Principal
def principal():
    print("\t Análisis De Texto | Con Letras 'pe'")
    print(("-+" * 40))
    texto = input("- Ingrese el texto a analizar, finaliza con punto: ")

    # Inicialización de contadores y booleanos.
    cont_palabras = cont_palabras_tres_letras = palabras_vocal_tercer_letras = 0
    palabras_dos_vocales = palabras_mas2_pe = 0

    cont_letras = cant_vocales = cant_pe = 0
    tiene_vocal = False
    anterior = ''

    # Recorremos el texto mediante ciclo for
    for letra in texto:
        if letra == ' ' or letra == '.':  # Fin de palabra
            if cont_letras > 0:
                cont_palabras += 1

                # Condición 1: palabras con 3, 5 o 7 letras
                if cont_letras in [3, 5, 7]:
                    cont_palabras_tres_letras += 1

                # Condición 2: palabras con una vocal en la tercera letra
                if cont_letras >= 3 and tiene_vocal:
                    palabras_vocal_tercer_letras += 1

                # Condición 3: palabras con máximo 2 vocales
                if cant_vocales <= 2:
                    palabras_dos_vocales += 1

                # Condición 4: palabras con más de una secuencia "pe"
                if cant_pe >= 2:
                    palabras_mas2_pe += 1

            # Resetear los contadores para la siguiente palabra
            cont_letras = cant_vocales = cant_pe = 0
            tiene_vocal = False

        elif letra.isalpha():  # Si es una letra válida
            # Contamos las letras de la palabra
            cont_letras += 1

            # Verificamos si es una vocal
            if es_vocal(letra):
                cant_vocales += 1
                if cont_letras == 3:
                    tiene_vocal = True

            # Verificamos si se forma la secuencia "pe"
            if letra == 'e' and anterior == 'p':
                cant_pe += 1

        else:
            # Manejo de posibles caracteres inválidos
            print(f"Aviso: El carácter '{letra}' no es válido o inesperado. Solo se aceptan letras, espacios y puntos.")
            return  # Termina la ejecución si hay un error inesperado

        # Guardamos la letra anterior
        anterior = letra

    # Calcular el porcentaje de palabras con 2 vocales
    porcentaje_palabras_dos_vocales = porcentaje_calcular(palabras_dos_vocales, cont_palabras)

    # Resultados
    print("\t Presentación De Resultados:")
    print("-+" * 40)
    print(f"- La cantidad de palabras con 3, 5 o 7 letras es: {cont_palabras_tres_letras}")
    print(f"- El porcentaje de palabras con 2 vocales es: {porcentaje_palabras_dos_vocales}%")
    print(f"- La cantidad de palabras con más de una secuencia 'pe' es: {palabras_mas2_pe}")

# Ejecutar el programa
principal()

