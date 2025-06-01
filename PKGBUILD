# Maintainer: Saeed Badreldin <saeedbadrelden2021@gmail.com>
pkgname=helwan-tutorial
pkgver=1.0.0
pkgrel=1
pkgdesc="Helwan Tutorial - Linux Bash Lessons viewer with PyQt5 GUI and font size control"
arch=('any')
url="https://github.com/helwan-linux/helwan-tutorial"
license=('MIT')
depends=('python' 'python-pyqt5')
# المصدر: يتم استنساخ مستودع Git للمشروع.
source=("git+${url}.git")
# sha256sums: يجب توليدها باستخدام 'makepkg -g' بعد التأكد من صحة المصادر.
# لا تستخدم 'SKIP' في النسخة النهائية للحزمة.
sha256sums=('SKIP')

package() {
  # الانتقال إلى دليل المشروع المستنسخ في srcdir
  cd "$srcdir/$pkgname"

  # تثبيت السكربت التنفيذي (بدون امتداد .py) إلى /usr/bin
  install -Dm755 "helwan-tutor.py" "$pkgdir/usr/bin/helwan-tutorial"

  # تثبيت مجلد الدروس (lessons) إلى /usr/share/helwan-tutorial/lessons
  install -d "$pkgdir/usr/share/$pkgname/lessons"
  cp -r "lessons/bash" "$pkgdir/usr/share/$pkgname/lessons/"

  # تثبيت ملف الديسكتوب (لظهور التطبيق في قائمة البرامج)
  # بافتراض أن ملف helwan-tutor.desktop موجود في جذر مستودع Git
  install -Dm644 "helwan-tutor.desktop" "$pkgdir/usr/share/applications/helwan-tutorial.desktop"

  # **تنبيه هام**: إذا كان سكربت helwan-tutor.py يستخدم مسارات نسبية لملف الدروس
  # (مثل 'lessons/bash' بدلاً من المسار الكامل)، فقد تحتاج إلى تعديل السكربت.
  # هذا الأمر يقوم بتعديل السكربت ليستخدم المسار المطلق.
  # تأكد من صحة 'lessons/bash' في الكود الأصلي قبل تطبيق هذا التعديل.
  sed -i "s|lessons/bash|/usr/share/helwan-tutorial/lessons/bash|g" "$pkgdir/usr/bin/helwan-tutorial"
}
