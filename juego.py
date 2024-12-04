from functions import *
import time



# MANEJO DE EVENTOS Y TIEMPO
def procesar_eventos_juego(evento, opciones, datos_juego) -> dict[str:pg.Rect]:
    '''
    Procesa los casos en los que se responda una pregunta seleccionando una opcion.
    En caso de acierto, suma puntos, caso contrario los resta (junto con una vida).
    Si no se selecciono ninguna opcion de respuesta, retornara False
    '''
    if evento.type == pg.MOUSEBUTTONUP:
        respuesta_correcta = datos_juego.get("pregunta").get("respuesta_correcta")
        opcion_seleccionada =  verificar_opcion_seleccionada(evento ,opciones)

        if opcion_seleccionada == respuesta_correcta and opcion_seleccionada in ["1", "2", "3"]:
            sumar_acierto(datos_juego)
            reiniciar_tiempo(datos_juego)
            print("ACIERTO")

        elif opcion_seleccionada != respuesta_correcta and opcion_seleccionada in ["1", "2", "3"]:
            restar_acierto(datos_juego)
            reiniciar_tiempo(datos_juego)
            print("FRACASO")
        
        elif opcion_seleccionada == "bomba":
            pass
        
        elif opcion_seleccionada == "x2":
            usar_com_x2(datos_juego)

        elif opcion_seleccionada == "pasar":
            usar_com_pasar(datos_juego)

        elif opcion_seleccionada == "doble":
            pass

        else:
            opcion_seleccionada = False

        print(opcion_seleccionada)

def procesar_eventos_tiempo(datos_juego:dict) -> None:
    '''
    
    '''
    tiempo_restante = determinar_tiempo_restante(datos_juego)
    if tiempo_restante == 0: 
        restar_acierto(datos_juego)
        reiniciar_tiempo(datos_juego)

def determinar_tiempo_restante(datos_juego):
    '''
    Determina el tiempo restante para cada pregunta.
    El valor es almacenado en los datos del juego.
    '''
    flag_tiempo = obtener_dato_tiempo(datos_juego,I_FLAG_TIEMPO)
    if flag_tiempo == True:
        tiempo_inicial = time.time()
        flag_tiempo  = False
    else:
        tiempo_inicial = obtener_dato_tiempo(datos_juego,I_TIEMPO_INICIAL)
    tiempo_transcurrido = int(time.time() - tiempo_inicial)

    tiempo_restante = TIEMPO_PREGUNTA - tiempo_transcurrido
    datos_juego["tiempo"] = (tiempo_restante, tiempo_inicial, flag_tiempo)

    return tiempo_restante

def reiniciar_tiempo(datos_juego:dict) -> None:
    '''
    Reinicia los valores de tiempo de juego a los originales
    '''
    datos_juego["tiempo"] = (TIEMPO_PREGUNTA,None,True)

def sumar_acierto(datos_juego):
    '''
    Suma los puntos correspondientes a un acierto.
    En caso de ser el quinto acierto seguido, tambien suma
    una vida.
    Pasa a la siguiente pregunta
    '''
    puntos_acierto = PUNTUACION_ACIERTO
    if datos_juego["flag_comodines"]["x2"] == True:
        puntos_acierto *= 2
        datos_juego["flag_comodines"]["x2"] = False
    datos_juego["puntaje"] += puntos_acierto
    datos_juego["aciertos"] += 1
    datos_juego["i_pregunta"] += 1
    datos_juego["tiempo"] = (TIEMPO_PREGUNTA,True)

    if datos_juego.get("aciertos") == 5:
        datos_juego["vidas"] += 1
        datos_juego["aciertos"] = 0

def restar_acierto(datos_juego):
    '''
    Resta los puntos correspondientes a un fracaso.
    Tambien resta una vida.
    Pasa a la siguiente pregunta
    '''
    if datos_juego["flag_comodines"]["x2"] == True:
        datos_juego["flag_comodines"]["x2"] = False
    datos_juego["puntaje"] -= PUNTUACION_ERROR
    datos_juego["aciertos"] = 0
    datos_juego["vidas"] -= 1
    datos_juego["i_pregunta"] += 1
    datos_juego["tiempo"] = (TIEMPO_PREGUNTA,True)

