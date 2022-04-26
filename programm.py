from machine import Pin, ADC
from time import sleep

sharp = ADC(Pin(34))
sharp.atten(ADC.ATTN_11DB)       #Full range: 3.3v

while True:
  sharp_value = sharp.read()
  print(sharp_value)
  sleep(0.1)