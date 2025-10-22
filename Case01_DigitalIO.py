import RPi.GPIO as GPIO # Llamar a la libreria que permite utilizar los pines GPIO, y renombrarla de una manera mas accecible.
import time # Llamar a la libreria que permite trabajar con funciones de manejo de tiempo.

PIN_BOTON = 3
PIN_LED = 7

estadoBoton = 0 # Inicializar una variable para almacenar el estado del boton.

GPIO.setmode(GPIO.BOARD) # Configurar los Piones de Raspberry segun la numeracion Fisica.
GPIO.setup(PIN_LED, GPIO.OUT) # Configurar el PIN FISICO 7 como salida. 
GPIO.setup(PIN_BOTON, GPIO.IN) # Configurar el PIN FISICO 3 como entrada.

while True: # Ciclo Infinito (Void Loop).
	estadoBoton = GPIO.input(PIN_BOTON) # Leer entrada Digital.
	GPIO.output(7, estadoBoton) # Enviar el estado del boton al PIN 7 (digitalWrite).
	
	if estadoBoton == 1: # Si el boton esta presionado, entonces:
		print("ENCENDIDO") # Imprima mensaje de encendido
		time.sleep(1) # Realizar una pausa de 1 seg.
	else: # si el boton NO esta presionado, entonces:
		print("APAGADO") # Imprima mensaje de APAGADO.
		time.sleep(1)
