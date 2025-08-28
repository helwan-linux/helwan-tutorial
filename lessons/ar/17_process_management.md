إدارة العمليات في Bash
تُعد إدارة العمليات جزءًا حيويًا من استخدام سطر أوامر لينكس. تسمح لك هذه المهارة بالتحكم في البرامج التي تعمل على نظامك، مما يمكنك من تنفيذ المهام في الخلفية، وإنهاء العمليات غير المستجيبة، ومراقبة أداء النظام.

1. تشغيل أمر في الخلفية
عندما تُضيف الرمز & إلى نهاية الأمر، فإنك تقوم بتنفيذه في الخلفية. هذا يُعيد إليك التحكم في سطر الأوامر على الفور دون انتظار انتهاء الأمر. هذا مفيد للعمليات طويلة الأمد التي لا تتطلب تفاعلك.

مثال:

sleep 60 &

مثال عملي: تشغيل عملية تنزيل في الخلفية.

# Run the download command in the background
wget https://example.com/large_file.zip &

# You can now type other commands immediately
echo "Download started in the background. You can continue working now."

2. سرد مهام الخلفية
لسرد جميع المهام التي تعمل حاليًا في الخلفية في جلستك الحالية، استخدم الأمر jobs. هذا يوفر قائمة بالعمليات مع معرف الوظيفة (Job ID) والحالة الخاصة بها.

مثال:

jobs

مثال عملي:

# Start two processes in the background
./script_one.sh &
./script_two.sh &

# View the list of jobs
jobs
# The output might look like this:
# [1]-  Running                 ./script_one.sh &
# [2]+  Running                 ./script_two.sh &

يُعد معرف الوظيفة ([1], [2]) مفيدًا للتحكم في هذه المهام.

3. جلب مهمة إلى الواجهة
إذا كنت تريد استعادة السيطرة على مهمة في الخلفية، استخدم الأمر fg (foreground) متبوعًا بمعرف الوظيفة. هذا يجلب المهمة إلى الواجهة، مما يسمح لك بالتفاعل معها مرة أخرى.

مثال:

fg %1

مثال عملي:

# Run a process in the background
./interactive_script.sh &
# [1] 1234

# Bring the process back to the foreground
fg %1

يشير %1 إلى المهمة الأولى في قائمة المهام.

4. إنهاء عملية
إذا كانت العملية لا تستجيب أو تستهلك موارد مفرطة، يمكنك إنهاؤها باستخدام الأمر kill مع معرف العملية (PID). يمكنك العثور على PID باستخدام أوامر ps aux أو top.

مثال:

kill PID

مثال عملي:

# Find the PID for the `firefox` process
ps aux | grep firefox
# Example output:
# user      1500  ... /usr/bin/firefox ...

# Terminate the process using its PID
kill 1500

# If the process doesn't stop, use forceful termination
kill -9 1500

⚠️ يجب أن يكون استخدام kill -9 هو الملاذ الأخير، لأنه لا يسمح للعملية بحفظ عملها قبل الخروج.