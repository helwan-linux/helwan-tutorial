Bash中的正则表达式(Regex)
正则表达式（regex）是用于模式匹配和文本操作的强大工具集。在 Bash 脚本编程中，它们使您能够以令人难以置信的精度搜索、验证和解析字符串。掌握 regex 对于任何严肃的文本处理任务都是必不可少的，例如处理日志文件、验证用户输入或提取结构化数据。

1. 使用 grep 和 Regex
grep 命令是用于使用模式搜索文本的经典 Linux 实用程序。您可以使用 -E 标志启用对扩展正则表达式的支持，这允许更高级的模式。

grep -E "^[a-z]+@[a-z]+\\.com$"

出色的实际示例: 系统管理员需要快速过滤日志文件以查找所有包含有效电子邮件地址的条目。 -E 标志用于解释 regex 模式，而 ^ 和 $ 锚点确保整个行都是一个有效的电子邮件。

#!/bin/bash

# The log file to search
LOG_FILE="application.log"

echo "Searching for valid email addresses in $LOG_FILE..."

# The regex pattern matches a string that starts with one or more letters,
# followed by an @, then more letters, and ends with .com
grep -E "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$" "$LOG_FILE"

echo "Search complete."

此示例使用更全面的 regex 模式来匹配更广泛的有效电子邮件地址，展示了该工具的强大功能。

2. 使用 [[...]] 进行 Bash Regex 匹配
Bash 使用 [[...]] 块内的 =~ 运算符内置了对 regex 匹配的支持。这使您能够将 regex 直接集成到脚本的条件逻辑中，而无需外部工具。

if [[ "Hello World" =~ "World" ]]; then
  echo "String contains 'World'"
fi

出色的实际示例
一个脚本，它要求用户输入电子邮件地址，并在继续之前对其进行验证。

#!/bin/bash

read -p "Enter your email address: " EMAIL

# Regex pattern for a simple email validation
if [[ "$EMAIL" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$ ]]; then
  echo "✅ Email address '$EMAIL' is valid."
else
  echo "❌ Error: Invalid email format. Please try again." >&2
  exit 1
fi

3. 提取子字符串
当您使用 [[...]] 块内的 =~ 运算符执行 regex 匹配时，任何捕获的组（用括号括起来的模式部分）都会自动存储在 BASH_REMATCH 数组中。这是一个非常强大的功能，用于从字符串中解析和提取特定信息。

if [[ "$string" =~ ([0-9]+) ]]; then
  echo "Number: ${BASH_REMATCH[1]}"
fi

出色的实际示例: 一个脚本，它处理日志输入字符串，提取时间戳和状态码，然后使用该信息进行进一步处理。

#!/bin/bash

LOG_ENTRY="[2023-08-25 10:30:00] - Request to /api/users successful with status 200"

# Regex to capture the timestamp and the status code
REGEX_PATTERN="^\\[([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})\\] .* status ([0-9]+)$"

if [[ "$LOG_ENTRY" =~ $REGEX_PATTERN ]]; then
  # The captured groups are stored in BASH_REMATCH
  TIMESTAMP="${BASH_REMATCH[1]}"
  STATUS_CODE="${BASH_REMATCH[2]}"

  echo "Timestamp: $TIMESTAMP"
  echo "Status Code: $STATUS_CODE"
  
  # You can now use these variables for further processing
  if [ "$STATUS_CODE" -eq 200 ]; then
    echo "Processing successful request data..."
  fi
else
  echo "Could not parse the log entry."
fi
