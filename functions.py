from constantes import *
import random
import pygame as pg
import pygame.mixer as mixer
import json as js
import copy

def mostrar_texto_original(pantalla:pg.Surface, texto: str,tamaño_caja:tuple, posicion: tuple, color:tuple = COLOR_NEGRO, tamaño:int=36) -> pg.Rect:
    '''
    Crea una caja de texto por defecto de fuente 36 y de color negro.
    Requiere darle una pantalla, la posicion donde se dibujara en la misma
    y el texto a mostrar.
    Retorna un objeto pygame.Rec
    '''

    imagen_boton = pg.image.load(r"Segundo parcial\imagenes\Fondo_rect_2.png")
    rec_boton = pg.Rect(posicion, tamaño_caja)
    boton_redimensionado = pg.transform.scale(imagen_boton, tamaño_caja)
    pantalla.blit(boton_redimensionado, posicion)

    fuente = pg.font.Font(None, tamaño)
    superficie_texto = fuente.render(texto, True, color)
    rec_texto = superficie_texto.get_rect(center=rec_boton.center)
    pantalla.blit(superficie_texto, rec_texto)

    return rec_boton

# Mostrar texto modificado por IA:
def mostrar_texto(pantalla: pg.Surface, texto: str, tamaño_caja: tuple, posicion: tuple, color: tuple = COLOR_NEGRO, tamaño: int = 36) -> pg.Rect:
    """
    Crea una caja de texto con líneas ajustadas al ancho de la caja.
    No reduce el tamaño de la fuente.
    Requiere una pantalla, la posición donde se dibujará, y el texto a mostrar.
    Retorna un objeto pygame.Rect.
    """
    # Cargar y redimensionar la imagen de fondo de la caja
    imagen_boton = pg.image.load(r"Segundo parcial\imagenes\Fondo_rect_2.png")
    rec_boton = pg.Rect(posicion, tamaño_caja)
    boton_redimensionado = pg.transform.scale(imagen_boton, tamaño_caja)
    pantalla.blit(boton_redimensionado, posicion)

    # Crear fuente
    fuente = pg.font.Font(None, tamaño)

    # Dividir texto en líneas si es necesario
    palabras = texto.split()  # Dividir texto en palabras
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        # Agregar palabra a la línea actual y calcular su ancho
        prueba_linea = f"{linea_actual} {palabra}".strip()
        if fuente.size(prueba_linea)[0] <= tamaño_caja[0] - 10:  # Margen de 10 px
            linea_actual = prueba_linea
        else:
            # Si no cabe, guardar línea y comenzar una nueva
            lineas.append(linea_actual)
            linea_actual = palabra

    # Agregar última línea
    if linea_actual:
        lineas.append(linea_actual)

    # Calcular altura de las líneas
    altura_texto = fuente.size("Texto")[1]
    max_lineas = (tamaño_caja[1] - 10) // altura_texto  # Número máximo de líneas que caben

    # Limitar las líneas a las que caben dentro de la caja
    if len(lineas) > max_lineas:
        lineas = lineas[:max_lineas]  # Solo mostrar las líneas que caben

    # Dibujar texto centrado en cada línea
    for i, linea in enumerate(lineas):
        superficie_texto = fuente.render(linea, True, color)
        rec_texto = superficie_texto.get_rect()
        rec_texto.midtop = (rec_boton.centerx, posicion[1] + i * altura_texto + 5)  # Margen superior de 5 px
        pantalla.blit(superficie_texto, rec_texto)

    return rec_boton

def dibujar_fondo_pantalla(pantalla:pg.surface) -> None:
    '''
    Dibuja el fondo de la ventana
    '''
    fondo_menu = pg.image.load(r"Segundo parcial\imagenes\Fondo_menu.png")
    fondo_menu = pg.transform.scale(fondo_menu,VENTANA) 
    pantalla.blit(fondo_menu,(0,0))


