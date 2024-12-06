from functions import *
from menu import *
from juego import *
from game_over import *
from configuracion  import *

#--------# INICIALIZANDO VENTANA #--------#
pg.init()

# SONIDO:
mixer.init()
sonido_menu = mixer.Sound(r"Segundo parcial\sonidos\menu_principal.mp3")


reloj = pg.time.Clock()

# VENTANA:
icono = pg.image.load(r"Segundo parcial\imagenes\UTN_Icon.png")
pg.display.set_caption("Preguntados Div 314 - UTN Avellaneda")
pg.display.set_icon(icono)
pantalla = pg.display.set_mode(VENTANA)

#--------# BUCLE PRINCIPAL #--------#
lista_preguntas = obtener_lista_csv(r"Segundo parcial\data\preguntas.csv")
randomizar_preguntas(lista_preguntas)
datos_juego = establecer_datos_juego()


while True:
    sonido_menu.set_volume(VOLUMEN)
    cola_eventos = pg.event.get()
    pantalla_actual = datos_juego.get("pantalla")

    #EVENTOS
    for evento in cola_eventos: 
        
        if evento.type == pg.QUIT:
            cerrar_programa()

        elif evento.type == pg.MOUSEBUTTONUP or evento.type == pg.KEYDOWN:
            if pantalla_actual == "Menu":
                procesar_eventos_menu(evento,opciones,datos_juego)
    
            elif pantalla_actual == "Jugar":
                procesar_eventos_juego(evento, opciones, datos_juego)
                determinar_pregunta(lista_preguntas,datos_juego)

            elif pantalla_actual == "Game Over":
                procesar_eventos_game_over(evento, opciones, datos_juego)
                
            
            elif pantalla_actual == "Top Partidas":
                pass
            
            elif pantalla_actual == "Configuracion":
                procesar_eventos_conf(evento, opciones,datos_juego)

            elif pantalla_actual == "Añadir preguntas":
                pass

            time.sleep(0.05)
            pg.event.clear()
    


    #ACTUALIZACION DE JUEGO
    reloj.tick(FPS)

    #DIBUJO DE PANTALLA
    if pantalla_actual == "Menu":
        opciones = mostrar_menu_principal(pantalla)
    
    elif pantalla_actual == "Jugar":

        estado_juego = determinar_game_over(datos_juego, lista_preguntas)

        if estado_juego == True:
            determinar_primer_pregunta(lista_preguntas,datos_juego)
            

            procesar_eventos_tiempo(datos_juego)
            opciones = mostrar_juego(pantalla, datos_juego) 

        else:
            randomizar_preguntas(lista_preguntas)
            cambiar_pantalla("Game Over",datos_juego)

    elif pantalla_actual == "Game Over":
        opciones = mostrar_game_over(pantalla,datos_juego)

    elif pantalla_actual == "Top Partidas":
        cambiar_pantalla("Menu",datos_juego)
    
    elif pantalla_actual == "Configuracion":
        opciones = mostrar_configuracion(pantalla)

    elif pantalla_actual == "Añadir preguntas":
        cambiar_pantalla("Menu",datos_juego)
    #sonido_menu.play()


    #ACTUALIZAR PANTALLA
    pg.display.flip()