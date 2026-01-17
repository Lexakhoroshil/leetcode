class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord)!= int:
            raise TypeError("should be int")
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord

    @property
    def y(self):
        return self._y
    
    @x.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property
    def z(self):
        return self._z
    
    @x.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord

p = Point3D(1, 2, 3)
print(p.__dict__) # {'_x': 1, '_y': 2, '_z': 3}