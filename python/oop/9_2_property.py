
# property
# декоратер - функция расширяющая другую функцию

class Person:
    def __init__(self, name, old):
        self.__name = name # private attributes
        self.__old = old

    @property # only before getter!! not setter
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old): # должно быть такое же имя
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

p = Person('Alex', 30)

p.old = 35
del p.old # уже не сможем обратиться к этому приватному свойству и при print(p.__dict__) увидим только person_name, но если p.old = 35 сделать ниже? то опять появится
print(p.__dict__)

print(p.old, p.__dict__)

print(None)

# теперь нет отдельно геттера и сеттера - нет функционального дублирования
# 