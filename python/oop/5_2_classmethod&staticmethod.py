# декораторы  @classmethod и @staticmethod

# @staticmethod - с помощью этого определим методы, которые не имеют доступа ни к аттрибутам класса, ни к аттрибутам его экземпляра
# т.е это самостоятельная функция внутри класса

class Vector:
    MIN_COORD = 0
    MAX_COORD =  100 # менял на 2 при запуске print(Vector.norm2(5,6))

    @classmethod
    def validate(cls, arg): 
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x, self.y))
    
    def get_coord(self):
        return self.x, self.y
    
# пропишем тут недопустимы self и cls - прописываются только параметры, которые используются внутри функции
    @staticmethod
    def norm2(x,y):
        return x*x + y*y
    
# v = Vector(1,200) # тут тогда будет 0,0 из-за validate в init

# print(Vector.norm2(5,6)) # ответ 61 - видно что в init при этом не зашло - просто взяты аргументы из этой же строки

# далее засунем norm2 в init и запустим с новыми аргументами

v = Vector(10,20) # тут 500
print(Vector.norm2(5,6)) # тут 61

print(None)


# Вообще можно засунуть и аттрибут класса в  @staticmethod типо указав название класса и его аттрибут
#    @staticmethod
#    def norm2(x,y):
#        return x*x + y*y + Vector.MAX_COORD
# но так не рекомендуется делать - если изменится имя класса, то придется менять имя класса и вообще в таком случае надо юзать тогда @classmethod с clss