Text Processing Tools in Linux
Linux systems come with a powerful suite of tools for processing text. These utilities allow you to search, analyze, and modify text content with high efficiency. They are essential for programmers, system administrators, and anyone who deals with text-based data.

1. grep: Search for Text Patterns
The grep (Global Regular Expression Print) command is the most popular tool for searching for specific patterns within text files.

grep "pattern" filename.txt

Practical Example: To find all lines containing the word "error" in a log file named server.log:
grep "error" server.log

Common Options:

-i: Ignores case (e.g., Error, error, and ERROR will all be matched).

-n: Displays the line number along with the matching line.

-v: Inverts the search, showing lines that do not contain the pattern.

grep -in "failed" logfile.txt

2. awk: Pattern Scanning and Processing
The awk command is a powerful programming language specifically designed for pattern scanning and text processing. awk separates each line into fields (columns) based on a specified delimiter (like a space) and then performs actions on those fields.

awk '{print $1}' file.txt

Practical Example: If you have a file named users.txt containing usernames and phone numbers formatted like this:
ali 123456789
ahmed 987654321

You can extract just the usernames (the first field) using:
awk '{print $1}' users.txt
The output will be:
ali
ahmed

Advanced Example: To extract the user consuming the most memory from the output of ps aux:
ps aux | awk 'NR>1 {print $1, $4}' | sort -k2nr | head -n 1
This command combines awk with other tools to achieve a complex result.

3. sed: Stream Editor
The sed (stream editor) command is used for modifying a stream of text. sed does not change the original file directly; instead, it applies a set of edits to the incoming data and prints the modified output.

sed 's/old/new/g' file.txt

s: The substitute command.

old: The pattern you want to replace.

new: The new value.

g: Stands for global, meaning it replaces all occurrences of the pattern on a single line. Without it, only the first occurrence would be replaced.

Practical Example: To replace all instances of "localhost" with "127.0.0.1" in a config.ini file and print the result:
sed 's/localhost/127.0.0.1/g' config.ini

Note: To modify the original file directly, use the -i option.
sed -i 's/localhost/127.0.0.1/g' config.ini