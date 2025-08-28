تقنيات متقدمة في كتابة Shell Script
إتقان تقنيات Shell Scripting المتقدمة هو أمر أساسي لأتمتة المهام المعقدة وكتابة أوامر أكثر كفاءة وقوة. هذه التقنيات تتجاوز الأوامر الأساسية، وتمنحك الأدوات اللازمة للتعامل مع البيانات، وإجراء العمليات الحسابية، وإدارة مجموعات من القيم.

1. استبدال الأوامر (Command Substitution)
تسمح لك خاصية استبدال الأوامر بالتقاط مخرجات أمر معين واستخدامها كقيمة لمتغير. هذه تقنية أساسية لكتابة الأوامر بشكل ديناميكي.

يمكنك استخدام الصيغة الحديثة $(...) أو الأقواس المعقوفة القديمة .... يوصى باستخدام صيغة $(...) لأنها أسهل في القراءة ووضع أوامر متداخلة.

output=$(ls -l)

مثال عملي: تخزين تاريخ اليوم في متغير واستخدامه لاسم ملف سجل.

#!/bin/bash
# Store the current date in a variable
today=$(date +%Y-%m-%d)

# Use the variable to create a log file
LOG_FILE="backup_log_${today}.txt"
echo "Backup started on $(date)" > $LOG_FILE

2. العمليات الحسابية (Arithmetic Operations)
يمكن لأوامر Shell أن تُجري عمليات حسابية بسيطة باستخدام صيغة $((...)). هذا ضروري للحسابات مثل العدادات أو النسب المئوية.

result=$(( 3 + 5 ))

مثال عملي: حساب نسبة مساحة القرص المستخدمة.

#!/bin/bash
TOTAL_SPACE=1000
USED_SPACE=$(df -h | grep "/dev/sda1" | awk '{print $3}' | sed 's/G//')

# Note: Use `bc` for floating-point arithmetic.
PERCENTAGE=$(( ($USED_SPACE * 100) / $TOTAL_SPACE ))

echo "Used space: ${USED_SPACE}G"
echo "Percentage of total space used: ${PERCENTAGE}%"

3. المصفوفات (Arrays)
تتيح لك المصفوفات تخزين عدة قيم في متغير واحد، وهي رائعة لإدارة القوائم.

my_array=(one two three)

الوصول إلى العناصر:

echo ${my_array[1]} # يطبع 'two'

جميع العناصر:

echo ${my_array[@]} # يطبع 'one two three'

طول المصفوفة:

echo ${#my_array[@]} # يطبع '3'

مثال عملي: التكرار على قائمة من الخوادم وإرسال أمر ping إليها.

#!/bin/bash
SERVERS=("web-server-1" "db-server" "app-server-alpha")

for server in "${SERVERS[@]}"; do
  echo "Pinging ${server}..."
  ping -c 1 "${server}"
  if [ $? -eq 0 ]; then
    echo "${server} is up."
  else
    echo "${server} is down!"
  fi
done

يوضح هذا المثال كيف تسهل المصفوفات إدارة قائمة من العناصر والتكرار عليها، مما يجعل أوامرك أكثر قابلية للتوسع والصيانة.