from machine import Pin, PWM    
import time               #importar librerias

servo = PWM(Pin(15))      #Seleccionamos el pin 15 para la señal PWM del Servo
servo.freq(50)            #Seleccionamos la frecuencia del servo 
ldr = machine.ADC(26)     #Seleccionamos el pin 26 ADC "pin analógico"
led = Pin(25,Pin.OUT)     #Seleccionamos el LED de la placa Pi Pico que corresponde al pin 25

while True:               #Se utiliza para especificar un bucle infinito 
    
     valor = ldr.read_u16()        # La variable "valor" es igual al voltaje lee, con una precisión de 16 bits
     print("Valor LDR: " , valor)  # Imprimimos las variables, en este caso es "valor"
     
     time.sleep(0)                 #Tiempo de espera
      
     if valor > 65000:             #Si "valor" es mayor a 65000 deberá alzar el brazo
         led.low()                 #Apago LED
         servo.duty_u16(4500)      #Gira brazo del servo 80°
         
     else:                         #Si no cumlple con valores mayores 65000
         led.high()                #Enciende LED
         servo.duty_u16(3000)      #Gira brazo del servo 40°
        
        