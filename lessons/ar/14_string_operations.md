عمليات السلسلة النصية في Bash
في كتابة أوامر Bash، تُعد السلاسل النصية نوع بيانات أساسيًا، وتوفر Shell مجموعة قوية من العمليات المدمجة لمعالجتها. إن إتقان هذه التقنيات ضروري لأي أمر يتضمن تحليل النصوص، معالجة أسماء الملفات، أو التعامل مع مدخلات المستخدم.

1. إيجاد طول السلسلة النصية
للحصول على طول السلسلة النصية، يمكنك استخدام صيغة ${#variable}. هذه طريقة بسيطة وسريعة للتحقق من عدد الأحرف في متغير.

STR="Hello World"
echo ${#STR}

المخرجات:

11

مثال عملي: التحقق من مدخلات المستخدم للتأكد من أن كلمة المرور تفي بمتطلبات الحد الأدنى للطول.

#!/bin/bash
read -p "Enter a password (min 8 characters): " PASSWORD
if [ ${#PASSWORD} -lt 8 ]; then
  echo "Password is too short!"
else
  echo "Password accepted."
fi

2. استخراج السلسلة الفرعية
تسمح لك Bash باستخراج جزء من السلسلة النصية باستخدام صيغة القوسين القائمين القائمة على النقطتين: ${string:position:length}.

position: الفهرس الابتدائي (بدءًا من 0).

length: عدد الأحرف المراد استخراجها.

echo ${STR:6:5}

المخرجات:

World

مثال عملي: استخراج اسم الملف من مسار كامل.

#!/bin/bash
FULL_PATH="/home/user/documents/report.txt"
FILE_NAME=$(basename "$FULL_PATH")
echo "File Name: $FILE_NAME"

المخرجات:

File Name: report.txt

3. استبدال السلسلة النصية
يمكنك استبدال أجزاء من السلسلة النصية باستخدام صيغة ${variable/pattern/replacement}.

echo ${STR/World/Bash}

المخرجات:

Hello Bash

مثال عملي: تنقية عناوين URL عن طريق إزالة البروتوكول.

#!/bin/bash
URL="https://www.example.com"
CLEAN_URL=${URL/https:\/\/}
echo "Clean URL: $CLEAN_URL"

المخرجات:

Clean URL: www.example.com

4. مقارنة السلاسل النصية
استخدم == أو = لمقارنة السلاسل النصية داخل [ ]. دائمًا ضع المتغيرات بين علامتي اقتباس مزدوجتين.

if [ "$STR" = "Hello World" ]; then
  echo "Strings are equal"
fi

مثال عملي: التحقق مما إذا كان المستخدم قد قدم المفتاح السري الصحيح.

#!/bin/bash
SECRET_KEY="SuperSecret123"
read -p "Enter the secret key: " INPUT

if [ "$INPUT" == "$SECRET_KEY" ]; then
  echo "Access granted."
else
  echo "Access denied."
fi
