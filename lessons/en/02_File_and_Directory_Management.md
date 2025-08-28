# File and Directory Management

Managing files and directories is an essential skill for any Linux user. Mastering these commands will give you efficient control over your file system.

## 1. Listing Files and Directories
The `ls` command is used to list the contents of the current directory. To show detailed information about files and directories, use:

```bash
ls -l
```

- `-l`: Displays a long listing that includes file permissions, number of links, owner, group, file size, and modification date.

## 2. Creating a Directory
To create a new directory (folder), use the `mkdir` (make directory) command.

```bash
mkdir my_directory
```

- You can create multiple directories at once by separating their names with a space.
- To create a directory within a nonexistent parent directory, use the `-p` option:

```bash
mkdir -p parent_directory/my_directory
```

## 3. Navigating Directories
The `cd` (change directory) command is used to move between directories.

```bash
cd my_directory
```

- `cd ..`: Moves up to the parent directory.
- `cd` or `cd ~`: Returns to your home directory.

## 4. Copying Files
The `cp` (copy) command is used to copy files from one location to another.

```bash
cp source.txt destination.txt
cp file.txt /path/to/directory/
cp -r directory_a directory_b
```

- `cp -r`: Copies a directory and all its contents recursively.

## 5. Moving and Renaming Files
The `mv` (move) command is used to move or rename files and directories.

```bash
mv oldname.txt newname.txt
```

- **Renaming**: If the new file is in the same directory.
- **Moving**: If `newname.txt` is a path to another directory, the file will be moved to that location.

## 6. Deleting Files and Directories
The `rm` (remove) command is used to delete files.

```bash
rm filename.txt
rm -i filename.txt
rm -r directory_name
rm -f file.txt
```

- `rm -i`: Prompts for confirmation before deletion (useful for safety).
- `rm -r`: Deletes a directory and all its contents recursively.
- `rm -f`: Forces deletion without confirmation.

## 7. Displaying the Current Directory
The `pwd` (print working directory) command prints the full path of the directory you're currently in.

```bash
pwd
