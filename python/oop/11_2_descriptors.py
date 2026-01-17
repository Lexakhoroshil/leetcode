# дескрипторы могут быть 2-х типов:
# - дескрипторы данных (например нащ Integer ) и дескрипторы не данных (ReadIntX:)

# дестриптор не данных нужен только для чтения
# у них разный приоритет :  у дескрипторов не данных он обычный на уровне обычного аттрибута в отличие от дескриптора днных


class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "_x"

class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord)!= int:
            raise TypeError("should be int")
        
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        #return instance.__dict__[self.name]
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.verify_coord(value)
        #instance.__dict__[self.name] = value
        setattr(instance, self.name, value)

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p = Point3D(1, 2, 3)
p.xr = 5
print( p.xr, p.__dict__)