---

# File and Directory Management (Spanish)

Administrar archivos y directorios es una habilidad esencial para cualquier usuario de Linux. Dominar estos comandos te dará un control eficiente sobre tu sistema de archivos.

## 1. Listar archivos y directorios

El comando `ls` se usa para listar el contenido del directorio actual. Para mostrar información detallada sobre archivos y directorios, usa:

```bash
ls -l
```

* `-l`: Muestra una lista larga que incluye permisos de archivo, número de enlaces, propietario, grupo, tamaño del archivo y fecha de modificación.

## 2. Crear un directorio

Para crear un nuevo directorio, usa el comando `mkdir` (make directory).

```bash
mkdir my_directory
```

* Puedes crear varios directorios a la vez separando sus nombres con un espacio.
* Para crear un directorio dentro de un directorio padre inexistente, usa la opción `-p`:

```bash
mkdir -p parent_directory/my_directory
```

## 3. Navegar entre directorios

El comando `cd` (change directory) se usa para moverse entre directorios.

```bash
cd my_directory
```

* `cd ..`: Se mueve al directorio padre.
* `cd` o `cd ~`: Regresa a tu directorio personal.

## 4. Copiar archivos

El comando `cp` (copy) se usa para copiar archivos de un lugar a otro.

```bash
cp source.txt destination.txt
cp file.txt /path/to/directory/
cp -r directory_a directory_b
```

* `cp -r`: Copia un directorio y todo su contenido de manera recursiva.

## 5. Mover y renombrar archivos

El comando `mv` (move) se usa para mover o renombrar archivos y directorios.

```bash
mv oldname.txt newname.txt
```

* **Renombrar**: Si el archivo nuevo está en el mismo directorio.
* **Mover**: Si `newname.txt` es una ruta a otro directorio, el archivo se moverá allí.

## 6. Eliminar archivos y directorios

El comando `rm` (remove) se usa para eliminar archivos.

```bash
rm filename.txt
rm -i filename.txt
rm -r directory_name
rm -f file.txt
```

* `rm -i`: Solicita confirmación antes de eliminar.
* `rm -r`: Elimina un directorio y todo su contenido de manera recursiva.
* `rm -f`: Fuerza la eliminación sin confirmación.

## 7. Mostrar el directorio actual

El comando `pwd` (print working directory) imprime la ruta completa del directorio en el que te encuentras.

```bash
pwd
```
