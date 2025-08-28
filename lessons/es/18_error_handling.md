Manejo de Errores en Scripts de Bash
El manejo adecuado de errores es una habilidad crucial para escribir scripts de shell robustos y fiables. Al anticipar y gestionar posibles fallos, puedes asegurarte de que tus scripts se comporten de forma predecible, proporcionen retroalimentación útil y eviten la corrupción de datos o un comportamiento inesperado del sistema.

1. Comprobación del Estado de Salida
Después de la ejecución de cada comando, se establece una variable especial $? en su estado de salida. Un valor de 0 indica éxito, mientras que cualquier otro valor (generalmente de 1 a 255) indica un fallo. La comprobación de este estado te permite crear una lógica condicional que responda a los fallos de los comandos.

command
if [ $? -ne 0 ]; then
  echo "Command failed."
fi

Brillante Ejemplo Práctico
Un script que intenta descargar un archivo y luego procede a procesarlo solo si la descarga fue exitosa.

#!/bin/bash

# Intenta descargar un archivo
wget -q http://example.com/data.txt

# Comprueba el estado de salida del comando wget
if [ $? -ne 0 ]; then
  echo "Error: Falló la descarga del archivo de la fuente." >&2
  exit 1
else
  echo "Archivo descargado con éxito. Procesando..."
  # Añade más comandos para procesar el archivo aquí
fi

2. Usando set -e
El comando set -e, también conocido como salir en caso de error, es una directiva poderosa que fuerza a un script a salir inmediatamente si algún comando falla. Esta es una excelente manera de evitar que un script continúe con una operación potencialmente peligrosa después de que un paso anterior haya fallado.

set -e

Brillante Ejemplo Práctico
Un script que realiza una serie de tareas críticas, como crear un directorio, copiar un archivo y luego comprimirlo. Si cualquiera de estos pasos falla, el script debe detenerse para evitar un estado inconsistente.

#!/bin/bash
# Salir inmediatamente si un comando falla
set -e

# Crear un directorio para la copia de seguridad
mkdir /tmp/backup_data

# Copiar un archivo crítico. Si esto falla, el script saldrá.
cp /var/log/syslog /tmp/backup_data/

# Comprimir el directorio. Esto no se ejecutará si el comando 'cp' falla.
tar -czf /root/backup.tar.gz /tmp/backup_data

echo "¡Copia de seguridad completada con éxito!"

3. Atrapando Errores
El comando trap te permite ejecutar un comando o función específica cuando se recibe una señal. La señal ERR es particularmente útil para el manejo de errores, ya que se activa cada vez que un comando sale con un estado no nulo.

trap 'echo "Error ocurrido!"' ERR

Brillante Ejemplo Práctico
Un script que necesita limpiar archivos temporales si ocurre un error durante su ejecución. El comando trap asegura que la función de limpieza sea llamada sin importar dónde falle el script.

#!/bin/bash

# Define una función para manejar la limpieza
cleanup() {
  echo "Ocurrió un error. Limpiando archivos temporales..." >&2
  rm -f /tmp/temp_file_*
}

# Establece el trap para llamar a la función de limpieza en cualquier error
trap cleanup ERR

echo "Iniciando script..."

# Un comando que probablemente fallará, activando el trap
touch /root/temp_file_1

echo "Esta línea no se alcanzará si el comando anterior falla."

4. Mensajes de Error Personalizados
Si bien set -e y trap son poderosos, puedes mejorar tu manejo de errores creando una función personalizada para proporcionar mensajes de error más descriptivos. Esta función puede imprimir un mensaje en el error estándar (stderr) y luego salir del script.

function error_exit {
  echo "$1" 1>&2
  exit 1
}

Brillante Ejemplo Práctico
Un script que valida los argumentos de la línea de comandos y proporciona un mensaje de uso útil si el usuario proporciona una entrada incorrecta.

#!/bin/bash

# Define una función personalizada para errores
function error_exit() {
  echo "Error: $1" >&2
  exit 1
}

# Comprueba si se proporciona el número correcto de argumentos
if [ "$#" -ne 2 ]; then
  error_exit "Número de argumentos incorrecto. Uso: $0 <directorio_origen> <directorio_destino>"
fi

SOURCE_DIR="$1"
DEST_DIR="$2"

# Comprueba si el directorio de origen existe
if [ ! -d "$SOURCE_DIR" ]; then
  error_exit "El directorio de origen '$SOURCE_DIR' no existe."
fi

echo "El script se está ejecutando con argumentos válidos."
# ... resto del script ...
