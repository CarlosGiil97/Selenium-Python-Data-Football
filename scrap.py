import json
from string import printable
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from termcolor import colored

import time





#-------------------------------------------------------------------------
# driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe")
# #driver = webdriver.Chrome("chromedriver.exe")
# driver.get('https://www.flashscore.es/')
# window_before = driver.window_handles[0]

# #primero vamos al dia de ayer
# ayer=driver.find_element_by_class_name('calendar__direction--yesterday')
# ayer.click()
# time.sleep(1)
# pepe=driver.find_element_by_class_name('event__scores')
# pepe.click()
# time.sleep(1)
# window_after = driver.window_handles[1]
# #cambio de ventana y le hago click a estadisticas
# driver.switch_to_window(window_after)
# #saber en que liga estamos
# liga=driver.find_element_by_class_name('description__country')
# print('Partido de la liga'+liga.text)
# #fecha en la que se jugó
# fecha=driver.find_element_by_class_name('description__time')
# print(fecha.text)
# #saber que equipos jugaron
# equipos=driver.find_elements_by_class_name('tname__text')
# print('Partido entre'+ equipos[0].text +' VS '+ equipos[1].text)
# time.sleep(1)
# #saber si en el primer tiempo hubo goles
# global golesPrimerTiempoLocal
# golesPrimerTiempoLocal = driver.find_element_by_class_name('p1_home').text
# golesPrimerTiempoLocal=int(golesPrimerTiempoLocal)
# golesPrimerTiempoVisitante = driver.find_element_by_class_name('p1_away').text
# golesPrimerTiempoVisitante=int(golesPrimerTiempoVisitante)
# # print(type(golesPrimerTiempoLocal))
# # print(f'Resultado primera parte:{golesPrimerTiempoLocal} - {golesPrimerTiempoVisitante}')
# print(f"Resultado primera parte: {golesPrimerTiempoLocal} - {golesPrimerTiempoVisitante}")
# time.sleep(1)
# if golesPrimerTiempoLocal>0 or golesPrimerTiempoVisitante>0:
#     # print ("hubo goles en la primera parte")
#     # golestotalesHT=int(golesPrimerTiempoLocal.text)+int(golesPrimerTiempoVisitante.text)
#     # if golestotalesHT == 1:
#     #   saberminPrimergol = driver.find_element_by_class_name('time-box')
#     #   print('Gol en el min'+saberminPrimergol.text)
#     # else:
#     #     saberminPrimergol = driver.find_elements_by_class_name('time-box')
#     estadisticas = driver.find_element_by_id('a-match-statistics')
#     estadisticas.click()
#     time.sleep(1)
#     #hacerle click al primer tiempo 
#     estadisticasPrimerTiempo = driver.find_element_by_id('statistics-1-statistic')
#     estadisticasPrimerTiempo.click()
#     time.sleep(1)
#     #hay que recorrer todas las estadisticas para obtener tiros a puerta y ataques peligrosos
#     bucledeinfoprimeraparte=driver.find_elements_by_xpath("//div[@class='statTextGroup']")
#     bucledeinfoprimeraparte1= driver.find_elements_by_xpath("//div[@class='statRow']/div[@class='statTextGroup']")
#     for x in bucledeinfoprimeraparte1:
#         rematesapuertaprimeraparte = "Remates a puerta"
#         ataquespeligrososprimeraparte = "Ataques peligrosos"
#         if rematesapuertaprimeraparte in x.text:
#             rematesapuertaprimeraparteseparadosporocoma = x.text.replace("\n", ",")
#             separacionRemates = rematesapuertaprimeraparteseparadosporocoma.split(",")
#             print('Remates a puerta HT Local:'+separacionRemates[0])
#             print('Remates a puerta HT Visitante:'+separacionRemates[2])
#         if ataquespeligrososprimeraparte in x.text :
#             ataquespeligrososparteseparadosporocoma = x.text.replace("\n", ",")
#             separacionAtaquesPeligrosos = ataquespeligrososparteseparadosporocoma.split(",")
#             print('Ataques peligrosos HT Local:'+separacionAtaquesPeligrosos[0])
#             print('Ataques peligrosos HT Visitante:'+separacionAtaquesPeligrosos[2])
# else:
#     print ("No Hubo goles en el primer tiempo")
# time.sleep(1)
# #---------pasamos al segundo tiempo--------
# #hacerle click al primer tiempo 
# vueltaAtrasPartido = driver.find_element_by_id('a-match-timeline')
# vueltaAtrasPartido.click()
# time.sleep(1)
# golesSegundoTiempoLocal = driver.find_element_by_class_name('p2_home').text
# golesSegundoTiempoLocal=int(golesSegundoTiempoLocal)
# golesSegundoTiempoVisitante = driver.find_element_by_class_name('p2_away').text
# golesSegundoTiempoVisitante=int(golesSegundoTiempoVisitante)
# print(f"Resultado segunda parte: {golesSegundoTiempoLocal} - {golesSegundoTiempoVisitante}")
# time.sleep(1)
# if golesSegundoTiempoLocal>0 or golesSegundoTiempoVisitante>0:
#     estadisticas = driver.find_element_by_id('a-match-statistics')
#     estadisticas.click()
#     time.sleep(1)
#     #hacerle click al segundo tiempo 
#     estadisticasPrimerTiempo = driver.find_element_by_id('statistics-2-statistic')
#     estadisticasPrimerTiempo.click()
#     time.sleep(1)
#     #hay que recorrer todas las estadisticas para obtener tiros a puerta y ataques peligrosos de la segunda parte
#     bucledeinfosegundaparte=driver.find_elements_by_xpath("//div[@class='statTextGroup']")
#     bucledeinfosegundaparte1= driver.find_elements_by_xpath("//div[@class='statRow']/div[@class='statTextGroup']")
#     for x in bucledeinfosegundaparte1:
#         rematesapuertaSegundaparte = "Remates a puerta"
#         ataquespeligrososSegundaparte = "Ataques peligrosos"
#         if rematesapuertaSegundaparte in x.text:
#             rematesapuertaSegundaparteseparadosporocoma = x.text.replace("\n", ",")
#             separacionRematesSegunda = rematesapuertaSegundaparteseparadosporocoma.split(",")
#             print('Remates a puerta ST Local:'+separacionRematesSegunda[0])

