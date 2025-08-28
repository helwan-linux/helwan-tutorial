عمليات الملفات في Bash
يُعد العمل مع الملفات جانبًا أساسيًا في أي سكريبت Shell. توفر Bash مجموعة قوية من الأوامر المدمجة والصيغ للتحقق من وجود الملفات، وقراءة المحتوى، والكتابة إلى الملفات. إن إتقان هذه العمليات أمر بالغ الأهمية لمهام مثل الأتمتة، ومعالجة البيانات، والتسجيل.

1. التحقق من وجود ملف
قبل أن يحاول السكريبت قراءة أو الكتابة إلى ملف، من أفضل الممارسات التحقق أولاً من وجوده. تُستخدم صيغة [ -f "filename" ] للتحقق مما إذا كان الملف العادي موجودًا وليس دليلًا.

if [ -f "myfile.txt" ]; then
  echo "File exists."
fi

مثال عملي رائع: سكريبت يتحقق من وجود ملف إعدادات قبل محاولة بدء خدمة. هذا يمنع السكريبت من الفشل بحدوث خطأ.

#!/bin/bash
CONFIG_FILE="/etc/my_app/config.conf"

if [ -f "$CONFIG_FILE" ]; then
  echo "Configuration file found. Starting application..."
  # Start the application or service here
else
  echo "Error: Configuration file not found at $CONFIG_FILE" >&2
  exit 1
fi

2. قراءة ملف سطرًا بسطر
تُعد قراءة ملف سطرًا بسطر مهمة شائعة لمعالجة ملفات السجل أو تقارير البيانات. تُعد حلقة while جنبًا إلى جنب مع read الطريقة الأكثر قوة وكفاءة للتعامل مع هذا، مما يمنع المشاكل مع الأحرف الخاصة والمسافات.

while IFS= read -r line; do
  echo "$line"
done < "myfile.txt"

IFS=: يُعين مؤقتًا فاصل الحقول الداخلي إلى لا شيء، مما يمنع قص المسافات البيضاء البادئة/اللاحقة.

-r: يمنع تفسير الرموز الخلفية.

done < "myfile.txt": يُعيد توجيه محتوى الملف إلى المدخل القياسي لحلقة while.

مثال عملي رائع: سكريبت يُعالج قائمة بأسماء المستخدمين من ملف ويُنشئ مستخدمًا جديدًا لكل واحد.

#!/bin/bash
USER_LIST_FILE="new_users.txt"

if [ ! -f "$USER_LIST_FILE" ]; then
  echo "Error: User list file not found!" >&2
  exit 1
fi

while IFS= read -r username; do
  echo "Creating user account for: $username"
  sudo useradd -m "$username"
done < "$USER_LIST_FILE"

echo "User creation process completed."

3. الكتابة إلى ملف
للكتابة إلى ملف، يمكنك استخدام عامل إعادة توجيه المخرجات >. هذا العامل سيحل محل محتوى الملف إذا كان موجودًا بالفعل.

echo "Hello World" > output.txt

مثال عملي رائع: سكريبت يُنشئ ملف سجل مع طابع زمني ورسالة حالة.

#!/bin/bash
LOG_FILE="server_status.log"

# Overwrite the log file with a new header
echo "--- Server Status Report ---" > "$LOG_FILE"

# Check server status and append the result
if ping -c 1 example.com &> /dev/null; then
  echo "Timestamp: $(date)" >> "$LOG_FILE"
  echo "Status: OK - Server is reachable." >> "$LOG_FILE"
else
  echo "Timestamp: $(date)" >> "$LOG_FILE"
  echo "Status: ERROR - Server is unreachable!" >> "$LOG_FILE"
fi

4. الإلحاق بملف
إذا كنت تريد إضافة محتوى إلى نهاية ملف دون استبدال محتواه الموجود، يمكنك استخدام عامل إعادة توجيه الإلحاق >>. هذا ضروري للتسجيل وإنشاء تقارير مستمرة.

echo "Another line" >> output.txt

مثال عملي رائع: سكريبت يُسجل جميع محاولات النسخ الاحتياطي الناجحة والفاشلة في ملف سجل واحد ومستمر.

#!/bin/bash
BACKUP_LOG="backup_history.log"
BACKUP_DIR="/var/www/data"

# Perform the backup
tar -czf "backup_$(date +%Y-%m-%d).tar.gz" "$BACKUP_DIR" &> /dev/null

# Check the exit status and append a status line to the log file
if [ $? -eq 0 ]; then
  echo "$(date): Backup of $BACKUP_DIR was successful." >> "$BACKUP_LOG"
else
  echo "$(date): ERROR: Backup of $BACKUP_DIR failed!" >> "$BACKUP_LOG"
fi
