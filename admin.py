from getpass import getpass
from plataforma import PlataformaStreaming


def menu_inicio_admin():
    plataforma = PlataformaStreaming()

    while True:
        print("\n--- Menú Inicial de Administradores ---")
        print("1. Iniciar sesión como Administrador")
        print("2. Crear nuevo Administrador")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Inicio de Sesión Administrador ---")
            usuario = input("Ingrese usuario: ").strip()
            contraseña = getpass("Ingrese contraseña: ").strip()

            if plataforma.iniciar_sesion_admin(usuario, contraseña):
                print(f"Bienvenido Administrador, {usuario}!")
                menu_administrador()
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "2":
            print("\n--- Crear Nuevo Administrador ---")
            nombre = input("Ingrese nombre completo: ").strip()
            fecha_nacimiento = input("Ingrese fecha de nacimiento (dd/mm/aaaa): ").strip()
            puesto = input("Ingrese puesto: ").strip()
            usuario = input("Ingrese nombre de usuario: ").strip()
            contraseña = getpass("Ingrese contraseña: ").strip()

            if plataforma.crear_admin(nombre, fecha_nacimiento, puesto, usuario, contraseña):
                print(f"Administrador '{usuario}' creado exitosamente.")
            else:
                print("Error al crear el administrador.")

        elif opcion == "3":
            print("Saliendo del menú de administradores.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


def menu_administrador():
    while True:
        print("\n--- Menú de Operaciones para Administradores ---")
        print("1. Agregar película")
        print("2. Borrar película")
        print("3. Agregar serie")
        print("4. Modificar serie")
        print("5. Borrar serie")
        print("6. Borrar usuario")
        print("7. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título de la película: ").strip()
            popularidad = int(input("Ingrese la popularidad de la película: "))
            plataforma.agregar_pelicula(titulo, popularidad)

        elif opcion == "2":
            titulo = input("Ingrese el título de la película a borrar: ").strip()
            plataforma.borrar_pelicula(titulo)

        elif opcion == "3":
            titulo = input("Ingrese el título de la serie: ").strip()
            plataforma.agregar_serie(titulo)

        elif opcion == "4":
            titulo = input("Ingrese el título de la serie a modificar: ").strip()
            temporada = int(input("Ingrese la temporada: "))
            capitulos = input("Ingrese capítulos separados por coma: ").split(",")
            plataforma.modificar_serie(titulo, temporada, [c.strip() for c in capitulos])

        elif opcion == "5":
            titulo = input("Ingrese el título de la serie a borrar: ").strip()
            plataforma.borrar_serie(titulo)

        elif opcion == "6":
            usuario = input("Ingrese el nombre de usuario a borrar: ").strip()
            plataforma.borrar_usuario(usuario)

        elif opcion == "7":
            print("\n¿Está seguro de que quiere salir?")
            print("1. No")
            print("2. Sí")
            confirmacion = input("Seleccione una opción: ")

            if confirmacion == "1":
                print("Regresando al menú de la plataforma.")
                continue
            elif confirmacion == "2":
                print("Saliendo del sistema. ¡Hasta luego!")
                exit()
            else:
                print("Opción no válida. Intente de nuevo")   

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_inicio_admin()