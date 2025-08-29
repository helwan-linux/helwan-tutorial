# Maintainer: Saeed Badreldin <saeedbadrelden2021@gmail.com>
pkgname=hel-tutorial
pkgver=1.0.0
pkgrel=1
pkgdesc="Helwan Tutorial - Linux Bash Lessons viewer with PyQt5 GUI and font size control"
arch=('any')
url="https://github.com/helwan-linux/helwan-tutorial"
license=('MIT')
depends=('python' 'python-pyqt5')
source=("git+${url}.git")
sha256sums=('SKIP')

package() {
  # الانتقال إلى دليل المشروع
  cd "$srcdir/helwan-tutorial"

  # تثبيت السكربت التنفيذي
  install -Dm755 "helwan-tutor.py" "$pkgdir/usr/bin/$pkgname"

  # تثبيت ملف الديسكتوب
  install -Dm644 "helwan-tutor.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
  
  # تثبيت مجلد الدروس
  install -d "$pkgdir/usr/share/$pkgname/"
  cp -r "lessons" "$pkgdir/usr/share/$pkgname/"

  # الحل النهائي: إنشاء رابط رمزي
  ln -s "/usr/share/$pkgname/lessons" "$pkgdir/usr/bin/lessons"
}

