import pandas as pd
import math
import re
from bs4 import BeautifulSoup
import requests



headers = {'User=Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}


pesquisa = input('o que deseja pesquisar? ')



url = f'https://www.kabum.com.br/busca/{pesquisa.replace(" ","-")}'



pagina = requests.get(url,headers=headers)


print(pagina)


pagina_html = BeautifulSoup(pagina.content,'html.parser')


qts_produtos = int(pagina_html.find('div', id = 'listingCount').text.split(' ')[0])

print(f'QUANTIDADE DE PRODUTOS : {qts_produtos}')


dict_pesquisa= {
    'Nome':[],
    'preco':[],
    'Links':[]
}


cont = 0 


for i in range(1,math.ceil(qts_produtos/20)+1):
   
    url = f'https://www.kabum.com.br/busca/{pesquisa.replace(" ","-")}?page_number={i}&page_size=20&facet_filters=&sort=most_searched&variant=catalog'
    pagina = requests.get(url,headers)
    pagina_html = BeautifulSoup(pagina.content,'html.parser')
    produtos = pagina_html.find_all('article',class_= re.compile('productCard'))

    for produto in produtos :
        nome = produto.find('span',class_=re.compile('nameCard')).text
        
        href = produto.find('a',href= re.compile("/produto/"))
        link = f'https://www.kabum.com.br/{href.get("href")}'
        cont+=1
        try:
            pagina = requests.get(link,headers)
            pagina_html = BeautifulSoup(pagina.content,'html.parser')
            preco = pagina_html.find('h4',class_=re.compile('finalPrice')).text
            
            preco = float(preco.split()[1].replace('.','').replace(',','.'))
            
            dict_pesquisa['preco'].append(preco)
        except:
            print('falhou')
            dict_pesquisa['preco'].append(None)   

        dict_pesquisa['Nome'].append(nome)
        
        dict_pesquisa['Links'].append(link)
        print(f'RESTA {qts_produtos-cont} PRODUTOS')





df = pd.DataFrame(dict_pesquisa)


df.to_excel(f'{pesquisa.strip()}.xlsx',index=False)

print('FINALIZADO')