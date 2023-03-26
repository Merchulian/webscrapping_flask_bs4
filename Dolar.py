from bs4 import BeautifulSoup
import requests
def cotizacion_dolar_hoy():
    url = 'https://dolarhoy.com/'                    #un string para guardar la url que accederemos
    response = requests.get(url)                              #el metodo que permite traer la info de la url solicitada
    #  parse the html content
    soup = BeautifulSoup(response.content, 'html.parser')


    ''' un ejemplo de pagina hecha medio para la miercole. dificil de scrappear. las tags son todas genericas de bootstrap entonces conviene ir trayendo la info y ver como la vamos filtrando por ejemplo la seccion que nos interesa que es una caja con la cotizacion para la compra y venta de dolares oficial, contado con liqui, solidario etc esta en una etiqueta div:
                            <div class='tile is-parent is-7 is-vertical'>
    como tantas otras. Lo que sabemos de esta caja en particular es que adentro tiene otras etiquetas. adentro tiene 2 hijos que nos pueden interesar:

    <a href="/cotizaciondolaroficial">   (aca solo pongo los atrributos de la tag que nos interesan)
    <div class='values'>
        <div class='compra'>
            <div class='val'>...</div>   <===========  A ESTA ETIQUETA TENEMOS QUE LLEGAR
        <div class='venta'>
            <div class='val'>...</div>    <============= A ESTA ETIQUETA TENEMOS QUE LLEGAR

    NOS INTERESA SCRAPPEAR:

    una <div> cuya clase sea "tile is-parent is-7 is-vertical"
    y de alli:

    (1) el href de la etiqueta <a> hija lo podemos usar para saber a que cotizacion se refiere (oficial bolsa etc)
    (2) scrappear la tag hermana de (1):  una <div> de clase 'values'
    (3) adentro de (2) scrapear el contenido de las cajas hijas <div> de class='compra' y class='venta'

    '''

    for element in soup.find_all('div', class_='tile is-child'):
        if element.find('a', href="/cotizaciondolaroficial"):
            compra_oficial = element.find('div', class_="compra").text
            venta_oficial =  element.find('div', class_="venta").text

        if element.find('a', href="/cotizaciondolarbolsa"):
            compra_bolsa = element.find('div', class_="compra").text
            venta_bolsa =  element.find('div', class_="venta").text
        
        if element.find('a', href="/cotizaciondolarcontadoconliqui"):
            compra_conliqui = element.find('div', class_="compra").text
            venta_conliqui =  element.find('div', class_="venta").text

        if element.find('a', href="/cotizaciondolarturista"):
            compra_turista = element.find('div', class_="compra").text
            venta_turista =  element.find('div', class_="venta").text

#    print(f"OFICIAL {compra_oficial}   ||   {venta_oficial}")
#    print(f"BOLSA: {compra_bolsa}   ||   {venta_bolsa}")
#    print(f"CONTADO CON LIQUI: {compra_conliqui}   ||   {venta_conliqui}")
#    print(f"TURISTA: {compra_turista}   ||   {venta_turista}")
    return {'compra_oficial':compra_oficial,"venta_oficial":venta_oficial,"compra_bolsa":compra_bolsa,"venta_bolsa":venta_bolsa,"compra_conliqui":compra_conliqui,"venta_conliqui":venta_conliqui,"compra_turista":compra_turista,"venta_turista":venta_turista}

print(cotizacion_dolar_hoy())