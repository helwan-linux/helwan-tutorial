# Maintainer: Saeed Badreldin <saeedbadrelden2021@gmail.com>
pkgname=helwan-tutorial
pkgver=1.0.0
pkgrel=1
pkgdesc="Helwan Tutorial - Linux Bash Lessons viewer with PyQt5 GUI and font size control"
arch=('any')
url="https://github.com/helwan-linux/helwan-tutorial"
license=('MIT')
depends=('python' 'python-pyqt5')
source=("git+https://github.com/helwan-linux/helwan-tutorial.git"
        "helwan-tutor.desktop")
sha256sums=('SKIP'
            'SKIP')

package() {
    cd "$srcdir/helwan-tutorial"

    # تثبيت السكربت التنفيذي
    install -Dm755 "helwan-tutor.py" "$pkgdir/usr/bin/helwan-tutorial"

    # تثبيت مجلد الدروس
    install -d "$pkgdir/usr/share/helwan-tutorial/lessons"
    cp -r lessons/bash "$pkgdir/usr/share/helwan-tutorial/lessons/"

    # تثبيت ملف الديسكتوب
    install -Dm644 "$srcdir/helwan-tutor.desktop" "$pkgdir/usr/share/applications/helwan-tutor.desktop"
}
