# Shell Scripting Basics

Shell scripting is a powerful way to automate repetitive tasks in Linux by writing a sequence of commands in a file that the shell can execute.

## Variables

Variables are used to store data that can be reused throughout the script. You assign values without spaces around the = sign:

NAME="Helwan"
AGE=25

To access the value of a variable, prefix it with $:

echo "Hello, $NAME! You are $AGE years old."

## Conditional Statements

Conditional statements allow you to make decisions in your script.

Example of an if statement:

if [ $AGE -ge 18 ]; then
  echo "You are an adult."
else
  echo "You are a minor."
fi

The square brackets [ ] are a synonym for the test command. You can use operators like:
- -eq (equal)
- -ne (not equal)
- -lt (less than)
- -le (less or equal)
- -gt (greater than)
- -ge (greater or equal)

## Loops

Loops help you execute commands multiple times.

Example of a for loop:

for i in 1 2 3 4 5
do
  echo "Number $i"
done

Example of a while loop:

count=1
while [ $count -le 5 ]
do
  echo "Count is $count"
  ((count++))
done

## Functions

Functions are reusable blocks of code.

Define a function:

greet() {
  echo "Hello, $1!"
}

Call a function with an argument:

greet "User"

The $1 represents the first argument passed to the function.

## Comments

Comments start with # and are ignored by the shell. Use comments to explain your code.

# This is a comment


echo "Hello World"  # This prints a message



#🧪 Useful Commands (Aliases)

alias sync = "sudo pacman -Syyy"

alias install = "sudo pacman -S"

alias update = "sudo pacman -Syyu"

alias search = "sudo pacman -Ss" 

alias search-local = "sudo pacman -Qs" 

alias pkg-info = "sudo pacman -Qi"

alias local-install = "sudo pacman -U" 

alias helwan = "uname -a"
