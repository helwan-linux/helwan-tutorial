---

# Process Management (Chinese)

进程是正在运行的程序。理解如何管理它们可以让你对系统性能有显著控制，并帮助排查问题。

## 1. 查看正在运行的进程

`ps aux` 命令是显示所有当前正在运行进程的最常用方法之一。

```bash
ps aux
```

* `a`: 显示所有用户的进程。
* `u`: 以用户友好的格式显示进程。
* `x`: 包括未附加到特定终端的进程。

运行此命令时，你会看到一个包含重要信息的表格，例如：

* **USER**: 拥有该进程的用户。
* **PID**: 每个进程的唯一进程ID。
* **%CPU**: CPU使用百分比。
* **%MEM**: 内存使用百分比。
* **COMMAND**: 启动该进程的命令。

## 2. 通过 PID 杀死进程

如果某个进程无响应或占用过多资源，可以使用 `kill` 命令及其进程ID终止它。

```bash
kill PID
kill 12345
```

* `kill 12345`: 尝试使用 **SIGTERM** 信号优雅地终止 PID 为 12345 的进程。

要强制杀死顽固进程，使用 `-9` 选项：

```bash
kill -9 PID
kill -9 12345
```

* `-9`: 发送强制终止信号 (**SIGKILL**)，进程无法忽略。

## 3. 通过名称杀死进程

如果你不知道 PID，可以使用 `pkill` 命令根据名称终止进程。

```bash
pkill process_name
pkill firefox
pkill -9 firefox
```

* `pkill firefox`: 终止所有名为 *firefox* 的进程。
* `pkill -9 firefox`: 强制终止所有 *firefox* 进程。

当你需要一次关闭特定程序的所有实例时，这非常有用。

## 4. 查看进程树

`pstree` 命令以层级树状显示进程，显示它们之间的父子关系。

```bash
pstree
pstree -p
pstree username
```

* `pstree`: 以树状显示所有进程。
* `pstree -p`: 显示包含 PID 的进程树。
* `pstree username`: 仅显示特定用户拥有的进程。

这种可视化表示使理解哪些子进程由主进程启动变得容易，有助于排查问题。
