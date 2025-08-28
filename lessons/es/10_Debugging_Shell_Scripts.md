

Depuración de Scripts de Shell
La depuración es una habilidad crucial para cualquiera que escriba scripts de shell. Cuando un script no se comporta como se espera, estas técnicas te ayudan a identificar errores, rastrear la ejecución del script y señalar dónde algo salió mal.

1. Ejecutar un Script en Modo de Depuración
La forma más efectiva de depurar un script de shell es ejecutarlo con el flag -x. Esto activa el modo de rastreo, que imprime cada comando y sus argumentos en la terminal justo antes de ser ejecutado.

bash -x script.sh

Qué hace: La salida mostrará un símbolo + seguido de la línea de comando que se está ejecutando, incluyendo los valores de cualquier variable. Esto proporciona un rastreo claro, paso a paso, del flujo de tu script.

Ejemplo Práctico:

COUNT=1
echo "Count is $COUNT"

Salida de depuración:

+ COUNT=1
+ echo 'Count is 1'
Count is 1

Esto hace que sea fácil ver las asignaciones de variables y las expansiones a medida que suceden.

2. Usar echo para Rastrear
Para una depuración más específica o dirigida, insertar sentencias echo en tu script es una técnica simple pero poderosa.

echo "Reached here"

Qué hace: El comando echo imprime un mensaje en la consola. Al colocar estos mensajes estratégicamente, puedes confirmar qué partes de tu código se están ejecutando y ver el valor de una variable en un punto específico.

Ejemplo Práctico:

#!/bin/bash
echo "Script started."

# Check if a file exists
if [ -f "my_file.txt" ]; then
  echo "File exists. Processing..."
  # ... further commands
else
  echo "File not found. Exiting."
  exit 1
fi

Este enfoque te ayuda a acotar rápidamente un problema al mostrar qué camino condicional está tomando el script.

3. Activar y Desactivar el Modo de Depuración Dentro de un Script
Para tener más control, puedes activar el modo de depuración para una sección específica de tu script en lugar de todo el archivo.

Activar la depuración: Agrega set -x antes de la sección que quieres depurar.

Desactivar la depuración: Agrega set +x después de la sección.

Ejemplo Práctico:

#!/bin/bash
# Regular script commands...

echo "Starting debug section for file processing."
set -x  # Turn on debug mode

# Debug this part
for file in *.log; do
  # ... commands
done

set +x  # Turn off debug mode
echo "Finished debug section."

Este método mantiene la salida de tu script limpia al mostrar el rastreo solo para las partes que estás solucionando activamente.

