import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/amanha/cidade/377/florianopolis-sc')

soup = BeautifulSoup(html.text, 'html.parser')

temp_min = soup.find(id='min-temp-1')
print(f'A temperatura mínima é: {temp_min.text}')

temp_max = soup.find(id='max-temp-1')
print(f'A temperatura máxima é: {temp_max.text}')

resumo = soup.find(class_='-gray -line-height-24 _center')
print(f'Resumo: {resumo.text}')