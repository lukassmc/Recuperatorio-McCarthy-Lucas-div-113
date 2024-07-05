from funciones_menu import *

lista_users = []

bandera_pedir_archivo = False
bandera_valores_cargados= False
while True:
    limpiar_terminal()
    match menu_users():
        case "a":
            try:  
                archivo_nombre = input("ingrese el nombre del archivo csv a cargar: ")
                cargar_csv(lista_users, archivo_nombre)
                
                bandera_pedir_archivo = True
                print("Archivo cargardo con exito!")
            except:
                print("Archivo inexistente, porfavor intentelo denuevo.")
            
        case "b":
            if bandera_pedir_archivo == False:
                print("Para imprimir la lista, primero debes de cargarla con el archivo.")
            else:
                printear_listas_usuarios(lista_users)
                
        case "c":
            if bandera_pedir_archivo == False:
                print("Para cargar los valores de los posts, primero debes cargar la lista con los datos del archivo.")
            else:
                cargar_posts_random(lista_users)
                print("Valores cargados con exito!")
                bandera_valores_cargados= True
        case "d":
            if bandera_pedir_archivo == False:
                print("Para analizar los valores, primero tienes que cargar el archivo.")
            elif bandera_valores_cargados == False:
               print("Para crear el archivo, primero tienes que cargar los valores.")
            else:
                crear_archivo_mejor_post(lista_users)
                print("Archivo creado con exito!")
                
        case "e":
            if bandera_pedir_archivo == False:
                print("Para analizar los valores, primero tienes que cargar el archivo.")
            elif bandera_valores_cargados == False:
               print("Para crear el archivo, primero tienes que cargar los valores.")
            else:
                crear_archivo_mayores_haters(lista_users)
                print("Archivo creado con exito!")
                
        case "f":
            if bandera_pedir_archivo == False:
                print("Para analizar los valores, primero tienes que cargar el archivo.")
            elif bandera_valores_cargados == False:
               print("Para crear el archivo, primero tienes que cargar los valores.")
            else:
                print(f"El promedio de followers entre todos los users es de {promedio_followers(lista_users)}")
                
        case "g":
            if bandera_pedir_archivo == False:
                print("Para analizar los valores, primero tienes que cargar el archivo.")
            else:
                lista_ordenada= ordenar_lista_ascendente("user",lista_users)
                escritor_json("posts.json", lista_ordenada)
               
        case "h":
            if bandera_pedir_archivo == False:
                print("Para analizar los valores, primero tienes que cargar el archivo.")
            elif bandera_valores_cargados == False:
               print("Para crear el archivo, primero tienes que cargar los valores.")
            else:
                print(post_mas_popular(lista_users))
            
            
        case "i":
            if confirmar_salida("Desea salir?\n "):
                break
            else:
                continue
    pausar()