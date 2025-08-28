Técnicas avanzadas de Shell Scripting
Dominar las técnicas avanzadas de Shell Scripting es un cambio de juego para automatizar tareas complejas y escribir scripts más eficientes y poderosos. Estas técnicas van más allá de los comandos básicos, dándote las herramientas para manejar datos, realizar cálculos y gestionar colecciones de valores.

1. Sustitución de Comandos (Command Substitution)
La sustitución de comandos te permite capturar la salida de un comando y usarla como el valor de una variable. Esta es una técnica fundamental para la escritura de scripts dinámicos.

Puedes usar la sintaxis moderna $(...) o los backticks antiguos .... Se recomienda la sintaxis $(...) ya que es más fácil de anidar y leer.

output=$(ls -l)

Ejemplo práctico: Almacena la fecha de hoy en una variable y úsala para el nombre de un archivo de registro.

#!/bin/bash
# Almacena la fecha actual en una variable
today=$(date +%Y-%m-%d)

# Usa la variable para crear un archivo de registro
LOG_FILE="backup_log_${today}.txt"
echo "Backup started on $(date)" > $LOG_FILE

2. Operaciones Aritméticas (Arithmetic Operations)
Los scripts de Shell pueden realizar operaciones aritméticas básicas usando la sintaxis $((...)). Esto es esencial para cálculos como contadores o porcentajes.

result=$(( 3 + 5 ))

Ejemplo práctico: Calcula el porcentaje de uso del espacio en disco.

#!/bin/bash
TOTAL_SPACE=1000
USED_SPACE=$(df -h | grep "/dev/sda1" | awk '{print $3}' | sed 's/G//')

# Nota: Usa `bc` para aritmética de punto flotante.
PERCENTAGE=$(( ($USED_SPACE * 100) / $TOTAL_SPACE ))

echo "Used space: ${USED_SPACE}G"
echo "Percentage of total space used: ${PERCENTAGE}%"

3. Arreglos (Arrays)
Los arreglos te permiten almacenar múltiples valores en una sola variable, ideal para gestionar listas.

my_array=(one two three)

Acceder a elementos:

echo ${my_array[1]} # imprime 'two'

Todos los elementos:

echo ${my_array[@]} # imprime 'one two three'

Longitud del arreglo:

echo ${#my_array[@]} # imprime '3'

Ejemplo práctico: Itera a través de una lista de servidores y hazles ping.

#!/bin/bash
SERVERS=("web-server-1" "db-server" "app-server-alpha")

for server in "${SERVERS[@]}"; do
  echo "Haciendo ping a ${server}..."
  ping -c 1 "${server}"
  if [ $? -eq 0 ]; then
    echo "${server} está activo."
  else
    echo "${server} está inactivo!"
  fi
done

Esto demuestra cómo los arreglos facilitan la gestión y el bucle a través de una lista de elementos, haciendo que tus scripts sean más escalables y fáciles de mantener.