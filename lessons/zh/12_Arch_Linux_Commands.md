Arch Linux基础命令
Arch Linux 是一个轻量级且灵活的 Linux 发行版，遵循“保持简单，傻瓜式” (KISS) 哲学。虽然它提供了很大的控制权，但其以命令行中心的方法需要对核心工具的良好理解。以下是帮助您入门和管理系统的基本命令。

1) 系统更新和软件包管理
Pacman 是 Arch 强大的软件包管理器。这些命令对于保持系统最新和安装新软件至关重要。

更新软件包数据库
sudo pacman -Sy

此命令将您的本地软件包数据库与 Arch 存储库同步。这是获取最新软件版本信息的快速且必不可少的步骤。

升级所有已安装的软件包
sudo pacman -Syu

这是 Arch 用户最常用的命令。 -S 标志用于同步和安装， -y 用于刷新软件包列表， -u 用于升级系统。它在更新数据库后将所有已安装的软件包升级到最新版本。

安装软件包
sudo pacman -S package_name

此命令安装新软件包及其所有必需的依赖项。

示例:

sudo pacman -S neofetch

删除软件包
sudo pacman -R package_name

删除指定的软件包。

更彻底的删除:

sudo pacman -Rs package_name   # 删除软件包 + 不需要的依赖项
sudo pacman -Rns package_name  # 删除软件包 + 不需要的依赖项 + 配置文件

搜索软件包
pacman -Ss keyword

在软件包数据库中搜索与关键字匹配的软件包。

列出已安装的软件包
pacman -Q

列出系统上当前安装的所有软件包。

2) 系统信息
这些命令让您可以快速概览系统状态和资源使用情况。

检查内核版本
uname -r

显示当前正在运行的 Linux 内核版本。

检查系统正常运行时间
uptime

显示系统已运行多长时间、登录用户数和负载平均值。

显示磁盘使用情况
df -h

以人类可读的格式显示已挂载文件系统的磁盘空间使用情况。

显示内存使用情况
free -h

以人类可读的格式显示总内存、已使用内存和可用内存。

3) 用户和权限管理
用于管理用户帐户和权限的命令。

添加新用户
sudo useradd -m username

创建一个新用户帐户 ( -m 创建主目录)。

为用户设置密码
sudo passwd username

为用户设置密码。

修改用户 (添加到组)
sudo usermod -aG groupname username

将用户添加到辅助组 ( -aG 用于追加到组)。

4) 系统控制 (systemd)
Arch Linux 使用 systemd 来管理服务。 systemctl 是用于控制服务的命令行界面。

启动 / 停止 / 重启服务
sudo systemctl start service_name
sudo systemctl stop service_name
sudo systemctl restart service_name

控制服务的运行状态。

开机启用 / 禁用服务
sudo systemctl enable service_name
sudo systemctl disable service_name
```enable` 在开机时自动启动服务； `disable` 阻止它自动启动。

---

## 5) 其他

对于常见的管理任务有用的其他命令。

### 查看系统日志

```bash
journalctl -xe

显示 systemd 日志中的系统日志条目 ( -x 添加额外上下文， -e 跳转到末尾)。

挂载文件系统
sudo mount /dev/sdXY /mnt

在指定的挂载点挂载设备 (例如，USB 驱动器或分区)。

卸载文件系统
sudo umount /mnt

从挂载点卸载文件系统 - 在物理移除设备之前是必需的。