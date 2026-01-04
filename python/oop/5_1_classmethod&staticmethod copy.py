# декораторы  @classmethod и @staticmethod

class Vector:
    # добавим 2 аттрибута класса:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg): 
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    # добавим validate в init:
    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
    
    def get_coord(self):
        return self.x, self.y
    
# v = Vector(1,2)
v = Vector(1,200) # тут тогда будет 0,0 из-за validate в init

print(None)

# в 5_2 - рассмотрим @staticmethod