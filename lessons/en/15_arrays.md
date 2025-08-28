# Arrays in Bash

Arrays in Bash are a powerful feature for storing collections of values in a single variable, making them ideal for managing lists of data in your scripts. Instead of dealing with each value as a separate variable, arrays allow you to access and manipulate data in an organized and efficient way.

## 1. Declaring Arrays

You can declare a one-dimensional array by assigning a list of values to it. The elements are placed inside parentheses `()` and separated by spaces.

```bash
FRUITS=("apple" "banana" "cherry")
```

**Practical Example:** Imagine you have a list of server names that you need to check. You can store them in an array to simplify the process.

```bash
#!/bin/bash
# Declare an array of server names
SERVERS=("web-server-01" "db-server-01" "app-server-02")

# You can print the entire array
echo "Server list: ${SERVERS[@]}"
```

---

## 2. Accessing Elements

To access an individual element of the array, use its index (position) which starts from 0.

```bash
echo ${FRUITS[1]}
# Output: banana
```

**Practical Example:** Accessing the first and third elements from the SERVERS array.

```bash
#!/bin/bash
SERVERS=("web-server-01" "db-server-01" "app-server-02")

# Access the first element (index 0)
echo "First server: ${SERVERS[0]}"

# Access the third element (index 2)
echo "Third server: ${SERVERS[2]}"
```

---

## 3. Adding Elements

You can add new elements to an existing array using the `+=` operator.

```bash
FRUITS+=("date")
```

**Practical Example:** Add a new server to the existing SERVERS array.

```bash
#!/bin/bash
SERVERS=("web-server-01" "db-server-01")
echo "Server list before adding: ${SERVERS[@]}"

# Add a new server
SERVERS+=("monitoring-server-03")

echo "Server list after adding: ${SERVERS[@]}"
```

---

## 4. Looping Through Arrays

To iterate over all elements of an array, you can use a `for` loop with the `[@]` symbol, which represents all elements.

```bash
for fruit in "${FRUITS[@]}"; do
  echo "Fruit: $fruit"
done
```

**Brilliant Practical Example:** Let's perform a ping check on each server in our array. This type of script is essential for monitoring network health.

```bash
#!/bin/bash

# List of server names
SERVERS=("web-server-01" "db-server-01" "google.com")

# Loop through each server in the array
for server in "${SERVERS[@]}"; do
  echo "Pinging server: $server..."

  # Send a single ping packet (-c 1) and redirect output to null
  ping -c 1 "$server" &> /dev/null

  # Check the exit status of the last command
  if [ $? -eq 0 ]; then
    echo "✅ Successfully connected to: $server"
  else
    echo "❌ Failed to connect to: $server"
  fi

  echo "---"
done
```

---

This example demonstrates how arrays simplify complex tasks that require iteration over a list of data.
