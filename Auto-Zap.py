from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Navergar Whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)

# Definir Contatos e Mensagem a ser Enviadas
contatos = ['Claudyany Estacio', 'Paulo Estacio T. I']
mensagem = 'Teste do AutoZap T.I da Estacio-FAL realizando com sucesso. by Alexandre Melo ;)'

# Buscar contatos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    
# Enviar mensagem    
def enviar_mensagem(mensagem):
    enviar_mensagem = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    enviar_mensagem[1].click()
    enviar_mensagem[1].send_keys(mensagem)
    enviar_mensagem[1].send_keys(Keys.ENTER)
    
# Funoções
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
