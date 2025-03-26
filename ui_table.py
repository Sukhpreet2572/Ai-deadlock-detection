from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QBrush, QColor, QLinearGradient

class ProcessTable(QTableWidget):
    def __init__(self):
        super().__init__(5, 5)
        self.setup_table()

    def setup_table(self):
        self.setHorizontalHeaderLabels(["P1", "P2", "P3", "P4", "P5"])
        self.setVerticalHeaderLabels(["P1", "P2", "P3", "P4", "P5"])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        for i in range(5):
            for j in range(5):
                self.setItem(i, j, QTableWidgetItem("0"))

    def get_table_data(self) -> list[list[str]]:
        data = []
        for i in range(5):
            row = []
            for j in range(5):
                item = self.item(i, j)
                row.append(item.text() if item else "0")
            data.append(row)
        return data

    def highlight_processes(self, processes: list[str], color_gradient: tuple[str, str]):
        pass
