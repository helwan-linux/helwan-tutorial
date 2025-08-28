# File Operations in Bash

Working with files is a fundamental aspect of any shell script. Bash provides a powerful set of built-in commands and syntax to check for file existence, read content, and write to files. Mastering these operations is crucial for tasks like automation, data processing, and logging.

## 1. Checking if a File Exists

Before a script tries to read or write to a file, it's a best practice to first verify that the file exists. The `[ -f "filename" ]` syntax is used to check if a regular file exists and is not a directory.

```bash
if [ -f "myfile.txt" ]; then
  echo "File exists."
fi
```

**Brilliant Practical Example**: A script that checks for the presence of a configuration file before attempting to start a service. This prevents the script from failing with an error.

```bash
#!/bin/bash
CONFIG_FILE="/etc/my_app/config.conf"

if [ -f "$CONFIG_FILE" ]; then
  echo "Configuration file found. Starting application..."
  # Start the application or service here
else
  echo "Error: Configuration file not found at $CONFIG_FILE" >&2
  exit 1
fi
```

---

## 2. Reading a File Line by Line

Reading a file line by line is a common task for processing log files or data reports. The `while` loop combined with `read` is the most robust and efficient way to handle this, preventing issues with special characters and spaces.

```bash
while IFS= read -r line; do
  echo "$line"
done < "myfile.txt"
```

* `IFS=":` Temporarily sets the Internal Field Separator to null, preventing leading/trailing whitespace from being trimmed.
* `-r`: Prevents backslash escapes from being interpreted.
* `done < "myfile.txt"`: Redirects the content of the file to the while loop's standard input.

**Brilliant Practical Example**: A script that processes a list of usernames from a file and creates a new user for each one.

```bash
#!/bin/bash
USER_LIST_FILE="new_users.txt"

if [ ! -f "$USER_LIST_FILE" ]; then
  echo "Error: User list file not found!" >&2
  exit 1
fi

while IFS= read -r username; do
  echo "Creating user account for: $username"
  sudo useradd -m "$username"
done < "$USER_LIST_FILE"

echo "User creation process completed."
```

---

## 3. Writing to a File

To write content to a file, you use the output redirection operator `>`. This operator will overwrite the file's contents if it already exists.

```bash
echo "Hello World" > output.txt
```

**Brilliant Practical Example**: A script that generates a log file with a timestamp and a status message.

```bash
#!/bin/bash
LOG_FILE="server_status.log"

# Overwrite the log file with a new header
echo "--- Server Status Report ---" > "$LOG_FILE"

# Check server status and append the result
if ping -c 1 example.com &> /dev/null; then
  echo "Timestamp: $(date)" >> "$LOG_FILE"
  echo "Status: OK - Server is reachable." >> "$LOG_FILE"
else
  echo "Timestamp: $(date)" >> "$LOG_FILE"
  echo "Status: ERROR - Server is unreachable!" >> "$LOG_FILE"
fi
```

---

## 4. Appending to a File

If you want to add content to the end of a file without overwriting its existing content, you use the append redirection operator `>>`. This is essential for logging and creating ongoing reports.

```bash
echo "Another line" >> output.txt
```

**Brilliant Practical Example**: A script that logs all successful and failed backup attempts to a single, continuous log file.

```bash
#!/bin/bash
BACKUP_LOG="backup_history.log"
BACKUP_DIR="/var/www/data"

# Perform the backup
tar -czf "backup_$(date +%Y-%m-%d).tar.gz" "$BACKUP_DIR" &> /dev/null

# Check the exit status and append a status line to the log file
if [ $? -eq 0 ]; then
  echo "$(date): Backup of $BACKUP_DIR was successful." >> "$BACKUP_LOG"
else
  echo "$(date): ERROR: Backup of $BACKUP_DIR failed!" >> "$BACKUP_LOG"
fi
```
