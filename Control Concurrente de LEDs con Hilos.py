import _thread
import time
from machine import Pin

# Definir los pines para los LEDs
led1 = Pin(22, Pin.OUT)  # LED en el pin 2
led2 = Pin(23, Pin.OUT)  # LED en el pin 4

def blink_led(led, delay):
    """Función para hacer parpadear un LED."""
    while True:
        led.value(not led.value())  # Cambiar estado del LED
        time.sleep(delay)  # Esperar el tiempo especificado

# Crear hilos para controlar los LEDs de forma independiente
_thread.start_new_thread(blink_led, (led1, 0.25))  # LED1 parpadea cada 500ms
_thread.start_new_thread(blink_led, (led2, 0.50))  # LED2 parpadea cada 1s

# Mantener el programa principal en ejecución
while True:
    time.sleep(1)  # Evita que el programa termine
