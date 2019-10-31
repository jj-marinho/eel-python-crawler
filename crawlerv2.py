import requests
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
import urllib.request
import time




def crawler(soup):
	table = []
	i = 0

	for products in soup.find_all('div', attrs={'class': 'estoque-linha'}): # Line looping
		row = {} # Empty Dictionary to initialize the information gathering, by row.
		products_columns = products.children # Line Children, (a.k.a table cell)

		for cells in products_columns: # Cell analisys

			if cells.name == 'div' and cells.get('class', '') == ['e-col1']: # StoreName
				row['store_name'] = cells.a.img.get('title')

			if cells.name == 'div' and cells.get('class', '') == ['e-col4']: # Card Quality
				row['card_quality'] = cells.font.text

			if cells.name == 'div' and cells.get('class', '') == ['e-col2']: # Edition Name
				row['edition'] = cells.find(text=True)

	# if cells.name == 'div' and cells.get('class', '') == ['e-col5']: ####Units (need decoding) NOT IMPLEMENTED ###

			if cells.name == 'div' and cells.get('class', '') == ['e-col3']: # Price (need decoding)
				encrypted_digit_list = []
				values = cells.children

	# Next loop cycle through all digits to get the complete value stored in a list, that list will be caled "crypto_values"
				for digits in values: 
					if digits.name == 'div':
						encrypted_digit_list.append(digits.get('class'))
					elif digits.name == 'font':
						encrypted_digit_list = float(digits.parent.contents[2].replace("R$ ", "").replace(",", "."))
						break
				row['crypto_values'] = encrypted_digit_list # Appending the encrypted cypher to a cell
		if len(row) == 0: ## REMOVES EMPTY ROw
			continue
		else:
			table.append(row) # Append to Final Table (SQL RESULT)
	return table




def css_style_crawler(soup):

	## Initializing Function
	table = []
	i = 0

	### Finds the Style Tag and fixes all the unwanted characters, then makes a list with the css tags
	styles = soup.find('style')
	text = styles.text
	text_fixed = text.replace("-", "").replace("backgroundposition:", "").replace(".", "").replace(";", "").replace("{", ";").replace(" }", ";").replace("}", ";").replace(
																										"width:5px!important", "").replace(")", "").replace("px", "")
	split = text_fixed.split(";")
	# print(split)

	############## BAD CODE, REFACTOR ##################
	### Creates a text_coordinates[i] = Name and text_coordinates[i + 1] = list with x, y coordinates. Needed for the next part of the function.
	text_coordinates = []
	for value in split:
		if value.split(" ")[0] != value:
			name = value.split(" ")
			text_coordinates.append(name)
		else: text_coordinates.append(value)

	########### Structure: table('css_class') =  coordinates (x, y), if its a link then a_link_css_class = "link"
	css_class_coordinates = {}
	while i < len(text_coordinates) - 1:
		if type(text_coordinates[i+1]) is list:
			css_class_coordinates[text_coordinates[i]] = [text_coordinates[i + 1][0], text_coordinates[i + 1][1]] # CSS Name is the dictionary name of its coordinates
		else:
			# Deleting width styles in css (unwanted)
				if 'backgroundimage:' not in text_coordinates[i+1]:
					del text_coordinates[i]
					del text_coordinates[i]
					i -= 2
				else:
					link_name = ("a_link_" + str(text_coordinates[i]))
					link_url = text_coordinates[i + 1].replace("backgroundimage:url(", "https://www.ligamagic.com.br/").replace("jpg", ".jpg")
					css_class_coordinates[link_name] = link_url # CSS Name is the dictionary name of its coordinates
		i += 2
	return css_class_coordinates



def css_html_match(table, css_class_coordinates):

	for row in table:
		decyphered_values = [] 
		decyphered_link = False # Necessário para evitar a repetição de links.

		if type(row['crypto_values']) == float:
			continue
		else:
			for crypto_value in row['crypto_values']:
				decyphered_digit = []

				if crypto_value is None: # Se o Valor encriptado for "nada", consideramos ele como uma virgula
					decyphered_digit.append(',')				

				elif crypto_value[0] == 'imgnum-monet': ### Retira os imgnum-monet, melhorando a leitura da lista
					continue
				else:
					for css_class in crypto_value:         
						if "a_link_" + str(css_class) in css_class_coordinates: # Define o link como primeiro elemento, apenas uma vez por linha
							if decyphered_link == True:
								continue
							else:
								decyphered_values.insert(0, css_class_coordinates['a_link_' + str(css_class)]) 
								decyphered_link = True	
						else:
							try:
								decyphered_digit.extend(css_class_coordinates[css_class]) # Para valores normais, extende a lista
							except KeyError: # Caso algum valor não esteja presente no CSS
								pass
				decyphered_values.append(decyphered_digit)
		row['crypto_values'] = decyphered_values # Retorna a nova linha.
		

def link_returner(listOfCards):
	const_link = "https://www.ligamagic.com.br/?view=cards%2Fsearch&card="

	for i in listOfCards:
		i.split(" ", "+")




# start_time = time.time()


# html = crawler("indexv3.html")
# css = css_style_crawler("indexv2.html")
# css_html_match(html, css)

# print(html[0].values)

# print("--- %s seconds ---" % (time.time() - start_time))