# MANEJO DE COMODINES

def usar_com_x2(datos_juego):

    cantidad_com = datos_juego.get("comodines").get("x2")
    if cantidad_com > 0:
        datos_juego["comodines"]["x2"] = cantidad_com -1
        datos_juego["flag_comodines"]["x2"] = True

def usar_com_pasar(datos_juego):

    cantidad_com = datos_juego.get("comodines").get("pasar")
    if cantidad_com > 0:
        datos_juego["comodines"]["pasar"] = cantidad_com -1
        datos_juego["i_pregunta"] += 1

# DETERMINACION DE PREGUNTAS

def determinar_pregunta_actual(lista_preguntas:list[dict], datos_juego:dict) -> None:
    '''
    En base a los datos del juego y una lista de preguntas. Determina cual
    es la pregunta actual durante una partida. La pregunta actual
    es actualizada sobre los datos del juego.
    '''
    i_pregunta = datos_juego.get("i_pregunta")
    datos_juego["pregunta"] = lista_preguntas[i_pregunta]

# DETERMINAR GAME OVER

def determinar_game_over(datos_juego:dict, lista_preguntas:list[dict]) -> bool:
    '''
    Determina si el juego se encuentra en condiciones de continuar
    o no. Retornara True, en caso afirmativo, False en caso contrario.
    '''
    retorno = True

    cantidad_preguntas = len(lista_preguntas) -1
    i_pregunta = datos_juego.get("i_pregunta")
    vidas = datos_juego.get("vidas")

    if i_pregunta > cantidad_preguntas or vidas == 0:
        retorno = False

    return retorno 


# DIBUJO JUEGO
def mostrar_juego(pantalla:pg.surface, datos_juego:dict) -> dict[str:pg.Rect]:
    '''
    Muestra la pantalla de juego principal.
    '''
    vidas = datos_juego.get("vidas")
    tiempo = datos_juego.get("tiempo")[I_TIEMPO_RESTANTE]
    puntaje = datos_juego.get("puntaje")
    comodines = datos_juego.get("comodines")
    pregunta = datos_juego.get("pregunta")

    dibujar_fondo_pantalla(pantalla)
    dibujar_hud(pantalla, vidas, tiempo, puntaje) 
    opciones_comodines = dibujar_comodines(pantalla, comodines)
    opciones_trivia = dibujar_trivia(pantalla, pregunta)
    opciones = opciones_comodines | opciones_trivia

    return opciones

# DIBUJO HUD
def dibujar_hud(pantalla:pg.surface, vidas:int, tiempo:int, puntaje:int)-> None:
    '''
    Muestra en pantalla la cantidad de vidas actuales y el tiempo
    restante.
    '''
    dibujar_vidas(pantalla, vidas)
    dibujar_tiempo(pantalla, tiempo)
    dibujar_puntaje(pantalla, puntaje)

def dibujar_vidas(pantalla:pg.surface, vidas:int) -> None:
    '''
    Dibuja la cantidad de vidas en pantalla.
    '''
    texto = f"Vidas: {vidas}"
    mostrar_texto(pantalla, texto, TAMAÑO_ITEM_HUD,POS_VIDAS)

def dibujar_tiempo(pantalla:pg.surface, tiempo:int) -> None:
    texto = f"Tiempo: {tiempo}"
    mostrar_texto(pantalla, texto, TAMAÑO_ITEM_HUD, POS_TIEMPO)

def dibujar_puntaje(pantalla:pg.surface, puntaje:int) -> None:
    texto = f"Puntaje: {puntaje}"
    mostrar_texto(pantalla, texto, TAMAÑO_ITEM_HUD,POS_PUNTUACION)

