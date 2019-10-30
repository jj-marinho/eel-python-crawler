import requests
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
import urllib.request
import time



def imgOpener(url):
	imgopen = Image.open(urllib.request.urlopen(url))
	return imgopen



def imgDiscover(imgopen, listofpositions): 

# initialize the width of the final image and the cropped number positions.
	croppednumbers = []
	width = 0
# open url using urllib
	# imgopen = Image.open(urllib.request.urlopen(url))
	# cropping imgs and appending them to the list.

	comma = 0
	for positions in listofpositions:
		if positions[0] == ',': # Defines comma positioning for future use.
			comma_position = comma
		else:
			x_pos = int(positions[0])
			y_pos = int(positions[1])
			imgCrop = imgopen.crop((x_pos, y_pos, x_pos + 7, y_pos + 15))
			width += 7 # Width of the final image
			croppednumbers.append(imgCrop)
		comma += 1

	# Create final image, blank.
	resultImg = Image.new("RGB", (width, 15))
	
	boxWidth = 0 # Defines a initial width to append to.
	for number in croppednumbers:
		resultImg.paste(im=number, box=(boxWidth , 0))
		boxWidth += 7
	return resultImg, comma_position



def recognize(img, comma_position):
	recognized_value = pytesseract.image_to_string(img)
	value_with_dot = (recognized_value[0:comma_position]) + '.' + recognized_value[comma_position:]
	return float(value_with_dot)

	





# start_time = time.time()

# x, y = imgDiscover("https://www.ligamagic.com.br/arquivos/up/comp/imgnum/files/img/191027sSl73z7k5s4syr3kb2p0b2jevf6xh6.jpg", [[256, 44],[','], [336, 65], [0, 44]])
# a = recognize(x, y)
# print(a)

# print("--- %s seconds ---" % (time.time() - start_time))
