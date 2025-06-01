# Lesson 19: Regular Expressions in Bash

Regular expressions (regex) allow pattern matching in strings.

## Using grep with regex
```bash
grep -E "^[a-z]+@[a-z]+\.com$" file.txt
```

## Bash regex matching
```bash
if [[ "$email" =~ ^[a-z]+@[a-z]+\.com$ ]]; then
  echo "Valid email."
fi
```

## Extracting substrings
```bash
if [[ "$string" =~ ([0-9]+) ]]; then
  echo "Number: ${BASH_REMATCH[1]}"
fi
```

Regex is powerful for validating and parsing text.