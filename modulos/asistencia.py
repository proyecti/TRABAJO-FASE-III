import json
import os
from datetime import datetime

RUTA_ASISTENCIA = "datos/asistencia.json"
RUTA_ESTUDIANTES = "datos/estudiantes.json"

def cargar_asistencias():
    try:
        os.makedirs("datos", exist_ok=True)
        if not os.path.exists(RUTA_ASISTENCIA):
            with open(RUTA_ASISTENCIA, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, indent=4)
        with open(RUTA_ASISTENCIA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception:
        return []

def guardar_asistencias(asistencias):
    with open(RUTA_ASISTENCIA, "w", encoding="utf-8") as archivo:
        json.dump(asistencias, archivo, indent=4, ensure_ascii=False)

def registrar_asistencia():
    print("\n===== REGISTRO DE ASISTENCIA =====")
    dni = input("DNI/Código del estudiante: ").strip()
    materia = input("Materia: ").strip()
    estado = input("Estado (Asiste/Falta/Tardanza): ").strip().title()
    if estado not in ["Asiste", "Falta", "Tardanza"]:
        print("[ERROR] Estado inválido.")
        return
    fecha = datetime.now().strftime("%Y-%m-%d")
    asistencias = cargar_asistencias()
    # Regla crítica: no permitir un segundo registro para el mismo
    # estudiante, en la misma materia y en la misma fecha.
    for r in asistencias:
        if r["dni"] == dni and r["materia"].lower() == materia.lower() and r["fecha"] == fecha:
            print("[ERROR] Ya existe un registro de asistencia para ese día.")
            return
    asistencias.append({"dni": dni, "materia": materia, "fecha": fecha, "estado": estado})
    guardar_asistencias(asistencias)
    print("\n[OK] Asistencia registrada.")

def modificar_asistencia():
    print("\n===== MODIFICAR ASISTENCIA =====")
    dni = input("DNI: ").strip()
    materia = input("Materia: ").strip()
    fecha = input("Fecha (AAAA-MM-DD): ").strip()
    asistencias = cargar_asistencias()
    for r in asistencias:
        if r["dni"] == dni and r["materia"].lower() == materia.lower() and r["fecha"] == fecha:
            nuevo = input("Nuevo estado (Asiste/Falta/Tardanza): ").strip().title()
            if nuevo in ["Asiste", "Falta", "Tardanza"]:
                r["estado"] = nuevo
                guardar_asistencias(asistencias)
                print("[OK] Actualizado.")
            return
    print("[ERROR] No se encontró registro.")

def consultar_asistencia_estudiante():
    print("\n===== CONSULTA DE ASISTENCIAS =====")
    dni = input("DNI: ").strip()
    asistencias = cargar_asistencias()
    historial = [r for r in asistencias if r["dni"] == dni]
    if not historial:
        print("[ERROR] No hay asistencias para este alumno.")
        return
    for h in historial:
        print(f"{h['fecha']} | {h['materia']} | {h['estado']}")
