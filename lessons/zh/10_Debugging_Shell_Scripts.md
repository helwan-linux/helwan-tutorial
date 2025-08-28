
Shell 脚本调试
调试是任何编写 shell 脚本的人都至关重要的技能。当脚本行为不符合预期时，这些技术可以帮助您识别错误、跟踪脚本的执行并找出问题所在。

1. 以调试模式运行脚本
调试 shell 脚本最有效的方法是使用 -x 标志运行它。这会打开跟踪模式，在每个命令执行前，它会将该命令及其参数打印到终端。

bash -x script.sh

它的作用： 输出将显示一个 + 符号，后跟正在执行的命令行，包括任何变量的值。这为脚本的流程提供了清晰、分步的跟踪。

实际例子：

COUNT=1
echo "Count is $COUNT"

调试输出：

+ COUNT=1
+ echo 'Count is 1'
Count is 1

这使得在变量赋值和扩展发生时很容易看到它们。

2. 使用 echo 进行跟踪
对于更具体或有针对性的调试，在脚本中插入 echo 语句是一种简单但功能强大的技术。

echo "Reached here"

它的作用： echo 命令会将消息打印到控制台。通过策略性地放置这些消息，您可以确认代码的哪些部分正在执行，并查看变量在特定点的值。

实际例子：

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

这种方法通过显示脚本正在采取的条件路径，帮助您快速缩小问题范围。

3. 在脚本内部设置和取消设置调试模式
为了获得更多控制，您可以为脚本的特定部分打开调试模式，而不是整个文件。

启用调试： 在您想要调试的部分之前添加 set -x。

禁用调试： 在该部分之后添加 set +x。

实际例子：

#!/bin/bash
# Regular script commands...

echo "Starting debug section for file processing."
set -x  # Turn on debug mode

# Debug this part
for file in *.log; do
  # ... commands
done

set +x  # Turn off debug mode
echo "Finished debug section."

此方法通过仅显示您正在积极排查的部分的跟踪，使您的脚本输出保持整洁。