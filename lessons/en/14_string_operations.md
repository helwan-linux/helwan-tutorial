# String Operations in Bash

In Bash scripting, strings are a fundamental data type, and the shell provides a powerful set of built-in operations to manipulate them. Mastering these techniques is essential for any script that involves parsing text, processing file names, or handling user input.

---

## 1. Finding the Length of a String

To get the length of a string, you can use the `${#variable}` syntax. This is a simple and quick way to check the number of characters in a variable.

```bash
STR="Hello World"
echo ${#STR}
```

**Output:**

```
11
```

**Practical Example:** Validate user input to ensure a password meets a minimum length requirement.

```bash
#!/bin/bash
read -p "Enter a password (min 8 characters): " PASSWORD
if [ ${#PASSWORD} -lt 8 ]; then
  echo "Password is too short!"
else
  echo "Password accepted."
fi
```

---

## 2. Substring Extraction

Bash allows you to extract a portion of a string using the colon-based syntax: `${string:position:length}`.

* **position**: The starting index (0-based).
* **length**: Number of characters to extract.

```bash
echo ${STR:6:5}
```

**Output:**

```
World
```

**Practical Example:** Extract the file name from a full path.

```bash
#!/bin/bash
FULL_PATH="/home/user/documents/report.txt"
FILE_NAME=$(basename "$FULL_PATH")
echo "File Name: $FILE_NAME"
```

**Output:**

```
File Name: report.txt
```

---

## 3. String Replacement

You can replace parts of a string using the `${variable/pattern/replacement}` syntax.

```bash
echo ${STR/World/Bash}
```

**Output:**

```
Hello Bash
```

**Practical Example:** Sanitize URLs by removing the protocol.

```bash
#!/bin/bash
URL="https://www.example.com"
CLEAN_URL=${URL/https:\/\/}
echo "Clean URL: $CLEAN_URL"
```

**Output:**

```
Clean URL: www.example.com
```

---

## 4. String Comparison

Use `==` or `=` for string comparison inside `[ ]`. Always double-quote variables.

```bash
if [ "$STR" = "Hello World" ]; then
  echo "Strings are equal"
fi
```

**Practical Example:** Check if the user provided the correct secret key.

```bash
#!/bin/bash
SECRET_KEY="SuperSecret123"
read -p "Enter the secret key: " INPUT

if [ "$INPUT" == "$SECRET_KEY" ]; then
  echo "Access granted."
else
  echo "Access denied."
fi
```
