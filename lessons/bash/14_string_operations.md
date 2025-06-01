# Lesson 14: String Operations in Bash

Strings in Bash can be manipulated in several ways.

## Length of a string
```bash
STR="Hello World"
echo ${#STR}  # Outputs 11
```

## Substring extraction
```bash
echo ${STR:6:5}  # Outputs "World"
```

## String replacement
```bash
echo ${STR/World/Bash}  # Outputs "Hello Bash"
```

## String comparison
```bash
if [ "$STR" = "Hello World" ]; then
  echo "Strings are equal"
fi
```

Mastering string operations helps in text processing scripts.