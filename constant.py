NAME = {
    'ring': '戒指',
    'earring': '耳饰',
    'accessory': '配饰',
    'bracelet': '手镯'
}

LEVEL_DICT = {
    1: 60,
    2: 80,
    3: 100,
    4: 120,
    5: 140,
    6: 160
}
TYPE_DICT = {
    1: 'ring',
    2: 'earring',
    3: 'accessory',
    4: 'bracelet'
}

LEVEL_POOL = [60, 80, 100, 120, 140, 160]

PIC_DIC = {
    'ring': {
        60: None,
        80: None,
        100: None,
        120: None,
        140: None,
        160: None
    },
    'earring': {
        60: None,
        80: None,
        100: None,
        120: None,
        140: None,
        160: None
    },
    'accessory': {
        60: None,
        80: None,
        100: None,
        120: None,
        140: None,
        160: None
    },
    'bracelet': {
        60: None,
        80: None,
        100: None,
        120: None,
        140: None,
        160: None
    }
}

NAME_DIC = {
    'ring': {
        60: '枫华戒',
        80: '芙蓉戒',
        100: '金鳞绕',
        120: '悦碧水',
        140: '九曜光华',
        160: '太虚渺云'
    },
    'earring': {
        60: '翠叶环',
        80: '明月珰',
        100: '玉蝶翩',
        120: '点星芒',
        140: '凤羽流苏',
        160: '焰云霞珠'
    },
    'accessory': {
        60: '芝兰佩',
        80: '逸云佩',
        100: '莲音玦',
        120: '相思染',
        140: '玄龙苍珀',
        160: '碧海青天'
    },
    'bracelet': {
        60: '香木镯',
        80: '翡玉镯',
        100: '墨影扣',
        120: '花映月',
        140: '金水菩提',
        160: '浮雪幻音'
    }
}

MAIN_PROP = {
    'ring': ['伤害', '防御'],
    'earring': ['法术伤害', '法术防御'],
    'accessory': ['速度'],
    'bracelet': ['封印命中等级', '抵抗封印等级']
}

MAIN_PROP_VAL = {
    'ring': [0.2, 0.3],
    'earring': [0.2, 0.3],
    'accessory': [0.1, 6, 0.15, 9],
    'bracelet': [0.2, 0.3]
}

ADDITION_PROP = {
    'ring': ['伤害', '法术伤害', '固定伤害', '速度', '物理暴击等级', '法术暴击等级', '法术伤害结果', '治疗能力', '封印命中等级', '狂暴等级', '穿刺等级'],
    'earring': ['伤害', '法术伤害', '固定伤害', '速度', '物理暴击等级', '法术暴击等级', '法术伤害结果', '治疗能力', '封印命中等级', '狂暴等级', '穿刺等级'],
    'accessory': ['气血', '防御', '法术防御', '格挡值', '气血回复效果', '抵抗封印等级', '抗物理暴击等级', '抗法术暴击等级'],
    'bracelet': ['气血', '防御', '法术防御', '格挡值', '气血回复效果', '抵抗封印等级', '抗物理暴击等级', '抗法术暴击等级']
}

ADDITION_CATE = [
    ['速度', '法术伤害结果', '治疗能力', '狂暴等级', '穿刺等级'],
    ['伤害', '法术伤害', '固定伤害', '物理暴击等级', '法术暴击等级', '封印命中等级', '气血回复效果'],
    ['防御', '法术防御', '格挡值', '抵抗封印等级', '抗物理暴击等级', '抗法术暴击等级'],
    ['气血']
]

ADDITION_PROP_VAL = [
    [0.05, 3],
    [0.1, 0.15],
    [0.2, 0.3],
    [0.7, 1.05],
]

SPECIAL_EFFECT = ['超级简易']

P_SPECIAL_EFFECT = 0.005
P_ADD_3 = 0.3
NORMAL_SCALE_FACTOR = 0.2