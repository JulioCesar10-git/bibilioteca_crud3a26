# DAO: DATA ACCES OBJECT
# libro_dao: Objeto de acceso a datos de la tabla libro

from database.conexion import Conexion
from models.libro import libro

class LibroDAO: 

    # SELCT * FROM libro
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()