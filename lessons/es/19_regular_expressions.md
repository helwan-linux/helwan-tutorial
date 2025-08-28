Expresiones Regulares (Regex) en Bash
Las expresiones regulares (regex) son un potente conjunto de herramientas para la coincidencia de patrones y la manipulación de texto. En la programación de scripts de Bash, te permiten buscar, validar y analizar cadenas con una precisión increíble. Dominar las regex es esencial para cualquier tarea seria de procesamiento de texto, como el manejo de archivos de registro, la validación de la entrada del usuario o la extracción de datos estructurados.

1. Uso de grep con Regex
El comando grep es la utilidad clásica de Linux para buscar texto usando patrones. Puedes habilitar el soporte para expresiones regulares extendidas con la bandera -E, que permite patrones más avanzados.

grep -E "^[a-z]+@[a-z]+\\.com$"

Brillante Ejemplo Práctico: Un administrador de sistemas necesita filtrar rápidamente un archivo de registro para encontrar todas las entradas que contengan una dirección de correo electrónico válida. La bandera -E se usa para interpretar el patrón regex, y los anclajes ^ y $ aseguran que toda la línea sea un correo electrónico válido.

#!/bin/bash

# The log file to search
LOG_FILE="application.log"

echo "Searching for valid email addresses in $LOG_FILE..."

# The regex pattern matches a string that starts with one or more letters,
# followed by an @, then more letters, and ends with .com
grep -E "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$" "$LOG_FILE"

echo "Search complete."

Este ejemplo utiliza un patrón regex más completo para coincidir con un rango más amplio de direcciones de correo electrónico válidas, demostrando el poder de la herramienta.

2. Coincidencia de Regex de Bash con [[...]]
Bash tiene soporte incorporado para la coincidencia de regex usando el operador =~ dentro de un bloque [[...]]. Esto te permite integrar regex directamente en la lógica condicional de tus scripts sin la necesidad de herramientas externas.

if [[ "Hello World" =~ "World" ]]; then
  echo "String contains 'World'"
fi

Brillante Ejemplo Práctico
Un script que le pide al usuario una dirección de correo electrónico y la valida antes de continuar.

#!/bin/bash

read -p "Enter your email address: " EMAIL

# Regex pattern for a simple email validation
if [[ "$EMAIL" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$ ]]; then
  echo "✅ Email address '$EMAIL' is valid."
else
  echo "❌ Error: Invalid email format. Please try again." >&2
  exit 1
fi

3. Extracción de Subcadenas
Cuando realizas una coincidencia de regex usando el operador =~ dentro de un bloque [[...]], cualquier grupo capturado (partes del patrón encerradas entre paréntesis) se almacena automáticamente en el array BASH_REMATCH. Esta es una característica increíblemente poderosa para analizar y extraer piezas específicas de información de una cadena.

if [[ "$string" =~ ([0-9]+) ]]; then
  echo "Number: ${BASH_REMATCH[1]}"
fi

Brillante Ejemplo Práctico: Un script que procesa una cadena de entrada de registro, extrae la marca de tiempo y el código de estado, y luego utiliza esa información para un procesamiento posterior.

#!/bin/bash

LOG_ENTRY="[2023-08-25 10:30:00] - Request to /api/users successful with status 200"

# Regex to capture the timestamp and the status code
REGEX_PATTERN="^\\[([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})\\] .* status ([0-9]+)$"

if [[ "$LOG_ENTRY" =~ $REGEX_PATTERN ]]; then
  # The captured groups are stored in BASH_REMATCH
  TIMESTAMP="${BASH_REMATCH[1]}"
  STATUS_CODE="${BASH_REMATCH[2]}"

  echo "Timestamp: $TIMESTAMP"
  echo "Status Code: $STATUS_CODE"
  
  # You can now use these variables for further processing
  if [ "$STATUS_CODE" -eq 200 ]; then
    echo "Processing successful request data..."
  fi
else
  echo "Could not parse the log entry."
fi
