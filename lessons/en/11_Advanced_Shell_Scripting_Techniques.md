# Advanced Shell Scripting Techniques

Mastering advanced shell scripting is a game-changer for automating complex tasks and writing more efficient and powerful scripts. These techniques go beyond basic commands, giving you the tools to handle data, perform calculations, and manage collections of values.

---

## 1. Command Substitution

Command substitution allows you to capture the output of a command and use it as the value of a variable. This is a fundamental technique for dynamic scripting.

You can use either the modern `$(...)` syntax or the older backticks `...`. The `$(...)` syntax is recommended as it's easier to nest and read.

```bash
output=$(ls -l)
```

**Practical Example:** Store today’s date in a variable and use it for a log file name.

```bash
#!/bin/bash
# Store the current date in a variable
today=$(date +%Y-%m-%d)

# Use the variable to create a log file
LOG_FILE="backup_log_${today}.txt"
echo "Backup started on $(date)" > $LOG_FILE
```

---

## 2. Arithmetic Operations

Shell scripts can perform basic arithmetic using the `$((...))` syntax. This is essential for calculations like counters or percentages.

```bash
result=$(( 3 + 5 ))
```

**Practical Example:** Calculate disk space usage percentage.

```bash
#!/bin/bash
TOTAL_SPACE=1000
USED_SPACE=$(df -h | grep "/dev/sda1" | awk '{print $3}' | sed 's/G//')

# Note: Use `bc` for floating-point arithmetic.
PERCENTAGE=$(( ($USED_SPACE * 100) / $TOTAL_SPACE ))

echo "Used space: ${USED_SPACE}G"
echo "Percentage of total space used: ${PERCENTAGE}%"
```

---

## 3. Arrays

Arrays let you store multiple values in one variable—great for managing lists.

```bash
my_array=(one two three)
```

**Accessing Elements:**

```bash
echo ${my_array[1]} # prints 'two'
```

**All Elements:**

```bash
echo ${my_array[@]} # prints 'one two three'
```

**Array Length:**

```bash
echo ${#my_array[@]} # prints '3'
```

**Practical Example:** Iterate through a list of servers and ping them.

```bash
#!/bin/bash
SERVERS=("web-server-1" "db-server" "app-server-alpha")

for server in "${SERVERS[@]}"; do
  echo "Pinging ${server}..."
  ping -c 1 "${server}"
  if [ $? -eq 0 ]; then
    echo "${server} is up."
  else
    echo "${server} is down!"
  fi
done
```
This demonstrates how arrays make it easy to manage and loop through a list of items, making your scripts more scalable and maintainable.