---

# Process Management (Spanish)

Los procesos son programas en ejecución. Comprender cómo gestionarlos te da un control significativo sobre el rendimiento de tu sistema y te permite solucionar problemas.

## 1. Ver procesos en ejecución

El comando `ps aux` es una de las formas más comunes de mostrar todos los procesos en ejecución actualmente.

```bash
ps aux
```

* `a`: Muestra procesos de todos los usuarios.
* `u`: Muestra procesos en un formato orientado al usuario.
* `x`: Incluye procesos no asociados a un terminal específico.

Al ejecutar este comando, verás una tabla con información importante, como:

* **USER**: El usuario que posee el proceso.
* **PID**: El ID único del proceso.
* **%CPU**: Porcentaje de uso de CPU.
* **%MEM**: Porcentaje de uso de memoria.
* **COMMAND**: El comando que inició el proceso.

## 2. Matar un proceso por PID

Si un proceso no responde o consume demasiados recursos, puedes terminarlo usando el comando `kill` y su PID.

```bash
kill PID
kill 12345
```

* `kill 12345`: Intenta terminar el proceso de forma elegante con la señal **SIGTERM**.

Para matar un proceso rebelde, usa la opción `-9`:

```bash
kill -9 PID
kill -9 12345
```

* `-9`: Envía una señal de terminación fuerte (**SIGKILL**) que el proceso no puede ignorar.

## 3. Matar un proceso por nombre

Si no conoces el PID, puedes usar el comando `pkill` para terminar procesos por su nombre.

```bash
pkill process_name
pkill firefox
pkill -9 firefox
```

* `pkill firefox`: Termina todos los procesos llamados *firefox*.
* `pkill -9 firefox`: Termina forzosamente todos los procesos *firefox*.

Esto es útil cuando necesitas cerrar todas las instancias de un programa específico a la vez.

## 4. Ver el árbol de procesos

El comando `pstree` muestra los procesos en un formato de árbol jerárquico, mostrando la relación padre-hijo entre ellos.

```bash
pstree
pstree -p
pstree username
```

* `pstree`: Muestra todos los procesos en formato de árbol.
* `pstree -p`: Muestra el árbol de procesos con PIDs.
* `pstree username`: Muestra solo los procesos de un usuario específico.

Esta representación visual facilita entender qué subprocesos fueron lanzados por un proceso principal, ayudando en la solución de problemas.
