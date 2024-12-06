COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)

VOLUMEN = 0.05 #subir de a 5% <-----

ANCHO = 800
ALTO = 600
VENTANA = (ANCHO,ALTO)

FPS = 60

TAMAÑO_PREGUNTA = (350,150)
TAMAÑO_RESPUESTA = (250,60)
TAMAÑO_BOTON = (250,60)
TAMAÑO_BOTON_CHICO = (150,40)
TAMAÑO_BOTON_PEQUEÑO = (50,40)
TAMAÑO_ITEM_HUD = (200, 40)

MARGEN = TAMAÑO_BOTON[1] + 40



#VIDAS
CANTIDAD_VIDAS = 3
POS_VIDAS = (25,25)

#TIEMPO
POS_TIEMPO = (300,25)
TIEMPO_PREGUNTA = 10

I_TIEMPO_RESTANTE = 0
I_TIEMPO_INICIAL = 1
I_FLAG_TIEMPO = 2

#PUNTUACION
POS_PUNTUACION = (575,25)
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 50

POS_BOMBAS = (25,515)
POS_X2 = (225,515)
POS_DOBLE_CHANCE = (425 ,515)
POS_PASAR = (625,515)

#PREGUNTAS Y RESPUESTAS
POS_PREGUNTA = (225 , 90)
POS_X_RESP = 275
POS_Y_RESP = 265
MARGEN_RESP = 80

POS_INPUT = (275 , 265)
POS_ACEPTAR = (325 , 400)

# CONSTANATES (y no tan constantes...) DEL MENU DE INICIO

LISTA_OPCIONES_MENU = [
    "Jugar",
    "Top Partidas",
    "Configuracion",
    "Añadir preguntas",
    "Salir"
    ]

POS_X_BOTON_MENU= ANCHO // 2 - TAMAÑO_BOTON[0] // 2
POS_Y_BOTON_MENU = ALTO // len(LISTA_OPCIONES_MENU) - TAMAÑO_BOTON[1]
POS_INICIO_MENU = (POS_X_BOTON_MENU , POS_Y_BOTON_MENU)


# POS BOTONES, CONFIGURACION
POS_CONFIG_VOLUMEN = (275,60)
POS_CONFIG_VIDAS = (275,150)
POS_CONFIG_TIEMPO = (275,240)
POS_CONFIG_COMODINES = (275,330)
POS_CONFIG_VOLVER = (275,420)


#COMODINES
CANT_COMODINES = 1
DICT_COMODINES_INICIAL ={
    "bombas":CANT_COMODINES,
    "x2":CANT_COMODINES,
    "doble_chance":CANT_COMODINES,
    "pasar":CANT_COMODINES
}

DICT_FLAG_COMODINES ={
    "x2":False,
    "doble_chance":False,
}

DATOS_JUEGO_INICIAL = {
        "vidas": CANTIDAD_VIDAS,
        "tiempo": (TIEMPO_PREGUNTA,None,True),
        "puntaje": 0,
        "comodines": DICT_COMODINES_INICIAL,
        "i_pregunta" : 0,
        "aciertos" : 0,
        "continua juego" : True,
        "pregunta": None,
        "pantalla" : "Menu",
        "jugador": "Ingrese su nombre",
        "flag_comodines" : DICT_FLAG_COMODINES
    }