Arrays en Bash
Los arrays en Bash son una característica poderosa para almacenar colecciones de valores en una sola variable, lo que los hace ideales para gestionar listas de datos en tus scripts. En lugar de tratar cada valor como una variable separada, los arrays te permiten acceder y manipular datos de una manera organizada y eficiente.

1. Declarar Arrays
Puedes declarar un array unidimensional asignándole una lista de valores. Los elementos se colocan dentro de paréntesis () y se separan por espacios.

FRUITS=("apple" "banana" "cherry")

Ejemplo práctico: Imagina que tienes una lista de nombres de servidores que necesitas verificar. Puedes almacenarlos en un array para simplificar el proceso.

#!/bin/bash
# Declare an array of server names
SERVERS=("web-server-01" "db-server-01" "app-server-02")

# You can print the entire array
echo "Server list: ${SERVERS[@]}"

2. Acceder a Elementos
Para acceder a un elemento individual del array, usa su índice (posición) que comienza desde 0.

echo ${FRUITS[1]}
# Output: banana

Ejemplo práctico: Acceder al primer y tercer elemento del array SERVERS.

#!/bin/bash
SERVERS=("web-server-01" "db-server-01" "app-server-02")

# Access the first element (index 0)
echo "First server: ${SERVERS[0]}"

# Access the third element (index 2)
echo "Third server: ${SERVERS[2]}"

3. Agregar Elementos
Puedes agregar nuevos elementos a un array existente usando el operador +=.

FRUITS+=("date")

Ejemplo práctico: Agregar un nuevo servidor al array SERVERS existente.

#!/bin/bash
SERVERS=("web-server-01" "db-server-01")
echo "Server list before adding: ${SERVERS[@]}"

# Add a new server
SERVERS+=("monitoring-server-03")

echo "Server list after adding: ${SERVERS[@]}"

4. Recorrer Arrays
Para iterar sobre todos los elementos de un array, puedes usar un bucle for con el símbolo [@], que representa todos los elementos.

for fruit in "${FRUITS[@]}"; do
  echo "Fruit: $fruit"
done

Brillante Ejemplo Práctico: Hagamos una verificación de ping en cada servidor de nuestro array. Este tipo de script es esencial para monitorear la salud de la red.

#!/bin/bash

# List of server names
SERVERS=("web-server-01" "db-server-01" "google.com")

# Loop through each server in the array
for server in "${SERVERS[@]}"; do
  echo "Pinging server: $server..."

  # Send a single ping packet (-c 1) and redirect output to null
  ping -c 1 "$server" &> /dev/null

  # Check the exit status of the last command
  if [ $? -eq 0 ]; then
    echo "✅ Successfully connected to: $server"
  else
    echo "❌ Failed to connect to: $server"
  fi

  echo "---"
done

Este ejemplo demuestra cómo los arrays simplifican tareas complejas que requieren iteración sobre una lista de datos.