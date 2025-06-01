# Lesson 13: Advanced Variables in Bash

In Bash scripting, variables can hold strings, numbers, or even command outputs.

## Command substitution
You can assign the output of a command to a variable using $(...):

```bash
CURRENT_DATE=$(date)
echo "Today is $CURRENT_DATE"
```

## Readonly variables
To make a variable read-only, use `readonly`:

```bash
readonly PI=3.14159
# PI=3  # This will cause an error
```

## Exporting variables
Use `export` to make a variable available to child processes:

```bash
export PATH=$PATH:/my/custom/path
```

## Unsetting variables
Use `unset` to delete a variable:

```bash
unset VARIABLE_NAME
```

Use variables carefully to avoid conflicts and keep your scripts clean.