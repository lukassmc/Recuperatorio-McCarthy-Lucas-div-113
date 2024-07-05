import random 
import json
import re



def generar_random(min:int, max:int)-> tuple:
    """genera un número entero aleatorio entre min y max.
    
    Args:
        min (int): valor minimo.
        max (int): valor maximo.
    
    Returns:
        tuple: tupla de numeros aleatorios generados.
    """
    tupla = random.randint(min, max)
    return tupla

def validar_lista(lista:list)-> None:
    """valida si la lista ingresada es una lista no vacía.
    
    Args:
        lista (list): Lista a validar.
    
    Raises:
        ValueError: Si la lista ingresada no es una lista o está vacía.
    """
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista.")
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")

def getpathactual(nombre_archivo)-> str:
    """obtiene la ruta completa del archivo en el directorio actual
    
    Args:
        nombre_archivo (str): nombre del archivo
    
    Returns:
        str: ruta completa del archivo
    """
    
    import os
    
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def printear_listas_usuarios(lista: list) -> None:
    """Función para mostrar de forma pareja los datos de usuarios

    Args:
        lista (list): lista con los datos de los usuarios
    """
    validar_lista(lista)

    print("                       LISTA DE USUARIOS")
    print("ID     Usuario            Likes   Dislikes   Followers")
    print("-------------------------------------------------------")
    for usuario in lista:
        print(f"{usuario['id']:6} {usuario['user']:15} {usuario['likes']:6} {usuario['dislikes']:10} {usuario['followers']:9}")

def filtrar_lista(filtro, lista: list) -> list:
    """filtra una lista según un el filtro ingresado
    
    Args:
        filtro (function): Función de filtro
        lista (list): Lista a filtrar
    
    Returns:
        list: Lista filtrada
    """

    lista_retorno = []
    
    for el in lista:
        if filtro(el):
            lista_retorno.append(el)    
            
    return lista_retorno

def mapear_campo(campo, lista: list) -> list:
    """aplica una funcio a cada elemento de la lista
    
    Args:
        campo (function): funcion a aplicar
        lista (list): lista de entrada
    
    Returns:
        list: Lista con los resultados de aplicar la funcion
    """
    validar_lista(lista)
    lista_retorno = []
    for el in lista :
        lista_retorno.append(campo(el))
    return lista_retorno

def mapear_campo_doble_criterio(campo1, campo2 ,lista: list) -> list:
    """aplica dos funciones a cada elemento de una lista
    
    Args:
        campo1 (function): primera función a aplicar
        campo2 (function): segunda función a aplicar
        lista (list): lista a mapear
    
    Returns:
        list: lista con los resultados de aplicar las funciones
    """
    
    validar_lista(lista)
    lista_retorno = []
    for el in lista :
        lista_retorno.append(campo1(el))
        lista_retorno.append(campo2(el))
        
    return lista_retorno

def swap_lista(lista:list, i: int, j: int)-> None:
    """intercambia dos elementos en una lista
    
    Args:
        lista (list): Lista de entrada
        i (int): indice del primer elemento
        j (int): indice del segundo elemento
    """
    validar_lista(lista)
    aux= lista[i]
    lista[i]= lista[j]
    lista[j]= aux

def ordenar_lista_doble_criterio_ascendente(lista: list, campo1, campo2):
    """ordena una lista de diccionarios segun dos campos de manera sacendente
    
    Args:
        lista (list): lista de diccionarios a ordenar
        campo1 (str): primer campo de ordenación
        campo2 (str): segundo campo de ordenación
    
    Returns:
        list: lista ordenada
    """
    validar_lista(lista)
    tam = len(lista)
    for i in range(0, tam-1):
        for j in range(i + 1, tam):
            
            if lista[i][campo1] == lista[j][campo1]:
                
                if lista[i][campo2] > lista[j][campo2]:
                    
                    swap_lista(lista, i, j)
                    
            elif lista[i][campo1] > lista[j][campo1]:
                
                swap_lista(lista, i, j)
    
    return lista

