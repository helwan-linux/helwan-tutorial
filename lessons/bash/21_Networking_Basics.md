# Lesson 13: Networking Basics
Networking is an essential part of Linux system management. Understanding how to use network commands and tools is critical.

## Common Networking Commands
- `ifconfig`: Display network interfaces and configuration.
- `ping <host>`: Test connectivity to a host.
- `netstat`: Display network connections, routing tables, and statistics.
- `ss`: Modern alternative to netstat.
- `traceroute <host>`: Trace the route packets take to a host.
- `nslookup <domain>`: Query DNS servers for domain info.

## Checking Network Status
```bash
ip addr show
ping google.com
netstat -tuln
```

## Managing Network Interfaces
To bring an interface up or down:
```bash
sudo ifconfig eth0 down
sudo ifconfig eth0 up
```

## Summary
Networking commands help monitor and configure Linux network interfaces and troubleshoot connectivity.
