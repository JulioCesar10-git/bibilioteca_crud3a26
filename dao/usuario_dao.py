from database import conexion
from database.conexion import Conexion
from models.usuario import usuario

class usuarioDAO: 

    # SELECT * FROM Usuario
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM vista_usuario")
        registros = cursor.fetchall()

        usuarios = []
        for registro in registros:
            usuario = usuario(id = registro[0], nombre = registro[1], matricula = registro[2], carrera = registro[3], correo = registro[4], activo = registro[5])
            usuario.append(usuario)
            
        cursor.close()
        conexion.close()
        return usuarios
    
    def insertar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """

            INSERT INTO usuario (id, nombre, matricula, carrera, correo, activo)
            VALUES (%s, %s, %s, %s, %s)

        """

        cursor.execute(
            sql, (usuario.id, usuario.nombre, usuario.matricula, usuario.carrera, usuario.correo, usuario.activo) 
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """

            UPDATE usuario SET nombre = %s, matricula = %s, carrera = %s, correo = %s, activo = %s, WHERE id = %
            
        """        

        cursor.execute(
            sql, (usuario.titulo, usuario.autor, usuario.isbn, usuario.disponible, usuario.id)
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, usuario_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,)) 

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM usuario ORDER BY id DESC")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado is None:
            return 0
        return resultado[0]   