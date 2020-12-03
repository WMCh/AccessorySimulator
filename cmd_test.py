import sys

from constant import *
from lingshi import accessory, bracelet, earring, ring

print("*********************************************")
print("**                                         **")
print("**     Make poor B's dream COME TRUE!      **")
print("**                                         **")
print("*********************************************")

type_dict = {
    1: ring,
    2: earring,
    3: accessory,
    4: bracelet
}
while(True):
    print()
    print('选择级别:')
    print('1. 60\t2. 80\t3. 100\t4. 120\t5. 140\t6. 160\t0. 退出')
    level = int(input())
    if level >= 1 and level <= 6:
        while(True):
            print()
            print('选择类型:')
            print(f"1. 戒指({NAME_DIC['ring'][LEVEL_DICT[level]]})\t2. 耳饰({NAME_DIC['earring'][LEVEL_DICT[level]]})\t3. 配饰({NAME_DIC['accessory'][LEVEL_DICT[level]]})\t4. 手镯({NAME_DIC['bracelet'][LEVEL_DICT[level]]})")
            print('5. 返回\t0. 退出')
            type = int(input())
            if type >= 1 and type <=4:
                o = type_dict[type](LEVEL_DICT[level])
            elif type == 5:
                break
            elif type == 0:
                sys.exit()
            else:
                print('输入0-5')
            while(True):
                print()
                print(f'你获得了{LEVEL_DICT[level]}级灵饰图鉴, 直接回车即可鉴定:')
                print('1. 鉴定\t2. 返回\t0. 退出')
                action = input()
                if action == '':
                    o.authenticate()
                    o.print()
                else:
                    action = int(action)
                    if action == 1:
                        o.authenticate()
                        o.print()
                    elif action == 2:
                        break
                    elif action == 0:
                        sys.exit()
                    else:
                        print('输入0-2')
    elif level == 0:
        sys.exit()
    else:
        print('输入0-6')