def totalizar_lista(lista: list)-> int:
    """suma todos los elementos de una lista

    Args:
        lista (list): lista a totalizar

    Returns:
        int: valor de la suma total de la lista
    """
    validar_lista(lista)

    total= 0
    for el in lista:
      total += el
      
    return total                

   
def calcular_promedio_lista(lista: list)-> float:
   """calcula el promedio de los elementos de una lista
    
    Args:
        lista (list): lista de numeros
    
    Returns:
        float: promedio de los elementos de la lista de numeros
    
    Raises:
        ValueError: si la lista esta vacia o el argumento no es una lista
    """
   
   if isinstance (lista, list):
      cant= len(lista)
      if cant == 0:
         raise ValueError("El promedio de una lista no puede ser definido.")
      promedio= totalizar_lista(lista) / cant
   
      return promedio 
      
   raise ValueError("Esto no es una lista")     


def escritor_json(path: str, lista: list):
    """escribe una lista en un archivo JSON
    
    Args:
        path (str): Ruta del archivo
        lista (list): Lista a escribir
    """
    validar_lista(lista)
    
    with open(path, "w") as archivo:
        json.dump(lista, archivo, indent=4)
    
    print("Archivo creado correctamente!")



'------------------------------------------------------------- CARGA DE CSV ----------------------------------------'
post= "posts"
lista_users= []
def cargar_csv(lista: list, nombre_archivo: str)-> list:
    """Carga una lista vacia con los datos del csv

    Args:
        lista (list): lista a cargar
        nombre_archio (str): nombre del archivo 

    Returns:
        list: lista con la informacion cargada
    """
   
    with open(getpathactual(nombre_archivo + ".csv"), "r", encoding= "utf-8") as archivo:
        for linea in archivo:
            diccionario={}
            split= re.split(",|\n", linea)
            
            diccionario["id"] = split[0]
            diccionario["user"] = split[1]
            diccionario["likes"] = split[2]
            diccionario["dislikes"] = split[3]
            diccionario["followers"] = split[4]
            lista.append(diccionario)
    
    print("Lista cargada correctamente!")   
    return lista



'------------------------------------------------------------- CARGA DE POSTS RANDOM----------------------------------------'


def cargar_posts_random(lista: list)-> None:
    """Se mapean los campos likes, dislikes y followers, y se le cargan valores aleatorios.

    Args:
        lista (list): lista a mapear
    """
    validar_lista(lista)
    
    lista_likes= mapear_campo(lambda likes : likes["likes"] , lista)
    lista_dislikes= mapear_campo(lambda dislikes : dislikes["dislikes"] , lista)
    lista_followers= mapear_campo(lambda followers : followers["followers"] , lista)
    
    
    for  user in range(len(lista_likes)):
        likes_random= generar_random(500, 3000)
        dislikes_random= generar_random(300, 3500)
        followers_random= generar_random(10000, 20000)
        
        lista_likes[user] = lista[user]['likes']=likes_random
        lista_likes[user]= lista[user]['dislikes'] = dislikes_random
        lista_likes[user]= lista[user]['followers'] = followers_random
        
    
    print("Tiempos random cargados con exito!")



'------------------------------------------------------------- MEJOR POST ----------------------------------------'

