# Механизм инкапсуляции 

# attribute - публичное свойство (public)
# _attribute - режим доступа protected (служит для обращения внутри класса и во всех его дочерних классах)
# __attribute - режим доступа private (служит для обращения только внутри класса)

# pip install accessify - для бОльшей защиты, чтобы действительно не было доступа к методам


from accessify import private, protected
class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    # декоратор из accessify
    @private
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x,y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1,2)
pt.set_coord(10,20)
pt.check_value(5) # accessify.errors.InaccessibleDueToItsProtectionLevelException: Point.check_value() is inaccessible due to its protection level
