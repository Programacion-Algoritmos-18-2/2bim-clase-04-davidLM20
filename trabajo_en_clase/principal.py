"""
Obtener la información del archivo informacion.csv

Ordenar los objetos por (nombres o campeonatos)

Guardar la nueva información (ordenada) en un archivo.
Liga de Quito|Quito|10|50
Barcelona|Guayaquil|15|51
Emelec|Guayaquil   |14|49
Dep Cuenca|Cuenca  | 1|30


"""
# se importa la informacion de paquetes
from data.archivo import *
from mi_modelo.modelo import *
# se crea los objetos para obtener la informacion y para escribir en un nuevo archivo
o = MiArchivo()
imprimir = MiArchivoEscribir()
# se crea la lista a la cual se le agrega la informacion
lista = o.obtener_informacion()
# se separa la informacion del archivo usando el split
lista = [l.split("|") for l in lista]
lista_jugadores = []
# se itera y se agrega un parametro para cada uno de las posiciones
for d  in lista:
	j = Equipo(d[0], d[1], d[2], d[3])
	lista_jugadores.append(j) # se aniade la informacion al objeto

operacion = Operaciones(lista_jugadores)
# se pregunta como se debe organizar la lista
pregunta = int(input("Ingrese 1 si quiere ordenar por nombres o 2 si quiere ordenar por campeonatos\n"))
# si se desea organizar por nombres se ejecuta esta condicion
if pregunta == 1: 
	print("Listado ordenado por Nombre del Equipo")
	lista_final = operacion.ordenarNombres()
else: # si se desea ordenar po camponatos se ejecuta esta condicion
	print("Listado ordenado por numero de campeonatos")
	lista_final = operacion.ordenarCampeonatos()
#se envia la informacion al nuevo archivo
for i in lista_final:
	imprimir.agregar_informacion(i)
	print(i)




