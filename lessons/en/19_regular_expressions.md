# Regular Expressions (Regex) in Bash

Regular expressions (regex) are a powerful toolset for pattern matching and text manipulation. In Bash scripting, they allow you to search, validate, and parse strings with incredible precision. Mastering regex is essential for any serious text-processing task, such as handling log files, validating user input, or extracting structured data.

---

## 1. Using `grep` with Regex

The `grep` command is the classic Linux utility for searching text using patterns. You can enable support for extended regular expressions with the `-E` flag, which allows for more advanced patterns.

```bash
grep -E "^[a-z]+@[a-z]+\\.com$"
```

> Brilliant Practical Example: A system administrator needs to quickly filter a log file to find all entries that contain a valid email address. The `-E` flag is used to interpret the regex pattern, and the `^` and `$` anchors ensure the entire line is a valid email.

```bash
#!/bin/bash

# The log file to search
LOG_FILE="application.log"

echo "Searching for valid email addresses in $LOG_FILE..."

# The regex pattern matches a string that starts with one or more letters,
# followed by an @, then more letters, and ends with .com
grep -E "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$" "$LOG_FILE"

echo "Search complete."
```

This example uses a more comprehensive regex pattern to match a wider range of valid email addresses, demonstrating the power of the tool.

---

## 2. Bash Regex Matching with `[[...]]`

Bash has a built-in operator `=~` for comparing a string against a regular expression. This is much more efficient than spawning an external process like `grep` and is ideal for conditional statements within a script. The regex pattern does not need to be quoted when used inside `[[...]]`.

```bash
if [[ "$email" =~ ^[a-z]+@[a-z]+\\.com$ ]]; then
  echo "Valid email."
fi
```

> Brilliant Practical Example: A script that prompts a user for an email address and validates it before proceeding. This is a common and critical task for input validation.

```bash
#!/bin/bash

# Prompt the user for input
read -p "Enter your email address: " EMAIL

# Use the =~ operator for regex validation
if [[ "$EMAIL" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$ ]]; then
  echo "✅ Email address '$EMAIL' is valid."
else
  echo "❌ Error: Invalid email format. Please try again." >&2
  exit 1
fi
```

---

## 3. Extracting Substrings

When you perform a regex match using the `=~` operator inside a `[[...]]` block, any captured groups (parts of the pattern enclosed in parentheses) are automatically stored in the `BASH_REMATCH` array. This is an incredibly powerful feature for parsing and extracting specific pieces of information from a string.

```bash
if [[ "$string" =~ ([0-9]+) ]]; then
  echo "Number: ${BASH_REMATCH[1]}"
fi
```

> Brilliant Practical Example: A script that processes a log entry string, extracts the timestamp and the status code, and then uses that information for further processing.

```bash
#!/bin/bash

LOG_ENTRY="[2023-08-25 10:30:00] - Request to /api/users successful with status 200"

# Regex to capture the timestamp and the status code
REGEX_PATTERN="^\\[([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})\\] .* status ([0-9]+)$"

if [[ "$LOG_ENTRY" =~ $REGEX_PATTERN ]]; then
  # The captured groups are stored in BASH_REMATCH
  TIMESTAMP="${BASH_REMATCH[1]}"
  STATUS_CODE="${BASH_REMATCH[2]}"

  echo "Extracted Timestamp: $TIMESTAMP"
  echo "Extracted Status Code: $STATUS_CODE"
else
  echo "Error: Could not parse the log entry." >&2
  exit 1
fi
```

This example demonstrates how `BASH_REMATCH` can be used to perform complex data extraction from a single operation.
