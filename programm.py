
# Sharp GP2Y0A21 Infrarot Entfernungsmesser
# Matthias Grafe
# 29.04.22
# Quelle: https://microcontrollerslab.com/esp32-esp8266-adc-micropython-measure-analog-readings/

from machine import Pin, ADC       #Klasse PIN und ADC importieren
from time import sleep             #Klasse sleep importieren

infrarot = ADC(Pin(37))            #Objekt Infrarot
infrarot.atten(ADC.ATTN_6DB)      #3.3V Spannungsbereich
infrarot.width(ADC.WIDTH_10BIT)   # Wert werden nur im Bereich zwischen 0-1023 ausgegeben


while True:
 infrarot_value = infrarot.read()   # Analog Pin auslesen
 print(infrarot_value)              # Wert vom Sensor ausgeben
 sleep(0.25)