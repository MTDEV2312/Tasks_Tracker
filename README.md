## Task Tracker (CLI)

Proyecto simple de linea de comandos para crear, actualizar y gestionar tareas.
Los datos se guardan en `task.json` dentro del mismo directorio.

### Requisitos

- Python 3.8+

### Uso

Ejecuta el script con un comando y sus argumentos:

```bash
python Task_Tracker.py [command] [args]
```

### Comandos

```bash
# Agregar una tarea
python Task_Tracker.py add "Descripcion de la tarea"

# Actualizar la descripcion de una tarea
python Task_Tracker.py update 1 "Nueva descripcion"

# Eliminar una tarea
python Task_Tracker.py delete 1

# Marcar como en progreso
python Task_Tracker.py mark-in-progress 1

# Marcar como hecha
python Task_Tracker.py mark-done 1

# Listar tareas (todas o filtradas)
python Task_Tracker.py list
python Task_Tracker.py list todo
python Task_Tracker.py list in-progress
python Task_Tracker.py list done
```

### Formato de datos

Cada tarea tiene esta estructura:

```json
{
	"id": 1,
	"description": "Mi tarea",
	"status": "todo",
	"createdAt": "2026-02-18T10:00:00",
	"updatedAt": "2026-02-18T10:00:00"
}
```

### Notas

- Si `task.json` no existe, se crea automaticamente al agregar la primera tarea.
- Los estados validos son: `todo`, `in-progress`, `done`.

### URL
https://roadmap.sh/projects/task-tracker