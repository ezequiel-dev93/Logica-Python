__autor__ = "Ezequiel Suarez"

"""
Silaba 'de' en la primera mitad
Desarrollar un Programa que permita cargar por teclado un texto completo. Siempre
se supone que el usuario cargará un punto para indicar el final del texto. y cada
palabra de ese texto está separda de los demás por un espacio en blanco. El programa debe:

Punto 1 - Determinar cuántas palabras tenían al menos un caracter que era realidad un dígito
( un cararter entre ('0' y '9')

Punto 2 - Determinar cuántas palabras 3 o al menos letras, cuántas tenían 4 y hasta 6 letras y
cuántas tenias más de 6 letras.

Punto 3 - Determinar la longitud de la palabra más larga del texto.

Punto 4 - Determinar cuántas palabras contuvieron la expresion 'de', pero en la primera mitad de la palabra.
"""

# Función Global
def es_digito(letra):
    digitos = '0123456789'
    return letra in digitos

# Función principal
def main():
    print("\t Análisis De Texto - Sílaba 'de'")
    print("-+" * 40)
    texto = input("\t Ingrese el texto a analizar, finaliza con punto: ")

    # Inicializaciones de contadores y booleanos
    tiene_digito = tiene_d = tiene_de = False
    palabra_digito = palabra_tres_letras = palabra_4_a_6_letras = palabra_mas_seis_letras = palabra_mitad = 0
    cant_letras = mayor_longitud = posicion = 0

    # Recorremos el texto mediante el ciclo for
    for letra in texto:
        if letra == ' ' or letra == '.':  # Fin de palabra
            # Punto 1 - verificar cuántas palabras tenían al menos un dígito
            if tiene_digito:
                palabra_digito += 1

            # Punto 2 - cuántas palabras tienen hasta 3 letras, cuántas tienen 4 a 6 letras, y cuántas tienen más de 6 letras
            if cant_letras <= 3:
                palabra_tres_letras += 1
            elif 4 <= cant_letras <= 6:
                palabra_4_a_6_letras += 1
            elif cant_letras > 6:
                palabra_mas_seis_letras += 1

            # Punto 3 - Determinar la longitud de la palabra más larga del texto
            if cant_letras > mayor_longitud:
                mayor_longitud = cant_letras

            # Punto 4 - Palabras que contienen la expresión 'de' en la primera mitad
            mitad = cant_letras // 2
            if tiene_de and 0 < posicion <= mitad:
                palabra_mitad += 1

            # Resetear los contadores para la siguiente palabra
            tiene_de = tiene_d = False
            tiene_digito = False
            cant_letras = 0
            posicion = 0  # Reseteamos la posición para la siguiente palabra

        else:  # Caracteres que forman palabras
            cant_letras += 1
            if es_digito(letra):
                tiene_digito = True

            if letra == 'd':
                tiene_d = True  # Activamos la bandera para la detección de "de"
            elif letra == 'e' and tiene_d:
                tiene_de = True  # Detectamos la secuencia "de"
                posicion = cant_letras
            else:
                tiene_d = False  # Resetear la detección de "d" si no sigue con "e"

    # Procesar la última palabra si termina en punto
    if texto[-1] == '.':
        # Repetimos el procesamiento de la palabra que ocurre al finalizar con un punto
        if tiene_digito:
            palabra_digito += 1
        if cant_letras <= 3:
            palabra_tres_letras += 1
        elif 4 <= cant_letras <= 6:
            palabra_4_a_6_letras += 1
        elif cant_letras > 6:
            palabra_mas_seis_letras += 1
        if cant_letras > mayor_longitud:
            mayor_longitud = cant_letras
        mitad = cant_letras // 2
        if tiene_de and 0 < posicion <= mitad:
            palabra_mitad += 1

    print("\t Presentación de Resultados:")
    print("-+" * 40)
    print(f'- La cantidad de palabras que contienen al menos un dígito: {palabra_digito}')
    print(f'- La cantidad de palabras con hasta 3 letras: {palabra_tres_letras}')
    print(f'- La cantidad de palabras con entre 4 y 6 letras: {palabra_4_a_6_letras}')
    print(f'- La cantidad de palabras con más de 6 letras: {palabra_mas_seis_letras}')
    print(f'- La cantidad de palabras con la secuencia "de" en la primera mitad: {palabra_mitad}')
    print(f'- La longitud de la palabra más larga es: {mayor_longitud} letras')

# Ejecutar el programa
main()
