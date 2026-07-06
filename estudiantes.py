import json
import os

RUTA_ARCHIVO = "datos/estudiantes.json"

def cargar_estudiantes():
    try:
        os.makedirs("datos", exist_ok=True)
        if not os.path.exists(RUTA_ARCHIVO):
            with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, indent=4)
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception:
        return []

def guardar_estudiantes(estudiantes):
    try:
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"\n[ERROR AL GUARDAR] {e}")

def registrar_estudiante():
    print("\n===== REGISTRO DE ESTUDIANTE =====")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    dni = input("DNI/Código: ").strip()
    if not nombre or not apellido or not dni:
        print("\n[ERROR] Ningún campo puede quedar vacío.")
        return
    if not dni.isdigit():
        print("\n[ERROR] El DNI debe contener solo números.")
        return
    estudiantes = cargar_estudiantes()
    for est in estudiantes:
        if est["dni"] == dni:
            print("\n[ERROR] Ya existe un estudiante registrado con ese DNI.")
            return
    nuevo = {"nombre": nombre, "apellido": apellido, "dni": dni, "materias": []}
    estudiantes.append(nuevo)
    guardar_estudiantes(estudiantes)
    print("\n[OK] Estudiante registrado correctamente.")

def buscar_estudiante():
    print("\n===== BÚSQUEDA DE ESTUDIANTE =====")
    dni = input("Ingrese DNI/Código: ").strip()
    estudiantes = cargar_estudiantes()
    for est in estudiantes:
        if est["dni"] == dni:
            print(f"\nNombre: {est['nombre']} {est['apellido']}\nDNI: {est['dni']}")
            print(f"Materias: {', '.join(est['materias']) if est['materias'] else 'Ninguna'}")
            return
    print("\n[ERROR] No existe un estudiante con ese DNI.")

def matricular_en_materia():
    print("\n===== MATRÍCULA EN MATERIA =====")
    dni = input("Ingrese DNI/Código del estudiante: ").strip()
    materia = input("Nombre de la materia: ").strip()
    estudiantes = cargar_estudiantes()
    for est in estudiantes:
        if est["dni"] == dni:
            if materia in est["materias"]:
                print("\n[ERROR] Ya está matriculado.")
                return
            est["materias"].append(materia)
            guardar_estudiantes(estudiantes)
            print("\n[OK] Materia matriculada correctamente.")
            return
    print("\n[ERROR] No existe el estudiante.")
