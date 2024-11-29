from functions import *


def procesar_eventos_game_over(evento, opciones, datos_juego):
    '''
    
    '''
    jugador = datos_juego.get("jugador")

    if evento.type == pg.KEYDOWN:
        if evento.key == pg.K_BACKSPACE:
            datos_juego["jugador"] = jugador[:-1]
        else:
            datos_juego["jugador"] += evento.unicode
    print(datos_juego["jugador"])

# DIBUJO
def mostrar_game_over(pantalla:pg.surface, datos_juego:dict) -> dict[str:pg.Rect]:
    '''
    
    '''
    dibujar_fondo_pantalla(pantalla)
    dibujar_puntaje_final(pantalla, datos_juego)
    dibujar_input_nombre(pantalla, datos_juego)

def dibujar_puntaje_final(pantalla:pg.surface, datos_juego:dict):
    '''
    Dibuja en la pantalla el puntaje final obtenido en una partida
    '''
    puntaje = datos_juego.get("puntaje")
    texto = f"GAME OVER Puntaje final: {puntaje}!"
    mostrar_texto(pantalla, texto, TAMAÑO_PREGUNTA, POS_PREGUNTA, tamaño = 56)

def dibujar_input_nombre(pantalla, datos_juego) -> str:
    '''
    
    '''
    texto = datos_juego.get("jugador")

    imagen_boton = pg.image.load(r"Segundo parcial\imagenes\Fondo_rect_2.png")
    rec_boton = pg.Rect(POS_INPUT, TAMAÑO_RESPUESTA)
    boton_redimensionado = pg.transform.scale(imagen_boton, TAMAÑO_RESPUESTA)
    pantalla.blit(boton_redimensionado, POS_INPUT)

    fuente = pg.font.Font(None, 36)
    superficie_texto = fuente.render(texto, True, COLOR_NEGRO)
    rec_texto = superficie_texto.get_rect(center=rec_boton.center)
    pantalla.blit(superficie_texto, rec_texto)

    return rec_boton