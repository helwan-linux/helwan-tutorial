---

# Text Processing Tools in Linux (Spanish)

Los sistemas Linux vienen con un conjunto potente de herramientas para procesar texto. Estas utilidades te permiten buscar, analizar y modificar contenido de texto con alta eficiencia. Son esenciales para programadores, administradores de sistemas y cualquier persona que trabaje con datos basados en texto.

## 1. grep: Buscar patrones de texto

El comando `grep` (Global Regular Expression Print) es la herramienta más popular para buscar patrones específicos dentro de archivos de texto.

```bash
grep "pattern" filename.txt
```

**Ejemplo práctico:** Para encontrar todas las líneas que contienen la palabra "error" en un archivo de registro llamado server.log:

```bash
grep "error" server.log
```

**Opciones comunes:**

* `-i`: Ignora mayúsculas y minúsculas (por ejemplo, Error, error y ERROR coincidirán).
* `-n`: Muestra el número de línea junto con la línea coincidente.
* `-v`: Invierte la búsqueda, mostrando las líneas que no contienen el patrón.

```bash
grep -in "failed" logfile.txt
```

## 2. awk: Escaneo y procesamiento de patrones

El comando `awk` es un lenguaje de programación potente diseñado específicamente para escaneo de patrones y procesamiento de texto. `awk` separa cada línea en campos (columnas) según un delimitador especificado (como un espacio) y luego realiza acciones sobre esos campos.

```bash
awk '{print $1}' file.txt
```

**Ejemplo práctico:** Si tienes un archivo llamado users.txt que contiene nombres de usuario y números de teléfono así:

```
ali 123456789
ahmed 987654321
```

Puedes extraer solo los nombres de usuario (primer campo) usando:

```bash
awk '{print $1}' users.txt
```

El resultado será:

```
ali
ahmed
```

**Ejemplo avanzado:** Para extraer el usuario que consume más memoria del resultado de `ps aux`:

```bash
ps aux | awk 'NR>1 {print $1, $4}' | sort -k2nr | head -n 1
```

Este comando combina `awk` con otras herramientas para lograr un resultado complejo.

## 3. sed: Editor de flujo

El comando `sed` (stream editor) se utiliza para modificar un flujo de texto. `sed` no cambia el archivo original directamente; en su lugar, aplica un conjunto de ediciones a los datos entrantes y muestra la salida modificada.

```bash
sed 's/old/new/g' file.txt
```

* `s`: comando de sustitución.
* `old`: el patrón que deseas reemplazar.
* `new`: el nuevo valor.
* `g`: significa global, reemplazando todas las ocurrencias en una línea. Sin ella, solo se reemplazaría la primera ocurrencia.

**Ejemplo práctico:** Para reemplazar todas las instancias de "localhost" por "127.0.0.1" en un archivo config.ini e imprimir el resultado:

```bash
sed 's/localhost/127.0.0.1/g' config.ini
```

**Nota:** Para modificar el archivo original directamente, usa la opción `-i`:

```bash
sed -i 's/localhost/127.0.0.1/g' config.ini

```
