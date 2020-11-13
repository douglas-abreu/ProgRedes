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
partidas=[]
empates=[]
gols_pro=[]
dif_gols=[]

indexMenosPartidas=[]
indexMaisGols=[]
indexMaisPartidasEmpatadas=[]
indexMaisSaldo=[]

colunasImportantes = [3, 5, 7, 9]
for linha in linhas:
    if linha.has_attr('data-filtered-table-row-name'): #se a tag tr tiver o atributo, entra no if
        colunas=linha.find_all("td") # de cada linha, busque as colunas
        colunaTime=colunas[2].find("span", class_="long")
        if(colunaTime): # se o type for noneType retorna false
            times.append(colunaTime.text)
            partidas.append(colunas[3].text.strip())    
            empates.append(colunas[5].text.strip())    
            gols_pro.append(colunas[7].text.strip())    
            dif_gols.append(colunas[9].text.strip())
browser.quit()

def maisGols():
    results = list(map(int, gols_pro))
    maxGols = max(results)
    for i in range(len(results)-1):
        if(results[i] is maxGols):
            indexMaisGols.append(i)
    print("-------Times com mais gols-------")            
    for r in range(len(indexMaisGols)):
        print("{} com {} gols".format(times[indexMaisGols[r]],maxGols))
    print("---------------------------------\n")
    
def maisEmpatou():
    results = list(map(int, empates))
    maxPartida = max(results)
    for i in range(len(results)-1):
        if(results[i] is maxPartida):
            indexMaisPartidasEmpatadas.append(i)
    print("-------Times com mais partidas empatadas-------")            
    for r in range(len(indexMenosPartidas)):
        print("{} com {} partidas empatadas".format(times[indexMaisPartidasEmpatadas[r]],maxPartida))
    print("---------------------------------\n")   

def menosPartidas():
    results = list(map(int, partidas))
    minPartida = min(results)
    for i in range(len(results)-1):
        if(results[i] is minPartida):
            indexMenosPartidas.append(i)
    print("-------Times com menos partidas-------")            
    for r in range(len(indexMenosPartidas)):
        print("{} com {} partidas".format(times[indexMenosPartidas[r]],minPartida))
    print("---------------------------------\n")
    
def saldoMaisPositivo():
    results = list(map(int, dif_gols))
    maxSaldo = max(results)
    for i in range(len(results)-1):
        if(results[i] is maxSaldo):
            indexMaisSaldo.append(i)
    print("-------Times com saldo mais positivo-------")            
    for r in range(len(indexMaisSaldo)):
        print("{} com +{} de saldo ".format(times[indexMaisSaldo[r]],maxSaldo))
    print("---------------------------------\n")
    

    
maisGols()
menosPartidas()
maisEmpatou()
saldoMaisPositivo()