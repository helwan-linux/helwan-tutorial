---

# Package Management (Spanish)

La gestión de paquetes es la piedra angular de la administración de sistemas Linux. Un gestor de paquetes es un conjunto de herramientas de software que automatiza el proceso de instalación, actualización, configuración y eliminación de paquetes de software. Usar un gestor de paquetes es la forma estándar y más segura de manejar el software en tu máquina Linux.

Este lección cubre los dos gestores de paquetes más comunes: **APT (usado por Debian/Ubuntu)** y **Pacman (usado por Arch Linux)**.

---

## 1. Debian/Ubuntu (APT)

**APT (Advanced Package Tool)** es el gestor de paquetes predeterminado de Debian y sus derivados como Ubuntu. Funciona con archivos `.deb` y depende de repositorios para obtener software.

### Actualizar listas de paquetes

```bash
sudo apt update
```

* **Importancia:** Sincroniza tu lista local de paquetes con los repositorios. No instala ni actualiza software, pero asegura que conozcas las últimas versiones y paquetes nuevos. Ejecútalo antes de instalar o actualizar.

### Actualizar paquetes instalados

```bash
sudo apt upgrade
```

* **Función:** Actualiza todos los paquetes instalados a sus versiones más recientes. Es esencial para mantener el sistema seguro y actualizado.

### Instalar un paquete nuevo

```bash
sudo apt install package_name
```

* **Cómo funciona:** Descarga e instala el paquete especificado junto con sus dependencias.
* **Ejemplo:**

```bash
sudo apt install neofetch
```

Instala *Neofetch*, una herramienta para mostrar información del sistema.

### Eliminar un paquete

```bash
sudo apt remove package_name
```

* **Función:** Elimina el paquete especificado, pero deja los archivos de configuración.

Para una eliminación completa (incluyendo archivos de configuración):

```bash
sudo apt purge package_name
```

---

## 2. Arch Linux (Pacman)

**Pacman** es el gestor de paquetes de Arch Linux y sus derivados. Es conocido por su simplicidad y potencia.

### Sincronizar y actualizar

```bash
sudo pacman -Sy
```

* **Función:** Sincroniza las bases de datos de paquetes (similar a `apt update`).

### Sincronizar, actualizar y mejorar

```bash
sudo pacman -Syu
```

* **Función:** El comando más común en Arch. Sincroniza bases de datos (`-y`) y actualiza todos los paquetes instalados (`-u`).

### Instalar un paquete nuevo

```bash
sudo pacman -S package_name
```

* **Cómo funciona:** Instala un paquete nuevo. A menudo se usa con sincronización.
* **Ejemplo:**

```bash
sudo pacman -S brave
```

Instala el navegador Brave.

### Eliminar un paquete

```bash
sudo pacman -R package_name
```

* **Función:** Elimina un paquete, pero deja dependencias no utilizadas.

Opciones recursivas y de limpieza:

```bash
sudo pacman -Rs package_name   # Elimina paquete + dependencias no utilizadas
sudo pacman -Rns package_name  # Elimina paquete + dependencias + archivos de configuración

```
