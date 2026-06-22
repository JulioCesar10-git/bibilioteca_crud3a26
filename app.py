from dao.libro_dao import LibroDAO
from models.libro import Libro

def ver_libros():
    try:    
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_todos()
        
        print("=========== Libros en la biblioteca ===========")

        if len(libros) == 0:
            print("No hay libros registrados.")
        else:
            for libro in libros:

                print("__________________________________________________________________") 
                print(
                    f"ID: {libro.id}, Titulo: {libro.titulo}, "
                    f"Autor:s {libro.autor}, ISBN: {libro.isbn}, " 
                    f"Disponible: {'Si' if libro.disponible else 'No'}"
                )
                print("__________________________________________________________________") 
        print("\n Conexion exitosa a la base de datos")
    except Exception as e:

        print("Error: ")
        print (e)

def insertar_libro():
    titulo = input("Escribe el titulo del nuevo libro: ")
    autor = int(input("Escribe el id del autor: "))
    isbn = input("Escribe el isbn del nuevo libro: ")
    disponible = True

    try:
        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1 
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.insertar(libro)
        print("Insercion realizada con exito")

    except Exception as e:
        print("Error al insertar un nuevo libro")
        print(e)

        

def main():

    print("======== BIBLIOTECA UNIVERSITARIA ========")
    print("1. Ver todos los libros")
    print("2. Insertar un nuevo libro")
    print("3. Actualizar un libro disponible")
    print("4. Eliminar un libro disponible")
    opcion = int(input("Selecciona una opcion (1-4): "))

    match opcion:
        case 1:
            ver_libros()
        case 2:
            insertar_libro()
            
if __name__ == "__main__":
    main()