def crear_archivo_mejor_post(lista:list)->None:
    """ Crea un archivo con la informacion de aquellos posts los cuales los likes sean mayores a 2000.


        lista (list): lista con datos para crear archivo
    """
    validar_lista(lista)

    mejores_posts= filtrar_lista(lambda likes: likes['likes'] > 2000, lista)
   
    
    with open(getpathactual( 'mejores_posts.csv'), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"   #lista[0].keys obtiene todas las claves del dict, y join las convina a todas en una linea, con el fin de separarlas con , y \n
        archivo.write(encabezado)
        
  

        for persona in mejores_posts:
            values = list(persona.values())
            lista_retorno = []
            for value in values:
                if isinstance(value,int):
                    lista_retorno.append(str(value))
                elif isinstance(value,float):
                    lista_retorno.append(str(value))
                else:
                    lista_retorno.append(value)
            linea = ",".join(lista_retorno) + "\n"
            archivo.write(linea)




'------------------------------------------------------------- MAYORES HATERS----------------------------------------'


def crear_archivo_mayores_haters(lista:list)->None:
    """ Crea un archivo con la informacion de aquellos posts los cuales los dislikes sean mayores a los likes.
    
        lista (list): lista con datos para crear archivo
    """
    validar_lista(lista)

    mejores_posts= filtrar_lista(lambda likes: likes['dislikes'] > likes['likes'], lista)
   
    
    with open(getpathactual( 'mayores_haters.csv'), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"   #lista[0].keys obtiene todas las claves del dict, y join las convina a todas en una linea, con el fin de separarlas con , y \n
        archivo.write(encabezado)
        
  

        for persona in mejores_posts:
            values = list(persona.values())
            lista_retorno = []
            for value in values:
                if isinstance(value,int):
                    lista_retorno.append(str(value))
                elif isinstance(value,float):
                    lista_retorno.append(str(value))
                else:
                    lista_retorno.append(value)
            linea = ",".join(lista_retorno) + "\n"
            archivo.write(linea)



'------------------------------------------------------------- PROMEDIO FOLLOWERS ----------------------------------------'

def promedio_followers(lista: list)-> float:
    """Realiza una suma de todos los valores de la lista followers para calcular el promedio de esta.

    Args:
        lista (list): lista de users

    Returns:
        float: Resultado del calculo de l promedio
    """
    validar_lista(lista)
    
    lista_followers= mapear_campo(lambda followers: followers["followers"], lista)
    
    promedio= round(calcular_promedio_lista(lista_followers), 2)

    return promedio



'------------------------------------------------------------- ORDENAR POR NOMBRE ASCENDENTE----------------------------------------'

def ordenar_lista_ascendente(campo, lista: list)-> list:
    """ordena una lista de diccionarios segun el campo ingresado de forma ascendente
    
    Args:
        lista (list): lista de diccionarios a ordenar
        campo (str): Campo a ordenar
       
    
    Returns:
        list: lista ordenada
    """
    validar_lista(lista)
    
    tam = len(lista)
    for i in range(0, tam-1):
        for j in range(i + 1, tam):
                   
            if lista[i][campo] > lista[j][campo]:
                
                swap_lista(lista, i, j)
    
    return lista



'------------------------------------------------------------- USUARIO MAS POPULAR ----------------------------------------'

def post_mas_popular(lista: list)-> dict:
    """Esta funcion recorre la lista de users, comparando sus likes, y devuelve a los mas populares.

    Args:
        lista (list): lista a recorrer

    Returns:
        dict: diccionario con los datos del post mas popular
    """
    validar_lista(lista)
    
    
    nombre_mayor_likes = ""
    bandera_mas_likes= False
    bandera_empate= False
    mayor_likes= lista[0]
    for user in lista:
    
        if user["likes"] == mayor_likes:
            mayor_likes_empate= user["likes"]
            user_likes_empate = user["user"]
            bandera_empate = True     
            
        if bandera_mas_likes == False or user["likes"] < mayor_likes:
           
            mayor_likes= user["likes"]
            nombre_mayor_likes = user["user"]
            bandera_mas_likes= True
        
        
    if bandera_empate == True:
        mas_populares= { "mayores likes": mayor_likes,
                    "user": nombre_mayor_likes,                    
                    "empato": mayor_likes_empate,
                    "nombre_empate": user_likes_empate
        }
    else:
        mas_populares= { "mayores likes": mayor_likes,
                    "user": nombre_mayor_likes
            
        }
             
    return mas_populares
