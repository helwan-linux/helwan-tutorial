# Lesson 18: Error Handling in Bash Scripts

Handling errors properly improves script robustness.

## Checking exit status
```bash
command
if [ $? -ne 0 ]; then
  echo "Command failed."
fi
```

## Using set -e
Make script exit on any command failure:

```bash
set -e
```

## Trapping errors
```bash
trap 'echo "Error occurred!"' ERR
```

## Custom error messages
```bash
function error_exit {
  echo "$1" 1>&2
  exit 1
}
```

Error handling helps maintain script stability.