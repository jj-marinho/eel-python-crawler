import eel




eel.init('web')

@eel.expose
def my_python_method(param1, param2):
    print (param1 + param2)


try:
	eel.start('index.html', host='localhost', port=0)
except (SystemExit, MemoryError, KeyboardInterrupt):
	pass
