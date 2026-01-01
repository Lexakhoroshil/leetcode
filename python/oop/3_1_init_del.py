
class Point:
    color = 'red'
    circle = 2

    def __init__(self, x = 0, y = 0):
        #print('вызов __init__')
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


# убрали все из 3_0:
#pt = Point()

#print(pt.__dict__)

#print(None)


# как это происходит:
# шаг 1: создание объекта в памяти устройства (метод __new__)
# шаг 2: инициализация объекта (метод __init__) - появляются x и y с указанными значениями


pt = Point(1,2)
print(pt.__dict__)

pt = Point()
print(pt.__dict__)

pt = Point(1)
print(pt.__dict__)

print(None)

# про __del__ в 3_2