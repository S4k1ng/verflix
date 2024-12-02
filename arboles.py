class NodoArbolBinario:
    def __init__(self, contenido):
        self.contenido = contenido
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, contenido):
        if self.raiz is None:
            self.raiz = NodoArbolBinario(contenido)
        else:
            self._insertar(self.raiz, contenido)

    def _insertar(self, nodo, contenido):
        if contenido["popularidad"] < nodo.contenido["popularidad"]:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbolBinario(contenido)
            else:
                self._insertar(nodo.izquierdo, contenido)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbolBinario(contenido)
            else:
                self._insertar(nodo.derecho, contenido)

    def buscar_mas_populares(self, limite):
        resultados = []
        self._inorden_desc(self.raiz, resultados, limite)
        return resultados

    def _inorden_desc(self, nodo, resultados, limite):
        if nodo is None or len(resultados) >= limite:
            return
        self._inorden_desc(nodo.derecho, resultados, limite)
        if len(resultados) < limite:
            resultados.append(nodo.contenido)
            self._inorden_desc(nodo.izquierdo, resultados, limite)


class NodoArbolGeneral:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []


class ArbolGeneral:
    def __init__(self):
        self.raiz = NodoArbolGeneral("Plataforma")

    def agregar_usuario(self, usuario):
        nodo_usuarios = self._obtener_o_crear_hijo(self.raiz, "Usuarios")
        nodo_usuarios.hijos.append(NodoArbolGeneral(usuario))

    def agregar_admin(self, administrador):
        nodo_administradores = self._obtener_o_crear_hijo(self.raiz, "administradores")
        nodo_administradores.hijos.append(NodoArbolGeneral(administrador))

    def agregar_contenido(self, contenido):
        nodo_contenidos = self._obtener_o_crear_hijo(self.raiz, "Películas y Series")
        nodo_contenidos.hijos.append(NodoArbolGeneral(contenido))

    def _obtener_o_crear_hijo(self, nodo, valor):
        for hijo in nodo.hijos:
            if hijo.valor == valor:
                return hijo
        nuevo_hijo = NodoArbolGeneral(valor)
        nodo.hijos.append(nuevo_hijo)
        return nuevo_hijo