#             print('Remates a puerta ST Visitante:'+separacionRematesSegunda[2])
#         if ataquespeligrososSegundaparte in x.text :
#             ataquespeligrososSegundaparteseparadosporocoma = x.text.replace("\n", ",")
#             separacionAtaquesPeligrososSegunda = ataquespeligrososSegundaparteseparadosporocoma.split(",")
#             print('Ataques peligrosos ST Local:'+separacionAtaquesPeligrososSegunda[0])
#             print('Ataques peligrosos ST Visitante:'+separacionAtaquesPeligrososSegunda[2])
# else:
#     print("No hubo goles en el segundo tiempo")

# golesTotalesLocal=golesPrimerTiempoLocal+golesSegundoTiempoLocal
# golesTotalesVisitante=golesPrimerTiempoVisitante+golesSegundoTiempoVisitante
# print('Resultado Final:'+str(golesTotalesLocal)+'-'+str(golesTotalesVisitante))


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def start(update, context):
    """Send a message when the command /start is issued."""
    driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe")
    #driver = webdriver.Chrome("chromedriver.exe")
    driver.get('https://www.flashscore.es/')
    window_before = driver.window_handles[0]

    #primero vamos al dia de ayer
    ayer=driver.find_element_by_class_name('calendar__direction--yesterday')
    ayer.click()
    time.sleep(1)
    pepe=driver.find_element_by_class_name('event__scores')
    pepe.click()
    time.sleep(1)
    window_after = driver.window_handles[1]
#cambio de ventana y le hago click a estadisticas
    driver.switch_to_window(window_after)
#saber en que liga estamos
    liga=driver.find_element_by_class_name('description__country')
    print('Partido de la liga'+liga.text)
#fecha en la que se jugó
    fecha=driver.find_element_by_class_name('description__time')
    print(fecha.text)
