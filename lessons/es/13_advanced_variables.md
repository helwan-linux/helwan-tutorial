Variables Avanzadas en Bash
En el entorno de la línea de comandos de Bash, las variables son herramientas fundamentales para almacenar datos. Comprender los tipos de variables avanzadas y cómo manejarlas te da un mayor control sobre tus scripts, haciéndolos más dinámicos y poderosos.

1. Sustitución de Comandos (Command Substitution)
La sustitución de comandos es una técnica que te permite asignar la salida de un comando a una variable. Esta es una característica poderosa para ejecutar un comando en tiempo de ejecución y almacenar su salida para su uso posterior en tu script.

Puedes usar la sintaxis moderna $(...) o los backticks antiguos .... Se prefiere la sintaxis moderna $(...) porque es más fácil de leer y se puede anidar.

Ejemplo:

CURRENT_DATE=$(date)

Brillante Ejemplo Práctico: Imagina que necesitas crear una copia de seguridad diaria y nombrarla basándote en la fecha actual. Puedes usar la sustitución de comandos para establecer automáticamente el nombre del archivo.

#!/bin/bash
# Almacenar la fecha actual en una variable
BACKUP_DATE=$(date +%Y-%m-%d)

# Usar la variable para determinar el nombre del archivo
BACKUP_FILE="backup_data_${BACKUP_DATE}.zip"

# Crear el archivo comprimido con el nombre dinámico
tar -czf "$BACKUP_FILE" /var/www/html/
echo "Backup file created: $BACKUP_FILE"

2. Variables de Solo Lectura (Read-only Variables)
Si quieres asegurarte de que el valor de una variable no se pueda cambiar por error en un script largo, puedes hacerla de solo lectura usando el comando readonly.

Ejemplo:

readonly PI=3.14159

Nota: Cualquier intento de cambiar el valor de esta variable (por ejemplo, PI=3) resultará en un error.

Brillante Ejemplo Práctico: En un script de administración de sistemas, podrías necesitar definir rutas sensibles que nunca deberían ser alteradas. Hacer que estas variables sean de solo lectura añade una capa de seguridad para prevenir modificaciones accidentales.

#!/bin/bash

# Definir el directorio de registro principal y hacerlo de solo lectura
readonly LOG_DIR="/var/log/my_app/"

# Intentar escribir un archivo de registro
echo "Application started." >> "${LOG_DIR}app.log"

# Si alguien intenta cambiar la ruta, fallará
# LOG_DIR="/tmp/" # Esta línea causará un error

3. Exportar Variables (Exporting Variables)
Por defecto, las variables en un script solo están disponibles dentro de ese script. Para hacer que una variable esté disponible para los procesos hijos que se ejecutan desde el script, debes exportarla usando el comando export.

Ejemplo:

export PATH=$PATH:/my/custom/path

Brillante Ejemplo Práctico: Supón que tienes un script principal que lanza un script hijo, y necesitas pasar una variable de entorno al script hijo.

Script Padre (parent_script.sh):

#!/bin/bash

# Definir y exportar una variable
export API_KEY="a1b2c3d4e5f6"

# Ejecutar el script hijo
./child_script.sh

Script Hijo (child_script.sh):

#!/bin/bash

# La variable exportada ahora es accesible
echo "API Key is: $API_KEY"

Gracias a export, child_script.sh puede acceder al valor de API_KEY.

4. Desestablecer Variables (Unsetting Variables)
Para eliminar una variable de la memoria y desdefinirla por completo, puedes usar el comando unset. Esto es útil para liberar memoria o para asegurarse de que una variable antigua no se use por error.

Ejemplo:

unset VARIABLE_NAME

Brillante Ejemplo Práctico: Después de usar una variable que contiene una contraseña u otra información sensible, es una buena práctica eliminarla de la memoria.

#!/bin/bash

# Una variable que contiene una contraseña
SECRET_PASSWORD="my_super_secret_password"

# Usar la contraseña (en este caso, imprimirla)
echo "Using password..."

# Eliminar la variable de la memoria
unset SECRET_PASSWORD

# Cualquier intento de acceder a la variable fallará
echo "Password variable is: $SECRET_PASSWORD"
# La línea anterior se mostrará en blanco o como un valor nulo
