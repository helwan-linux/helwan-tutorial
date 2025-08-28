---

# File and Directory Management (Chinese)

管理文件和目录是每个 Linux 用户的基本技能。掌握这些命令可以让你高效地控制文件系统。

## 1. 列出文件和目录

`ls` 命令用于列出当前目录的内容。要显示文件和目录的详细信息，请使用：

```bash
ls -l
```

* `-l`: 显示长列表，包括文件权限、链接数、所有者、组、文件大小和修改日期。

## 2. 创建目录

要创建新目录，请使用 `mkdir` 命令。

```bash
mkdir my_directory
```

* 可以一次创建多个目录，用空格分隔它们的名字。
* 要在不存在的父目录下创建目录，请使用 `-p` 选项：

```bash
mkdir -p parent_directory/my_directory
```

## 3. 目录导航

`cd`（change directory）命令用于在目录之间移动。

```bash
cd my_directory
```

* `cd ..`: 返回上级目录。
* `cd` 或 `cd ~`: 返回你的主目录。

## 4. 复制文件

`cp`（copy）命令用于将文件从一个位置复制到另一个位置。

```bash
cp source.txt destination.txt
cp file.txt /path/to/directory/
cp -r directory_a directory_b
```

* `cp -r`: 递归复制目录及其所有内容。

## 5. 移动和重命名文件

`mv`（move）命令用于移动或重命名文件和目录。

```bash
mv oldname.txt newname.txt
```

* **重命名**：如果新文件在同一目录。
* **移动**：如果 `newname.txt` 是另一个目录的路径，文件将被移动到该位置。

## 6. 删除文件和目录

`rm`（remove）命令用于删除文件。

```bash
rm filename.txt
rm -i filename.txt
rm -r directory_name
rm -f file.txt
```

* `rm -i`: 删除前提示确认。
* `rm -r`: 递归删除目录及其所有内容。
* `rm -f`: 强制删除，无需确认。

## 7. 显示当前目录

`pwd`（print working directory）命令打印你当前所在目录的完整路径。

```bash
pwd
```
