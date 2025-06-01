# Maintainer: Your Name <saeedbadrelden2021@gmail.com>
pkgname=helwan-tutorial
pkgver=1.0.0
pkgrel=1
pkgdesc="Helwan Tutorial - Linux Bash Lessons viewer with PyQt5 GUI and font size control"
arch=('any')
url="https://github.com/helwan-linux/helwan-tutorial"
license=('MIT')
depends=('python' 'python-pyqt5')
source=("git+https://github.com/helwan-linux/helwan-tutorial.git")
sha256sums=('SKIP')

package() {
    cd "$srcdir/helwan-tutorial"

    # تثبيت السكربت التنفيذي مع صلاحيات التنفيذ
    install -Dm755 "helwan-tutor.py" "$pkgdir/usr/bin/helwan-tutor"

    # نسخ مجلد الدروس
    cp -r "lessons/bash" "$pkgdir/usr/share/helwan-tutor/lessons/bash"

    # تثبيت ملف الديسكتوب
    install -Dm644 helwan-tutor.desktop "$pkgdir/usr/share/applications/helwan-tutor.desktop"
}
