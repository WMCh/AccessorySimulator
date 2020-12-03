from PyQt5.QtWidgets import QLabel
from constant import LEVEL_DICT, TYPE_DICT
from lingshi import ring, earring, accessory, bracelet


class myLabel(QLabel):
    def __init__(self, *args):
        super(myLabel, self).__init__(*args)
        self.lingshi = None
        self.type_dict = {
            'ring': ring,
            'earring': earring,
            'accessory': accessory,
            'bracelet': bracelet
        }
    
    def setInfo(self, type, level):
        self.lingshi = self.type_dict[type](level)

    def getInfo(self):
        self.lingshi.authenticate()
        return self.lingshi.print_ui()
