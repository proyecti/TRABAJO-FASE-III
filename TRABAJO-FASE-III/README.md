# Sistema de Control Académico

Proyecto de investigación formativa — Computación Aplicada, Sección "E"
Escuela Profesional de Ingeniería Industrial (EPII), UCSM

## Integrantes y módulos

| Integrante | Módulo | Archivo |
|---|---|---|
| Alumno 1 | Integrador, pruebas y documentación | `main.py` |
| Alumno 2 | Estudiantes y matrículas | `modulos/estudiantes.py` |
| Alumno 3 | Asistencia y clases | `modulos/asistencia.py` |
| Alumno 4 | Notas y calificaciones | `modulos/notas.py` |
| Alumno 5 | Informes y rendimiento | `modulos/informes.py` |

## Cómo ejecutar

```bash
python main.py
```

Los datos se guardan automáticamente en la carpeta `datos/` (se crea sola en el primer arranque) como archivos JSON independientes: `estudiantes.json`, `asistencia.json` y `notas.json`.

## Estructura

```
proyecto_academico/
├── main.py
├── modulos/
│   ├── estudiantes.py
│   ├── asistencia.py
│   ├── notas.py
│   └── informes.py
└── datos/          # se genera al ejecutar el programa
```