# DIBUJO COMODINES
def dibujar_comodines(pantalla:pg.surface, dict_comodines:dict[str:int]) -> None:
    '''
    Muestra en pantalla los comodines disponibles
    '''
    dict_bombas = dibujar_bombas(pantalla, dict_comodines.get("bombas"))
    dict_x2 = dibujar_X2(pantalla, dict_comodines.get("x2"))
    dict_doble = dibujar_doble_chance(pantalla, dict_comodines.get("doble_chance"))
    dict_pasar = dibujar_pasar(pantalla, dict_comodines.get("pasar"))

    opciones_comodines = dict_bombas | dict_x2 | dict_doble | dict_pasar

    return opciones_comodines

def dibujar_bombas(pantalla:pg.surface, cant_bomba:int) -> None:
    '''
    Muestra en pantalla la cantidad de comodines bomba disponibles.
    '''
    texto = f"Bombas: {cant_bomba}"
    dict_bomba = {}
    dict_bomba["bomba"] = mostrar_texto(pantalla, texto, TAMAÑO_BOTON_CHICO,POS_BOMBAS,tamaño= 25)
    return dict_bomba

def dibujar_X2(pantalla:pg.surface, cant_X2:int):
    '''
    Muestra en pantalla la cantidad de comodines x2 disponibles.
    '''
    texto = f"X2: {cant_X2}"
    dict_x2 ={}
    dict_x2["x2"] = mostrar_texto(pantalla, texto, TAMAÑO_BOTON_CHICO, POS_X2, tamaño= 25)
    return dict_x2

def dibujar_doble_chance(pantalla:pg.surface, cant_doble_chance:int) -> None:
    '''
    Muestra en pantalla la cantidad de comodines x2 disponibles.
    '''
    texto = f"Doble Chance: {cant_doble_chance}"
    dict_doble = {}
    dict_doble["doble"] = mostrar_texto(pantalla, texto, TAMAÑO_BOTON_CHICO, POS_DOBLE_CHANCE, tamaño= 25)

    return dict_doble

def dibujar_pasar(pantalla:pg.surface, cant_pasar:int) -> None:
    '''
    Muestra en pantalla la cantidad de comodines x2 disponibles.
    '''
    texto = f"Pasar: {cant_pasar}"
    dict_pasar = {}
    dict_pasar["pasar"] = mostrar_texto(pantalla, texto, TAMAÑO_BOTON_CHICO, POS_PASAR, tamaño= 25)

    return dict_pasar

# DIBUJO PREGUNTA

def dibujar_trivia(pantalla:pg.surface, trivia:dict[str:str]) -> dict[str:pg.Rect]:
    '''
    Dibuja en pantalla una pregunta y sus opciones correspondientes.
    '''
    dibujar_pregunta(pantalla, trivia)
    rect_opciones = dibujar_opciones(pantalla, trivia)
    
    return rect_opciones

def dibujar_pregunta(pantalla:pg.surface, trivia:dict[str:str]) -> None:
    '''
    Dibuja una pregunta en la pantalla
    '''
    texto = trivia.get("pregunta")
    mostrar_texto(pantalla, texto, TAMAÑO_PREGUNTA, POS_PREGUNTA)

def dibujar_opciones(pantalla:pg.surface, trivia:dict[str:str]) -> dict[str:pg.Rect]:
    '''
    Dibuja las opciones en una pantalla y crea un diccionario con la informacion
    de las ubicaciones de cada Rect.
    '''
    dict_retorno = {}
    respuestas = obtener_respuestas(trivia)
    margen = 0
    for i in range(len(respuestas)):
        texto = respuestas[i]
        num_opcion = str(i+1)
        rect_opcion = mostrar_texto(pantalla, texto, TAMAÑO_RESPUESTA, (POS_X_RESP, POS_Y_RESP + margen))
        dict_retorno[num_opcion] = rect_opcion
        margen += MARGEN_RESP
    
    return dict_retorno

def obtener_respuestas(trivia:dict[str:str]) -> dict[str:str]:
    '''
    Crea una lista con las opciones de una trivia a mostrar en pantalla.
    '''
    lista_retorno = []
    lista_retorno.append(trivia.get("respuesta_1"))
    lista_retorno.append(trivia.get("respuesta_2"))
    lista_retorno.append(trivia.get("respuesta_3"))
    
    return lista_retorno

