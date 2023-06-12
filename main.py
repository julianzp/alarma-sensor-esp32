from config import utelegram_config
from config import wifi_config
from machine import Pin

import time
import utelegram
import network
import utime

buzzer = Pin(13, Pin.OUT)
pir = Pin(22, Pin.IN, Pin.PULL_DOWN)

debug = True

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()
sta_if.connect(wifi_config['ssid'], wifi_config['password'])

if debug: print('WAITING FOR NETWORK - sleep 20')
utime.sleep(20)

if sta_if.isconnected():
    bot = utelegram.ubot(utelegram_config['token'])

    print('BOT LISTENING')
    bot.listen()

    #ENVIAR el mensaje al Bot de Telegram Configurado, cuando detecta un MOVIMIENTO
    while True:
    if pir.value() ==1:
        print("Movimiento detectado")
        bot.send(message['message']['chat']['id'], 'Movimiento Detectado')
        buzzer.value(1)
        time.sleep(3)

    else:
        print("Sin movimiento")
        buzzer.value(0)
        time.sleep(1)


else:
    print('NOT CONNECTED - aborting')
