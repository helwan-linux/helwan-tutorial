

# Cron Jobs and Scheduling (Spanish)

Cron es una herramienta potente en Linux utilizada para automatizar tareas recurrentes. Un "trabajo cron" es un comando o script programado que se ejecuta automáticamente en un momento o intervalo específico. Esto es esencial para tareas de administración del sistema como respaldos, rotación de registros y ejecución de scripts personalizados.

## 1. Editar trabajos Cron

Para gestionar trabajos cron del usuario actual, utiliza `crontab` con la opción `-e`.

```bash
crontab -e
```

**Qué hace:** Abre tu archivo crontab en un editor de texto (generalmente nano o vim). Cada línea representa un trabajo cron.

## 2. Sintaxis de trabajo Cron

Un trabajo cron tiene dos partes: **el horario** y **el comando a ejecutar**. El horario se define mediante cinco campos:

```
minute hour day_of_month month day_of_week command_to_execute
```

* **Minuto (0-59)**
* **Hora (0-23)**
* **Día del mes (1-31)**
* **Mes (1-12)**
* **Día de la semana (0-6)**, 0 y 7 son domingo.

El asterisco (`*`) significa "cada" valor posible.

## 3. Ejemplos prácticos

### Ejemplo 1: Ejecutar todos los días a medianoche

```bash
0 0 * * * /path/to/script.sh
```

### Ejemplo 2: Ejecutar cada 30 minutos

```bash
*/30 * * * * /path/to/another_script.sh
```

### Ejemplo 3: Ejecutar a las 2:30 PM el primer día de cada mes

```bash
30 14 1 * * /path/to/monthly_report.sh
```

## 4. Gestión de Crontab

* `crontab -l`: lista trabajos cron actuales.
* `crontab -r`: elimina todos los trabajos cron (**¡usar con precaución!**).

✅ Usar trabajos cron garantiza que las tareas repetitivas se ejecuten de manera confiable y automática.

---

