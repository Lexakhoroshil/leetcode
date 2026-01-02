# декораторы  @classmethod и @staticmethod

class Vector:
    # добавим 2 аттрибута класса:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg): #cls - это ссылка на текущий класс Vector
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

# т.е метод класса работает исключительно с аттрибутами данного класса (MIN_COORD) & (MAX_COORD)
# но не может обращаться к локальным аттрибутам экземпляра класса - потому что нет ссылки на экземпляр класса (self)
# более того, теперь метод класса validate теперь можем вызывать непосредственно через class Vector - см # для @classmethod
# т.е метод класса можно вызывать через сам класс, при этом не указывая параметрт cls - в этом отличие между @classmethod и обычным


    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_coord(self):
        return self.x, self.y
    
v = Vector(1,2)

res = v.get_coord()
#print(res)



# для обычного класса
v = Vector(1,2)
res = Vector.get_coord(v)
# print(res)

# для @classmethod
print(Vector.validate(5)) # Выведет True, вызываем его без доп ссылок



print(None)

# далее в 5_1 воспользуемся методом класса внутри метода __init__

