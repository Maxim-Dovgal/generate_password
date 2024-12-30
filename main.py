import os
os.environ['QT_PLUGIN_PATH'] = r"C:/Users/Макс/AppData/Local/Programs/Python/Python312/plugins"
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from random import randint, choice
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generate)
    def generate(self):
        signs = ''
        if self.ui.check_leters.isChecked():
            signs = signs + "qwertyuiopasdfghjklzxcvbnm🤢"
        if self.ui.check_members.isChecked(): 
            signs = signs + '1234567890🤢'
            
        password = ''
        for i in range(randint(8, 160)):
            password += choice(signs)
        self.ui.result.setText(password)  
        print(password)
       
        


app = QApplication([])
window = Widget()
window.show()
app.exec_()