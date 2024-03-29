#Alejandra Rodriguez Guevara 21310127 6E1

#Las Redes de Decisión (también conocidas como Diagramas de Influencia o Redes Bayesianas) son una herramienta gráfica 
#utilizada para modelar y resolver problemas de toma de decisiones bajo incertidumbre. Estas redes combinan elementos de 
#la teoría de grafos con la teoría de la probabilidad para representar de manera intuitiva relaciones entre variables, eventos y decisiones.

#Este es un ejemplo simple de cómo podemos implementar una red de decisión  utilizando estructuras de datos en Python. 
#Este código crea un grafo de decisiones simple utilizando un diccionario de Python. Cada clave del diccionario representa 
#un estado, y los valores asociados son otro diccionario que mapea eventos a decisiones.
grafo_decision = {
    #ESCENARIOS
    'Inicio': {'Esta lloviendo fuerte Que tomas?': '-> Paraguas', '': '-> Sin Paraguas', ' ': '-> En el Auto', '  ': '-> SALIR'},
    '-> En el Auto' : {'Hay Lluvia Fuerte Que eliges?': '-> Permanecer en Casa', '': '-> Manejar aun asi', ' ': '-> SALIR'},
    '-> Paraguas': {'Hay Lluvia Fuerte Que eliges?': '-> Permanecer en Casa', '': '-> Ir al Trabajo con el Paraguas', ' ': '-> SALIR'},
    '-> Sin Paraguas': {'Hay Lluvia Fuerte Que eliges?': '-> Permanecer en Casa', '': '-> Ir al Trabajo sin nada', ' ': '-> SALIR'},
    '-> Manejar aun asi' : {'Limpiabrisas?': '-> SI', '': '-> NO', ' ': '-> SALIR'},
    #FINALES
    '-> Permanecer en Casa': {'Sobreviviste Yei (Dale a 1 para SALIR)':'Final Bueno num 1'},
    '-> Ir al Trabajo con el Paraguas' : {'Te cayo un rayo, te creiste semidios pa (Dale a 1 para SALIR)':'Final Malo num 1'},
    '-> Ir al Trabajo sin nada' : {'Te dio neumonia y valiste, no valio la pena (Dale a 1 para SALIR)':'Final Malo num 2'},
    '-> SI' : {'Llegaste al trabajo a salvo (Dale a 1 para SALIR)':'Final Bueno? num 2'},
    '-> NO' : {'Chocaste contra un arbol chiale (Dale a 1 para SALIR)':'Final Malo num 3'}
}

def tomar_decision(grafo, estado_actual): #Función para recorrer el grafo y tomar decisiones.
    while True:  #Iniciamos un bucle.

        if estado_actual not in grafo:  #Verificamos si el estado actual no está en el grafo.
            print("\nDesbloqueaste el final:", estado_actual)  #Imprimimos un mensaje de estado final.
            break  #Salimos del bucle infinito 
        opciones = grafo[estado_actual]  #Obtenemos las opciones disponibles para el estado actual.
        i = 1

        for evento, decision in opciones.items():  #Iteramos sobre las opciones disponibles.
            print(f"\n{i}. {evento}: {decision}")  #Imprimimos las opciones con un índice numérico.
            i += 1

        while True:  #Iniciamos otro bucle para manejar la entrada del usuario.
            eleccion = input("\n\tSelecciona una opción (número): ")  #Solicitamos al usuario que seleccione una opción.

            if eleccion.isdigit():  #Verificamos si la entrada del usuario es un número.
                eleccion = int(eleccion)

                if 1 <= eleccion <= len(opciones):  #Verificamos si la opción seleccionada está dentro del rango válido.
                    break  #Salimos del bucle interno.
            print("\nOpción inválida. Inténtalo de nuevo.")  #Imprimimos un mensaje en caso de que la opción elegida sea inválida.
        
        siguiente_estado = list(opciones.values())[eleccion - 1]  #Obtenemos el siguiente estado basado en la elección del usuario.
        estado_actual = siguiente_estado  #Actualizamoa el estado actual con el siguiente estado elegido por el usuario.

tomar_decision(grafo_decision, 'Inicio') #Iniciamos la toma de decisiones desde el estado inicial