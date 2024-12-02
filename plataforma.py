from arboles import ArbolGeneral, ArbolBinarioBusqueda
from utilidades import validar_fecha

class PlataformaStreaming():
    def __init__(self):
        self.arbol = ArbolGeneral()
        self.arbol_popularidad = ArbolBinarioBusqueda()
        self.usuarios = {}
        self.historial = {}
        self.administradores = {}

    #Usuario:
    def iniciar_sesion(self, nombre, contraseña):
        if nombre in self.usuarios:
            if self.usuarios[nombre]["contraseña"] == contraseña:
                print(f"Bienvenido, {nombre}!")
                return True
            else:
                print("Contraseña incorrecta.")
        else:
            print(f"El usuario '{nombre}' no existe.")
        return False


    def crear_usuario(self, nombre_completo, usuario, fecha_nacimiento, preferencias, contraseña):
        if not nombre_completo.strip():
            print("Error: El nombre completo no puede estar vacío.")
            return False

        if usuario in self.usuarios:
            print(f"Error: El usuario '{usuario}' ya existe.")
            return False

        if not validar_fecha(fecha_nacimiento):
            print("Error: La fecha de nacimiento no es válida.")
            return False

        if not preferencias:
            print("Error: Debe seleccionar al menos una preferencia.")
            return False

        if not contraseña.strip():
            print("Error: La contraseña no puede estar vacía.")
            return False

        usuario_data = {
            "nombre_completo": nombre_completo,
            "fecha_nacimiento": fecha_nacimiento,
            "preferencias": preferencias,
            "contraseña": contraseña,
        }
        self.usuarios[usuario] = usuario_data
        self.historial[usuario] = []
        self.arbol.agregar_usuario(usuario_data)
        return True

    #Admin:
    def crear_admin(self, nombre, fecha_nacimiento, puesto, usuario, contraseña):
        if usuario in self.administradores:
            print(f"El administrador '{usuario}' ya existe.")
            return False
        if not validar_fecha(fecha_nacimiento):
            print("Error: Fecha de nacimiento inválida.")
            return False
        admin_data = {
            "nombre": nombre,
            "fecha_nacimiento": fecha_nacimiento,
            "puesto": puesto,
            "usuario": usuario,
            "contraseña": contraseña,
        }
        self.administradores[usuario] = admin_data
        self.arbol.agregar_usuario({"tipo": "Administrador", "usuario": usuario, **admin_data})
        return True

    def iniciar_sesion_admin(self, usuario, contraseña):
        if usuario in self.administradores and self.administradores[usuario]["contraseña"] == contraseña:
            return True
        return False

    # Operaciones del menú de administrador
    def agregar_pelicula(self, titulo, popularidad):
        self.arbol_popularidad.insertar({"titulo": titulo, "popularidad": popularidad})
        print(f"Película '{titulo}' agregada con éxito.")

    def borrar_pelicula(self, titulo):
        # Aquí se debe implementar la lógica para eliminar del ABB
        print(f"Película '{titulo}' eliminada con éxito.")

    def agregar_serie(self, titulo):
        if not hasattr(self, "series"):
            self.series = {}
        if titulo in self.series:
            print(f"La serie '{titulo}' ya existe.")
        else:
            self.series[titulo] = {}
            print(f"Serie '{titulo}' agregada con éxito.")

    def modificar_serie(self, titulo, temporada=None, capitulos=None):
        if titulo not in self.series:
            print(f"La serie '{titulo}' no existe.")
            return False
        if temporada and temporada not in self.series[titulo]:
            self.series[titulo][temporada] = []
        if capitulos:
            self.series[titulo][temporada].extend(capitulos)
        print(f"Modificaciones realizadas a la serie '{titulo}'.")
        return True

    def borrar_serie(self, titulo):
        if titulo in self.series:
            del self.series[titulo]
            print(f"Serie '{titulo}' eliminada con éxito.")
            return True
        print(f"La serie '{titulo}' no existe.")
        return False

    def borrar_usuario(self, usuario):
        if usuario in self.usuarios:
            del self.usuarios[usuario]
            print(f"Usuario '{usuario}' eliminado con éxito.")
            return True
        print(f"Usuario '{usuario}' no encontrado.")
        return False
