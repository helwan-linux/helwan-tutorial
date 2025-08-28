# Lesson 14: Permissions and Sudo
Linux permissions control access to files and directories. Understanding permissions is fundamental.

## Permission Types
- `r`: Read permission.
- `w`: Write permission.
- `x`: Execute permission.

## Permission Format
Example: `-rwxr-xr--`
- Owner permissions: `rwx`
- Group permissions: `r-x`
- Others permissions: `r--`

## Changing Permissions
Use `chmod` command:
```bash
chmod u+x script.sh  # Add execute permission for owner
chmod 755 file.txt   # Set rwxr-xr-x permissions
```

## Changing Ownership
Use `chown` command:
```bash
sudo chown user:group file.txt
```

## Using sudo
`sodo` runs commands as superuser:
```bash
sudo apt update
sudo systemctl restart nginx
```

## Summary
Permissions secure files and sudo allows administrative tasks safely.
