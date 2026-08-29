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

        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_name)
        self.enter_name.returnPressed.connect(self.add_name)
        remove_button = QPushButton("Remove")
        remove_button.clicked.connect(self.remove_name)
        row1.addWidget(add_button)
        row1.addWidget(remove_button)

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
        preview_button.clicked.connect(self.generate_preview)
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

    def add_name(self):
        text = self.enter_name.text().strip()
        if text:
            self.input_list.addItem(text)
            self.enter_name.clear()

    def remove_name(self):
        selected = self.input_list.currentRow()
        if selected >= 0:
            self.input_list.takeItem(selected)

    def generate_new_name(self, name):
        prefix = self.prefix_input.text()
        suffix = self.suffix_input.text()
        find = self.find_input.text()
        replace = self.replace_input.text()

        if find:
            name = name.replace(find, replace)

        if prefix:
            name = prefix + name
            
        if suffix:
            name = name + suffix

        return name

    def generate_preview(self):
        self.preview_list.clear()
        for i in range(self.input_list.count()):
            file = self.input_list.item(i).text()
            new_name = self.generate_new_name(file)
            self.preview_list.addItem(new_name)
            

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()