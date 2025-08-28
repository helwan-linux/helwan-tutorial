

# Cron Jobs and Scheduling (Chinese)

Cron 是 Linux 中用于自动化重复任务的强大工具。"Cron 任务" 是一个在指定时间或间隔自动执行的命令或脚本。这对于系统管理任务如备份、日志轮转和自定义脚本非常重要。

## 1. 编辑 Cron 任务

要管理当前用户的 Cron 任务，使用 `crontab` 命令和 `-e` 选项。

```bash
crontab -e
```

**功能:** 打开你的 crontab 文件在文本编辑器中（通常是 nano 或 vim）。文件中的每一行代表一个 Cron 任务。

## 2. Cron 任务语法

Cron 任务由两部分组成：**时间表** 和 **要执行的命令**。时间表由五个字段定义：

```
minute hour day_of_month month day_of_week command_to_execute
```

* **分钟 (0-59)**
* **小时 (0-23)**
* **月份中的天 (1-31)**
* **月份 (1-12)**
* **星期几 (0-6)**，0 和 7 表示星期日。

任何字段中的星号 (`*`) 表示“每一个可能的值”。

## 3. 实际示例

### 示例 1：每天午夜运行

```bash
0 0 * * * /path/to/script.sh
```

### 示例 2：每 30 分钟运行一次

```bash
*/30 * * * * /path/to/another_script.sh
```

### 示例 3：每月 1 日下午 2:30 运行

```bash
30 14 1 * * /path/to/monthly_report.sh
```

## 4. 管理 Crontab

* `crontab -l`: 列出当前 Cron 任务。
* `crontab -r`: 删除所有 Cron 任务 (**小心使用！**)

✅ 使用 Cron 任务可以确保重复维护和数据处理任务可靠且自动执行。
