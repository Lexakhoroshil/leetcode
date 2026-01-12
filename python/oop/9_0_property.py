# разработаем класс для хранения данных о персонале
class Person:
    def __init__(self, name, old):
        self.__name = name # private attributes
        self.__old = old

    # так как private пропишем геттеры и сеттеры - нужно чтобы не нарушалась внутренняя логика работы алгоритма класса
    # и взаимодействие с классом, его объектами извне осуществлялось только с помощью разрешенных публичных методов

    def get_old(self):
        return self.__old
    
    def set_old(self, old):
        self.__old = old



p = Person('Alex', 30)
p.set_old(32)
print(p.get_old())


# но вот например у нас много аттрибутов и в таком случае придется писать много геттеров и сеттеров
# избежать этого можно через property - см (9_1)




print(None)