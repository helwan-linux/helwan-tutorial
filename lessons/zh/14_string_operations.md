Bash中的字符串操作
在Bash脚本编写中，字符串是一种基本数据类型，shell 提供了一套强大的内置操作来操纵它们。掌握这些技术对于任何涉及文本解析、处理文件名或处理用户输入的脚本都至关重要。

1. 查找字符串长度
要获取字符串的长度，可以使用 ${#variable} 语法。这是一种简单快速的方法来检查变量中的字符数。

STR="Hello World"
echo ${#STR}

输出:

11

实际示例: 验证用户输入，以确保密码满足最低长度要求。

#!/bin/bash
read -p "Enter a password (min 8 characters): " PASSWORD
if [ ${#PASSWORD} -lt 8 ]; then
  echo "Password is too short!"
else
  echo "Password accepted."
fi

2. 提取子字符串
Bash 允许您使用基于冒号的语法提取字符串的一部分: ${string:position:length}。

position: 起始索引 (从0开始)。

length: 要提取的字符数。

echo ${STR:6:5}

输出:

World

实际示例: 从完整路径中提取文件名。

#!/bin/bash
FULL_PATH="/home/user/documents/report.txt"
FILE_NAME=$(basename "$FULL_PATH")
echo "File Name: $FILE_NAME"

输出:

File Name: report.txt

3. 字符串替换
您可以使用 ${variable/pattern/replacement} 语法替换字符串的一部分。

echo ${STR/World/Bash}

输出:

Hello Bash

实际示例: 通过删除协议来清理URL。

#!/bin/bash
URL="https://www.example.com"
CLEAN_URL=${URL/https:\/\/}
echo "Clean URL: $CLEAN_URL"

输出:

Clean URL: www.example.com

4. 字符串比较
在 [ ] 内部使用 == 或 = 进行字符串比较。始终将变量用双引号括起来。

if [ "$STR" = "Hello World" ]; then
  echo "Strings are equal"
fi

实际示例: 检查用户是否提供了正确的密钥。

#!/bin/bash
SECRET_KEY="SuperSecret123"
read -p "Enter the secret key: " INPUT

if [ "$INPUT" == "$SECRET_KEY" ]; then
  echo "Access granted."
else
  echo "Access denied."
fi
