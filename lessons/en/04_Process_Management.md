# Process Management

Processes are running programs. Understanding how to manage them gives you significant control over your system's performance and allows you to troubleshoot issues.

## 1. Viewing Running Processes
The `ps aux` command is one of the most common ways to display all currently running processes.

```bash
ps aux
```

- `a`: Shows processes for all users.
- `u`: Displays processes in a user-oriented format.
- `x`: Includes processes not attached to a specific terminal.

When you run this command, you'll see a table with important information, such as:
- **USER**: The user who owns the process.
- **PID**: The unique Process ID for each process.
- **%CPU**: The percentage of CPU usage.
- **%MEM**: The percentage of memory usage.
- **COMMAND**: The command that started the process.

## 2. Killing a Process by its PID
If a process is unresponsive or consuming excessive resources, you can terminate it using the `kill` command and its Process ID.

```bash
kill PID
kill 12345
```

- `kill 12345`: Attempts to gracefully terminate the process with PID 12345 (sending a **SIGTERM** signal).

To forcefully kill a stubborn process, use the `-9` option:

```bash
kill -9 PID
kill -9 12345
```

- `-9`: Sends a strong termination signal (**SIGKILL**) that the process cannot ignore.

## 3. Killing a Process by Name
If you don't know the PID, you can use the `pkill` command to terminate processes based on their name.

```bash
pkill process_name
pkill firefox
pkill -9 firefox
```

- `pkill firefox`: Terminates all processes named *firefox*.
- `pkill -9 firefox`: Forcefully terminates all *firefox* processes.

This is very useful when you need to close all instances of a specific program at once.

## 4. Viewing the Process Tree
The `pstree` command displays processes in a hierarchical tree format, showing the parent-child relationship between them.

```bash
pstree
pstree -p
pstree username
```

- `pstree`: Shows all processes in tree format.
- `pstree -p`: Displays the process tree with PIDs.
- `pstree username`: Shows only the processes owned by a specific user.

This visual representation makes it easy to understand which subprocesses were launched by a main process, aiding in troubleshooting.
