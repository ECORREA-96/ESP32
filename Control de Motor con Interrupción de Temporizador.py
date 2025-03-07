from machine import Pin, Timer

motor = Pin(16, Pin.OUT)  


ciclo_trabajo = 50 ##(50%)
contador = 0  


def generar_pwm(t):
    global contador
    if contador < ciclo_trabajo:
        motor.value(1)  
    else:
        motor.value(0) 
    
    contador += 1
    if contador >= 100:  # Reinicio del ciclo cada 100 interrupciones (100 * 10 ms = 1000 ms)
        contador = 0  

# Configuración del temporizador en modo periódico
temporizador = Timer(0)
temporizador.init(period=5, mode=Timer.PERIODIC, callback=generar_pwm)
