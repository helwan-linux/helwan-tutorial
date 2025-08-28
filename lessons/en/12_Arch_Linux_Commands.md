# Arch Linux Basic Commands

Arch Linux is a lightweight and flexible Linux distribution that follows the "Keep It Simple, Stupid" (KISS) philosophy. While it offers a great deal of control, its command-line-centric approach requires a good understanding of its core utilities. Here are the essential commands to get you started and manage your system.

---

## 1) System Update and Package Management

Pacman is Arch's powerful package manager. These commands are critical for keeping your system up to date and installing new software.

### Update Package Database

```bash
sudo pacman -Sy
```

This command synchronizes your local package database with the Arch repositories. It's a quick and essential step to get information about the latest software versions.

### Upgrade All Installed Packages

```bash
sudo pacman -Syu
```

This is the most common command for an Arch user. The `-S` flag is for synchronization and installation, `-y` is for refreshing the package list, and `-u` is for upgrading the system. It upgrades all installed packages to their newest versions after updating the database.

### Install a Package

```bash
sudo pacman -S package_name
```

This command installs a new package and all of its required dependencies.

**Example:**

```bash
sudo pacman -S neofetch
```

### Remove a Package

```bash
sudo pacman -R package_name
```

Removes the specified package.

More thorough removals:

```bash
sudo pacman -Rs package_name   # Remove package + unneeded dependencies
sudo pacman -Rns package_name  # Remove package + unneeded deps + config files
```

### Search for a Package

```bash
pacman -Ss keyword
```

Searches the package database for packages matching the keyword.

### List Installed Packages

```bash
pacman -Q
```

Lists all packages currently installed on your system.

---

## 2) System Information

Commands that give you a quick overview of system status and resource usage.

### Check Kernel Version

```bash
uname -r
```

Displays the version of the currently running Linux kernel.

### Check System Uptime

```bash
uptime
```

Shows how long the system has been running, number of logged-in users, and load averages.

### Show Disk Usage

```bash
df -h
```

Shows disk space usage of mounted filesystems in human-readable format.

### Show Memory Usage

```bash
free -h
```

Displays total, used, and free memory in human-readable format.

---

## 3) User and Permission Management

Commands for managing user accounts and privileges.

### Add a New User

```bash
sudo useradd -m username
```

Creates a new user account (`-m` creates the home directory).

### Set Password for User

```bash
sudo passwd username
```

Sets a password for the user.

### Modify User (Add to a Group)

```bash
sudo usermod -aG groupname username
```

Adds the user to a supplementary group (`-aG` for append to group).

---

## 4) System Control (systemd)

Arch Linux uses systemd to manage services. `systemctl` is the CLI for controlling services.

### Start / Stop / Restart a Service

```bash
sudo systemctl start service_name
sudo systemctl stop service_name
sudo systemctl restart service_name
```

Controls the runtime state of a service.

### Enable / Disable Service at Boot

```bash
sudo systemctl enable service_name
sudo systemctl disable service_name
```

`enable` starts the service automatically at boot; `disable` prevents it from starting automatically.

---

## 5) Miscellaneous

Additional commands helpful for common administration tasks.

### View System Logs

```bash
journalctl -xe
```

Shows system log entries from the systemd journal (`-x` adds extra context, `-e` jumps to the end).

### Mount a Filesystem

```bash
sudo mount /dev/sdXY /mnt
```

Mounts a device (e.g., USB drive or partition) at the specified mount point.

### Unmount a Filesystem

```bash
sudo umount /mnt
```

Unmounts a filesystem from its mount point—necessary before physically removing a device.
