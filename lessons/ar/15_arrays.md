المصفوفات في Bash
المصفوفات في Bash هي ميزة قوية لتخزين مجموعات من القيم في متغير واحد، مما يجعلها مثالية لإدارة قوائم البيانات في أوامرك. بدلاً من التعامل مع كل قيمة كمتغير منفصل، تتيح لك المصفوفات الوصول إلى البيانات ومعالجتها بطريقة منظمة وفعالة.

1. الإعلان عن المصفوفات
يمكنك الإعلان عن مصفوفة أحادية البعد عن طريق تعيين قائمة من القيم لها. يتم وضع العناصر داخل أقواس () وفصلها بمسافات.

FRUITS=("apple" "banana" "cherry")

مثال عملي: تخيل أن لديك قائمة بأسماء الخوادم التي تحتاج إلى التحقق منها. يمكنك تخزينها في مصفوفة لتبسيط العملية.

#!/bin/bash
# Declare an array of server names
SERVERS=("web-server-01" "db-server-01" "app-server-02")

# You can print the entire array
echo "Server list: ${SERVERS[@]}"

2. الوصول إلى العناصر
للوصول إلى عنصر فردي من المصفوفة، استخدم فهرسه (موضعه) الذي يبدأ من 0.

echo ${FRUITS[1]}
# Output: banana

مثال عملي: الوصول إلى العنصر الأول والثالث من مصفوفة SERVERS.

#!/bin/bash
SERVERS=("web-server-01" "db-server-01" "app-server-02")

# Access the first element (index 0)
echo "First server: ${SERVERS[0]}"

# Access the third element (index 2)
echo "Third server: ${SERVERS[2]}"

3. إضافة عناصر
يمكنك إضافة عناصر جديدة إلى مصفوفة موجودة باستخدام المعامل +=.

FRUITS+=("date")

مثال عملي: إضافة خادم جديد إلى مصفوفة SERVERS الموجودة.

#!/bin/bash
SERVERS=("web-server-01" "db-server-01")
echo "Server list before adding: ${SERVERS[@]}"

# Add a new server
SERVERS+=("monitoring-server-03")

echo "Server list after adding: ${SERVERS[@]}"

4. التكرار عبر المصفوفات
للتكرار على جميع عناصر المصفوفة، يمكنك استخدام حلقة for مع الرمز [@]، الذي يمثل جميع العناصر.

for fruit in "${FRUITS[@]}"; do
  echo "Fruit: $fruit"
done

مثال عملي رائع: دعنا نُجري فحص ping على كل خادم في مصفوفتنا. هذا النوع من الأوامر ضروري لمراقبة سلامة الشبكة.

#!/bin/bash

# List of server names
SERVERS=("web-server-01" "db-server-01" "google.com")

# Loop through each server in the array
for server in "${SERVERS[@]}"; do
  echo "Pinging server: $server..."

  # Send a single ping packet (-c 1) and redirect output to null
  ping -c 1 "$server" &> /dev/null

  # Check the exit status of the last command
  if [ $? -eq 0 ]; then
    echo "✅ Successfully connected to: $server"
  else
    echo "❌ Failed to connect to: $server"
  fi

  echo "---"
done

يوضح هذا المثال كيف تبسط المصفوفات المهام المعقدة التي تتطلب التكرار على قائمة من البيانات.