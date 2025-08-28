Bash脚本中的错误处理
适当的错误处理是编写健壮、可靠的 Shell 脚本的关键技能。通过预测和管理潜在的故障，您可以确保脚本的行为可预测，提供有用的反馈，并防止数据损坏或意外的系统行为。

1. 检查退出状态
每个命令执行后，一个特殊的变量 $? 将被设置为其退出状态。值 0 表示成功，而任何其他值（通常为 1 到 255）表示失败。检查此状态允许您创建响应命令失败的条件逻辑。

command
if [ $? -ne 0 ]; then
  echo "Command failed."
fi

出色的实际示例
一个脚本，它尝试下载一个文件，然后仅在下载成功时才继续处理它。

#!/bin/bash

# 尝试下载一个文件
wget -q http://example.com/data.txt

# 检查 wget 命令的退出状态
if [ $? -ne 0 ]; then
  echo "Error: Failed to download the file from the source." >&2
  exit 1
else
  echo "File downloaded successfully. Processing..."
  # 在此处添加更多命令来处理文件
fi

2. 使用 set -e
set -e 命令，也称为 遇到错误即退出，是一个强大的指令，它强制脚本在任何命令失败时立即退出。这是防止脚本在先前步骤失败后继续执行潜在危险操作的绝佳方法。

set -e

出色的实际示例
一个脚本，它执行一系列关键任务，例如创建目录、复制文件，然后对其进行压缩。如果这些步骤中的任何一个失败，脚本应停止以防止状态不一致。

#!/bin/bash
# 立即退出（如果命令失败）
set -e

# 为备份创建一个目录
mkdir /tmp/backup_data

# 复制一个关键文件。如果此操作失败，脚本将退出。
cp /var/log/syslog /tmp/backup_data/

# 压缩目录。如果 'cp' 命令失败，此操作将不会运行。
tar -czf /root/backup.tar.gz /tmp/backup_data

echo "Backup completed successfully!"

3. 捕获错误 (trap)
trap 命令允许您在接收到信号时执行特定的命令或函数。 ERR 信号对于错误处理特别有用，因为它在命令以非零状态退出时触发。

trap 'echo "Error occurred!"' ERR

出色的实际示例
一个脚本，如果其执行过程中发生错误，需要清理临时文件。 trap 命令确保无论脚本在哪里失败，都会调用清理函数。

#!/bin/bash

# 定义一个处理清理的函数
cleanup() {
  echo "An error occurred. Cleaning up temporary files..." >&2
  rm -f /tmp/temp_file_*
}

# 设置 trap 以在任何错误时调用清理函数
trap cleanup ERR

echo "Starting script..."

# 一个可能失败的命令，它将触发 trap
touch /root/temp_file_1

echo "This line will not be reached if the above command fails."

4. 自定义错误消息
虽然 set -e 和 trap 功能强大，但您可以通过创建自定义函数来增强错误处理，以提供更具描述性的错误消息。此函数可以将消息打印到标准错误 (stderr)，然后退出脚本。

function error_exit {
  echo "$1" 1>&2
  exit 1
}

出色的实际示例
一个脚本，它验证命令行参数，并在用户提供不正确的输入时提供有用的使用消息。

#!/bin/bash

# 定义一个用于错误的自定义函数
function error_exit() {
  echo "Error: $1" >&2
  exit 1
}

# 检查是否提供了正确数量的参数
if [ "$#" -ne 2 ]; then
  error_exit "Incorrect number of arguments. Usage: $0 <source_dir> <destination_dir>"
fi

SOURCE_DIR="$1"
DEST_DIR="$2"

# 检查源目录是否存在
if [ ! -d "$SOURCE_DIR" ]; then
  error_exit "Source directory '$SOURCE_DIR' does not exist."
fi

echo "Script is running with valid arguments."
# ... rest of the script ...
