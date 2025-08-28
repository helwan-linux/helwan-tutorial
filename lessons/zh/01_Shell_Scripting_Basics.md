---

# Shell Scripting Basics (Chinese)

Shell 脚本是一种强大的方法，可以通过在文件中编写命令序列来自动化 Linux 中的重复任务，Shell 会执行这些命令。

## 变量

变量用于存储可以在脚本中重复使用的数据。赋值时等号两边不要有空格：

NAME="Helwan"
AGE=25

要访问变量的值，请在前面加 \$：

echo "你好, \$NAME! 你 \$AGE 岁。"

## 条件语句

条件语句允许你在脚本中做出决策。

if 语句示例：

if \[ \$AGE -ge 18 ]; then
echo "你是成年人。"
else
echo "你是未成年人。"
fi

方括号 \[ ] 是 test 命令的同义词。可以使用以下运算符：

* -eq (等于)
* -ne (不等于)
* -lt (小于)
* -le (小于或等于)
* -gt (大于)
* -ge (大于或等于)

## 循环

循环帮助你多次执行命令。

for 循环示例：

for i in 1 2 3 4 5
do
echo "数字 \$i"
done

while 循环示例：

count=1
while \[ \$count -le 5 ]
do
echo "计数 \$count"
((count++))
done

## 函数

函数是可重用的代码块。

定义函数：

greet() {
echo "你好, \$1!"
}

调用函数并传递参数：

greet "用户"

\$1 代表传递给函数的第一个参数。

## 注释

注释以 # 开头，Shell 会忽略它们。使用注释解释代码。

# 这是一个注释

echo "你好，世界"  # 这会打印一条消息

---

## 🧪 有用的命令 (Aliases)

```bash
alias sync="sudo pacman -Syyy"
alias install="sudo pacman -S"
alias update="sudo pacman -Syyu"
alias search="sudo pacman -Ss"
alias search-local="sudo pacman -Qs"
alias pkg-info="sudo pacman -Qi"
alias local-install="sudo pacman -U"
alias helwan="uname -a"
```
