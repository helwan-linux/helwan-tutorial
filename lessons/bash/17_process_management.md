# Lesson 17: Process Management in Bash

Bash allows you to manage processes easily.

## Running a command in background
```bash
sleep 60 &
```

## Listing background jobs
```bash
jobs
```

## Bringing a job to foreground
```bash
fg %1
```

## Killing a process
```bash
kill PID
```

Managing processes can help in complex scripting tasks.