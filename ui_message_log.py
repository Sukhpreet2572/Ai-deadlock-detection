from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QColor

class MessageLog(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setup_log()

    def setup_log(self):
        self.setReadOnly(True)
        self.setStyleSheet("""
            QTextEdit {
                background-color: #F5E6E8;
                color: black;
                font-size: 16px;
                border: none;
            }
        """)

    def add_message(self, message: str, message_type: str = "info"):
        colors = {
            "info": "black",
            "warning": "orange",
            "error": "red",
            "success": "green"
        }
        self.append(f'<p style="color:{colors[message_type]}">{message}</p>')
