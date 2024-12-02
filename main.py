import getpass
from plataforma import PlataformaStreaming
from utilidades import capturar_preferencias

def menu_inicio_usuario():
    plataforma = PlataformaStreaming()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Crear usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = input("Ingrese su usuario: ")
            contraseña = getpass.getpass("Ingrese su contraseña: ")
            if plataforma.iniciar_sesion(usuario, contraseña):
                nombre_completo = plataforma.usuarios[usuario]["nombre_completo"]
                print(f"Bienvenido, {nombre_completo}!")
                mostrar_inicio(plataforma, usuario)

        elif opcion == "2":
            print("\n--- Registro de Usuario ---")
            nombre_completo = input("Ingrese su nombre y apellido: ").strip()
            usuario = input("Ingrese un nombre de usuario: ").strip()
            fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ").strip()
            preferencias = capturar_preferencias()
            contraseña = getpass.getpass("Ingrese una contraseña: ").strip()

            if plataforma.crear_usuario(nombre_completo, usuario, fecha_nacimiento, preferencias, contraseña):
                print(f"Usuario '{usuario}' registrado con éxito.")
            else:
                print("Error al registrar el usuario. Intente de nuevo.")

        elif opcion == "3":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def mostrar_inicio(plataforma, usuario):
    while True:
        print("\n--- Inicio de la Plataforma ---")
        print("1. Ver catálogo de series")
        print("2. Ver catálogo de películas")
        print("3. Ver preferencias")
        print("4. Ver historial")
        print("5. Cerrar sesión")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Catálogo de Series ---")
            print("Series no implementadas aún.")

        elif opcion == "2":
            print("\n--- Catálogo de Películas ---")
            print("Películas no implementadas aún.")

        elif opcion == "3":
            print("\n--- Tus preferencias ---")
            preferencias = plataforma.usuarios[usuario]["preferencias"]
            print(", ".join(preferencias))

        elif opcion == "4":
            print("\n--- Historial de visualización ---")
            historial = plataforma.historial.get(usuario, [])
            if historial:
                print("\n".join(historial))
            else:
                print("No hay historial disponible.")

        elif opcion == "5":
            print("Sesión cerrada. Volviendo al menú principal.")
            break

        elif opcion == "6":
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
    menu()
