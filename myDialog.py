from PyQt5.QtWidgets import QDialog
from constant import LEVEL_DICT, TYPE_DICT, COST


class myDialog(QDialog):
    def __init__(self):
        super(myDialog, self).__init__()
        self.level = None
        self.type = None
        self.cost = 0
    
    def setInfo(self, type, level):
        self.type = TYPE_DICT[type]
        self.level = LEVEL_DICT[level]
        self.cost = COST[self.type][self.level]

    def getInfo(self):
        return self.type, self.level, self.cost
