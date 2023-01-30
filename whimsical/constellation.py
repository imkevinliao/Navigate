import abc
import sys
from enum import Enum, auto


class Constellation(Enum):
    Aquarius = "宝瓶"  # 水瓶
    Pisces = "双鱼"
    Aries = "白羊"
    Taurus = "金牛"
    Gemini = "双子"
    Cancer = "巨蟹"
    Leo = "狮子"
    Virgo = "处女"
    Libra = "天秤"
    Scorpius = "天蝎"
    Sagittarius = "射手"
    Capricornus = "摩羯"


class Zodiac(object):
    def __init__(self):
        self.__name = None  # 星座名字:Aquarius
        self.__duration_time = None  # 星座持续时间段:(1.21,2.19); range=(1.1,12.31)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        return self.__name
    
    @property
    def duration_time(self):
        return self.__duration_time
    
    @duration_time.setter
    def duration_time(self, value):
        self.__duration_time = value
        return self.__duration_time
    
    @abc.abstractmethod
    def personality_traits(self, value) -> str: ...  # 星座性格特点描述
    
    @abc.abstractmethod
    def guarding(self, value) -> str: ...  # 星座对应的守护星座


class Aquarius(Zodiac):
    def __init__(self):
        self.name = "Aquarius"
        self.duration_time = (1.21, 2.19)
    
    def personality_traits(self, value):
        ...
    
    def guarding(self, value):
        ...


if __name__ == '__main__':
    inst = Aquarius()
    print(sys.version_info)
    
    ...
