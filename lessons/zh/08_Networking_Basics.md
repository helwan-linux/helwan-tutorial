---

# Networking Basics (Chinese)

理解基本的网络命令对于排查连接问题和监控 Linux 系统的网络活动至关重要。这些工具可以让你查看机器的网络接口、连接以及与其他主机的通信情况。

## 1. 检查 IP 地址

命令 `ip addr show` 是查看网络接口信息（包括 IP 地址）的现代标准。它替代了旧的 `ifconfig` 命令。

```bash
ip addr show
```

**功能:** 显示系统中所有网络接口的列表（例如，Ethernet 的 eth0，Wi-Fi 的 wlan0）以及其分配的 IP 地址（IPv4 和 IPv6）、MAC 地址及其他信息。

**示例:** 输出会显示每个接口的部分。查找 `inet` 可查看 IPv4 地址（例如 `inet 192.168.1.100/24`），`inet6` 可查看 IPv6 地址。

---

## 2. Ping 主机

命令 `ping` 是测试与远程主机连接的经典工具。它发送一系列小数据包并测量响应时间。

```bash
ping google.com
```

**功能:** 向指定主机（google.com）发送 ICMP 数据包，以检查是否可达并测量往返延迟。

**用途:** 快速判断主机是否在线，以及你与远程主机之间是否存在网络延迟问题。

---

## 3. 显示开放端口和监听套接字

命令 `ss`（socket statistics）是检查活动连接和监听端口的现代高效工具，是 `netstat` 的继任者。

```bash
ss -tuln
```

* `-t`: 显示 TCP 套接字
* `-u`: 显示 UDP 套接字
* `-l`: 仅显示监听套接字
* `-n`: 显示数字地址而非尝试解析主机名

**实际示例:** 检查系统上运行的服务及其监听端口，如 Web 服务器监听 80 或 443 端口。

**netstat 注释:** 虽然推荐使用 `ss`，但 `netstat` 仍被广泛使用并可用。

```bash
netstat -tuln
```

---

## 4. 跟踪到主机的路由

命令 `traceroute` 用于显示数据包从你的机器到目标主机的路径，非常适合识别网络瓶颈或故障。

```bash
traceroute google.com
```

**功能:**

* 显示数据包经过的所有中间路由器（跳数）
* 显示每跳的往返时间

**用途:** 帮助诊断连接问题发生的位置（例如 ISP 或更上游）。

---

## 5. DNS 查询

命令 `dig`（Domain Information Groper）是强大的工具，用于查询 DNS 服务器和记录。

```bash
dig google.com
```

**功能:**

* 显示域名的 IP 地址
* 显示 DNS 记录详情（A, MX, TXT, CNAME 等）

**示例:** 查找域的 MX（邮件交换）记录:

```bash
dig google.com MX
```

---

## 6. 使用 curl 或 wget 检查连接

`curl` 和 `wget` 是测试 HTTP/HTTPS 服务连接的实用工具。

```bash
curl -I https://example.com
```

**功能:** 获取服务器的 HTTP 头以验证服务是否响应。
