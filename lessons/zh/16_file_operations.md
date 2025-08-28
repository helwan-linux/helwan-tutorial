Bash中的文件操作
处理文件是任何 Shell 脚本的一个基本方面。Bash 提供了一套强大的内置命令和语法来检查文件是否存在、读取内容和写入文件。掌握这些操作对于自动化、数据处理和日志记录等任务至关重要。

1. 检查文件是否存在
在脚本尝试读取或写入文件之前，最佳实践是首先验证文件是否存在。 [ -f "filename" ] 语法用于检查常规文件是否存在且不是目录。

if [ -f "myfile.txt" ]; then
  echo "File exists."
fi

出色的实际示例: 一个脚本在尝试启动服务之前检查配置文件是否存在。这可以防止脚本因错误而失败。

#!/bin/bash
CONFIG_FILE="/etc/my_app/config.conf"

if [ -f "$CONFIG_FILE" ]; then
  echo "Configuration file found. Starting application..."
  # Start the application or service here
else
  echo "Error: Configuration file not found at $CONFIG_FILE" >&2
  exit 1
fi

2. 逐行读取文件
逐行读取文件是处理日志文件或数据报告的常见任务。 while 循环与 read 结合是处理此问题的最健壮和有效的方法，可以防止出现特殊字符和空格问题。

while IFS= read -r line; do
  echo "$line"
done < "myfile.txt"

IFS=: 临时将内部字段分隔符设置为空，以防止修剪前导/尾随空格。

-r: 防止反斜杠转义被解释。

done < "myfile.txt": 将文件内容重定向到 while 循环的标准输入。

出色的实际示例: 一个脚本，它处理文件中的用户名列表，并为每个用户名创建一个新用户。

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

3. 写入文件
要将内容写入文件，您可以使用输出重定向运算符 >。如果文件已存在，此运算符将覆盖文件内容。

echo "Hello World" > output.txt

出色的实际示例: 一个脚本，它生成一个带有时间戳和状态消息的日志文件。

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

4. 追加到文件
如果要将内容添加到文件末尾而不覆盖其现有内容，请使用追加重定向运算符 >>。这对于日志记录和创建持续报告至关重要。

echo "Another line" >> output.txt

出色的实际示例: 一个脚本，它将所有成功和失败的备份尝试记录到一个单一的、连续的日志文件中。

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
