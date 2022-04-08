'''
T-Traiko — hoy a las 16:43
@drago un programa que ordene palabras alfabeticamente
'''

palabras = []   # Aqui se van a agregar las palabras
palabras.sort() # Esta funcion es para ordenar la lista alfabeticamente

while True:

    while True:
        # Opciones 
        print("""
    [1] Agregar palabra
    [2] Mostrar palabras
    [3] Salir de la aplicación
        """)
        try:
            entrada = int(input("=> "))
        except ValueError as e:
            print(e)
        else:
            break

    # Agregar palabra
    if entrada == 1:
        print("\nEscriba una palabra para mostrarla alfabeticamente")
        entrada = input("=> ")

        if entrada.isnumeric() or entrada.isspace(): # Por si el input es un numero
            print("Introduzca una palabra real.")
        else:
            print("Se agrego la palabra")
            palabras.append(entrada) # Añadiendo la palabra a la lista

    # Mostrar palabras
    elif entrada == 2: 
        contador = 0 # Contador para ir contando la cantidad de palabras

        if not palabras: # Verificar si la lista no está vacia
            print("Aun no a agregado palabras")
        else:
            print("\nLista de palabras ordenadas alfabeticamente: ")
            for i in palabras: # Cada que la "i" encuentre una palabra la va a imprimir
                contador += 1 # Sumandole al contador para que se vayan numerando las palabras
                print(f'{contador}. "{i}"')

    # Salir de la aplicación
    elif entrada == 3:
        quit()

    else:
        pass
