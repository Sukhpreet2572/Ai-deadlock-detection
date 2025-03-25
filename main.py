import sys
from PyQt6.QtWidgets import QApplication
from ui import DeadlockDetectionAI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeadlockDetectionAI()
    window.show()
    sys.exit(app.exec())
