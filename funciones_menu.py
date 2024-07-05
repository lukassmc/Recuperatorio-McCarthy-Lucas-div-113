from funciones import *
from os import system


def pausar()-> None:
    system("pause")

def limpiar_terminal()-> None:
    
    system("cls")

def menu_users()-> str:
    """Menu de opciones para obtener datos.

    Returns:
        str: Devuelve el dato de la opción elegida. 
    """
    limpiar_terminal()
    print("     Menu de opciones")
    print("A- Cargar archivos .CSV .")
    print("B- Mostrar lista de users.")
    print("C- Asignar valores de likes, dislikes y followers random.")
    print("D- Generar archivo de mejores posts (Mas de 2000 likes.)")
    print("E- Generar archivo de los posts con mayores haters(Mas dislikes que likes.)")
    print("F- Mostrar promedio de followers.")
    print("G- Crear .JSON con la lista ordenada por los users de forma ascendente.")
    print("H- Post mas popular.")
    print("I- Salir")
    
    return obtener_opcion("Ingrese una opcion:  ").lower()


def confirmar_salida(mensaje: str)-> bool:
    """Le pregunta al usuario si desea salir o no.

    Args:
        mensaje (str): Mensaje para preguntar si desea salir

    Returns:
        bool: Devuelve True si la opción es "Si"
    """
    respuesta= input(mensaje).lower()
    
    return respuesta == "si"



def es_texto(entrada:str)-> bool:
    """Verifica si es str

    Args:
        entrada (str): Valor de entrada

    Returns:
        bool: devuelve true si es str
    """
    return isinstance(entrada, str)



def obtener_opcion(mensaje: str)-> str:
    """Valida que la opción ingresada esté dentro de las opciones validas.

    Args:
        mensaje (str): mensaje para pedir el dato

    Returns:
        str : deuelve la opcion ingresada. 
    """
    
    lista_opciones= ["a","b","c","d","e","f","g","h","i","j"]
    
    while True:
        
        entrada = input(mensaje)
        if entrada in lista_opciones:
            
            return entrada
        else:
            print("Entrada inválida. Por favor, ingrese una opción válida.")
            

            
