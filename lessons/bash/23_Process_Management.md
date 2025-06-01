# Lesson 15: Process Management
Processes are running programs. Managing them is crucial for system stability.

## Common Commands
- `ps aux`: List all running processes.
- `top`: Interactive process viewer.
- `htop`: Enhanced `top` (if installed).
- `kill <PID>`: Terminate a process by PID.
- `killall <name>`: Kill all processes by name.
- `nice` and `renice`: Change process priority.

## Example
```bash
ps aux | grep apache2
kill 1234
```

## Summary
Process management helps control system resource usage and troubleshoot issues.
