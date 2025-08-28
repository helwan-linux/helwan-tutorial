Manejo de Procesos en Bash
Manejar procesos es una parte vital del uso de la línea de comandos de Linux. Esta habilidad te permite controlar los programas que se ejecutan en tu sistema, lo que te permite ejecutar tareas en segundo plano, terminar procesos que no responden y monitorear el rendimiento del sistema.

1. Ejecutar un Comando en Segundo Plano
Cuando añades el símbolo & al final de un comando, lo ejecutas en segundo plano. Esto te devuelve inmediatamente el control de la línea de comandos sin esperar a que el comando termine. Esto es útil para operaciones de larga duración que no requieren tu interacción.

Ejemplo:

sleep 60 &

Ejemplo práctico: Ejecutar una descarga en segundo plano.

# Ejecutar el comando de descarga en segundo plano
wget https://example.com/large_file.zip &

# Ahora puedes escribir otros comandos inmediatamente
echo "Descarga iniciada en segundo plano. Puedes seguir trabajando ahora."

2. Listar Trabajos en Segundo Plano
Para listar todas las tareas que se ejecutan actualmente en segundo plano en tu sesión actual, usa el comando jobs. Esto proporciona una lista de procesos con su ID de trabajo y estado.

Ejemplo:

jobs

Ejemplo práctico:

# Iniciar dos procesos en segundo plano
./script_one.sh &
./script_two.sh &

# Ver la lista de trabajos
jobs
# La salida podría verse así:
# [1]-  Running                 ./script_one.sh &
# [2]+  Running                 ./script_two.sh &

El ID de trabajo ([1], [2]) es útil para controlar estas tareas.

3. Traer un Trabajo a Primer Plano
Si quieres recuperar el control de una tarea en segundo plano, usa el comando fg (foreground) seguido del ID de trabajo. Esto trae la tarea a primer plano, permitiéndote interactuar con ella de nuevo.

Ejemplo:

fg %1

Ejemplo práctico:

# Ejecutar un proceso en segundo plano
./interactive_script.sh &
# [1] 1234

# Traer el proceso de vuelta a primer plano
fg %1

El %1 se refiere al primer trabajo en la lista de trabajos.

4. Matar un Proceso
Si un proceso no responde o consume recursos excesivos, puedes terminarlo usando el comando kill con su ID de Proceso (PID). Puedes encontrar el PID usando los comandos ps aux o top.

Ejemplo:

kill PID

Ejemplo práctico:

# Encontrar el PID del proceso `firefox`
ps aux | grep firefox
# Ejemplo de salida:
# user      1500  ... /usr/bin/firefox ...

# Terminar el proceso usando su PID
kill 1500

# Si el proceso no se detiene, usa la terminación forzada
kill -9 1500

⚠️ Usar kill -9 debe ser el último recurso, ya que no permite que el proceso guarde su trabajo antes de salir.