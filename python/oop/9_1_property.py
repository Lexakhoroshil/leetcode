# разработаем класс для хранения данных о персонале
# property


class Person:
    def __init__(self, name, old):
        self.__name = name # private attributes
        self.__old = old

    def get_old(self):
        return self.__old
    
    def set_old(self, old):
        self.__old = old


    old = property(get_old, set_old) # если создается такой аттрибут, то в первую очередь выбирается имеено оно, даже если в экземпляре класса есть локальное свойство с таким именем

# с помощью него можно и get и set и ничего не нужно запоминать
# a = p.old
# p.old = 35



p = Person('Alex', 30)
p.__dict__['old'] = 'old in object p' # запускаем и видим что хоть и создатся 'old': 'old in object p', но  '_Person__old': все равно 35
a = p.old
p.old = 35

print(p.old, p.__dict__)



# rewrite using property in 9_2


print(None)