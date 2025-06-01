# Lesson 17: Automating Tasks with Cron
Cron allows scheduling tasks automatically.

## Viewing Cron Jobs
```bash
crontab -l
```

## Editing Cron Jobs
```bash
crontab -e
```

## Cron Format
```
* * * * * command_to_run
- - - - -
| | | | |
| | | | +---- Day of week (0-7)
| | | +------ Month (1-12)
| | +-------- Day of month (1-31)
| +---------- Hour (0-23)
+------------ Minute (0-59)
```

## Example Cron Job
Run backup script every day at 2am:
```bash
0 2 * * * /home/user/backup.sh
```

## Summary
Cron automates repetitive tasks by scheduling commands to run at specified times.
