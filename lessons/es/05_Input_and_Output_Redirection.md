---

# Input and Output Redirection (Spanish)

En Linux, una de las características más poderosas de la línea de comandos es la capacidad de redirigir la entrada y salida de los comandos. Esto te permite encadenar comandos y automatizar tareas sin necesidad de escribir scripts complejos.

## 1. Redirigir la salida a un archivo (sobrescribir)

El operador `>` envía la salida estándar de un comando a un archivo especificado. Si el archivo ya existe, se sobrescribirá completamente con la nueva salida.

```bash
ls -l > file_list.txt
```

**Ejemplo:** Normalmente, `ls -l` muestra una lista larga de archivos y directorios en tu terminal. Usando `>`, esta salida se redirige y se guarda en un nuevo archivo llamado `file_list.txt`.

## 2. Añadir la salida a un archivo

El operador `>>` también redirige la salida estándar a un archivo, pero en lugar de sobrescribirlo, añade la nueva salida al final del contenido existente.

```bash
echo "This is a new line" >> logfile.txt
```

**Ejemplo:** Si `logfile.txt` ya contiene texto, este comando agregará la línea *"This is a new line"* al final del archivo, preservando su contenido original. Esto es común en registros (logging).

## 3. Redirigir la entrada desde un archivo

El operador `<` redirige la entrada estándar de un comando para que provenga de un archivo en lugar del teclado. Esto es útil para comandos que esperan recibir datos del usuario.

```bash
sort < unsorted_list.txt
```

**Ejemplo:** El comando `sort` normalmente espera que escribas líneas de texto y luego las ordena. Usando `<`, le dices a `sort` que obtenga su entrada de `unsorted_list.txt` y luego imprima la salida ordenada en la terminal.

## 4. Pasar la salida a otro comando (Pipe)

El operador `|` (pipe) es una herramienta poderosa que toma la salida estándar de un comando y la usa como entrada estándar para otro comando. Esto permite combinar comandos simples para realizar operaciones complejas.

```bash
ls -l | grep ".txt"
```

**Ejemplo:** La salida de `ls -l` (la lista de todos los archivos y directorios) se *pasa* al comando `grep`. Luego, `grep` filtra esta lista y muestra solo las líneas que contienen `.txt`. Esto permite encontrar rápidamente todos los archivos de texto en un directorio.
