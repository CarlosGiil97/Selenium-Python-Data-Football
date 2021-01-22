import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By


import time

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe")
#driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.flashscore.es/')
window_before = driver.window_handles[0]

#primero vamos al dia de ayer
ayer=driver.find_element_by_class_name('calendar__direction--yesterday')
ayer.click()
time.sleep(5)
pepe=driver.find_element_by_class_name('event__scores')
pepe.click()
time.sleep(5)
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
time.sleep(5)
#saber si en el primer tiempo hubo goles
golesPrimerTiempoLocal = driver.find_element_by_class_name('p1_home')
golesPrimerTiempoVisitante = driver.find_element_by_class_name('p1_away')
print('Resultado primera parte:'+golesPrimerTiempoLocal+'-'+golesPrimerTiempoVisitante)
print(golesPrimerTiempoLocal.text)
estadisticas = driver.find_element_by_id('a-match-statistics')
estadisticas.click()
time.sleep(5)

#hacerle click al primer tiempo 
estadisticasPrimerTiempo = driver.find_element_by_id('statistics-1-statistic')
estadisticasPrimerTiempo.click()
time.sleep(50)
driver.close()