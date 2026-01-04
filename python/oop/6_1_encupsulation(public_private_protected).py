# Механизм инкапсуляции 

# attribute - публичное свойство (public)
# _attribute - режим доступа protected (служит для обращения внутри класса и во всех его дочерних классах)
# __attribute - режим доступа private (служит для обращения только внутри класса)

class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0 # приватные локальные свойства
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

# добавим приватный метод проверки и сделаем его методом класса и добавим его выше и ниже
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float) # таким образом проверка если изменится, то только тут и не нужно бегать по коду искать где еще менять проверки

    def set_coord(self, x,y):
        # и вставим его сюда
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1,2)
pt.set_coord(10,20)
print(pt.get_coord())

###

print (dir(pt)) # посмотрим какие свойства существуют в этом экземпляре: '_Point__x', '_Point__y'

print(pt._Point__x) # отработает, однако так делать крайне не рекомендуется

# если нам нужно сильнее защитить - то юзаем модуль accessify см 6_2

print(None)