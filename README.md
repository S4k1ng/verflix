# Plataforma Verflix (Carlos Vega)
Este proyecto es una simulación de una plataforma de streaming que organiza y gestiona datos como usuarios, administradores, y contenido (películas y series). Utiliza herramientas avanzadas llamadas árboles, que ayudan a guardar y buscar información de manera ordenada y eficiente.

El programa está diseñado para que sea fácil de entender y usar. Por ejemplo, permite agregar y buscar contenido popular rápidamente, y organiza todo en categorías claras. Además, está hecho de forma que se le puedan agregar nuevas funciones sin complicaciones.

En pocas palabras, este proyecto no solo muestra cómo podría funcionar una plataforma real, sino que también sirve como un ejemplo práctico para aprender cómo manejar datos de forma inteligente en un programa. Es ideal para cualquiera interesado en ver cómo la tecnología organiza grandes cantidades de información.

___

## Descripcion del código:
**La plataforma permite:**
1) *Registro y autenticación:*
 - Usuarios pueden registrarse y acceder a su perfil, preferencias y contenido.
 - Administradores tienen permisos especiales para gestionar el sistema.

2) *Gestión de contenido:*
 - Agregar, modificar y eliminar películas y series.
 - Organización jerárquica y búsqueda eficiente basada en popularidad.
 
3) *Personalización y optimización:*
 - Captura de preferencias de los usuarios para una experiencia más personalizada.
 - Almacenamiento estructurado para una mejor organización y acceso rápido.


___

## Estructura del proyecto:
El programa está dividido en módulos que trabajan juntos para lograr un diseño modular y organizado:

### **1. `arboles.py`** 
Este módulo define las estructuras de datos que representan la base organizativa de la plataforma:

**Árbol General**
- *Definición*: Implementado con las clases NodoArbolGeneral y ArbolGeneral.
- *Propósito*: Representa jerarquías como:

      Plataforma
      ├── Usuarios
      │   ├── Usuario1
      │   └── Usuario2
      ├── Administradores
      │   ├── Admin1
      │   └── Admin2
      └── Películas y Series
          ├── Película1
          ├── Película2
          └── Serie1
             └── Temporada1
                 └── Capitulo1
- *Ventajas*:
  - Es flexible para almacenar categorías y subcategorías.
  - Permite añadir nodos dinámicamente según las necesidades del sistema.
 
**Árbol Binario de Búsqueda** *(ABB)*
- *Definición*: Implementado con las clases NodoArbolBinario y ArbolBinarioBusqueda.
- *Propósito*: Organiza las películas según su popularidad para búsquedas rápidas.
  - Ejemplo:
    
                       [Película (80)]
                    /                   \
               [Película (50)]     [Película (90)]
                 /          \               \
        [Película (30)] [Película (60)]   [Película (100)]

- **Funciones principales**:
- `insertar`: Añade un nuevo contenido al árbol, posicionándolo según su popularidad.
- `buscar_mas_populares`: Realiza un recorrido **inorden descendente** para listar los contenidos más populares.
- `_inorden_desc`: Implementa la lógica del recorrido inverso (derecha, nodo, izquierda).


---

### **2. `plataforma.py`**
Este módulo contiene la lógica principal del sistema, vinculando los datos con la interacción del usuario:

#### **Gestión de Usuarios**
- **`crear_usuario`**: Valida y registra nuevos usuarios, asegurándose de que todos los datos sean correctos.
- **`iniciar_sesion`**: Permite a los usuarios autenticarse con sus credenciales.

#### **Gestión de Administradores**
- **`crear_admin`**: Registra nuevos administradores con validación adicional.
- **`iniciar_sesion_admin`**: Verifica las credenciales de los administradores antes de otorgarles acceso.

#### **Gestión de Contenido**
- **Películas**:
- **`agregar_pelicula`**: Inserta películas en el ABB según su popularidad.
- **`borrar_pelicula`**: (Pendiente) Lógica para eliminar películas del ABB.
- **Series**:
- **`agregar_serie`**: Añade nuevas series al sistema.
- **`modificar_serie`**: Permite actualizar temporadas y capítulos.
- **`borrar_serie`**: Elimina series registradas en el sistema.


---

### **3. `admin.py`**
Proporciona un **menú interactivo** para que los administradores gestionen la plataforma:
- Agregar, modificar y eliminar películas o series.
- Eliminar usuarios.
- Cerrar sesión.


---

### **4. `main.py`**
Proporciona un **menú interactivo para usuarios generales**, con funcionalidades como:
- Registro de nuevos usuarios con captura de preferencias.
- Autenticación para iniciar sesión.
- Opciones para ver contenido y personalizar la experiencia (pendiente de implementación completa).


---

### **5. `utilidades.py`**
Funciones auxiliares para mejorar la interacción y validación:
- **`validar_fecha`**: Comprueba que las fechas ingresadas estén en el formato correcto.
- **`capturar_preferencias`**: Permite a los usuarios seleccionar géneros favoritos de manera interactiva.


---

## **Diseño del Árbol**

### **Árbol Binario de Búsqueda**
- **Organización**: Cada nodo contiene una película con su título y popularidad.
- **Ventajas**:
- Inserción rápida según la popularidad.
- Consultas eficientes para encontrar los contenidos más populares.
- **Recorrido**: 
- El recorrido inorden inverso se utiliza para devolver los elementos en orden descendente de popularidad, priorizando los más vistos.

### **Árbol General**
- **Organización**: Jerarquía flexible para clasificar elementos en categorías principales y subcategorías.
- **Uso en la Plataforma**:
- Categoriza usuarios, administradores y contenido.
- Permite una estructura intuitiva para la navegación y gestión de datos.


---


 
