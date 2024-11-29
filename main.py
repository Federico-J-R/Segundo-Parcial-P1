from functions import *
from menu import *
from juego import *
from game_over import *


#--------# INICIALIZANDO VENTANA #--------#
pg.init()

# SONIDO:
mixer.init()
sonido_menu = mixer.Sound(r"Segundo parcial\sonidos\menu_principal.mp3")
sonido_menu.set_volume(0.04)

reloj = pg.time.Clock()

# VENTANA:
icono = pg.image.load(r"Segundo parcial\imagenes\UTN_Icon.png")
pg.display.set_caption("Preguntados Div 314 - UTN Avellaneda")
pg.display.set_icon(icono)
pantalla = pg.display.set_mode(VENTANA)

#--------# BUCLE PRINCIPAL #--------#
lista_preguntas = obtener_lista_csv(r"Segundo parcial\data\preguntas.csv")
randomizar_preguntas(lista_preguntas)

datos_juego = {
        "vidas": CANTIDAD_VIDAS,
        "tiempo": (TIEMPO_PREGUNTA,None,True),
        "puntaje": 0,
        "comodines": DICT_COMODINES_INICIAL,
        "i_pregunta" : 0,
        "pregunta" : lista_preguntas[0],
        "aciertos" : 0,
        "continua juego" : True,
        "jugador": ""
    }
pantalla_actual = "Menu"
estado_juego = determinar_game_over(datos_juego, lista_preguntas)


while True:
    cola_eventos = pg.event.get()

    #EVENTOS
    for evento in cola_eventos:
        if evento.type == pg.QUIT:
            cerrar_programa()

        elif evento.type == pg.MOUSEBUTTONUP:
            if pantalla_actual == "Menu":
                pantalla_actual = procesar_eventos_menu(evento,opciones)
    
            elif pantalla_actual == "Jugar":
                procesar_eventos_juego(evento, opciones, datos_juego)

            elif pantalla_actual == "Game Over":
                procesar_eventos_game_over(evento, opciones, datos_juego)
            
            elif pantalla_actual == "Top Partidas":
                pantalla_actual = "Menu"
            
            elif pantalla_actual == "Configuracion":
                pantalla_actual = "Menu"

            elif pantalla_actual == "Añadir preguntas":
                pantalla_actual = "Menu"

            time.sleep(0.1)
            pg.event.clear()
    


    #ACTUALIZACION DE JUEGO
    reloj.tick(FPS)

    #DIBUJO DE PANTALLA
    if pantalla_actual == "Menu":
        opciones = mostrar_menu_principal(pantalla)
    
    elif pantalla_actual == "Jugar":
        estado_juego = determinar_game_over(datos_juego, lista_preguntas)
        if estado_juego == True:
            procesar_eventos_tiempo(datos_juego)
            determinar_pregunta_actual(lista_preguntas,datos_juego)
            opciones = mostrar_juego(pantalla, datos_juego)
        else:
            pantalla_actual = "Game Over"

    elif pantalla_actual == "Game Over":
        mostrar_game_over(pantalla,datos_juego)
        

    elif pantalla_actual == "Top Partidas":
        pantalla_actual = "Menu"
    
    elif pantalla_actual == "Configuracion":
        pantalla_actual = "Menu"

    elif pantalla_actual == "Añadir preguntas":
        pantalla_actual = "Menu"
    #sonido_menu.play()


    #ACTUALIZAR PANTALLA
    pg.display.flip()