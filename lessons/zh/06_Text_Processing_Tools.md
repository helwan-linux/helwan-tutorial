---

# Text Processing Tools in Linux (Chinese)

Linux 系统提供了一套强大的文本处理工具。这些工具允许你高效地搜索、分析和修改文本内容。它们对于程序员、系统管理员以及处理基于文本数据的人员来说至关重要。

## 1. grep: 搜索文本模式

命令 `grep`（Global Regular Expression Print）是最常用的工具，用于在文本文件中搜索特定模式。

```bash
grep "pattern" filename.txt
```

**实用示例:** 要在名为 server.log 的日志文件中查找包含 "error" 的所有行：

```bash
grep "error" server.log
```

**常用选项:**

* `-i`: 忽略大小写（例如 Error、error 和 ERROR 都会匹配）。
* `-n`: 显示匹配行的行号。
* `-v`: 反转搜索，显示不包含模式的行。

```bash
grep -in "failed" logfile.txt
```

## 2. awk: 模式扫描和处理

命令 `awk` 是一种专门用于模式扫描和文本处理的强大编程语言。`awk` 根据指定分隔符（如空格）将每行分隔为字段（列），然后对这些字段执行操作。

```bash
awk '{print $1}' file.txt
```

**实用示例:** 如果你有一个名为 users.txt 的文件，内容如下：

```
ali 123456789
ahmed 987654321
```

你可以只提取用户名（第一个字段）使用：

```bash
awk '{print $1}' users.txt
```

输出将是：

```
ali
ahmed
```

**高级示例:** 从 `ps aux` 输出中提取占用内存最多的用户：

```bash
ps aux | awk 'NR>1 {print $1, $4}' | sort -k2nr | head -n 1
```

该命令将 `awk` 与其他工具结合以实现复杂结果。

## 3. sed: 流编辑器

命令 `sed`（stream editor）用于修改文本流。`sed` 不会直接更改原始文件，而是对输入数据应用一系列编辑并打印修改后的输出。

```bash
sed 's/old/new/g' file.txt
```

* `s`: 替换命令。
* `old`: 要替换的模式。
* `new`: 新值。
* `g`: 表示全局替换，替换行内所有匹配项。没有它，则只替换第一次匹配。

**实用示例:** 将 config.ini 文件中所有 "localhost" 替换为 "127.0.0.1" 并打印结果：

```bash
sed 's/localhost/127.0.0.1/g' config.ini
```

**注意:** 若要直接修改原文件，请使用 `-i` 选项：

```bash
sed -i 's/localhost/127.0.0.1/g' config.ini

```