#saber que equipos jugaron
    equipos=driver.find_elements_by_class_name('tname__text')
    print('Partido entre'+ equipos[0].text +' VS '+ equipos[1].text)
    time.sleep(1)
#saber si en el primer tiempo hubo goles
    global golesPrimerTiempoLocal
    golesPrimerTiempoLocal = driver.find_element_by_class_name('p1_home').text
    golesPrimerTiempoLocal=int(golesPrimerTiempoLocal)
    golesPrimerTiempoVisitante = driver.find_element_by_class_name('p1_away').text
    golesPrimerTiempoVisitante=int(golesPrimerTiempoVisitante)
# print(type(golesPrimerTiempoLocal))
# print(f'Resultado primera parte:{golesPrimerTiempoLocal} - {golesPrimerTiempoVisitante}')
    print(f"Resultado primera parte: {golesPrimerTiempoLocal} - {golesPrimerTiempoVisitante}")
    time.sleep(1)
    if golesPrimerTiempoLocal>0 or golesPrimerTiempoVisitante>0:
    # print ("hubo goles en la primera parte")
    # golestotalesHT=int(golesPrimerTiempoLocal.text)+int(golesPrimerTiempoVisitante.text)
    # if golestotalesHT == 1:
    #   saberminPrimergol = driver.find_element_by_class_name('time-box')
    #   print('Gol en el min'+saberminPrimergol.text)
    # else:
    #     saberminPrimergol = driver.find_elements_by_class_name('time-box')
        estadisticas = driver.find_element_by_id('a-match-statistics')
        estadisticas.click()
        time.sleep(1)
    #hacerle click al primer tiempo 
        estadisticasPrimerTiempo = driver.find_element_by_id('statistics-1-statistic')
        estadisticasPrimerTiempo.click()
        time.sleep(1)
    #hay que recorrer todas las estadisticas para obtener tiros a puerta y ataques peligrosos
        bucledeinfoprimeraparte=driver.find_elements_by_xpath("//div[@class='statTextGroup']")
        bucledeinfoprimeraparte1= driver.find_elements_by_xpath("//div[@class='statRow']/div[@class='statTextGroup']")
        for x in bucledeinfoprimeraparte1:
            rematesapuertaprimeraparte = "Remates a puerta"
            ataquespeligrososprimeraparte = "Ataques peligrosos"
            if rematesapuertaprimeraparte in x.text:
                rematesapuertaprimeraparteseparadosporocoma = x.text.replace("\n", ",")
                separacionRemates = rematesapuertaprimeraparteseparadosporocoma.split(",")
                print('Remates a puerta HT Local:'+separacionRemates[0])
                print('Remates a puerta HT Visitante:'+separacionRemates[2])
            if ataquespeligrososprimeraparte in x.text :
                ataquespeligrososparteseparadosporocoma = x.text.replace("\n", ",")
                separacionAtaquesPeligrosos = ataquespeligrososparteseparadosporocoma.split(",")
                print('Ataques peligrosos HT Local:'+separacionAtaquesPeligrosos[0])
                print('Ataques peligrosos HT Visitante:'+separacionAtaquesPeligrosos[2])
    else:
        print ("No Hubo goles en el primer tiempo")
        update.message.reply_text("No hubo goles en el primer tiempo")
    time.sleep(1)
