---

# Networking Basics (Spanish)

Comprender los comandos de red fundamentales es esencial para solucionar problemas de conectividad y monitorear la actividad de red en un sistema Linux. Estas herramientas proporcionan visibilidad en las interfaces de red, conexiones y comunicación con otros hosts.

## 1. Comprobar la dirección IP

El comando `ip addr show` es el estándar moderno para ver la información de las interfaces de red, incluyendo direcciones IP. Reemplaza al comando antiguo `ifconfig`.

```bash
ip addr show
```

**Qué hace:** Muestra una lista de todas las interfaces de red en tu sistema (por ejemplo, eth0 para Ethernet, wlan0 para Wi-Fi) junto con sus direcciones IP asignadas (IPv4 e IPv6), direcciones MAC y otros detalles.

**Ejemplo:** La salida mostrará secciones para cada interfaz. Busca `inet` para ver la dirección IPv4 (por ejemplo, `inet 192.168.1.100/24`) y `inet6` para la dirección IPv6.

---

## 2. Hacer ping a un host

El comando `ping` es una herramienta clásica para probar la conectividad con un host remoto. Envía una serie de paquetes de datos pequeños y mide el tiempo de respuesta.

```bash
ping google.com
```

**Qué hace:** Envía paquetes ICMP al host especificado (google.com) para comprobar si es accesible y medir el retraso de ida y vuelta.

**Por qué es útil:** Ayuda a determinar rápidamente si un host está en línea y si hay problemas de latencia entre tu máquina y el host remoto.

---

## 3. Mostrar puertos abiertos y sockets en escucha

El comando `ss` (estadísticas de sockets) es una utilidad moderna y eficiente para examinar conexiones activas y puertos en escucha. Es el sucesor de `netstat`.

```bash
ss -tuln
```

* `-t`: Muestra sockets TCP.
* `-u`: Muestra sockets UDP.
* `-l`: Muestra solo sockets en escucha.
* `-n`: Muestra direcciones numéricas en lugar de resolver nombres de host.

**Ejemplo práctico:** Perfecto para comprobar qué servicios se están ejecutando y en qué puertos están escuchando, como un servidor web en el puerto 80 o 443.

**Nota sobre netstat:** Aunque se recomienda `ss`, el comando `netstat` todavía se usa ampliamente.

```bash
netstat -tuln
```

---

## 4. Rastrear la ruta a un host

`traceroute` se usa para mostrar la ruta que toman los paquetes desde tu máquina hasta un host objetivo. Muy útil para identificar cuellos de botella o fallos en la red.

```bash
traceroute google.com
```

**Qué hace:**

* Muestra todos los routers intermedios (hops) que atraviesa el paquete.
* Muestra el tiempo de ida y vuelta en cada hop.

**Caso de uso:** Ayuda a diagnosticar dónde ocurren problemas de conectividad (por ejemplo, en tu ISP o más arriba).

---

## 5. Consulta DNS

`dig` (Domain Information Groper) es una herramienta potente para consultar servidores DNS y buscar registros.

```bash
dig google.com
```

**Qué hace:**

* Muestra la dirección IP del dominio.
* Muestra detalles de registros DNS (A, MX, TXT, CNAME, etc.).

**Ejemplo:** Para encontrar los registros MX de un dominio:

```bash
dig google.com MX
```

---

## 6. Comprobar conectividad con curl o wget

`curl` y `wget` son herramientas útiles para probar la conectividad a servicios HTTP/HTTPS.

```bash
curl -I https://example.com
```

**Qué hace:**

* Obtiene los encabezados HTTP del servidor para verificar que el servicio responde.
