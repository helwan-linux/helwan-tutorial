# Input and Output Redirection

In Linux, one of the most powerful features of the command line is the ability to redirect the input and output of commands. This allows you to chain commands together and automate tasks without needing to write complex scripts.

## 1. Redirecting Output to a File (Overwrite)
The `>` operator sends the standard output of a command to a specified file. If the file already exists, it will be completely overwritten with the new output.

```bash
ls -l > file_list.txt
```

**Example:** Normally, `ls -l` displays a long list of files and directories on your terminal. By using `>`, this output is redirected and saved to a new file called `file_list.txt`.

## 2. Appending Output to a File
The `>>` operator also redirects standard output to a file, but instead of overwriting the file, it appends the new output to the end of the file's existing content.

```bash
echo "This is a new line" >> logfile.txt
```

**Example:** If `logfile.txt` already contains some text, this command will add the line *"This is a new line"* to the very end of the file, preserving its original content. This is a common practice for logging.

## 3. Redirecting Input from a File
The `<` operator redirects the standard input of a command to come from a file instead of the keyboard. This is useful for commands that expect to receive data from the user.

```bash
sort < unsorted_list.txt
```

**Example:** The `sort` command typically waits for you to type in lines of text and then sorts them. By using `<`, you tell `sort` to get its input from `unsorted_list.txt` and then print the sorted output to the terminal.

## 4. Piping Output to Another Command
The `|` (pipe) operator is a powerful tool that takes the standard output of one command and uses it as the standard input for another command. This allows you to combine simple commands to perform complex operations.

```bash
ls -l | grep ".txt"
```

**Example:** The output of `ls -l` (the list of all files and directories) is *piped* to the `grep` command. `grep` then filters this incoming list and only shows the lines that contain the string `.txt`. This effectively allows you to quickly find all text files in a directory.
