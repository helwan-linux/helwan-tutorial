高级Shell脚本技术
掌握高级Shell脚本技术对于自动化复杂任务和编写更高效、更强大的脚本至关重要。这些技术超越了基本命令，为您提供了处理数据、执行计算和管理值集合的工具。

1. 命令替换 (Command Substitution)
命令替换允许您捕获命令的输出并将其用作变量的值。这是动态脚本编写的基本技术。

您可以使用现代的 $(...) 语法或旧式的反引号 ...。推荐使用 $(...) 语法，因为它更易于嵌套和阅读。

output=$(ls -l)

实际示例: 将今天的日期存储在变量中，并将其用于日志文件的名称。

#!/bin/bash
# 将当前日期存储在变量中
today=$(date +%Y-%m-%d)

# 使用变量创建日志文件
LOG_FILE="backup_log_${today}.txt"
echo "Backup started on $(date)" > $LOG_FILE

2. 算术运算 (Arithmetic Operations)
Shell脚本可以使用 $((...)) 语法执行基本的算术运算。这对于计数器或百分比等计算至关重要。

result=$(( 3 + 5 ))

实际示例: 计算磁盘空间使用百分比。

#!/bin/bash
TOTAL_SPACE=1000
USED_SPACE=$(df -h | grep "/dev/sda1" | awk '{print $3}' | sed 's/G//')

# 注意: 使用 `bc` 进行浮点运算。
PERCENTAGE=$(( ($USED_SPACE * 100) / $TOTAL_SPACE ))

echo "Used space: ${USED_SPACE}G"
echo "Percentage of total space used: ${PERCENTAGE}%"

3. 数组 (Arrays)
数组允许您在一个变量中存储多个值，非常适合管理列表。

my_array=(one two three)

访问元素:

echo ${my_array[1]} # 输出 'two'

所有元素:

echo ${my_array[@]} # 输出 'one two three'

数组长度:

echo ${#my_array[@]} # 输出 '3'

实际示例: 遍历服务器列表并ping它们。

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

这展示了数组如何轻松管理和遍历项目列表，使您的脚本更具可扩展性和可维护性。