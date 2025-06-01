# Arch Linux Basic Commands

Arch Linux is a lightweight and flexible Linux distribution that tries to Keep It Simple. Here are some essential commands to get you started:

## System Update and Package Management

- Update package database:

  sudo pacman -Sy

- Upgrade all installed packages:

  sudo pacman -Syu

- Install a package:

  sudo pacman -S package_name

- Remove a package:

  sudo pacman -R package_name

- Search for a package:

  pacman -Ss keyword

- List installed packages:

  pacman -Q

## System Information

- Check kernel version:

  uname -r

- Check system uptime:

  uptime

- Show disk usage:

  df -h

- Show memory usage:

  free -h

## User and Permission Management

- Add a new user:

  sudo useradd -m username

- Set password for user:

  sudo passwd username

- Modify user (add to group):

  sudo usermod -aG groupname username

## System Control

- Start/stop/restart a service:

  sudo systemctl start service_name
  sudo systemctl stop service_name
  sudo systemctl restart service_name

- Enable service at boot:

  sudo systemctl enable service_name

- Disable service at boot:

  sudo systemctl disable service_name

## Miscellaneous

- View system logs:

  journalctl -xe

- Mount a filesystem:

  sudo mount /dev/sdXY /mnt

- Unmount a filesystem:

  sudo umount /mnt

---

End of Arch Linux commands essentials.
