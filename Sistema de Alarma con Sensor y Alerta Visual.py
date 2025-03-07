# LED verde pin 25, led amarrillo pin 32, pulsador pin 15
from machine import Pin, Timer
led = Pin(25, Pin.OUT)
pulsador = Pin(15, Pin.IN, Pin.PULL_UP)

alerta_activa = False

timer_parpadeo = Timer(0)
timer_duracion = Timer(1)

def pulsador_callback(pin):
    global alerta_activa
    if not alerta_activa:
        alerta_activa = True
        iniciar_parpadeo()  
         
def iniciar_parpadeo():
    timer_parpadeo.init(period=100, mode=Timer.PERIODIC, callback=lambda t: led.value(not led.value()))
    timer_duracion.init(period=5000, mode=Timer.ONE_SHOT, callback=detener_parpadeo)
    
def detener_parpadeo(timer):
    global alerta_activa
    alerta_activa = False
    timer_parpadeo.deinit() 
    led.off()  
    
    
    
pulsador.irq(trigger=Pin.IRQ_FALLING, handler=pulsador_callback)

while True:
    
    pass
