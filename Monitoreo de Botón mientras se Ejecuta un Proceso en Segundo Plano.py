import _thread
from machine import Pin, Timer
import time

contador = 0
bloqueo = _thread.allocate_lock()
sensor = Pin(18, Pin.IN, Pin.PULL_UP)
restart_flag = False

debounce_time = 200  # Tiempo de anti-rebote en ms
last_interrupt = 0

def incrementar():
    global contador, restart_flag
    while True:
        with bloqueo:
            if restart_flag:
                contador = 0
                restart_flag = False
            contador += 1
            print("Contador:", contador)
        time.sleep(0.1)

def sensor_callback(pin):
    global last_interrupt, restart_flag
    current_time = time.ticks_ms()
    if time.ticks_diff(current_time, last_interrupt) > debounce_time:  # Anti-rebote
        last_interrupt = current_time
        restart_flag = True

# Iniciar el hilo para incrementar el contador
_thread.start_new_thread(incrementar, ())

# Configurar la interrupción del sensor
sensor.irq(trigger=Pin.IRQ_FALLING, handler=sensor_callback)

# Mantener el programa en ejecución
while True:
    time.sleep(1)
