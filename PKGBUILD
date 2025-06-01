# Maintainer: Saeed Badreldin <saeedbadrelden2021@gmail.com>
pkgname=hel-tutorial # <--- اسم الحزمة الجديد
pkgver=1.0.0
pkgrel=1
pkgdesc="Helwan Tutorial - Linux Bash Lessons viewer with PyQt5 GUI and font size control"
arch=('any')
url="https://github.com/helwan-linux/helwan-tutorial"
license=('MIT')
depends=('python' 'python-pyqt5')
# المصدر: يتم استنساخ مستودع Git للمشروع.
# لاحظ أن المستودع سيتم استنساخه باسم "helwan-tutorial"
source=("git+${url}.git")
# sha256sums: يجب توليدها باستخدام 'makepkg -g' بعد التأكد من صحة المصادر.
# لا تستخدم 'SKIP' في النسخة النهائية للحزمة.
sha256sums=('SKIP')

package() {
  # الانتقال إلى دليل المشروع المستنسخ في srcdir
  # اسم المجلد المستنسخ من Git هو "helwan-tutorial" (وليس $pkgname)
  cd "$srcdir/helwan-tutorial"

  # تثبيت السكربت التنفيذي (بدون امتداد .py) إلى /usr/bin
  # سيتم تسمية الملف التنفيذي بـ 'hel-tutorial' ليطابق pkgname
  install -Dm755 "helwan-tutor.py" "$pkgdir/usr/bin/$pkgname"

  # تثبيت مجلد الدروس (lessons) إلى /usr/share/hel-tutorial/lessons
  install -d "$pkgdir/usr/share/$pkgname/lessons"
  cp -r "lessons/bash" "$pkgdir/usr/share/$pkgname/lessons/"

  # تثبيت ملف الديسكتوب (لظهور التطبيق في قائمة البرامج)
  # اسم ملف الديسكتوب سيصبح 'hel-tutorial.desktop'
  install -Dm644 "helwan-tutor.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"

  # **تنبيه هام**: إذا كان سكربت helwan-tutor.py يستخدم مسارات نسبية لملف الدروس
  # هذا الأمر يقوم بتعديل السكربت ليستخدم المسار المطلق الجديد.
  # تأكد من صحة 'lessons/bash' في الكود الأصلي قبل تطبيق هذا التعديل.
  # لاحظ أن المسار الجديد يستخدم $pkgname
  sed -i "s|lessons/bash|/usr/share/$pkgname/lessons/bash|g" "$pkgdir/usr/bin/$pkgname"
}