#---------pasamos al segundo tiempo--------
#hacerle click al primer tiempo 
    vueltaAtrasPartido = driver.find_element_by_id('a-match-timeline')
    vueltaAtrasPartido.click()
    time.sleep(1)
    golesSegundoTiempoLocal = driver.find_element_by_class_name('p2_home').text
    golesSegundoTiempoLocal=int(golesSegundoTiempoLocal)
    golesSegundoTiempoVisitante = driver.find_element_by_class_name('p2_away').text
    golesSegundoTiempoVisitante=int(golesSegundoTiempoVisitante)
    print(f"Resultado segunda parte: {golesSegundoTiempoLocal} - {golesSegundoTiempoVisitante}")
    time.sleep(1)
    if golesSegundoTiempoLocal>0 or golesSegundoTiempoVisitante>0:
        estadisticas = driver.find_element_by_id('a-match-statistics')
        estadisticas.click()
        time.sleep(1)
    #hacerle click al segundo tiempo 
        estadisticasPrimerTiempo = driver.find_element_by_id('statistics-2-statistic')
        estadisticasPrimerTiempo.click()
        time.sleep(1)
    #hay que recorrer todas las estadisticas para obtener tiros a puerta y ataques peligrosos de la segunda parte
        bucledeinfosegundaparte=driver.find_elements_by_xpath("//div[@class='statTextGroup']")
        bucledeinfosegundaparte1= driver.find_elements_by_xpath("//div[@class='statRow']/div[@class='statTextGroup']")
        for x in bucledeinfosegundaparte1:
            rematesapuertaSegundaparte = "Remates a puerta"
            ataquespeligrososSegundaparte = "Ataques peligrosos"
            if rematesapuertaSegundaparte in x.text:
                rematesapuertaSegundaparteseparadosporocoma = x.text.replace("\n", ",")
                separacionRematesSegunda = rematesapuertaSegundaparteseparadosporocoma.split(",")
                print('Remates a puerta ST Local:'+separacionRematesSegunda[0])

                print('Remates a puerta ST Visitante:'+separacionRematesSegunda[2])
            if ataquespeligrososSegundaparte in x.text :
                ataquespeligrososSegundaparteseparadosporocoma = x.text.replace("\n", ",")
                separacionAtaquesPeligrososSegunda = ataquespeligrososSegundaparteseparadosporocoma.split(",")
                print('Ataques peligrosos ST Local:'+separacionAtaquesPeligrososSegunda[0])
                print('Ataques peligrosos ST Visitante:'+separacionAtaquesPeligrososSegunda[2])
    else:
        print("No hubo goles en el segundo tiempo")
        update.message.reply_text("No hubo goles en el segundo tiempo")

    golesTotalesLocal=golesPrimerTiempoLocal+golesSegundoTiempoLocal
    golesTotalesVisitante=golesPrimerTiempoVisitante+golesSegundoTiempoVisitante
    print('Resultado Final:'+str(golesTotalesLocal)+'-'+str(golesTotalesVisitante))
    update.message.reply_text(f'<b>📃Liga: </b>'+liga.text+'\n'+'<b>🗓 Fecha: </b>'+fecha.text+'\n'+'<b>⚽ Partido: </b>'+ equipos[0].text +' VS '+ equipos[1].text + '\n'+
    '-------------- \n'+
    '<b>Resultado HT: </b>'+str(golesPrimerTiempoLocal)+'-'+ str(golesPrimerTiempoVisitante)+'\n'+
    '<b>Remates a puerta HT Local: </b>'+ separacionRemates[0]+'\n'+
    '<b>Remates a puerta HT Visitante: </b>'+ separacionRemates[2]+'\n'+
    '<b>Ataques Peligrosos HT Local: </b>'+ separacionAtaquesPeligrosos[0]+'\n'+
    '<b>Ataques Peligrosos HT Visitante: </b>'+ separacionAtaquesPeligrosos[2]+'\n'+
    '-------------- \n'+
    '<b>Resultado ST: </b>'+str(golesSegundoTiempoLocal)+'-'+ str(golesSegundoTiempoVisitante)+'\n'+
    '<b>Remates a puerta ST Local: </b>'+ separacionRematesSegunda[0]+'\n'+
    '<b>Remates a puerta ST Visitante: </b>'+ separacionRematesSegunda[2]+'\n'+
    '<b>Ataques Peligrosos ST Local: </b>'+ separacionAtaquesPeligrososSegunda[0]+'\n'+
    '<b>Ataques Peligrosos ST Visitante: </b>'+ separacionAtaquesPeligrososSegunda[2]+'\n'+
    '-------------- \n'+
    '<b>RESULTADO FINAL:</b>'+str(golesTotalesLocal)+'-'+str(golesTotalesVisitante)
    ,parse_mode='HTML')
    
def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1522299509:AAGOjxGZhgISADz0-4-4vnBGy_aFkpxuY1U", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()