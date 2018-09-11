import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.OUT)

def Rbpi(estado):
    if estado['foco1']:
        print('El FOCO1 esta ENCENDIDO.')
        GPIO.output(14, True)
    else:
        print('El FOCO1 esta APAGADO.')
		#GPIO.setmode(GPIO.BOARD)
        GPIO.output(14, False)
    if estado['foco2']:
        print('El FOCO2 esta ENCENDIDO.')
    else:
        print('El FOCO2 esta APAGADO.')
    if estado['foco3']:
        print('El FOCO3 esta ENCENDIDO.')
    else:
        print('El FOCO3 esta APAGADO.')
    if estado['foco4']:
        print('El FOCO4 esta ENCENDIDO.')
    else:
        print('El FOCO4 esta APAGADO.')
    if estado['ventilador']:
        print('El VENTILADOR esta ENCENDIDO.')
    else:
        print('El VENTILADOR esta APAGADO.')
    if estado['puerta']:
        print('La PUERTA esta ABIERTA.')
    else:
        print('La PUERTA esta BLOQUEADA.')
