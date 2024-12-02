from datetime import datetime

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def capturar_preferencias():
    generos = [
        "Terror",
        "Drama",
        "Ciencia Ficción",
        "Comedia",
        "Romance",
        "Aventura",
        "Otras",
    ]
    while True:
        print("\nSeleccione sus géneros favoritos (ingrese los números separados por comas):")
        for i, genero in enumerate(generos, 1):
            print(f"{i}. {genero}")
        seleccion = input("Ingrese sus opciones: ").split(",")
        try:
            preferencias = [generos[int(opcion.strip()) - 1] for opcion in seleccion if opcion.strip().isdigit()]
            if not preferencias:
                raise ValueError
            return preferencias
        except (ValueError, IndexError):
            print("Por favor, ingrese una opción válida.")
