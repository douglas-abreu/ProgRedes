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

URL='https://www.futebolinterior.com.br/futebol/Brasileiro/Serie-A/2020/classificacao' #passando a URL

browser.get(URL) #fazendo nosso objeto browser receber a URL passada

wait=WebDriverWait(browser,4) #espera por 4 segundos para garantir que a pag carregue.

soup=BeautifulSoup(browser.page_source,'html.parser') #puxando a fonte da página do browser e dizendo que a fonte é um HTML
#aqui iniciamos o scraping
tabela_classificacao=soup.find(id='tbody_classificacao') #buscando uma ocorrencia pelo identificador da tabela com o métodod find

linhas=tabela_classificacao.find_all("tr",class_="linha-class") #buscando todas as tags "tr" que possuam a class "linha-class"
times=[]
pontos_ganhos=[]
jogos=[]
vitorias=[]
empates=[]
derrotas=[]
gols_pro=[]
gols_sofridos=[]
for linha in linhas:
    times.append(linha.find(class_='coluna-participante').text)
    pontos_ganhos.append(int(linha.find(class_='coluna-pg').text))
    jogos.append(int(linha.find(class_='coluna-j').text))
    vitorias.append(int(linha.find(class_='coluna-v').text))
    empates.append(int(linha.find(class_='coluna-e').text))
    derrotas.append(int(linha.find(class_='coluna-d').text))
    gols_pro.append(int(linha.find(class_='coluna-gp').text))
    gols_sofridos.append(int(linha.find(class_='coluna-gc').text))

dados={
    'time':times,
    'pontos_ganhos':pontos_ganhos,
    'jogos':jogos,
    'vitorias':vitorias,
    'empates':empates,
    'derrotas':derrotas,
    'gols_pro':gols_pro,
    'gols_sofridos':gols_sofridos
}
#print(derrotas,vitorias,empates)...
data_frame=pd.DataFrame(dados)


data_frame['saldo_gols']=data_frame['gols_pro']-data_frame['gols_sofridos']

cabecalho=['Clube','Pontos Ganhos','Jogos','Vitórias','Empates','Derrotas','Gols-Pró','Gols Sofridos','Saldo de Gols']

print(tabulate(data_frame,headers=cabecalho,tablefmt='github'))

browser.quit()
