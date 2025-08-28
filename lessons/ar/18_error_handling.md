معالجة الأخطاء في أوامر Bash
تُعد المعالجة السليمة للأخطاء مهارة حاسمة لكتابة أوامر Shell قوية وموثوقة. من خلال توقع وإدارة حالات الفشل المحتملة، يمكنك ضمان أن تتصرف أوامرك بشكل متوقع، وتقدم ملاحظات مفيدة، وتمنع تلف البيانات أو سلوك النظام غير المتوقع.

1. التحقق من حالة الخروج
بعد تنفيذ كل أمر، يتم تعيين متغير خاص $؟ على حالة الخروج الخاصة به. تشير القيمة 0 إلى النجاح، بينما تشير أي قيمة أخرى (عادةً من 1 إلى 255) إلى الفشل. يتيح لك التحقق من هذه الحالة إنشاء منطق شرطي يستجيب لفشل الأوامر.

command
if [ $? -ne 0 ]; then
  echo "Command failed."
fi

مثال عملي رائع
سكريبت يحاول تنزيل ملف ثم يشرع في معالجته فقط إذا كان التنزيل ناجحًا.

#!/bin/bash

# Attempt to download a file
wget -q http://example.com/data.txt

# Check the exit status of the wget command
if [ $? -ne 0 ]; then
  echo "Error: Failed to download the file from the source." >&2
  exit 1
else
  echo "File downloaded successfully. Processing..."
  # Add further commands to process the file here
fi

2. استخدام set -e
يُعد الأمر set -e، المعروف أيضًا باسم الخروج عند الخطأ، توجيهًا قويًا يجبر السكريبت على الخروج فورًا إذا فشل أي أمر. هذه طريقة ممتازة لمنع السكريبت من الاستمرار في عملية يحتمل أن تكون خطيرة بعد فشل خطوة سابقة.

set -e

مثال عملي رائع
سكريبت يُنفذ سلسلة من المهام الحرجة، مثل إنشاء دليل، ونسخ ملف، ثم ضغطه. إذا فشلت أي من هذه الخطوات، يجب أن يتوقف السكريبت لمنع حالة غير متسقة.

#!/bin/bash
# Exit immediately if a command fails
set -e

# Create a directory for the backup
mkdir /tmp/backup_data

# Copy a critical file. If this fails, the script will exit.
cp /var/log/syslog /tmp/backup_data/

# Compress the directory. This will not run if the 'cp' command fails.
tar -czf /root/backup.tar.gz /tmp/backup_data

echo "Backup completed successfully!"

3. اعتراض الأخطاء (trap)
يسمح لك الأمر trap بتنفيذ أمر أو دالة محددة عند تلقي إشارة. تُعد إشارة ERR مفيدة بشكل خاص لمعالجة الأخطاء، حيث يتم تشغيلها كلما خرج أمر بحالة غير صفرية.

trap 'echo "Error occurred!"' ERR

مثال عملي رائع
سكريبت يحتاج إلى تنظيف الملفات المؤقتة إذا حدث خطأ أثناء تنفيذه. يضمن الأمر trap أن يتم استدعاء دالة التنظيف بغض النظر عن مكان فشل السكريبت.

#!/bin/bash

# Define a function to handle cleanup
cleanup() {
  echo "An error occurred. Cleaning up temporary files..." >&2
  rm -f /tmp/temp_file_*
}

# Set the trap to call the cleanup function on any error
trap cleanup ERR

echo "Starting script..."

# A command that is likely to fail, triggering the trap
touch /root/temp_file_1

echo "This line will not be reached if the above command fails."

4. رسائل خطأ مخصصة
بينما تُعد set -e و trap قويتين، يمكنك تحسين معالجة الأخطاء عن طريق إنشاء دالة مخصصة لتوفير رسائل خطأ أكثر وصفية. يمكن لهذه الدالة طباعة رسالة إلى الخطأ القياسي (stderr) ثم إنهاء السكريبت.

function error_exit {
  echo "$1" 1>&2
  exit 1
}

مثال عملي رائع
سكريبت يتحقق من صحة وسيطات سطر الأوامر ويوفر رسالة استخدام مفيدة إذا قدم المستخدم مدخلات غير صحيحة.

#!/bin/bash

# Define a custom function for errors
function error_exit() {
  echo "Error: $1" >&2
  exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  error_exit "Incorrect number of arguments. Usage: $0 <source_dir> <destination_dir>"
fi

SOURCE_DIR="$1"
DEST_DIR="$2"

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
  error_exit "Source directory '$SOURCE_DIR' does not exist."
fi

echo "Script is running with valid arguments."
# ... rest of the script ...
