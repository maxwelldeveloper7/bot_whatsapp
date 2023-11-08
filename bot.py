from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Inicialize o driver do Chrome
browser = webdriver.Firefox()

# Abra o WhatsApp Web
browser.get("https://web.whatsapp.com/")

# Aguarde até que o usuário escaneie o código QR manualmente
input("Após escanear o código QR, pressione Enter para continuar...")

# Lista de números de telefone ou contatos
contacts = ["+553388117010"]

# Mensagem a ser enviada
message = "Sua mensagem em massa aqui."

# Loop para enviar mensagens para cada contato
for contact in contacts:
    browser.get("https://web.whatsapp.com/send?phone=" + contact)
    time.sleep(2)
    message_box = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

# Feche o navegador do WhatsApp Web
browser.quit()
