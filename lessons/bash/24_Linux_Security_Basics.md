# Lesson 16: Linux Security Basics
Security is vital in Linux environments.

## Tips
- Keep system updated: `sudo pacman -Syu`
- Use strong passwords and ssh keys
- Limit sudo access
- Use firewalls like `ufw` or `iptables`
- Monitor logs in `/var/log`

## Example Firewall Commands
```bash
sudo ufw enable
sudo ufw allow 22/tcp
sudo ufw status
```

## Summary
Basic security measures protect your Linux system from unauthorized access.
