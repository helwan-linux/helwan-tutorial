# Permissions and Ownership

In Linux, a robust permissions system controls access to files and directories, ensuring security and proper access for users and applications.

## 1. Viewing Permissions
To see the permissions of a file or directory, you can use the `ls -l` command.

```bash
ls -l filename.txt
```

Example output:
```
-rwxr-xr-- 1 user group 123 Jan 1 12:00 filename.txt
```

- The first part (`-rwxr-xr--`) is the permission string.
- The first character indicates the file type:
  - `-` for a regular file
  - `d` for a directory
  - `l` for a symbolic link
- The next nine characters are in three sets of three, representing permissions for **user (owner)**, **group**, and **others**.

## 2. Understanding Permission Notation
Each permission set uses three characters:

- `r`: Read permission → view file content or list directory contents.
- `w`: Write permission → modify/delete a file, or create/delete files within a directory.
- `x`: Execute permission → run a file as a program or access a directory.

### Octal Number Representation
Permissions can also be represented by a three-digit octal number:

- `r = 4`
- `w = 2`
- `x = 1`
- `No permission = 0`

These numbers are added together to form the permission value for each category (user, group, others).

Examples:
- `7 (rwx) = 4 + 2 + 1`
- `6 (rw-) = 4 + 2 + 0`
- `5 (r-x) = 4 + 0 + 1`

## 3. Changing Permissions
The `chmod` (change mode) command is used to change file permissions. The most common method uses the octal notation.

```bash
chmod 755 filename.txt
```

Explanation:
- `7 (rwx)`: The owner can read, write, and execute.
- `5 (r-x)`: The group can read and execute.
- `5 (r-x)`: Others can read and execute.

## 4. Changing Ownership
The `chown` (change owner) command is used to change the owner and/or group of a file or directory. This command requires administrator (root) privileges, so you often need to use `sudo`.

```bash
sudo chown newuser filename.txt
sudo chown newuser:newgroup filename.txt
```

- `newuser`: Changes the file owner.
- `newuser:newgroup`: Changes both the owner and the group.

This command is particularly useful when you've created a file as a root user and need to give a standard user ownership to edit it.
