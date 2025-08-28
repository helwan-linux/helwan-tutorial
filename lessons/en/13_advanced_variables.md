# Advanced Variables in Bash

In the Bash command-line environment, variables are fundamental tools for storing data. Understanding advanced variable types and how to handle them gives you greater control over your scripts, making them more dynamic and powerful.

---

## 1. Command Substitution

Command substitution is a technique that lets you assign the output of a command to a variable. This is a powerful feature for running a command at runtime and storing its output for later use in your script.

You can use either the modern `$(...)` syntax or the older backticks `...`. The modern `$(...)` syntax is preferred because it is easier to read and can be nested.

**Example:**

```bash
CURRENT_DATE=$(date)
```

**Brilliant Practical Example:** Imagine you need to create a daily backup and name it based on the current date. You can use command substitution to automatically set the file name.

```bash
#!/bin/bash
# Store the current date in a variable
BACKUP_DATE=$(date +%Y-%m-%d)

# Use the variable to determine the file name
BACKUP_FILE="backup_data_${BACKUP_DATE}.zip"

# Create the compressed file with the dynamic name
tar -czf "$BACKUP_FILE" /var/www/html/
echo "Backup file created: $BACKUP_FILE"
```

---

## 2. Read-only Variables

If you want to ensure a variable's value cannot be changed by mistake in a long script, you can make it read-only using the `readonly` command.

**Example:**

```bash
readonly PI=3.14159
```

**Note:** Any attempt to change the value of this variable (e.g., `PI=3`) will result in an error.

**Brilliant Practical Example:** In a system administration script, you might need to define sensitive paths that should never be altered. Making these variables read-only adds a layer of security to prevent accidental modifications.

```bash
#!/bin/bash

# Define the core log directory and make it read-only
readonly LOG_DIR="/var/log/my_app/"

# Attempt to write a log file
echo "Application started." >> "${LOG_DIR}app.log"

# If someone tries to change the path, it will fail
# LOG_DIR="/tmp/" # This line will cause an error
```

---

## 3. Exporting Variables

By default, variables in a script are only available within that script. To make a variable available to child processes run from the script, you must export it using the `export` command.

**Example:**

```bash
export PATH=$PATH:/my/custom/path
```

**Brilliant Practical Example:** Suppose you have a main script that launches a child script, and you need to pass an environment variable to the child script.

**Parent Script (parent\_script.sh):**

```bash
#!/bin/bash

# Define and export a variable
export API_KEY="a1b2c3d4e5f6"

# Run the child script
./child_script.sh
```

**Child Script (child\_script.sh):**

```bash
#!/bin/bash

# The exported variable is now accessible
echo "API Key is: $API_KEY"
```

Thanks to `export`, `child_script.sh` is able to access the value of `API_KEY`.

---

## 4. Unsetting Variables

To remove a variable from memory and completely undefine it, you can use the `unset` command. This is useful for freeing up memory or for ensuring an old variable isn't used by mistake.

**Example:**

```bash
unset VARIABLE_NAME
```

**Brilliant Practical Example:** After using a variable containing a password or other sensitive information, it's good practice to remove it from memory.

```bash
#!/bin/bash

# A variable containing a password
SECRET_PASSWORD="my_super_secret_password"

# Use the password (in this case, print it)
echo "Using password..."

# Remove the variable from memory
unset SECRET_PASSWORD

# Any attempt to access the variable will fail
echo "Password variable is: $SECRET_PASSWORD"
# The previous line will show as blank or a null value
```
