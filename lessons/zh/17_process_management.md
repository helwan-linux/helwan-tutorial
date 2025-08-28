Bash中的进程管理
管理进程是使用 Linux 命令行的重要组成部分。此技能可让您控制在系统上运行的程序，使您能够在后台执行任务、终止无响应的进程以及监控系统性能。

1. 在后台运行命令
当您在命令末尾添加 & 符号时，您将在后台执行它。这会立即将命令行控制权返回给您，而无需等待命令完成。这对于不需要您交互的长时间运行操作非常有用。

示例:

sleep 60 &

实际示例: 在后台运行下载。

# 在后台运行下载命令
wget https://example.com/large_file.zip &

# 您现在可以立即输入其他命令
echo "Download started in the background. You can continue working now."

2. 列出后台作业
要列出当前会话中在后台运行的所有任务，请使用 jobs 命令。这会提供一个包含进程及其作业 ID 和状态的列表。

示例:

jobs

实际示例:

# 在后台启动两个进程
./script_one.sh &
./script_two.sh &

# 查看作业列表
jobs
# 输出可能如下所示:
# [1]-  Running                 ./script_one.sh &
# [2]+  Running                 ./script_two.sh &

作业 ID ([1], [2]) 对于控制这些任务非常有用。

3. 将作业带到前台
如果您想重新获得后台任务的控制权，请使用 fg (foreground) 命令，后跟作业 ID。这会将任务带到前台，使您可以再次与它交互。

示例:

fg %1

实际示例:

# 在后台运行一个进程
./interactive_script.sh &
# [1] 1234

# 将进程带回前台
fg %1
```%1` 指的是作业列表中的第一个作业。

---

## 4. 终止进程

如果进程无响应或消耗过多资源，您可以使用 `kill` 命令及其进程 ID (PID) 来终止它。您可以使用 `ps aux` 或 `top` 命令找到 PID。

**示例:**

```bash
kill PID

实际示例:

# 找到 `firefox` 进程的 PID
ps aux | grep firefox
# 示例输出:
# user      1500  ... /usr/bin/firefox ...

# 使用其 PID 终止进程
kill 1500

# 如果进程没有停止，请使用强制终止
kill -9 1500

⚠️ 使用 kill -9 应该是最后的手段，因为它不允许进程在退出前保存其工作。