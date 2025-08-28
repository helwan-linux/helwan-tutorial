---

# Package Management (Chinese)

软件包管理是 Linux 系统管理的基石。软件包管理器是一组自动化工具，用于安装、升级、配置和移除软件包。在 Linux 系统上使用软件包管理器是标准且最安全的方式。

本课涵盖两种最常用的软件包管理器：**APT（Debian/Ubuntu 使用）** 和 **Pacman（Arch Linux 使用）**。

---

## 1. Debian/Ubuntu (APT)

**APT (Advanced Package Tool)** 是 Debian 及其衍生版（如 Ubuntu）的默认软件包管理器。它使用 `.deb` 文件，并依赖软件仓库获取软件。

### 更新软件包列表

```bash
sudo apt update
```

* **重要性:** 将本地软件包列表与仓库同步。不会安装或升级软件，但确保你知道最新版本和新软件包。安装或升级前运行。

### 升级已安装的软件包

```bash
sudo apt upgrade
```

* **功能:** 将所有已安装的软件包升级到最新可用版本。对于保持系统安全和最新至关重要。

### 安装新软件包

```bash
sudo apt install package_name
```

* **工作原理:** 下载并安装指定软件包及其依赖项。
* **示例:**

```bash
sudo apt install neofetch
```

安装 *Neofetch*，用于显示系统信息的工具。

### 删除软件包

```bash
sudo apt remove package_name
```

* **功能:** 删除指定软件包，但保留配置文件。

完全删除（包括配置文件）:

```bash
sudo apt purge package_name
```

---

## 2. Arch Linux (Pacman)

**Pacman** 是 Arch Linux 及其衍生版的软件包管理器，以简单和强大著称。

### 同步并更新

```bash
sudo pacman -Sy
```

* **功能:** 同步软件包数据库（类似于 `apt update`）。

### 同步、更新并升级

```bash
sudo pacman -Syu
```

* **功能:** Arch 系统最常用命令。同步数据库 (`-y`) 并升级所有已安装的软件包 (`-u`)。

### 安装新软件包

```bash
sudo pacman -S package_name
```

* **工作原理:** 安装新软件包。通常与同步一起使用。
* **示例:**

```bash
sudo pacman -S brave
```

安装 Brave 浏览器。

### 删除软件包

```bash
sudo pacman -R package_name
```

* **功能:** 删除软件包，但保留未使用的依赖。

递归和清理选项:

```bash
sudo pacman -Rs package_name   # 删除软件包 + 未使用依赖
sudo pacman -Rns package_name  # 删除软件包 + 依赖 + 配置文件

```
