Comandos Básicos de Arch Linux
Arch Linux es una distribución de Linux ligera y flexible que sigue la filosofía "Keep It Simple, Stupid" (KISS). Aunque ofrece un gran control, su enfoque centrado en la línea de comandos requiere una buena comprensión de sus utilidades principales. Aquí están los comandos esenciales para empezar y gestionar tu sistema.

1) Actualización del Sistema y Gestión de Paquetes
Pacman es el potente gestor de paquetes de Arch. Estos comandos son críticos para mantener tu sistema actualizado e instalar nuevo software.

Actualizar la Base de Datos de Paquetes
sudo pacman -Sy

Este comando sincroniza tu base de datos local de paquetes con los repositorios de Arch. Es un paso rápido y esencial para obtener información sobre las últimas versiones de software.

Actualizar Todos los Paquetes Instalados
sudo pacman -Syu

Este es el comando más común para un usuario de Arch. La bandera -S es para sincronización e instalación, -y es para refrescar la lista de paquetes y -u es para actualizar el sistema. Actualiza todos los paquetes instalados a sus versiones más nuevas después de actualizar la base de datos.

Instalar un Paquete
sudo pacman -S package_name

Este comando instala un nuevo paquete y todas sus dependencias requeridas.

Ejemplo:

sudo pacman -S neofetch

Eliminar un Paquete
sudo pacman -R package_name

Elimina el paquete especificado.

Para eliminaciones más exhaustivas:

sudo pacman -Rs package_name   # Eliminar paquete + dependencias innecesarias
sudo pacman -Rns package_name  # Eliminar paquete + dependencias innecesarias + archivos de configuración

Buscar un Paquete
pacman -Ss keyword

Busca en la base de datos de paquetes aquellos que coincidan con la palabra clave.

Listar Paquetes Instalados
pacman -Q

Lista todos los paquetes instalados actualmente en tu sistema.

2) Información del Sistema
Comandos que te dan una visión general rápida del estado del sistema y el uso de recursos.

Comprobar la Versión del Kernel
uname -r

Muestra la versión del kernel de Linux que se está ejecutando actualmente.

Comprobar el Tiempo de Actividad del Sistema (Uptime)
uptime

Muestra cuánto tiempo ha estado funcionando el sistema, el número de usuarios conectados y los promedios de carga.

Mostrar el Uso del Disco
df -h

Muestra el uso del espacio en disco de los sistemas de archivos montados en un formato legible por humanos.

Mostrar el Uso de la Memoria
free -h

Muestra la memoria total, usada y libre en un formato legible por humanos.

3) Gestión de Usuarios y Permisos
Comandos para gestionar cuentas de usuario y privilegios.

Añadir un Nuevo Usuario
sudo useradd -m username

Crea una nueva cuenta de usuario (-m crea el directorio de inicio).

Establecer Contraseña para un Usuario
sudo passwd username

Establece una contraseña para el usuario.

Modificar Usuario (Añadir a un Grupo)
sudo usermod -aG groupname username

Añade al usuario a un grupo suplementario (-aG para añadir al grupo).

4) Control del Sistema (systemd)
Arch Linux usa systemd para gestionar servicios. systemctl es la CLI para controlar servicios.

Iniciar / Detener / Reiniciar un Servicio
sudo systemctl start service_name
sudo systemctl stop service_name
sudo systemctl restart service_name

Controla el estado de ejecución de un servicio.

Habilitar / Deshabilitar Servicio al Inicio
sudo systemctl enable service_name
sudo systemctl disable service_name
```enable` inicia el servicio automáticamente al arrancar; `disable` evita que se inicie automáticamente.

---

## 5) Varios

Comandos adicionales útiles para tareas de administración comunes.

### Ver los Registros del Sistema

```bash
journalctl -xe

Muestra las entradas de registro del sistema del journal de systemd (-x añade contexto extra, -e salta al final).

Montar un Sistema de Archivos
sudo mount /dev/sdXY /mnt

Monta un dispositivo (p.ej., una unidad USB o una partición) en el punto de montaje especificado.

Desmontar un Sistema de Archivos
sudo umount /mnt

Desmonta un sistema de archivos de su punto de montaje, lo cual es necesario antes de retirar físicamente un dispositivo.