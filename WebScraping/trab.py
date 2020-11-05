# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
chrome_options=Options()
chrome_options.add_argument('--headless') #não abra a janela, e sim como um processo.
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')

browser=Chrome(options=chrome_options) #criando objeto da classe chrome para usar o navegador como interpretador

URL='https://www.premierleague.com/tables' #passando a URL

browser.get(URL) #fazendo nosso objeto browser receber a URL passada

wait=WebDriverWait(browser,4) #espera por 4 segundos para garantir que a pag carregue.

soup=BeautifulSoup(browser.page_source,'html.parser') #puxando a fonte da página do browser e dizendo que a fonte é um HTML
#--------------aqui iniciamos o scraping----------------


linhas=soup.find_all("tr") #buscando todas as tags "tr"
times=[]
pontos_ganhos=[]
jogos=[]
vitorias=[]
empates=[]
derrotas=[]
gols_pro=[]
gols_sofridos=[]
for linha in linhas:
    if linha.has_attr('data-filtered-table-row-name'):
        colunas=linha.find_all("td")
        # 2 3 4 5 6 9 10 
        colunaTime=colunas[2].find("span", class_="long")
        if(colunaTime): # se o type for noneType retorna false
            print(colunaTime.text)
browser.quit()
