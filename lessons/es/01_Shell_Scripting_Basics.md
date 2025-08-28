---

# Shell Scripting Basics (Spanish)

La programación de scripts en Shell es una manera poderosa de automatizar tareas repetitivas en Linux escribiendo una secuencia de comandos en un archivo que el shell puede ejecutar.

## Variables

Las variables se utilizan para almacenar datos que se pueden reutilizar en todo el script. Asigna valores sin espacios alrededor del signo =:

NAME="Helwan"
AGE=25

Para acceder al valor de una variable, pon \$ delante:

echo "¡Hola, \$NAME! Tienes \$AGE años."

## Sentencias Condicionales

Las sentencias condicionales permiten tomar decisiones en el script.

Ejemplo de una sentencia if:

if \[ \$AGE -ge 18 ]; then
echo "Eres adulto."
else
echo "Eres menor de edad."
fi

Los corchetes \[ ] son sinónimo del comando test. Puedes usar operadores como:

* -eq (igual)
* -ne (no igual)
* -lt (menor que)
* -le (menor o igual)
* -gt (mayor que)
* -ge (mayor o igual)

## Bucles

Los bucles te ayudan a ejecutar comandos varias veces.

Ejemplo de un bucle for:

for i in 1 2 3 4 5
do
echo "Número \$i"
done

Ejemplo de un bucle while:

count=1
while \[ \$count -le 5 ]
do
echo "Contador es \$count"
((count++))
done

## Funciones

Las funciones son bloques de código reutilizables.

Definir una función:

greet() {
echo "¡Hola, \$1!"
}

Llamar a una función con un argumento:

greet "Usuario"

\$1 representa el primer argumento pasado a la función.

## Comentarios

Los comentarios comienzan con # y son ignorados por el shell. Úsalos para explicar tu código.

# Esto es un comentario

echo "Hola Mundo"  # Esto imprime un mensaje

---

## 🧪 Comandos Útiles (Aliases)

```bash
alias sync="sudo pacman -Syyy"
alias install="sudo pacman -S"
alias update="sudo pacman -Syyu"
alias search="sudo pacman -Ss"
alias search-local="sudo pacman -Qs"
alias pkg-info="sudo pacman -Qi"
alias local-install="sudo pacman -U"
alias helwan="uname -a"
```
