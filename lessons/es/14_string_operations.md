Operaciones de Cadenas de Texto en Bash
En la escritura de scripts de Bash, las cadenas de texto son un tipo de dato fundamental, y la shell proporciona un potente conjunto de operaciones integradas para manipularlas. Dominar estas técnicas es esencial para cualquier script que implique analizar texto, procesar nombres de archivos o manejar la entrada del usuario.

1. Encontrar la Longitud de una Cadena
Para obtener la longitud de una cadena, puedes usar la sintaxis ${#variable}. Esta es una forma simple y rápida de verificar el número de caracteres en una variable.

STR="Hello World"
echo ${#STR}

Salida:

11

Ejemplo práctico: Validar la entrada del usuario para asegurar que una contraseña cumpla con un requisito de longitud mínima.

#!/bin/bash
read -p "Enter a password (min 8 characters): " PASSWORD
if [ ${#PASSWORD} -lt 8 ]; then
  echo "Password is too short!"
else
  echo "Password accepted."
fi

2. Extracción de Subcadenas
Bash te permite extraer una porción de una cadena usando la sintaxis basada en dos puntos: ${string:position:length}.

position: El índice de inicio (basado en 0).

length: El número de caracteres a extraer.

echo ${STR:6:5}

Salida:

World

Ejemplo práctico: Extraer el nombre del archivo de una ruta completa.

#!/bin/bash
FULL_PATH="/home/user/documents/report.txt"
FILE_NAME=$(basename "$FULL_PATH")
echo "File Name: $FILE_NAME"

Salida:

File Name: report.txt

3. Reemplazo de Cadenas
Puedes reemplazar partes de una cadena usando la sintaxis ${variable/pattern/replacement}.

echo ${STR/World/Bash}

Salida:

Hello Bash

Ejemplo práctico: Sanitizar URLs eliminando el protocolo.

#!/bin/bash
URL="https://www.example.com"
CLEAN_URL=${URL/https:\/\/}
echo "Clean URL: $CLEAN_URL"

Salida:

Clean URL: www.example.com

4. Comparación de Cadenas
Usa == o = para la comparación de cadenas dentro de [ ]. Siempre pon las variables entre comillas dobles.

if [ "$STR" = "Hello World" ]; then
  echo "Strings are equal"
fi

Ejemplo práctico: Comprobar si el usuario proporcionó la clave secreta correcta.

#!/bin/bash
SECRET_KEY="SuperSecret123"
read -p "Enter the secret key: " INPUT

if [ "$INPUT" == "$SECRET_KEY" ]; then
  echo "Access granted."
else
  echo "Access denied."
fi
