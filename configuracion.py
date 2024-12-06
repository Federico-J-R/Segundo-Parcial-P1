from functions import *
from constantes import *

# EVENTOS
def procesar_eventos_conf(evento, opciones,datos_juego:dict) -> dict[str:pg.Rect]:
    '''
    Procesa los casos en los que se responda una pregunta seleccionando una opcion.
    En caso de acierto, suma puntos, caso contrario los resta (junto con una vida).
    Si no se selecciono ninguna opcion de respuesta, retornara False
    '''
    global VOLUMEN, CANTIDAD_VIDAS, TIEMPO_PREGUNTA, CANT_COMODINES
    
    if evento.type == pg.MOUSEBUTTONUP:
        #print(opciones)
        opcion_seleccionada =  verificar_opcion_seleccionada(evento ,opciones)

        if opcion_seleccionada == "+_vol":
            VOLUMEN = VOLUMEN + 0.05

        elif opcion_seleccionada == "-_vol":
            VOLUMEN = VOLUMEN - 0.05
        
        elif opcion_seleccionada == "+_vidas":
            CANTIDAD_VIDAS = CANTIDAD_VIDAS + 1
        
        elif opcion_seleccionada == "-_vidas":
            CANTIDAD_VIDAS = CANTIDAD_VIDAS - 1

        elif opcion_seleccionada == "+_tiempo":
            TIEMPO_PREGUNTA = TIEMPO_PREGUNTA + 1

        elif opcion_seleccionada == "-_tiempo":
            TIEMPO_PREGUNTA = TIEMPO_PREGUNTA - 1

        elif opcion_seleccionada == "+_com":
            CANT_COMODINES = CANT_COMODINES + 1

        elif opcion_seleccionada == "-_com":
            CANT_COMODINES = CANT_COMODINES - 1

        elif opcion_seleccionada == "volver":

            DICT_COMODINES_INICIAL.update(
                {
                "bombas":CANT_COMODINES,
                "x2":CANT_COMODINES,
                "doble_chance":CANT_COMODINES,
                "pasar":CANT_COMODINES
                }
            )

            DATOS_JUEGO_INICIAL.update(
                {
                "vidas": CANTIDAD_VIDAS,
                "tiempo": (TIEMPO_PREGUNTA,None,True,TIEMPO_PREGUNTA),
                "comodines": DICT_COMODINES_INICIAL,
                "pantalla" : "Menu",
            }
            )
            datos_juego.update(establecer_datos_juego())
            print("Configuracion guardada!")

        else:
            opcion_seleccionada = False

        
        print(opcion_seleccionada)


# DIBUJO
def mostrar_configuracion(pantalla:pg.surface) -> dict[str:pg.Rect]:
    '''
    Dibuja en pantalla el estado de las opciones configurables del juego.
    retorna las opciones con las que modificar los valores.
    '''
    dibujar_fondo_pantalla(pantalla)

    opciones_vol = dibujar_volumen(pantalla)
    opciones_vidas = dibujar_cantidad_vidas(pantalla)
    opciones_tiempo = dibujar_tiempo_preguntas(pantalla)
    opciones_com = dibujar_cantidad_comodines(pantalla)
    opcion_volver = dibujar_volver(pantalla)

    return opciones_vol | opciones_vidas | opciones_tiempo | opciones_com | opcion_volver

def dibujar_volumen(pantalla)-> dict[str,pg.Rect]:
    '''
    dibuja en pantalla el nivel de volumen actual, junto
    a las opciones de subir o bajar el mismo.
    Retorna un diccionario con las posiciones de los rectangulos
    de los botones + y -
    '''
    volumen = f"Volumen: {int(VOLUMEN*100)} %"
    mostrar_texto(pantalla,volumen,TAMAÑO_BOTON,POS_CONFIG_VOLUMEN)

    #CALCULO DE POSICIONES PARA DIBUJAR VOTONES + Y -
    pos_x_izquierda = POS_CONFIG_VOLUMEN[0] - TAMAÑO_BOTON_PEQUEÑO[0] - 30
    pos_x_derecha = POS_CONFIG_VOLUMEN[0] + TAMAÑO_BOTON[0] + 30
    pos_y = POS_CONFIG_VOLUMEN[1] + 10

    pos_mas = (pos_x_derecha,pos_y)
    pos_menos = (pos_x_izquierda,pos_y)
    #CREO Y GUARDO LAS POSICIONES DE LOS BOTONES
    dict_botones = {}
    dict_botones["+_vol"] = mostrar_texto(pantalla,"+",TAMAÑO_BOTON_PEQUEÑO,pos_mas,tamaño=42)
    dict_botones["-_vol"] =mostrar_texto(pantalla,"-",TAMAÑO_BOTON_PEQUEÑO,pos_menos,tamaño=42)

    return dict_botones

