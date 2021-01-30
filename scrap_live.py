from functools import partialmethod
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from re import search
from selenium.webdriver.common.by import By
import logging
from selenium.common.exceptions import NoSuchElementException

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


import time


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


    endirecto=driver.find_elements_by_class_name('tabs__tab')
    endirecto[1].click()
    time.sleep(3)
    #hacer click en mas eventos para desplegar todos los partidos
    endirectoTODOS=driver.find_elements_by_class_name('onetrust-group-container')
    # endirectoTODOS=endirectoTODOS.strip() 
    for x in endirectoTODOS:
        pepe=x.text.replace(" ", "")
        stringss='mostrarpartidos'
        if stringss in pepe:
            x.click()
        time.sleep(1)
            

    clickpartido=driver.find_elements_by_xpath("//*[contains(@id,'g_1_')]")
    time.sleep(5)


    for hola in clickpartido:
        time.sleep(4)
        hola.click()
        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        time.sleep(4)
        status=driver.find_element_by_xpath("//div[contains(@class,'info-status')]").text
        print (status)
        #saber en que liga estamos
        liga=driver.find_element_by_class_name('description__country')
        print(liga.text)
        #saber que equipos jugaron
        equipos=driver.find_elements_by_class_name('tname__text')
        print(equipos[0].text +' VS '+ equipos[1].text)
        time.sleep(1)
        try:
            estadisticas = driver.find_element_by_id('a-match-statistics')
            time.sleep(3)
            estadisticas.click()
            time.sleep(3)
            #hacerle click al primer tiempo 
            estadisticasPrimerTiempo = driver.find_element_by_id('statistics-1-statistic')
            time.sleep(1)
            estadisticasPrimerTiempo.click()
            time.sleep(3)
            eventosPrimerTiempo=driver.find_elements_by_xpath("//div[@class='statRow']/div[@class='statTextGroup']")
            time.sleep(3)
            for cozi in eventosPrimerTiempo:
                rematesapuertaprimeraparte = "Remates a puerta"
                if cozi.text in rematesapuertaprimeraparte:
                   rematesapuertaprimeraparteseparadosporocoma = cozi.text.replace("\n", ",")
                   print (rematesapuertaprimeraparteseparadosporocoma)
                #    print('Remates a puerta HT Local:'+separacionRemates[0])
                #    print('Remates a puerta HT Visitante:'+separacionRemates[2])
                else:
                    print ('no')
                update.message.reply_text(cozi)
                driver.close()
                driver.switch_to_window(window_before)
            
            
            
            #hay que recorrer todas las estadisticas para obtener tiros a puerta y ataques peligrosos
            # bucledeinfoprimeraparte=driver.find_elements_by_xpath("//div[@class='statTextGroup']")
            
            # for x in bucledeinfoprimeraparte1:
            #     print (x.text)
            #     rematesapuertaprimeraparte = "Remates a puerta"
            #     ataquespeligrososprimeraparte = "Ataques peligrosos"
            #     if rematesapuertaprimeraparte in x.text:
            #             rematesapuertaprimeraparteseparadosporocoma = x.text.replace("\n", ",")
            #             separacionRemates = rematesapuertaprimeraparteseparadosporocoma.split(",")
            #             print('Remates a puerta HT Local:'+separacionRemates[0])
            #             print('Remates a puerta HT Visitante:'+separacionRemates[2])
            #     if ataquespeligrososprimeraparte in x.text :
            #             ataquespeligrososparteseparadosporocoma = x.text.replace("\n", ",")
            #             separacionAtaquesPeligrosos = ataquespeligrososparteseparadosporocoma.split(",")
            #             print('Ataques peligrosos HT Local:'+separacionAtaquesPeligrosos[0])
            #             print('Ataques peligrosos HT Visitante:'+separacionAtaquesPeligrosos[2])
            #     update.message.reply_text(f'<b>📃Liga: </b>'+liga.text+'\n'+'<b>⚽ Partido: </b>'+ equipos[0].text +' VS '+ equipos[1].text + '\n'+
            #     '<b>Hora ⌚</b>'+status+'\n'+
            #     '-------------- \n'+
            #     '<b>Remates a puerta HT Local: </b>'+ separacionRemates[0]+'\n'+
            #     '<b>Remates a puerta HT Visitante: </b>'+ separacionRemates[2]+'\n'+
            #     '<b>Ataques Peligrosos HT Local: </b>'+ separacionAtaquesPeligrosos[0]+'\n'+
            #     '<b>Ataques Peligrosos HT Visitante: </b>'+ separacionAtaquesPeligrosos[2]+'\n'
            #     ,parse_mode='HTML')   
            

        except:
            print('Este partido no tiene stats en directo')
            update.message.reply_text('no tiene')
            driver.close()
            driver.switch_to_window(window_before)
            time.sleep(3)
       
    time.sleep(5)
    #•hasta aquí he desplegado todos los partidos IN LIVE
    time.sleep(1)

    
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


#click partido
# pepe=driver.find_element_by_class_name('event__info')
# pepe.click()
# try:
#   # Tries to click an element
#     driver.find_element_by_class_name('event__scores').click()
# except ElementClickInterceptedException:
#   # If pop-up overlay appears, click the X button to close
#   time.sleep(2) # Sometimes the pop-up takes time to load
#   driver.find_element_by_css_selector("close event__scores").click()
# # time.sleep(5)


# clickpartido=driver.find_element_by_xpath("//div[@class='event__match--oneLine']")
# clickpartido.click()

time.sleep(50)
driver.close()