Bash中的高级变量
在Bash命令行环境中，变量是存储数据的基本工具。理解高级变量类型以及如何处理它们，可以让你对脚本有更大的控制权，使其更具动态性和强大。

1. 命令替换 (Command Substitution)
命令替换是一种技术，它允许您将命令的输出分配给一个变量。这是在运行时执行命令并存储其输出以便在脚本中后续使用的强大功能。

您可以使用现代的 $(...) 语法或旧式的反引号 ...。推荐使用现代的 $(...) 语法，因为它更易于阅读和嵌套。

示例:

CURRENT_DATE=$(date)

出色的实际示例: 假设您需要创建每日备份并根据当前日期命名。您可以使用命令替换来自动设置文件名。

#!/bin/bash
# 将当前日期存储在变量中
BACKUP_DATE=$(date +%Y-%m-%d)

# 使用变量来确定文件名
BACKUP_FILE="backup_data_${BACKUP_DATE}.zip"

# 创建带有动态名称的压缩文件
tar -czf "$BACKUP_FILE" /var/www/html/
echo "Backup file created: $BACKUP_FILE"

2. 只读变量 (Read-only Variables)
如果您想确保变量的值在长脚本中不会被意外更改，可以使用 readonly 命令将其设置为只读。

示例:

readonly PI=3.14159

注意: 任何试图更改此变量值的尝试 (例如，PI=3) 都将导致错误。

出色的实际示例: 在系统管理脚本中，您可能需要定义不应更改的敏感路径。将这些变量设置为只读可以增加一层安全性，以防止意外修改。

#!/bin/bash

# 定义核心日志目录并使其只读
readonly LOG_DIR="/var/log/my_app/"

# 尝试写入日志文件
echo "Application started." >> "${LOG_DIR}app.log"

# 如果有人试图更改路径，它将失败
# LOG_DIR="/tmp/" # 这一行将导致错误

3. 导出变量 (Exporting Variables)
默认情况下，脚本中的变量仅在该脚本内部可用。要使变量对从该脚本运行的子进程可用，必须使用 export 命令将其导出。

示例:

export PATH=$PATH:/my/custom/path

出色的实际示例: 假设您有一个主脚本启动一个子脚本，并且需要将一个环境变量传递给子脚本。

主脚本 (parent_script.sh):

#!/bin/bash

# 定义并导出一个变量
export API_KEY="a1b2c3d4e5f6"

# 运行子脚本
./child_script.sh

子脚本 (child_script.sh):

#!/bin/bash

# 导出的变量现在可以访问
echo "API Key is: $API_KEY"

由于 export，child_script.sh 能够访问 API_KEY 的值。

4. 取消设置变量 (Unsetting Variables)
要从内存中删除变量并完全取消其定义，可以使用 unset 命令。这对于释放内存或确保旧变量不会被错误使用非常有用。

示例:

unset VARIABLE_NAME

出色的实际示例: 在使用包含密码或其他敏感信息的变量后，最佳实践是将其从内存中删除。

#!/bin/bash

# 一个包含密码的变量
SECRET_PASSWORD="my_super_secret_password"

# 使用密码 (在这种情况下，打印它)
echo "Using password..."

# 从内存中删除变量
unset SECRET_PASSWORD

# 任何试图访问该变量的尝试都将失败
echo "Password variable is: $SECRET_PASSWORD"
# 上一行将显示为空白或空值
