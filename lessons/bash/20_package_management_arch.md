# Lesson 20: Package Management in Arch Linux

Arch Linux uses `pacman` as its package manager.

## Updating package database and system
```bash
sudo pacman -Syu
```

## Installing a package
```bash
sudo pacman -S package_name
```

## Removing a package
```bash
sudo pacman -R package_name
```

## Searching packages
```bash
pacman -Ss keyword
```

## Querying installed packages
```bash
pacman -Qs keyword
```

## Cleaning package cache
```bash
sudo pacman -Sc
```

Learning package management helps keep your system updated and clean.