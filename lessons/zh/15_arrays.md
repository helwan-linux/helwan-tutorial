Bash中的数组
Bash 中的数组是用于在单个变量中存储值集合的强大功能，使其成为在脚本中管理数据列表的理想选择。与将每个值作为单独的变量处理不同，数组允许您以有组织且高效的方式访问和操作数据。

1. 声明数组
您可以通过为其分配值列表来声明一维数组。元素放在括号 () 内，并用空格分隔。

FRUITS=("apple" "banana" "cherry")

实际示例: 想象您有一个需要检查的服务器名称列表。您可以将它们存储在数组中以简化过程。

#!/bin/bash
# Declare an array of server names
SERVERS=("web-server-01" "db-server-01" "app-server-02")

# You can print the entire array
echo "Server list: ${SERVERS[@]}"

2. 访问元素
要访问数组的单个元素，请使用其索引（位置），该索引从0开始。

echo ${FRUITS[1]}
# Output: banana

实际示例: 访问 SERVERS 数组的第一个和第三个元素。

#!/bin/bash
SERVERS=("web-server-01" "db-server-01" "app-server-02")

# Access the first element (index 0)
echo "First server: ${SERVERS[0]}"

# Access the third element (index 2)
echo "Third server: ${SERVERS[2]}"

3. 添加元素
您可以使用 += 运算符向现有数组添加新元素。

FRUITS+=("date")

实际示例: 向现有的 SERVERS 数组添加一个新服务器。

#!/bin/bash
SERVERS=("web-server-01" "db-server-01")
echo "Server list before adding: ${SERVERS[@]}"

# Add a new server
SERVERS+=("monitoring-server-03")

echo "Server list after adding: ${SERVERS[@]}"

4. 遍历数组
要遍历数组的所有元素，可以使用带有 [@] 符号的 for 循环，该符号表示所有元素。

for fruit in "${FRUITS[@]}"; do
  echo "Fruit: $fruit"
done

出色的实际示例: 让我们对数组中的每个服务器执行 ping 检查。此类脚本对于监控网络健康状况至关重要。

#!/bin/bash

# List of server names
SERVERS=("web-server-01" "db-server-01" "google.com")

# Loop through each server in the array
for server in "${SERVERS[@]}"; do
  echo "Pinging server: $server..."

  # Send a single ping packet (-c 1) and redirect output to null
  ping -c 1 "$server" &> /dev/null

  # Check the exit status of the last command
  if [ $? -eq 0 ]; then
    echo "✅ Successfully connected to: $server"
  else
    echo "❌ Failed to connect to: $server"
  fi

  echo "---"
done

此示例演示了数组如何简化需要对数据列表进行迭代的复杂任务。