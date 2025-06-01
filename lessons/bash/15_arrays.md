# Lesson 15: Arrays in Bash

Bash supports one-dimensional arrays.

## Declaring arrays
```bash
FRUITS=("apple" "banana" "cherry")
```

## Accessing elements
```bash
echo ${FRUITS[1]}  # Outputs banana
```

## Adding elements
```bash
FRUITS+=("date")
```

## Looping through arrays
```bash
for fruit in "${FRUITS[@]}"; do
  echo "Fruit: $fruit"
done
```

Arrays are useful for handling lists of data in your scripts.