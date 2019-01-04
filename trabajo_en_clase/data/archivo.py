import codecs # se importa la libreria codecs
import sys # se importa la libreria sys

# se crea la clase Mi arcivo
class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion.csv", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion_final.csv", "a")

    def agregar_informacion(self, j):
        self.archivo.write("%s-%s-%d-%d\n" % (j.nombres, j.ciudad,\
                j.campeonatos, j.numJugadores))

    def cerrar_archivo(self):
        self.archivo.close()
