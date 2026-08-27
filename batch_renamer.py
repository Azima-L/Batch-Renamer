from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget, QCheckBox, QPushButton
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Batch Renamer")
        self.setFixedSize(350, 400)

        master_layout = QVBoxLayout()
        self.setLayout(master_layout)

        row1 = QHBoxLayout()
        
        self.enter_name = QLineEdit()
        self.enter_name.setPlaceholderText("Add name")
        row1.addWidget(self.enter_name)

        self.add_button = QPushButton("Add")
        self.remove_button = QPushButton("Remove")
        row1.addWidget(self.add_button)
        row1.addWidget(self.remove_button)

        row2 = QHBoxLayout()

        self.input_list = QListWidget()
        self.preview_list = QListWidget()

        row2_column1 = QVBoxLayout()
        row2_column1.addWidget(QLabel("Input Names"))
        row2_column1.addWidget(self.input_list)

        row2_column2 = QVBoxLayout()
        row2_column2.addWidget(QLabel("Preview"))
        row2_column2.addWidget(self.preview_list)

        row2.addLayout(row2_column1)
        row2.addLayout(row2_column2)

        row3 = QHBoxLayout()

        prefix_input_label = QLabel("Prefix")
        self.prefix_input = QLineEdit()
        find_input_label = QLabel("Find")
        self.find_input = QLineEdit()
        suffix_input_label = QLabel("Suffix")
        self.suffix_input = QLineEdit()
        replace_input_label = QLabel("Replace")
        self.replace_input = QLineEdit()

        row3_column1 = QVBoxLayout()
        row3_column1.addWidget(prefix_input_label)
        row3_column1.addWidget(find_input_label)

        row3_column2 = QVBoxLayout()
        row3_column2.addWidget(self.prefix_input)
        row3_column2.addWidget(self.find_input)

        row3_column3 = QVBoxLayout()
        row3_column3.addWidget(suffix_input_label)
        row3_column3.addWidget(replace_input_label)

        row3_column4 = QVBoxLayout()
        row3_column4.addWidget(self.suffix_input)
        row3_column4.addWidget(self.replace_input)

        row3.addLayout(row3_column1)
        row3.addLayout(row3_column2)
        row3.addLayout(row3_column3)
        row3.addLayout(row3_column4)

        row4 = QHBoxLayout()

        self.auto_number_checkbox = QCheckBox("Auto-number")
        row4.addWidget(self.auto_number_checkbox)

        row5 = QHBoxLayout()

        preview_button = QPushButton("Preview")
        export_button = QPushButton("Export")
        row5.addWidget(preview_button)
        row5.addWidget(export_button)

        master_layout.addLayout(row1)
        master_layout.addLayout(row2)
        master_layout.addLayout(row3)
        master_layout.addLayout(row4)
        master_layout.addLayout(row5)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-family: Arial;
                font-size: 12px;
            }
            QLineEdit {
                background-color: #2d2d2d;
                color: white;
                border: 1px solid #3d3d3d;
                border-radius: 4px;
                padding: 2px;
            }
            QListWidget {
                background-color: black;
                border: none;
            }
            QPushButton {
                background-color: #0078d4;
                color: white;
                border-radius: 4px;
                padding: 4px;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
        """)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()