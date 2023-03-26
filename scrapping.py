
from bs4 import BeautifulSoup
import requests

url = 'https://www.lanacion.com.ar/'                    #un string para guardar la url que accederemos
response = requests.get(url)                              #el metodo que permite traer la info de la url solicitada
#  parse the html content
soup = BeautifulSoup(response.content, 'html.parser')

h2_tags = soup.find_all('h2',  class_="com-title")     #esto es un objeto de la clase Soup pero es un iterable ordenado le pido que me busque todas las etiquetas html 'h2' que ademas sean de la clase 'com-title'
print(f'se han producido {len(h2_tags)} resultados:')
#print(soup.prettify())               #muestra el codigo indentado mucho mas legible

n  = 0
# loop through each 'h2' tag and find the 'a' tag inside it
for element in h2_tags:
    element = element.find('a')
    
    if element and element.has_attr('title'):              #si existe la etiqueta (no es de tipo None) y ademas posee el atributo 'title'
        n += 1
        print(f" {n}    {element['title']} \n\n https://www.lanacion.com.ar/{element['href']}")

