import imaginador
import crawlerv2

import requests
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
import urllib.request
import time



def main():

	card_name =  "Ganso" #input("Digite o nome da Carta: ")
	url = input("Digite a URL da carta: ")
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page.read(), 'html.parser')


	html_extract = crawlerv2.crawler(soup)
	css_extract =  crawlerv2.css_style_crawler(soup)
	crawlerv2.css_html_match(html_extract, css_extract)
	previous_img_link = False

	for row in html_extract:
		if type(row['crypto_values']) == float:
			valor_com_ponto = row['crypto_values']
		elif len(row['crypto_values']) == 0:
			valor_com_ponto = "Desconhecido"
		else:
			if previous_img_link != row['crypto_values'][0]:
				imgopen = imaginador.imgOpener(row['crypto_values'][0])
				previous_img_link = row['crypto_values'][0]
			(resultadoImagem, virgula) = imaginador.imgDiscover(imgopen, row['crypto_values'][1:])
			valor_com_ponto = imaginador.recognize(resultadoImagem, virgula)
		row['crypto_values'] = valor_com_ponto
		row['card_name'] = card_name
		print(row)

	
	for i in html_extract:
		print(i)

	return html_extract




main()



