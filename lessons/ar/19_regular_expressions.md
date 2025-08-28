التعبيرات النمطية (Regex) في Bash
التعبيرات النمطية (regex) هي مجموعة أدوات قوية لمطابقة الأنماط ومعالجة النصوص. في برمجة أوامر Bash، تسمح لك بالبحث عن السلاسل النصية والتحقق منها وتحليلها بدقة مذهلة. إن إتقان الـ regex ضروري لأي مهمة جدية في معالجة النصوص، مثل التعامل مع ملفات السجل، والتحقق من صحة مدخلات المستخدم، أو استخراج البيانات المنظمة.

1. استخدام grep مع الـ Regex
يُعد أمر grep أداة لينكس الكلاسيكية للبحث في النصوص باستخدام الأنماط. يمكنك تمكين دعم التعبيرات النمطية الموسعة باستخدام العلامة -E، والتي تسمح بأنماط أكثر تقدمًا.

grep -E "^[a-z]+@[a-z]+\\.com$"

مثال عملي رائع: يحتاج مسؤول النظام إلى تصفية ملف سجل بسرعة للعثور على جميع الإدخالات التي تحتوي على عنوان بريد إلكتروني صالح. تُستخدم العلامة -E لتفسير النمط النمطي، وتضمن أدوات الربط ^ و $ أن السطر بأكمله هو بريد إلكتروني صالح.

#!/bin/bash

# The log file to search
LOG_FILE="application.log"

echo "Searching for valid email addresses in $LOG_FILE..."

# The regex pattern matches a string that starts with one or more letters,
# followed by an @, then more letters, and ends with .com
grep -E "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$" "$LOG_FILE"

echo "Search complete."

يستخدم هذا المثال نمطًا نمطيًا أكثر شمولاً لمطابقة مجموعة أوسع من عناوين البريد الإلكتروني الصالحة، مما يوضح قوة الأداة.

2. مطابقة الـ Regex في Bash باستخدام [[...]]
لدى Bash دعم مدمج لمطابقة الـ regex باستخدام عامل التشغيل =~ داخل كتلة [[...]]. هذا يسمح لك بدمج الـ regex مباشرة في المنطق الشرطي للسكريبتات الخاصة بك دون الحاجة إلى أدوات خارجية.

if [[ "Hello World" =~ "World" ]]; then
  echo "String contains 'World'"
fi

مثال عملي رائع
سكريبت يطلب من المستخدم إدخال عنوان بريد إلكتروني ويتحقق من صحته قبل المتابعة.

#!/bin/bash

read -p "Enter your email address: " EMAIL

# Regex pattern for a simple email validation
if [[ "$EMAIL" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$ ]]; then
  echo "✅ Email address '$EMAIL' is valid."
else
  echo "❌ Error: Invalid email format. Please try again." >&2
  exit 1
fi

3. استخراج السلاسل الفرعية
عندما تقوم بمطابقة الـ regex باستخدام عامل التشغيل =~ داخل كتلة [[...]]، يتم تخزين أي مجموعات تم التقاطها (أجزاء من النمط محاطة بأقواس) تلقائيًا في مصفوفة BASH_REMATCH. هذه ميزة قوية للغاية لتحليل واستخراج أجزاء محددة من المعلومات من سلسلة نصية.

if [[ "$string" =~ ([0-9]+) ]]; then
  echo "Number: ${BASH_REMATCH[1]}"
fi

مثال عملي رائع: سكريبت يعالج سلسلة إدخال سجل، ويستخرج الطابع الزمني ورمز الحالة، ثم يستخدم تلك المعلومات لمزيد من المعالجة.

#!/bin/bash

LOG_ENTRY="[2023-08-25 10:30:00] - Request to /api/users successful with status 200"

# Regex to capture the timestamp and the status code
REGEX_PATTERN="^\\[([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})\\] .* status ([0-9]+)$"

if [[ "$LOG_ENTRY" =~ $REGEX_PATTERN ]]; then
  # The captured groups are stored in BASH_REMATCH
  TIMESTAMP="${BASH_REMATCH[1]}"
  STATUS_CODE="${BASH_REMATCH[2]}"

  echo "Timestamp: $TIMESTAMP"
  echo "Status Code: $STATUS_CODE"
  
  # You can now use these variables for further processing
  if [ "$STATUS_CODE" -eq 200 ]; then
    echo "Processing successful request data..."
  fi
else
  echo "Could not parse the log entry."
fi
