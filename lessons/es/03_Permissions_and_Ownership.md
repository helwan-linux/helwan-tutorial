---

# Permissions and Ownership (Spanish)

En Linux, un sistema de permisos robusto controla el acceso a archivos y directorios, garantizando seguridad y acceso adecuado para usuarios y aplicaciones.

## 1. Ver permisos

Para ver los permisos de un archivo o directorio, puedes usar el comando `ls -l`.

```bash
ls -l filename.txt
```

Ejemplo de salida:

```
-rwxr-xr-- 1 user group 123 Jan 1 12:00 filename.txt
```

* La primera parte (`-rwxr-xr--`) es la cadena de permisos.
* El primer carácter indica el tipo de archivo:

  * `-` archivo regular
  * `d` directorio
  * `l` enlace simbólico
* Los nueve caracteres siguientes están en tres conjuntos de tres, representando permisos para **usuario (propietario)**, **grupo**, y **otros**.

## 2. Entendiendo la notación de permisos

Cada conjunto de permisos utiliza tres caracteres:

* `r`: permiso de lectura → ver contenido del archivo o listar contenido del directorio.
* `w`: permiso de escritura → modificar/eliminar un archivo, o crear/eliminar archivos dentro de un directorio.
* `x`: permiso de ejecución → ejecutar un archivo como programa o acceder a un directorio.

### Representación en número octal

Los permisos también pueden representarse con un número octal de tres dígitos:

* `r = 4`
* `w = 2`
* `x = 1`
* Sin permiso = 0

Estos números se suman para formar el valor de permisos de cada categoría (usuario, grupo, otros).

Ejemplos:

* `7 (rwx) = 4 + 2 + 1`
* `6 (rw-) = 4 + 2 + 0`
* `5 (r-x) = 4 + 0 + 1`

## 3. Cambiar permisos

El comando `chmod` (change mode) se usa para cambiar los permisos de archivos. El método más común utiliza la notación octal.

```bash
chmod 755 filename.txt
```

Explicación:

* `7 (rwx)`: El propietario puede leer, escribir y ejecutar.
* `5 (r-x)`: El grupo puede leer y ejecutar.
* `5 (r-x)`: Otros pueden leer y ejecutar.

## 4. Cambiar propiedad

El comando `chown` (change owner) se usa para cambiar el propietario y/o grupo de un archivo o directorio. Este comando requiere privilegios de administrador (root), por lo que a menudo necesitarás usar `sudo`.

```bash
sudo chown newuser filename.txt
sudo chown newuser:newgroup filename.txt
```

* `newuser`: Cambia el propietario del archivo.
* `newuser:newgroup`: Cambia tanto el propietario como el grupo.

Este comando es especialmente útil cuando has creado un archivo como usuario root y necesitas dar a un usuario estándar la propiedad para poder editarlo.
