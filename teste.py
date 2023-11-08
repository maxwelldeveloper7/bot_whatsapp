from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Firefox()

navegador.get('https://web.whatsapp.com/')

while len(navegador.find_element(By.TAG_NAME, '<canva>')) < 1:
    pass