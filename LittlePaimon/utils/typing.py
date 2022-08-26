from typing import Literal

ElementType = Literal['火', '水', '冰', '雷', '风', '岩', '草', '物理']
WeaponType = Literal['单手剑', '双手剑', '长柄武器', '弓', '法器']
DataSourceType = Literal['mihoyo', 'enka']
RegionType = Literal['蒙德', '璃月', '稻妻', '须弥', '枫丹', '纳塔', '至冬']
TalentType = Literal['name', 'level', 'icon']
ConstellationType = Literal['name', 'icon']
EquipType = Literal['name', 'value']
PropType = Literal['基础生命', '额外生命', '基础攻击', '额外攻击', '基础防御', '额外防御', '暴击率', '暴击伤害', '元素精通', '元素充能效率', '治疗加成', '受治疗加成', '护盾强效', '伤害加成']


CN_NUMBER = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']

CHARACTERS = ['神里绫华', '琴', '丽莎', '芭芭拉', '凯亚', '迪卢克', '雷泽', '安柏', '温迪', '香菱', '北斗', '行秋', '魈', '凝光', '可莉', '钟离',
                      '菲谢尔', '班尼特', '达达利亚', '诺艾尔', '七七', '重云', '甘雨', '阿贝多', '迪奥娜', '莫娜', '刻晴', '砂糖', '辛焱', '罗莎莉亚', '胡桃',
                      '枫原万叶', '烟绯', '宵宫', '托马', '优菈', '雷电将军', '早柚', '珊瑚宫心海', '五郎', '九条裟罗', '荒泷一斗', '八重神子', '夜兰', '埃洛伊',
                      '申鹤', '云堇', '久岐忍', '神里绫人', '鹿野院平藏', '提纳里', '柯莱']
"""全角色"""
MALE_CHARACTERS = ['凯亚', '迪卢克', '钟离', '达达利亚', '托马', '荒泷一斗', '神里绫人']
"""成男角色"""
FEMALE_CHARACTERS = ['琴', '丽莎', '北斗', '凝光', '罗莎莉亚', '优菈', '雷电将军', '九条裟罗', '八重神子', '夜兰', '申鹤']
"""成女角色"""
GIRL_CHARACTERS = ['神里绫华', '芭芭拉', '安柏', '香菱', '菲谢尔', '诺艾尔', '甘雨', '莫娜', '刻晴', '砂糖', '辛焱', '胡桃', '烟绯', '宵宫', '珊瑚宫心海', '埃洛伊', '云堇', '久岐忍', '柯莱']
"""少女角色"""
BOY_CHARACTERS = ['雷泽', '温迪', '行秋', '魈', '班尼特', '重云', '阿贝多', '枫原万叶', '五郎', '鹿野院平藏', '提纳里']
"""少男角色"""
LOLI_CHARACTERS = ['七七', '可莉', '迪奥娜', '早柚']
"""萝莉"""

CHARA_RE = '|'.join(CHARACTERS)