def dibujar_cantidad_vidas(pantalla)-> pg.rect.Rect:
    vidas = f"Vidas iniciales: {CANTIDAD_VIDAS}"
    mostrar_texto(pantalla,vidas,TAMAÑO_BOTON,POS_CONFIG_VIDAS)

    #CALCULO DE POSICIONES PARA DIBUJAR VOTONES + Y -
    pos_x_izquierda = POS_CONFIG_VIDAS[0] - TAMAÑO_BOTON_PEQUEÑO[0] - 30
    pos_x_derecha = POS_CONFIG_VIDAS[0] + TAMAÑO_BOTON[0] + 30
    pos_y = POS_CONFIG_VIDAS[1] + 10

    pos_mas = (pos_x_derecha,pos_y)
    pos_menos = (pos_x_izquierda,pos_y)
    #CREO Y GUARDO LAS POSICIONES DE LOS BOTONES
    dict_botones = {}
    dict_botones["+_vidas"] = mostrar_texto(pantalla,"+",TAMAÑO_BOTON_PEQUEÑO,pos_mas,tamaño=42)
    dict_botones["-_vidas"] =mostrar_texto(pantalla,"-",TAMAÑO_BOTON_PEQUEÑO,pos_menos,tamaño=42)

    return dict_botones

def dibujar_tiempo_preguntas(pantalla)-> pg.rect.Rect:
    tiempo = f"Tiempo pregunta: {TIEMPO_PREGUNTA} seg"
    mostrar_texto(pantalla,tiempo,TAMAÑO_BOTON,POS_CONFIG_TIEMPO)

    #CALCULO DE POSICIONES PARA DIBUJAR VOTONES + Y -
    pos_x_izquierda = POS_CONFIG_TIEMPO[0] - TAMAÑO_BOTON_PEQUEÑO[0] - 30
    pos_x_derecha = POS_CONFIG_TIEMPO[0] + TAMAÑO_BOTON[0] + 30
    pos_y = POS_CONFIG_TIEMPO[1] + 10

    pos_mas = (pos_x_derecha,pos_y)
    pos_menos = (pos_x_izquierda,pos_y)
    #CREO Y GUARDO LAS POSICIONES DE LOS BOTONES
    dict_botones = {}
    dict_botones["+_tiempo"] = mostrar_texto(pantalla,"+",TAMAÑO_BOTON_PEQUEÑO,pos_mas,tamaño=42)
    dict_botones["-_tiempo"] =mostrar_texto(pantalla,"-",TAMAÑO_BOTON_PEQUEÑO,pos_menos,tamaño=42)

    return dict_botones

def dibujar_cantidad_comodines(pantalla)-> pg.rect.Rect:
    comodines = f"Comodines: {CANT_COMODINES}"
    mostrar_texto(pantalla,comodines,TAMAÑO_BOTON,POS_CONFIG_COMODINES)

    #CALCULO DE POSICIONES PARA DIBUJAR VOTONES + Y -
    pos_x_izquierda = POS_CONFIG_COMODINES[0] - TAMAÑO_BOTON_PEQUEÑO[0] - 30
    pos_x_derecha = POS_CONFIG_COMODINES[0] + TAMAÑO_BOTON[0] + 30
    pos_y = POS_CONFIG_COMODINES[1] + 10

    pos_mas = (pos_x_derecha,pos_y)
    pos_menos = (pos_x_izquierda,pos_y)
    #CREO Y GUARDO LAS POSICIONES DE LOS BOTONES
    dict_botones = {}
    dict_botones["+_com"] = mostrar_texto(pantalla,"+",TAMAÑO_BOTON_PEQUEÑO,pos_mas,tamaño=42)
    dict_botones["-_com"] =mostrar_texto(pantalla,"-",TAMAÑO_BOTON_PEQUEÑO,pos_menos,tamaño=42)

    return dict_botones

def dibujar_volver(pantalla)-> pg.rect.Rect:
    retorno = {}
    retorno["volver"] = mostrar_texto(pantalla,"Volver",TAMAÑO_BOTON,POS_CONFIG_VOLVER)
    return retorno

