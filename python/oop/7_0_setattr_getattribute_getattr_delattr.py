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

# пропишем метод который будет менять аттрибуи MIN_COORD
# однако если пишем так , то будет только меняться внутри экземпляра класса, а не в классе
#    def set_bound(self, left):
#        self.MIN_COORD = left   

# если нужно менять в классе, то
    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left  



pt1 = Point(1,2)
pt2 = Point(10,20)

pt1.set_bound(-100)

print(pt1.MIN_COORD)
print(pt2.MIN_COORD) # тоже будет -100 - потому что изменили внутри класса

print(None)

# см далее 7_1