class Equipo:
	def __init__(self, n, c, cam, j):
		self.nombres = n
		self.ciudad = c
		self.campeonatos = int(cam)
		self.numJugadores = int(j)

	def setNombres(self, n): # metodo agregar el nombre
		self.nombres = n 

	def setCiudad(self, c): # metodo agregar la ciudad
		self.ciudad = c

	def setCampeonatos(self, cam): # metodo agrgar el campeonato
		self.campeonatos = cam

	def setNumJugadores(self, j): # metodo agregar el numero de jugadores
		self.numJugadores 

	def getNombres(self): # metodo obtener el nombre
		return self.nombres 

	def getCiudad(self): # metodo obtner la ciudad
		return self.ciudad 

	def getCampeonatos(self): # metodo obtner el campeonato
		return self.campeonatos 

	def getNumJugadores(self): # metodo obtner el numero de jugadores
		return self.numJugadores 

	def __repr__(self):
		return "%s %s - %d - %d" % (self.getNombres(), self.getCiudad(), self.getCampeonatos(),self.getNumJugadores())


class Operaciones(object):
    
    def __init__(self, listado):
        self.listado_jugadores = listado

    def ordenarNombres(self):
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
        return sorted(self.listado_jugadores, key=lambda jugador: jugador.nombres)

    def ordenarNumeroJugadores(self):
    	return sorted(self.listado_jugadores, key=lambda jugador: jugador.numJugadores)