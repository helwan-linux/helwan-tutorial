import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QListWidget, QTextBrowser, QSplitter, QMessageBox, QHBoxLayout
)
from PyQt5.QtCore import Qt
import os

LESSONS_PATH = "lessons/bash"

class HelwanTutor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Helwan Tutor")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout(self)

        self.splitter = QSplitter(Qt.Horizontal)

        # قائمة الدروس
        self.lesson_list = QListWidget()
        self.lesson_list.itemClicked.connect(self.load_lesson)
        self.load_lesson_titles()

        # عارض الدرس
        self.lesson_view = QTextBrowser()
        self.default_font_size = 12  # حجم الخط الافتراضي
        self.lesson_view.setStyleSheet(f"font-size: {self.default_font_size}pt;")

        self.splitter.addWidget(self.lesson_list)
        self.splitter.addWidget(self.lesson_view)

        layout.addWidget(self.splitter)

        # أزرار التحكم في حجم الخط مع زر النسخ في صف أفقي
        btn_layout = QHBoxLayout()

        self.increase_font_btn = QPushButton("A+")
        self.increase_font_btn.setToolTip("Increase font size")
        self.increase_font_btn.clicked.connect(self.increase_font_size)
        btn_layout.addWidget(self.increase_font_btn)

        self.decrease_font_btn = QPushButton("A-")
        self.decrease_font_btn.setToolTip("Decrease font size")
        self.decrease_font_btn.clicked.connect(self.decrease_font_size)
        btn_layout.addWidget(self.decrease_font_btn)

        self.copy_button = QPushButton("Copy Lesson Text")
        self.copy_button.clicked.connect(self.copy_text_to_clipboard)
        btn_layout.addWidget(self.copy_button)

        layout.addLayout(btn_layout)

    def load_lesson_titles(self):
        if not os.path.exists(LESSONS_PATH):
            os.makedirs(LESSONS_PATH)

        self.lesson_list.clear()
        for filename in sorted(os.listdir(LESSONS_PATH)):
            if filename.endswith(".md"):
                self.lesson_list.addItem(filename)

    def load_lesson(self, item):
        file_path = os.path.join(LESSONS_PATH, item.text())
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.lesson_view.setMarkdown(content)

    def copy_text_to_clipboard(self):
        content = self.lesson_view.toPlainText()
        if content.strip():
            clipboard = QApplication.clipboard()
            clipboard.setText(content)
            QMessageBox.information(self, "Copied", "Lesson text copied to clipboard!")
        else:
            QMessageBox.warning(self, "Empty", "No lesson content to copy!")

    def increase_font_size(self):
        if self.default_font_size < 30:
            self.default_font_size += 2
            self.lesson_view.setStyleSheet(f"font-size: {self.default_font_size}pt;")

    def decrease_font_size(self):
        if self.default_font_size > 6:
            self.default_font_size -= 2
            self.lesson_view.setStyleSheet(f"font-size: {self.default_font_size}pt;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tutor = HelwanTutor()
    tutor.show()
    sys.exit(app.exec_())
