'''
Tipo: Concepto, Ejercicio, Pregunta...
Fuente: libro, curso, ...


Este chunk de código tiene como propósito...
Volver  las cosas que le paso como valroes de un diccionario.


Given three arguments ⁠— a dictionary obj, a key name and a value ⁠— return a dictionary with that name and value in it (as key-value pairs).

Examples
add_name({}, "Brutus", 300) ➞ { "Brutus": 300 }

add_name({ "piano": 500 }, "Brutus", 400) ➞ { "piano": 500, "Brutus": 400 }

add_name({ "piano": 500, "stereo": 300 }, "Caligula", 440) ➞ { "piano": 500, "stereo": 300, "Caligula": 440 }

'''

#
# obj = {}
# def add_name(obj, name, value):
#     '''
#         Esta función recibe un objeto dic vacío, un nombre  y un valor.
#         La idea es que actualice lso valores d eun diccionario.
#     '''
#     obj.update({name:value})
#     return  print(obj)
#


def add_name(obj,name,value):
	obj[name] = value
	return print(obj)


add_name({ "piano": 500, "stereo": 300 }, "Caligula", 440)

