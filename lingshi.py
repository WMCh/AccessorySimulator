from constant import *
from generate import (generate_addition_prop, generate_main_prop,
                      generate_special_effect)


class lingshi_base(object):
    def __init__(self, level, type):
        self.level = level
        self.type = type
        self.pic = PIC_DIC[self.type][self.level]
        self.name = NAME_DIC[self.type][self.level]
        self.main_prop = None
        self.main_val = 0
        self.addition_prop = []
        self.special_effect = None

    def authenticate(self):
        self.special_effect = generate_special_effect()
        self.main_prop, self.main_val = generate_main_prop(self.level, self.type)
        self.addition_prop = generate_addition_prop(self.level, self.type)

    def print(self):
        print(f'{self.level}级{NAME[self.type]}: {self.name}')
        print(self.main_prop, self.main_val)
        if self.special_effect is not None:
            print(f'特效: {self.special_effect}')
        for i in range(len(self.addition_prop)):
            print(self.addition_prop[i])
    
    def print_ui(self):
        aut_str = f"{self.name}\n{NAME[self.type]} 等级: {self.level}\n{self.main_prop} +{self.main_val}\n"
        if self.special_effect is not None:
            aut_str += f"特效: {self.special_effect}\n"
        else:
            aut_str += '\n'
        for i in range(len(self.addition_prop)):
            aut_str += f"{self.addition_prop[i][0]} +{self.addition_prop[i][1]}\n"
        return aut_str[:-1]


class ring(lingshi_base):
    def __init__(self, level):
        assert level in LEVEL_POOL
        super().__init__(level, type='ring')


class earring(lingshi_base):
    def __init__(self, level):
        assert level in LEVEL_POOL
        super().__init__(level, type='earring')


class accessory(lingshi_base):
    def __init__(self, level):
        assert level in LEVEL_POOL
        super().__init__(level, type='accessory')


class bracelet(lingshi_base):
    def __init__(self, level):
        assert level in LEVEL_POOL
        super().__init__(level, type='bracelet')
