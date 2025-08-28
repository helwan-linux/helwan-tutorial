المتغيرات المتقدمة في Bash
في بيئة سطر الأوامر Bash، تُعد المتغيرات أدوات أساسية لتخزين البيانات. إن فهم أنواع المتغيرات المتقدمة وكيفية التعامل معها يمنحك تحكمًا أكبر في أوامرك، مما يجعلها أكثر ديناميكية وقوة.

1. استبدال الأوامر (Command Substitution)
استبدال الأوامر هو تقنية تتيح لك تعيين مخرجات أمر لمتغير. هذه ميزة قوية لتشغيل أمر في وقت التشغيل وتخزين مخرجاته لاستخدامها لاحقًا في الأمر الخاص بك.

يمكنك استخدام الصيغة الحديثة $(...) أو الأقواس المعقوفة القديمة .... يفضل استخدام الصيغة الحديثة $(...) لأنها أسهل في القراءة ويمكن أن تكون متداخلة.

مثال:

CURRENT_DATE=$(date)

مثال عملي رائع: تخيل أنك بحاجة إلى إنشاء نسخة احتياطية يومية وتسميتها بناءً على التاريخ الحالي. يمكنك استخدام استبدال الأوامر لتعيين اسم الملف تلقائيًا.

#!/bin/bash
# Store the current date in a variable
BACKUP_DATE=$(date +%Y-%m-%d)

# Use the variable to determine the file name
BACKUP_FILE="backup_data_${BACKUP_DATE}.zip"

# Create the compressed file with the dynamic name
tar -czf "$BACKUP_FILE" /var/www/html/
echo "Backup file created: $BACKUP_FILE"

2. المتغيرات للقراءة فقط (Read-only Variables)
إذا كنت تريد التأكد من أن قيمة متغير لا يمكن تغييرها عن طريق الخطأ في أمر طويل، يمكنك جعله للقراءة فقط باستخدام الأمر readonly.

مثال:

readonly PI=3.14159

ملاحظة: أي محاولة لتغيير قيمة هذا المتغير (على سبيل المثال، PI=3) ستؤدي إلى حدوث خطأ.

مثال عملي رائع: في أمر إدارة النظام، قد تحتاج إلى تعريف مسارات حساسة لا ينبغي تغييرها أبدًا. جعل هذه المتغيرات للقراءة فقط يضيف طبقة من الأمان لمنع التعديلات العرضية.

#!/bin/bash

# Define the core log directory and make it read-only
readonly LOG_DIR="/var/log/my_app/"

# Attempt to write a log file
echo "Application started." >> "${LOG_DIR}app.log"

# If someone tries to change the path, it will fail
# LOG_DIR="/tmp/" # This line will cause an error

3. تصدير المتغيرات (Exporting Variables)
بشكل افتراضي، تكون المتغيرات في أمر معين متاحة فقط داخل هذا الأمر. لجعل متغير متاحًا للعمليات الفرعية التي تعمل من الأمر، يجب عليك تصديره باستخدام الأمر export.

مثال:

export PATH=$PATH:/my/custom/path

مثال عملي رائع: افترض أن لديك أمرًا رئيسيًا يقوم بتشغيل أمر فرعي، وتحتاج إلى تمرير متغير بيئة إلى الأمر الفرعي.

الأمر الرئيسي (parent_script.sh):

#!/bin/bash

# Define and export a variable
export API_KEY="a1b2c3d4e5f6"

# Run the child script
./child_script.sh

الأمر الفرعي (child_script.sh):

#!/bin/bash

# The exported variable is now accessible
echo "API Key is: $API_KEY"

بفضل export، يمكن لـ child_script.sh الوصول إلى قيمة API_KEY.

4. إلغاء تعيين المتغيرات (Unsetting Variables)
لإزالة متغير من الذاكرة وإلغاء تعريفه تمامًا، يمكنك استخدام الأمر unset. هذا مفيد لتحرير الذاكرة أو للتأكد من عدم استخدام متغير قديم عن طريق الخطأ.

مثال:

unset VARIABLE_NAME

مثال عملي رائع: بعد استخدام متغير يحتوي على كلمة مرور أو معلومات حساسة أخرى، من الممارسات الجيدة إزالته من الذاكرة.

#!/bin/bash

# A variable containing a password
SECRET_PASSWORD="my_super_secret_password"

# Use the password (in this case, print it)
echo "Using password..."

# Remove the variable from memory
unset SECRET_PASSWORD

# Any attempt to access the variable will fail
echo "Password variable is: $SECRET_PASSWORD"
# The previous line will show as blank or a null value
