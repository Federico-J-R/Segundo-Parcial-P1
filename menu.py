from functions import *

def mostrar_menu_principal(pantalla:pg.surface) -> dict[str:pg.Rect]:
    '''
    Muestra el menu principal del juego.
    Retorna un diccionario con los rectangulos de cada boton del menu.
    '''
    dibujar_fondo_pantalla(pantalla)
    dict_opciones = dibujar_listado_opciones(pantalla, LISTA_OPCIONES_MENU, POS_INICIO_MENU, MARGEN)

    return dict_opciones

def dibujar_listado_opciones(pantalla:pg.Surface, lista_opciones:list[str], pos_inicio:tuple, margen:int) -> dict[str:pg.Rect]:
    '''
    Dibuja en pantalla una lista de opciones dada y retorna una diccionario correspondiente al nombre de la opcion
    y los rectangulos correspondientes a cada una. El dibujo comienza a dibujarse desde una posicion de inicio
    dada. La distancia entre los bloques esta dada por el margen.
    '''
    dict_opciones = {}
    pos_x = pos_inicio[0]
    pos_y = pos_inicio[1]
    cantidad_opciones = len(lista_opciones)
    for i_opcion in range(cantidad_opciones):
        opcion = lista_opciones[i_opcion]
        dict_opciones[opcion] = mostrar_texto(pantalla,opcion,TAMAÑO_RESPUESTA,(pos_x , pos_y + (margen * i_opcion)))

    return dict_opciones    

#EVENTOS
def cerrar_programa() -> None:
    '''
    Cierra el pygame y la ventana del juego
    '''
    print("Saliendo...")
    pg.quit()
    quit() 

#EVENTOS DEL MENU

def procesar_eventos_menu(evento:pg.event.Event ,opciones:dict[str,pg.Rect], datos_juego:dict) -> str:
    '''
    Realiza las acciones correspondientes segun la opcion seleccionada
    en el menu de inicio.
    '''
    if evento.type == pg.MOUSEBUTTONUP:
        opcion_seleccionada = verificar_opcion_seleccionada(evento,opciones)
        print(opcion_seleccionada)

        if opcion_seleccionada == "Salir":
            cerrar_programa()
        elif opcion_seleccionada == False:
            pantalla = "Menu"
        else:
            pantalla = opcion_seleccionada

        cambiar_pantalla(pantalla,datos_juego)
