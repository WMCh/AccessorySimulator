from PyQt5.QtWidgets import QDialog
from constant import LEVEL_DICT, TYPE_DICT


class myDialog(QDialog):
    def __init__(self):
        super(myDialog, self).__init__()
        self.level = None
        self.type = None
    
    def setInfo(self, type, level):
        self.type = TYPE_DICT[type]
        self.level = LEVEL_DICT[level]

    def getInfo(self):
        return self.type, self.level
