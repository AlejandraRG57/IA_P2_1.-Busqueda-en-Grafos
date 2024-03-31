#Alejandra Rodriguez Guevara 21310127 6E1

#Un Proceso de Decisión de Markov Parcialmente Observable (POMDP) es una extensión de un MDP en el cual el agente no tiene acceso directo al estado real del sistema, 
#sino que recibe observaciones que son ruidosas o parciales lo que significa que no proporcionan información completa sobre el estado real. 

#La tarea del agente en un POMDP es tomar decisiones secuenciales que maximicen la recompensa esperada a pesar de la incertidumbre sobre el estado real.

import random

pomdp_grafo = { #Definimos el grafo POMDP.
    'A': {
        'transiciones': {'B': 0.5, 'E': 0.5},
        'observaciones': {'obs1': {'obs_B': 0.2, 'obs_E': 0.8}}
    },
    'B': {
        'transiciones': {'A': 0.5, 'C': 0.5},
        'observaciones': {'obs2': {'obs_A': 0.3, 'obs_C': 0.7}}
    },
    'C': {
        'transiciones': {'B': 0.33, 'D': 0.33, 'F': 0.34},
        'observaciones': {'obs3': {'obs_B': 0.4, 'obs_D': 0.6}}
    },
    'D': {
        'transiciones': {'C': 0.5, 'I': 0.5},
        'observaciones': {'obs4': {'obs_C': 0.2, 'obs_I': 0.8}}
    },
    'E': {
        'transiciones': {'A': 0.25, 'F': 0.25, 'G': 0.25, 'H': 0.25},
        'observaciones': {'obs5': {'obs_A': 0.1, 'obs_F': 0.9}}
    },
    'F': {
        'transiciones': {'C': 0.5, 'E': 0.5},
        'observaciones': {'obs6': {'obs_C': 0.6, 'obs_E': 0.4}}
    },
    'G': {
        'transiciones': {'E': 0.5, 'J': 0.5},
        'observaciones': {'obs7': {'obs_E': 0.7, 'obs_J': 0.3}}
    },
    'H': {
        'transiciones': {'E': 0.33, 'I': 0.33, 'J': 0.34},
        'observaciones': {'obs8': {'obs_E': 0.5, 'obs_I': 0.5}}
    },
    'I': {
        'transiciones': {'D': 0.33, 'H': 0.33, 'L': 0.34},
        'observaciones': {'obs9': {'obs_D': 0.8, 'obs_H': 0.2}}
    },
    'J': {
        'transiciones': {'G': 0.25, 'H': 0.25, 'K': 0.25, 'M': 0.25},
        'observaciones': {'obs10': {'obs_G': 0.4, 'obs_H': 0.6}}
    },
    'K': {
        'transiciones': {'J': 0.5, 'L': 0.5},
        'observaciones': {'obs11': {'obs_J': 0.7, 'obs_L': 0.3}}
    },
    'L': {
        'transiciones': {'I': 0.33, 'K': 0.33, 'N': 0.34},
        'observaciones': {'obs12': {'obs_I': 0.9, 'obs_K': 0.1}}
    },
    'M': {
        'transiciones': {'J': 0.5, 'N': 0.5},
        'observaciones': {'obs13': {'obs_J': 0.2, 'obs_N': 0.8}}
    },
    'N': {
        'transiciones': {'L': 0.5, 'M': 0.5},
        'observaciones': {'obs14': {'obs_L': 0.5, 'obs_M': 0.5}}
    }
}

def simular_paso(estado_actual, grafo): #Función para simular un paso en el POMDP.
    transiciones = grafo[estado_actual]['transiciones'] #Realizamos una transición basada en las probabilidades.
    nuevo_estado = random.choices(list(transiciones.keys()), weights=list(transiciones.values()))[0]
    observaciones = grafo[estado_actual]['observaciones'] #Observamos el estado basado en las probabilidades de observación.
    observacion_probabilidades = observaciones[list(observaciones.keys())[0]]  #Suponemos una sola observación.
    observacion = random.choices(list(observacion_probabilidades.keys()), weights=list(observacion_probabilidades.values()))[0]
    
    return nuevo_estado, observacion

estado_actual = 'A' #Simulamos una secuencia de pasos en el POMDP.
observaciones = []
for _ in range(10):
    nuevo_estado, observacion = simular_paso(estado_actual, pomdp_grafo)
    print(f"Estado actual: {estado_actual}, Nueva observación: {observacion}") #Imprimimos el estado y su observacion por cada estado.
    estado_actual = nuevo_estado
    observaciones.append(observacion)

print("\nSecuencia de observaciones:", observaciones) #Imprimimos la Secuencia de observaciones.