#EVENTOS (y otras cosas)
def verificar_opcion_seleccionada(evento:pg.event.Event ,opciones:dict[str,pg.Rect]) -> str:
    '''
    Verifica segun un evento dado, en el caso del que el mismo sea
    un click. Si se realizo sobre una caja de las opciones dada.
    En caso afirmativo, retorna el str correspondiente a la opcion
    seleccionada. En caso de que no se seleccione ninguna opcion, 
    retornara False
    '''
    opcion_seleccionada = False
    if evento.type ==pg.MOUSEBUTTONUP and evento.button == 1:
        mouse_pos = evento.pos
        for k_opcion, v_opcion in opciones.items():
            if v_opcion.collidepoint(mouse_pos):
                opcion_seleccionada = k_opcion
                break
    return opcion_seleccionada

def cerrar_programa() -> None:
    '''
    Cierra el pygame y la ventana del juego
    '''
    print("Saliendo...")
    pg.quit()
    quit() 

def obtener_dato_tiempo(datos_juego:dict, i_dato:int) -> bool:
    '''
    Obtiene la flag, dentro de la tupla tiempo
    '''
    return datos_juego.get("tiempo")[i_dato]

def cambiar_pantalla(pantalla:str,datos_juego:dict) -> None:
    '''
    Cambia el dato de la pantalla de juego, al nombre de
    la pantalla dado
    '''
    datos_juego["pantalla"] = pantalla

def reiniciar_datos_juego(datos_juego:dict):
    datos_juego.update(copy.deepcopy(DATOS_JUEGO_INICIAL))

def guardar_jugador_js(ruta:str,datos_juego):
    data = {}
    data["jugador"] = datos_juego.get("jugador")
    data["puntaje"] = datos_juego.get("puntaje")
    
    with open(ruta, "r") as archivo:
        datos_json = archivo.read()
        

        if datos_json == "":
            datos_archivo = []
        
        else:
            archivo.seek(0)
            datos_archivo = js.load(archivo)
            if type(datos_archivo) == dict:
                datos_archivo = datos_archivo

    datos_archivo.append(data)

    with open(ruta, "w") as archivo:
        js.dump(datos_archivo, archivo, indent=4)

def terminar_partida(ruta,datos_juego):
    '''
    Guarda los datos del final de la partida en un json.
    Cambia la pantalla actual a la pantalla de menu y reinicia
    los datos del juego al estado original.
    '''
    guardar_jugador_js(ruta,datos_juego)
    cambiar_pantalla("Menu",datos_juego)
    reiniciar_datos_juego(datos_juego)

def establecer_datos_juego() ->dict:
    '''
    Establece los datos del juego (configuracion del mismo).
    segun los datos almacenados en las constantes.
    Los datos del juego son retornados como diccionario
    '''
    return copy.deepcopy(DATOS_JUEGO_INICIAL)

#PREGUNTAS

def obtener_lista_csv(nombre_archivo:str) -> list[dict]:
    '''
    Crea una lista a partir de un archivo.csv, la misma contiene diccionarios
    cuyos valores "Clave" seran el titulo de la cada columna.
    El archivo ingresado como parametro debe existir y debe estar en formato csv
    '''
    lista_datos = []

    with open(nombre_archivo,"r", encoding='utf-8') as archivo:
        
        encabezados = archivo.readline().replace("\n", "")
        lista_claves = encabezados.split(",")

        for linea in archivo:
            datos = linea.replace("\n", "").split(",")
            diccionario = {}

            rango = len(lista_claves)
            for i in range(rango):
                clave_dict = lista_claves[i]
                valor_dict = datos[i]
                diccionario[clave_dict] = valor_dict
            
            lista_datos.append(diccionario)

    return lista_datos

def randomizar_preguntas(lista_preguntas:list)->int:
    '''
    Desordena una lista de preguntas dadas.
    '''
    return random.shuffle(lista_preguntas)












