import json
import os

RUTA_NOTAS = "datos/notas.json"

def cargar_notas():
    try:
        os.makedirs("datos", exist_ok=True)
        if not os.path.exists(RUTA_NOTAS):
            with open(RUTA_NOTAS, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, indent=4)
        with open(RUTA_NOTAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception:
        return []

def guardar_notas(notas):
    with open(RUTA_NOTAS, "w", encoding="utf-8") as archivo:
        json.dump(notas, archivo, indent=4, ensure_ascii=False)

def ingresar_nota():
    print("\n===== INGRESO DE NOTAS =====")
    dni = input("DNI: ").strip()
    materia = input("Materia: ").strip()
    evaluacion = input("Tipo de Evaluación: ").strip()
    try:
        nota = float(input("Nota (0-20): "))
        if not (0 <= nota <= 20): raise ValueError()
    except ValueError:
        print("[ERROR] Nota inválida.")
        return
    notas = cargar_notas()
    notas.append({"dni": dni, "materia": materia, "tipo_evaluacion": evaluacion, "nota": nota})
    guardar_notas(notas)
    print("[OK] Nota guardada.")

def modificar_nota():
    print("\n===== MODIFICAR NOTA =====")
    dni = input("DNI: ").strip()
    materia = input("Materia: ").strip()
    ev = input("Evaluación: ").strip()
    notas = cargar_notas()
    for r in notas:
        if r["dni"] == dni and r["materia"].lower() == materia.lower() and r["tipo_evaluacion"].lower() == ev.lower():
            try:
                r["nota"] = float(input("Nueva nota (0-20): "))
                guardar_notas(notas)
                print("[OK] Nota modificada.")
            except ValueError:
                print("[ERROR] Valor inválido.")
            return
    print("[ERROR] No encontrado.")

def calcular_promedio_materia():
    print("\n===== PROMEDIO POR MATERIA =====")
    dni = input("DNI: ").strip()
    materia = input("Materia: ").strip()
    notas = cargar_notas()
    filtradas = [r["nota"] for r in notas if r["dni"] == dni and r["materia"].lower() == materia.lower()]
    if not filtradas:
        print("No hay notas registradas.")
        return
    promedio = sum(filtradas) / len(filtradas)
    estado = "Aprobado" if promedio >= 11 else "Desaprobado"
    print(f"Promedio Final en {materia}: {promedio:.2f} ({estado})")
