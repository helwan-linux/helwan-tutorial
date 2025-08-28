Operaciones de Archivos en Bash
Trabajar con archivos es un aspecto fundamental de cualquier script de shell. Bash proporciona un potente conjunto de comandos y sintaxis integrados para verificar la existencia de archivos, leer contenido y escribir en archivos. Dominar estas operaciones es crucial para tareas como la automatización, el procesamiento de datos y el registro.

1. Comprobar si un Archivo Existe
Antes de que un script intente leer o escribir en un archivo, es una buena práctica verificar primero que el archivo existe. La sintaxis [ -f "filename" ] se utiliza para comprobar si un archivo regular existe y no es un directorio.

if [ -f "myfile.txt" ]; then
  echo "File exists."
fi

Brillante Ejemplo Práctico: Un script que comprueba la presencia de un archivo de configuración antes de intentar iniciar un servicio. Esto evita que el script falle con un error.

#!/bin/bash
CONFIG_FILE="/etc/my_app/config.conf"

if [ -f "$CONFIG_FILE" ]; then
  echo "Configuration file found. Starting application..."
  # Start the application or service here
else
  echo "Error: Configuration file not found at $CONFIG_FILE" >&2
  exit 1
fi

2. Leer un Archivo Línea por Línea
Leer un archivo línea por línea es una tarea común para procesar archivos de registro o informes de datos. El bucle while combinado con read es la forma más robusta y eficiente de manejar esto, evitando problemas con caracteres especiales y espacios.

while IFS= read -r line; do
  echo "$line"
done < "myfile.txt"

IFS=: Establece temporalmente el Separador de Campo Interno en nulo, lo que evita que se recorten los espacios en blanco iniciales/finales.

-r: Evita que las secuencias de escape de barra invertida sean interpretadas.

done < "myfile.txt": Redirige el contenido del archivo a la entrada estándar del bucle while.

Brillante Ejemplo Práctico: Un script que procesa una lista de nombres de usuario de un archivo y crea un nuevo usuario para cada uno.

#!/bin/bash
USER_LIST_FILE="new_users.txt"

if [ ! -f "$USER_LIST_FILE" ]; then
  echo "Error: User list file not found!" >&2
  exit 1
fi

while IFS= read -r username; do
  echo "Creating user account for: $username"
  sudo useradd -m "$username"
done < "$USER_LIST_FILE"

echo "User creation process completed."

3. Escribir en un Archivo
Para escribir contenido en un archivo, se utiliza el operador de redirección de salida >. Este operador sobrescribirá el contenido del archivo si ya existe.

echo "Hello World" > output.txt

Brillante Ejemplo Práctico: Un script que genera un archivo de registro con una marca de tiempo y un mensaje de estado.

#!/bin/bash
LOG_FILE="server_status.log"

# Sobrescribir el archivo de registro con un nuevo encabezado
echo "--- Server Status Report ---" > "$LOG_FILE"

# Comprobar el estado del servidor y adjuntar el resultado
if ping -c 1 example.com &> /dev/null; then
  echo "Timestamp: $(date)" >> "$LOG_FILE"
  echo "Status: OK - Server is reachable." >> "$LOG_FILE"
else
  echo "Timestamp: $(date)" >> "$LOG_FILE"
  echo "Status: ERROR - Server is unreachable!" >> "$LOG_FILE"
fi

4. Adjuntar a un Archivo
Si quieres añadir contenido al final de un archivo sin sobrescribir su contenido existente, utilizas el operador de redirección de adjuntar >>. Esto es esencial para el registro y la creación de informes continuos.

echo "Another line" >> output.txt

Brillante Ejemplo Práctico: Un script que registra todos los intentos de copia de seguridad exitosos y fallidos en un único archivo de registro continuo.

#!/bin/bash
BACKUP_LOG="backup_history.log"
BACKUP_DIR="/var/www/data"

# Realizar la copia de seguridad
tar -czf "backup_$(date +%Y-%m-%d).tar.gz" "$BACKUP_DIR" &> /dev/null

# Comprobar el estado de salida y adjuntar una línea de estado al archivo de registro
if [ $? -eq 0 ]; then
  echo "$(date): Backup of $BACKUP_DIR was successful." >> "$BACKUP_LOG"
else
  echo "$(date): ERROR: Backup of $BACKUP_DIR failed!" >> "$BACKUP_LOG"
fi
