أساسيات أمان لينكس
يُعد الأمان جانبًا حيويًا في أي بيئة لينكس، سواء كنت تدير خادمًا أو تعمل على جهاز شخصي. فهم وتطبيق الممارسات الأمنية الأساسية أمر بالغ الأهمية لحماية نظامك من الوصول غير المصرح به وضمان سلامة البيانات. سيشرح هذا الدرس ببراعة كيفية تأمين نظامك بخطوات بسيطة وفعالة.

1. حافظ على تحديث نظامك
تعد تحديثات النظام أهم خطوة في الحفاظ على الأمان. تعمل التحديثات على إصلاح الثغرات الأمنية المكتشفة، مما يمنع المهاجمين من استغلالها. على توزيعات مثل Arch Linux، يمكنك استخدام:

sudo pacman -Syu

مثال عملي رائع: جدولة مهمة cron لتحديث النظام تلقائيًا خلال ساعات الذروة المنخفضة.

#!/bin/bash

# Update the system and ignore any errors
sudo pacman -Syu --noconfirm &> /dev/null

# Log the outcome to a file
if [ $? -eq 0 ]; then
  echo "$(date): System update completed successfully." >> /var/log/system_updates.log
else
  echo "$(date): Error during system update!" >> /var/log/system_updates.log
fi

هذا يضمن بقاء نظامك محدثًا دون تدخل يدوي.

2. استخدم كلمات مرور قوية ومفاتيح SSH
تُعد كلمات المرور الضعيفة خطرًا أمنيًا كبيرًا. استخدم كلمات مرور طويلة ومعقدة. بالنسبة للخوادم، اعتمد دائمًا على مفاتيح SSH للوصول عن بعد بدلاً من كلمات المرور.

مثال عملي رائع: تعطيل الوصول عبر SSH القائم على كلمة المرور والسماح فقط بالمصادقة القائمة على مفتاح SSH.

# Edit the SSH configuration file
sudo nano /etc/ssh/sshd_config

# Change the following line:
# PasswordAuthentication yes
# to
PasswordAuthentication no

# Restart SSH service
sudo systemctl restart sshd

هذا يمنع هجمات القوة الغاشمة ويعزز أمان الخادم بشكل كبير.

3. استخدم جدار حماية
جدار الحماية هو خط دفاعك الأول ضد الهجمات الخارجية. يسمح لك بتحديد المنافذ والبروتوكولات المسموح بها.

مثال عملي رائع: بالنسبة لخادم ويب مزود بوصول SSH، افتح فقط المنفذين 22 (SSH) و 80 (HTTP).

# Enable the firewall
sudo ufw enable

# Allow access to SSH (22) and web (80) ports
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp

# Deny all other incoming connections
sudo ufw default deny incoming

# Verify the rules
sudo ufw status

هذا يضمن أن نظامك يقبل فقط الاتصالات الضرورية.

4. مراقبة السجلات
تسجل أنظمة لينكس الأنشطة في /var/log. تساعد مراقبة السجلات على اكتشاف الأنشطة المشبوهة.

مثال عملي رائع: مراقبة سجلات المصادقة لمحاولات تسجيل الدخول الفاشلة.

# Display the last 500 lines of failed logins
tail -n 500 /var/log/auth.log | grep "Failed password"

هذا يسلط الضوء على محاولات تسجيل الدخول الفاشلة، مما يساعد في تحديد الهجمات المحتملة.