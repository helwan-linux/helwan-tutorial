# Lesson 16: File Operations in Bash

Working with files is common in Bash scripting.

## Checking if a file exists
```bash
if [ -f "myfile.txt" ]; then
  echo "File exists."
fi
```

## Reading a file line by line
```bash
while IFS= read -r line; do
  echo "$line"
done < "myfile.txt"
```

## Writing to a file
```bash
echo "Hello World" > output.txt
```

## Appending to a file
```bash
echo "Another line" >> output.txt
```

File manipulation is essential for automation and logging.