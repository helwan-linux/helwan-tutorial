Lección 14: Permisos y Sudo
Los permisos de Linux controlan el acceso a archivos y directorios. Comprender los permisos es fundamental.

Tipos de Permisos
r: Permiso de lectura.

w: Permiso de escritura.

x: Permiso de ejecución.

Formato de Permisos
Ejemplo: -rwxr-xr--

Permisos del propietario: rwx

Permisos del grupo: r-x

Permisos de otros: r--

Cambio de Permisos
Usa el comando chmod:

chmod u+x script.sh  # Añadir permiso de ejecución para el propietario
chmod 755 file.txt   # Establecer permisos rwxr-xr-x

Cambio de Propiedad
Usa el comando chown:

sudo chown user:group file.txt

Uso de sudo
sudo ejecuta comandos como superusuario:

sudo apt update
sudo systemctl restart nginx

Resumen
Los permisos aseguran los archivos y sudo permite tareas administrativas de forma segura.