"""
Obtener la información del archivo informacion.csv

Ordenar los objetos por (nombres o campeonatos)

Guardar la nueva información (ordenada) en un archivo.
Liga de Quito|Quito|10|50
Barcelona|Guayaquil|15|51
Emelec|Guayaquil   |14|49
Dep Cuenca|Cuenca  | 1|30


"""
from data.archivo import *
from mi_modelo.modelo import *

o = MiArchivo()
imprimir = MiArchivoEscribir()

lista = o.obtener_informacion()

lista = [l.split("|") for l in lista]
lista_jugadores = []
for d  in lista:
	j = Equipo(d[0], d[1], d[2], d[3])
	lista_jugadores.append(j)

operacion = Operaciones(lista_jugadores)

pregunta = int(input("Ingrese 1 si quiere ordenar por nombres o 2 si quiere ordenar por numero de jugadores\n"))
if pregunta == 1:
	lista_final = operacion.ordenarNombres()
else:
	lista_final = operacion.ordenarNumeroJugadores()

for i in lista_final:
	imprimir.agregar_informacion(i)
	print(i)




