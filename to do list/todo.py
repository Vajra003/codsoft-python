import os

os.system('cls')

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QStandardItemModel
from PyQt5 import uic
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton



class MyGUI(QMainWindow):
    
    def __init__(self):
        super(MyGUI , self).__init__()
        uic.loadUi("todogui.ui" , self)
        self.show()
        self.setFixedSize(540,406)

        self.setWindowTitle("Vajra to do list")
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.add_item.clicked.connect(self.add_todo)
        self.delete_item.clicked.connect(self.remove_todo)
        self.actionload.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.saveState)
    def add_todo(self):
        todo , confirmed = QInputDialog.getText(self, "Add ToDo","New ToDo:", QLineEdit.Normal,"")


        if confirmed and not todo.isspace():
           
            item = QStandardItem(todo)
            self.model.appendRow(item)            




    def remove_todo(self):
        if len(self.listView.selectedIndexes()) != 0:
            selected = self.listView.selectedIndexes()[0]
            dialog = QMessageBox()
            dialog.setText("Are you sure about that?")
            dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)
            dialog.addButton(QPushButton("No"), QMessageBox.NoRole)
            if dialog.exec_() == 0:
                self.model.removeRow(selected.row())





    def open_file(self):
        options = QFileDialog.Options()
        filename,_=QFileDialog.getOpenFileName(self , "open file", "", "todo files (*.todo)",options=options)
        if filename != "":
            with open(filename , "rb") as f:
                item_list = pickle.load(f)
                self.model = QStandardItemModel()
                self.listView.setModel(self.model)
                for item in item_list:
                    self.model.appendRow(QStandardItem(item))

    def saveState(self):
        item_list = []
        for x in range(self.model.rowCount()):
            item_list.append(self.model.item(x).text())
        options = QFileDialog.Options()
        filename , _=QFileDialog.getSaveFileName(self , "save file","","Todo files(*.todo)",options=options)
        if filename !="":
            with open(filename,"wb") as f:
                pickle.dump(item_list,f)


app = QApplication([])
window = MyGUI()
app.exec_()