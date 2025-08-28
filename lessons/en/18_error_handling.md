# Error Handling in Bash Scripts

Proper error handling is a crucial skill for writing robust and reliable shell scripts. By anticipating and managing potential failures, you can ensure your scripts behave predictably, provide useful feedback, and prevent data corruption or unexpected system behavior.

---

## 1. Checking the Exit Status

After every command is executed, a special variable `$?` is set to its exit status. A value of `0` indicates success, while any other value (usually 1 to 255) indicates a failure. Checking this status allows you to create conditional logic that responds to command failures.

```bash
command
if [ $? -ne 0 ]; then
  echo "Command failed."
fi
```

### Brilliant Practical Example

A script that attempts to download a file and then proceeds to process it only if the download was successful.

```bash
#!/bin/bash

# Attempt to download a file
wget -q http://example.com/data.txt

# Check the exit status of the wget command
if [ $? -ne 0 ]; then
  echo "Error: Failed to download the file from the source." >&2
  exit 1
else
  echo "File downloaded successfully. Processing..."
  # Add further commands to process the file here
fi
```

---

## 2. Using `set -e`

The `set -e` command, also known as *exit on error*, is a powerful directive that forces a script to exit immediately if any command fails. This is an excellent way to prevent a script from continuing with a potentially dangerous operation after a previous step has failed.

```bash
set -e
```

### Brilliant Practical Example

A script that performs a series of critical tasks, such as creating a directory, copying a file, and then compressing it. If any of these steps fail, the script should stop to prevent inconsistent state.

```bash
#!/bin/bash
# Exit immediately if a command fails
set -e

# Create a directory for the backup
mkdir /tmp/backup_data

# Copy a critical file. If this fails, the script will exit.
cp /var/log/syslog /tmp/backup_data/

# Compress the directory. This will not run if the 'cp' command fails.
tar -czf /root/backup.tar.gz /tmp/backup_data

echo "Backup completed successfully!"
```

---

## 3. Trapping Errors

The `trap` command allows you to execute a specific command or function when a signal is received. The `ERR` signal is particularly useful for error handling, as it is triggered whenever a command exits with a non-zero status.

```bash
trap 'echo "Error occurred!"' ERR
```

### Brilliant Practical Example

A script that needs to clean up temporary files if an error occurs during its execution. The `trap` command ensures the cleanup function is called no matter where the script fails.

```bash
#!/bin/bash

# Define a function to handle cleanup
cleanup() {
  echo "An error occurred. Cleaning up temporary files..." >&2
  rm -f /tmp/temp_file_*
}

# Set the trap to call the cleanup function on any error
trap cleanup ERR

echo "Starting script..."

# A command that is likely to fail, triggering the trap
touch /root/temp_file_1

echo "This line will not be reached if the above command fails."
```

---

## 4. Custom Error Messages

While `set -e` and `trap` are powerful, you can enhance your error handling by creating a custom function to provide more descriptive error messages. This function can print a message to the standard error (`stderr`) and then exit the script.

```bash
function error_exit {
  echo "$1" 1>&2
  exit 1
}
```

### Brilliant Practical Example

A script that validates command-line arguments and provides a helpful usage message if the user provides incorrect input.

```bash
#!/bin/bash

# Define a custom function for errors
function error_exit() {
  echo "Error: $1" >&2
  exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  error_exit "Incorrect number of arguments. Usage: $0 <source_dir> <destination_dir>"
fi

SOURCE_DIR="$1"
DEST_DIR="$2"

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
  error_exit "Source directory '$SOURCE_DIR' does not exist."
fi

echo "Script is running with valid arguments."
# ... rest of the script ...
```
