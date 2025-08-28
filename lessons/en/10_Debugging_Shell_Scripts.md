# Debugging Shell Scripts

Debugging is a crucial skill for anyone who writes shell scripts. When a script doesn't behave as expected, these techniques help you identify errors, trace the script's execution, and pinpoint where things went wrong.

---

## 1. Running a Script in Debug Mode

The most effective way to debug a shell script is to run it with the `-x` flag. This turns on **trace mode**, which prints each command and its arguments to the terminal just before it's executed.

```bash
bash -x script.sh
```

**What it does:** The output will show a `+` symbol followed by the command line being executed, including the values of any variables. This provides a clear, step-by-step trace of your script's flow.

**Practical Example:**

```bash
COUNT=1
echo "Count is $COUNT"
```

Debug output:

```
+ COUNT=1
+ echo 'Count is 1'
Count is 1
```

This makes it easy to see the variable assignments and expansions as they happen.

---

## 2. Using echo for Tracing

For more specific or targeted debugging, inserting `echo` statements into your script is a simple yet powerful technique.

```bash
echo "Reached here"
```

**What it does:** The `echo` command prints a message to the console. By strategically placing these messages, you can confirm which parts of your code are being executed and see the value of a variable at a specific point.

**Practical Example:**

```bash
#!/bin/bash
echo "Script started."

# Check if a file exists
if [ -f "my_file.txt" ]; then
  echo "File exists. Processing..."
  # ... further commands
else
  echo "File not found. Exiting."
  exit 1
fi
```

This approach helps you quickly narrow down a problem by showing which conditional path the script is taking.

---

## 3. Setting and Unsetting Debug Mode Within a Script

For more control, you can turn on debug mode for a specific section of your script rather than the entire file.

* **Enable debugging:** Add `set -x` before the section you want to debug.
* **Disable debugging:** Add `set +x` after the section.

**Practical Example:**

```bash
#!/bin/bash
# Regular script commands...

echo "Starting debug section for file processing."
set -x  # Turn on debug mode

# Debug this part
for file in *.log; do
  # ... commands
done

set +x  # Turn off debug mode
echo "Finished debug section."
```

This method keeps your script's output clean by only showing the trace for the parts you're actively troubleshooting.
