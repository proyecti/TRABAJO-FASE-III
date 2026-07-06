from modulos.estudiantes import registrar_estudiante, buscar_estudiante, matricular_en_materia
from modulos.asistencia import registrar_asistencia, modificar_asistencia, consultar_asistencia_estudiante
from modulos.notas import ingresar_nota, modificar_nota, calcular_promedio_materia
from modulos.informes import informe_general_materia, listar_alumnos_criticos, estadisticas_asistencia_global

def obtener_opcion(min_opcion, max_opcion):
    while True:
        try:
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "":
                raise ValueError("La entrada no puede estar vacía.")
            opcion = int(opcion)
            if opcion < min_opcion or opcion > max_opcion:
                raise ValueError(f"Ingrese un número entre {min_opcion} y {max_opcion}.")
            return opcion
        except ValueError as e:
            print(f"\n[ERROR] {e}\n")

def menu_estudiantes():
    while True:
        print("\n===== GESTIÓN DE ESTUDIANTES Y MATRÍCULAS =====")
        print("1. Registrar estudiante")
        print("2. Buscar estudiante")
        print("3. Matricular estudiante en materia")
        print("4. Volver al menú principal")
        opcion = obtener_opcion(1, 4)
        if opcion == 1: registrar_estudiante()
        elif opcion == 2: buscar_estudiante()
        elif opcion == 3: matricular_en_materia()
        elif opcion == 4: break

def menu_asistencia():
    while True:
        print("\n===== CONTROL DE ASISTENCIA =====")
        print("1. Registrar asistencia diaria")
        print("2. Modificar registro de asistencia")
        print("3. Consultar historial de estudiante")
        print("4. Volver al menú principal")
        opcion = obtener_opcion(1, 4)
        if opcion == 1: registrar_asistencia()
        elif opcion == 2: modificar_asistencia()
        elif opcion == 3: consultar_asistencia_estudiante()
        elif opcion == 4: break

def menu_notas():
    while True:
        print("\n===== GESTIÓN DE NOTAS Y CALIFICACIONES =====")
        print("1. Ingresar nueva nota")
        print("2. Modificar nota existente")
        print("3. Calcular promedio final de materia")
        print("4. Volver al menú principal")
        opcion = obtener_opcion(1, 4)
        if opcion == 1: ingresar_nota()
        elif opcion == 2: modificar_nota()
        elif opcion == 3: calcular_promedio_materia()
        elif opcion == 4: break

def menu_informes():
    while True:
        print("\n===== INFORMES Y RENDIMIENTO ACADÉMICO =====")
        print("1. Informe general por materia")
        print("2. Listar alumnos en riesgo crítico")
        print("3. Estadísticas globales de asistencia")
        print("4. Volver al menú principal")
        opcion = obtener_opcion(1, 4)
        if opcion == 1: informe_general_materia()
        elif opcion == 2: listar_alumnos_criticos()
        elif opcion == 3: estadisticas_asistencia_global()
        elif opcion == 4: break

def main():
    while True:
        print("\n======================================")
        print("   SISTEMA DE CONTROL ACADÉMICO")
        print("======================================")
        print("1. Gestión de Estudiantes y Matrículas")
        print("2. Control de Asistencia")
        print("3. Gestión de Notas y Calificaciones")
        print("4. Informes y Rendimiento Académico")
        print("5. Salir")
        opcion = obtener_opcion(1, 5)
        if opcion == 1: menu_estudiantes()
        elif opcion == 2: menu_asistencia()
        elif opcion == 3: menu_notas()
        elif opcion == 4: menu_informes()
        elif opcion == 5:
            print("\nGracias por utilizar el sistema.\nSaliendo...")
            break

if __name__ == "__main__":
    main()
