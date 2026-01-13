# example of development class Person

# FIO                                               list
# age(int 14-120)                                   int
# series, number (xxxx-xxxxxx, where x in [0,9])    str
# weight (float >=20)                               float
from string import ascii_letters

class Person:
    S_RUS = 'абвгдеёжзиклмнопрстуфхчшщьъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("FIO should be str")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("wrong format fio")
        
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s)<1:
                raise TypeError("Should be 1 symbol at least in FIO")
            if len(s.strip(letters)) !=0:
                raise TypeError("only letters and - are allowed")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old<14 or old >120:
            raise TypeError("age error")


    @classmethod
    def verify_w(cls, w):
        if type(w) != float or w<20:
            raise TypeError("weight error")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("passport error")
        
        s = ps.split()

        if len(s) !=2 or len(s[0]) !=4 or len(s[1]) != 6:
            raise TypeError("passport error")
        

        for p in s:
            if not p.isdigit():
                raise TypeError("passport must be number")

    @property # сделаем без сеттера только геттер - ну как будто не предполагается что фио изменится
    def fio(self):
        return self.__fio
    
    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        self.verify_w(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport
    
    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps



p = Person('Хорошилов А В', 30, '1234 567890', 80.0)
# p = Person('Хорошилов А1 В', 30, '1234 567890', 80.0) # error
p.old = 100
p.passport = "0987 654321"
print(p.__dict__)

# в конце лекции не совсем понял - пересмотреть