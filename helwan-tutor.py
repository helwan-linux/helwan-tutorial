import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QListWidget, QTextBrowser, QSplitter, QMessageBox, QHBoxLayout,
    QComboBox, QLabel
)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
import os

# Base path for lesson files
BASE_LESSONS_PATH = "lessons"
# Dictionary to map language names to their codes
LANGUAGES = {
    "العربية": "ar",
    "English": "en",
    "Español": "es",
    "中文": "zh"
}

class HelwanTutor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Helwan Tutor")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout(self)
        
        # Language selection container
        language_layout = QHBoxLayout()
        language_label = QLabel("Select Language:")
        self.language_selector = QComboBox()
        self.language_selector.addItems(LANGUAGES.keys())
        # Connect the change signal to the language change function
        self.language_selector.currentIndexChanged.connect(self.change_language)
        
        language_layout.addWidget(language_label)
        language_layout.addWidget(self.language_selector)
        language_layout.addStretch(1)
        
        main_layout.addLayout(language_layout)

        self.splitter = QSplitter(Qt.Horizontal)

        # Lessons list
        self.lesson_list = QListWidget()
        self.lesson_list.itemClicked.connect(self.load_lesson)
        self.current_language_code = "en" # Default language
        self.load_lessons_for_current_language()

        # Lesson viewer
        self.lesson_view = QTextBrowser()
        self.default_font_size = 12
        self.lesson_view.setStyleSheet(f"font-size: {self.default_font_size}pt;")
        self.lesson_view.anchorClicked.connect(self.open_external_link)

        self.splitter.addWidget(self.lesson_list)
        self.splitter.addWidget(self.lesson_view)

        main_layout.addWidget(self.splitter)

        # Buttons container
        btn_layout = QHBoxLayout()

        self.increase_font_btn = QPushButton("Increase Font")
        self.increase_font_btn.setToolTip("Increase font size")
        self.increase_font_btn.clicked.connect(self.increase_font_size)
        btn_layout.addWidget(self.increase_font_btn)

        self.decrease_font_btn = QPushButton("Decrease Font")
        self.decrease_font_btn.setToolTip("Decrease font size")
        self.decrease_font_btn.clicked.connect(self.decrease_font_size)
        btn_layout.addWidget(self.decrease_font_btn)

        self.copy_button = QPushButton("Copy Lesson Text")
        self.copy_button.clicked.connect(self.copy_text_to_clipboard)
        btn_layout.addWidget(self.copy_button)

        main_layout.addLayout(btn_layout)

    def change_language(self, index):
        """Changes the language and reloads the lessons list."""
        language_name = self.language_selector.currentText()
        self.current_language_code = LANGUAGES[language_name]
        self.load_lessons_for_current_language()

    def load_lessons_for_current_language(self):
        """Loads lesson titles based on the current language folder."""
        lessons_path = os.path.join(BASE_LESSONS_PATH, self.current_language_code)
        
        if not os.path.exists(lessons_path):
            os.makedirs(lessons_path)
        
        self.lesson_list.clear()
        for filename in sorted(os.listdir(lessons_path)):
            if filename.endswith(".md"):
                self.lesson_list.addItem(filename)
    
    def load_lesson(self, item):
        """Loads the content of the selected lesson."""
        lessons_path = os.path.join(BASE_LESSONS_PATH, self.current_language_code)
        file_path = os.path.join(lessons_path, item.text())
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.lesson_view.setMarkdown(content)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load lesson: {e}")

    def copy_text_to_clipboard(self):
        """Copies the lesson text to the clipboard."""
        content = self.lesson_view.toPlainText()
        if content.strip():
            clipboard = QApplication.clipboard()
            clipboard.setText(content)
            QMessageBox.information(self, "Copied", "The lesson text has been copied to the clipboard!")
        else:
            QMessageBox.warning(self, "Empty", "There is no content in the lesson to copy.")

    def increase_font_size(self):
        """Increases the displayed font size."""
        if self.default_font_size < 30:
            self.default_font_size += 2
            self.lesson_view.setStyleSheet(f"font-size: {self.default_font_size}pt;")

    def decrease_font_size(self):
        """Decreases the displayed font size."""
        if self.default_font_size > 6:
            self.default_font_size -= 2
            self.lesson_view.setStyleSheet(f"font-size: {self.default_font_size}pt;")

    def open_external_link(self, url):
        """Opens external links in the system's default web browser."""
        if url.isValid():
            QDesktopServices.openUrl(url)
        else:
            QMessageBox.warning(self, "Link Error", "The link is not valid.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tutor = HelwanTutor()
    tutor.show()
    sys.exit(app.exec_())
