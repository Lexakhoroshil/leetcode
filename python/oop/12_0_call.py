# magic method __call__
# dunder-method (from double underscope - двойное подчеркивание)

class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print("__call__")
        self.__counter +=1
        return self.__counter
    

c = Counter()

# при вызове класса вызывается метод __call__
# схема вызова call 
# __call__(self, *args, **kwargs):
#     obj = self.__new__(self, *args, **kwards)
#     self.__init__(obj, *args, **kwards)
#     return obj


#c() # TypeError: 'Counter' object is not callable - определим __call__ выше

#c() # теперь работатет -теперь можно вызывать классы подобно функциям


c()
c()

res = c() 
print(res) # теперь счетчик у нас равен 3 , так как вызвали 3 раза

# создадим еще один экземпляр класса

c2 = Counter()
res2 = c2()
print(res, res2) # 3  1


