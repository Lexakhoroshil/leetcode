# Магические методы
# __setattr__(self,key,value) - автоматически вызывается при изменении свойства key класса
# __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item
# __gettattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса
# __delattr__(self, item) -  автоматически вызывается при удалении свойства item (неважно, существует оно или нет)


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def set_coord(self, x,y):
        if self.MIN_COORD <=x <=self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        print("__getattribute__")
        return object.__getattribute__(self, item) # базовый класс object в python3, без return булет None

    # зачем он может понадобиться в таком виде? Ну например мы хотим запретить обращаться к x:

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("доступ запрещен")
        else:
            return object.__getattribute__(self, item)


#    def __setattr__(self, key, value):
#        print("__setattr__")
#        object.__setattr__(self, key, value)

    # например с помощью __setattr__ мы можем запретить создавать какой-либо локальный аттрибут в экземплярах класса

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя аттрибута")
        else:
            object.__setattr__(self, key, value)

# далее

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя аттрибута")
        else:
            object.__setattr__(self, key, value)
        # self.x = value  - так делать нельзя, иначе попадем в рекурсию : __setattr__ будет вызываться снова и снова
        # self.__dict__[key] = value # только так, но лучше через object.__setattr__(self, key, value)


    def __getattr__(self, item):
        print("__getattr__: " + item)

    def __getattr__(self, item):
        return False


    def __delattr__(self, item):
        print("__delattr__: "+item)
        object.__delattr__(self, item)


pt1 = Point(1,2)  # 4 раза вызовется __setattr__ (2 пары аттрибутов в каждом из pt1 и pt2)
pt2 = Point(10,20)

#a = pt1.x # в консоли идет принт __getattribute__, а после переопределение __getattribute__ - доступ запрещен
#a = pt1.y # все заработает потому что y а не x
# print(a) 

# pt1.y = 5 # всплывет AttributeError: недопустимое имя аттрибута

# print(pt1.COORD) # None и всплывает __getattr__

#print(pt1.MAX_COORD) # уже не всплывает __getattr__

#print(pt1.COORD) # return False
# если закоментить __getattr__ , то всплывет ошибка - такого аттрибута нет

del pt1.x
print(pt1.__dict__) # x удален

