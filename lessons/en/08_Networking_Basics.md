# Networking Basics

Understanding fundamental networking commands is essential for troubleshooting connectivity issues and monitoring network activity on a Linux system. These tools provide visibility into your machine's network interfaces, connections, and communication with other hosts.

## 1. Checking IP Address

The `ip addr show` command is the modern standard for viewing network interface information, including IP addresses. It's the replacement for the older `ifconfig` command.

```bash
ip addr show
```

**What it does:** Displays a list of all network interfaces on your system (e.g., eth0 for Ethernet, wlan0 for Wi-Fi) along with their assigned IP addresses (both IPv4 and IPv6), MAC addresses, and other details.

**Example:** The output will show sections for each interface. Look for `inet` to see the IPv4 address (e.g., `inet 192.168.1.100/24`) and `inet6` for the IPv6 address.

---

## 2. Pinging a Host

The `ping` command is a classic tool used to test connectivity to a remote host. It sends a series of small data packets and measures the response time.

```bash
ping google.com
```

**What it does:** Sends ICMP packets to the specified host (google.com) to check if it's reachable and to measure the round-trip delay.

**Why it's useful:** It helps you quickly determine if a host is online and if there are network latency issues between your machine and the remote host. It's a first-step troubleshooting tool.

---

## 3. Displaying Open Ports and Listening Sockets

The `ss` (socket statistics) command is a modern and more efficient utility for examining active connections and listening ports. It's a successor to `netstat`.

```bash
ss -tuln
```

* `-t`: Shows TCP sockets.
* `-u`: Shows UDP sockets.
* `-l`: Displays only listening sockets (programs waiting for connections).
* `-n`: Shows numerical addresses instead of trying to resolve hostnames.

**Practical Example:** This command is perfect for checking which services are running on your machine and which ports they are listening on, such as a web server listening on port 80 or 443.

**Note on netstat:** While `ss` is the recommended modern tool, the older `netstat` command is still widely used and available on most systems. The equivalent command is:

```bash
netstat -tuln
```

---

## 4. Tracing the Route to a Host

`traceroute` is used to display the path packets take from your machine to a target host. It’s very useful for identifying network bottlenecks or failures along the route.

```bash
traceroute google.com
```

**What it does:**

* Shows all the intermediate routers (hops) the packet travels through.
* Displays the round-trip time at each hop.

**Use case:** Helps diagnose where connectivity issues are occurring (e.g., at your ISP or further upstream).

---

## 5. DNS Lookup

`dig` (Domain Information Groper) is a powerful tool for querying DNS servers and looking up records.

```bash
dig google.com
```

**What it does:**

* Shows the IP address of the domain.
* Displays DNS record details (A, MX, TXT, CNAME, etc.).

**Example:** To find the MX (mail exchange) records for a domain:

```bash
dig google.com MX
```

---

## 6. Checking Connectivity with curl or wget

`curl` and `wget` are handy tools for testing connectivity to HTTP/HTTPS services.

```bash
curl -I https://example.com
```

**What it does:**

* Fetches the HTTP headers from the server to verify that the service is responding.

---
