from functools import partialmethod
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from re import search
from selenium.webdriver.common.by import By


import time

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe")
#driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.flashscore.es/')


#primero vamos al dia de ayer
endirecto=driver.find_elements_by_class_name('tabs__tab')
endirecto[1].click()
time.sleep(3)
#hacer click en mas eventos para desplegar todos los partidos
endirectoTODOS=driver.find_elements_by_class_name('event__info')
for x in endirectoTODOS:
    
    if x.text == 'mostrar partidos (1)':
        print('ok')
        print('Esto esta en el bucle'+x.text)
        x.click()
    else:
        print('Esto no esta en el bucle'+x.text)

# print(clickardesplegablemostrarpartidos)
# for x in clickardesplegablemostrarpartidos:
#     x.click


# desplegartidos=driver.find_elements_by_class_name('event__info')
# for hola in desplegartidos:
#     # print(hola.text)
#     if hola.text in 'mostrar partidos (1)':
        
#         time.sleep(2)
#     else:
#         print(hola.text)
#         time.sleep(2)
# window_after = driver.window_handles[1]
# driver.switch_to_window(window_after)
time.sleep(5)
# parditosenlive=driver.find_elements_by_class_name('event__match--live')
# for x in parditosenlive:
#     x.click()

time.sleep(50)
driver.close()