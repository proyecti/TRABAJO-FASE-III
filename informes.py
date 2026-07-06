import json
import os

RUTA_ESTUDIANTES = "datos/estudiantes.json"
RUTA_ASISTENCIA = "datos/asistencia.json"
RUTA_NOTAS = "datos/notas.json"

def cargar_datos(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as a:
        return json.load(a)

def informe_general_materia():
    materia = input("Ingrese la materia para el reporte: ").strip()
    notas = cargar_datos(RUTA_NOTAS)
    notas_m = [r["nota"] for r in notas if r["materia"].lower() == materia.lower()]
    if not notas_m:
        print("No hay registros de notas para esta materia.")
        return
    print(f"\n--- REPORTE {materia.upper()} ---")
    print(f"Promedio grupal: {sum(notas_m)/len(notas_m):.2f}")

def listar_alumnos_criticos():
    print("\n--- ALUMNOS EN RIESGO ---")
    notas = cargar_datos(RUTA_NOTAS)
    criticos = set([r["dni"] for r in notas if r["nota"] < 11])
    if not criticos:
        print("No hay alumnos en riesgo.")
    for c in criticos:
        print(f"- Estudiante DNI/Código: {c}")

def estadisticas_asistencia_global():
    asistencias = cargar_datos(RUTA_ASISTENCIA)
    if not asistencias:
        print("No hay asistencias registradas.")
        return
    total = len(asistencias)
    asiste = sum(1 for r in asistencias if r["estado"] == "Asiste")
    print(f"\nPorcentaje global de asistencia: {(asiste/total)*100:.2f}%")
