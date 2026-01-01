class Point:    # class
    color = 'red' # attributes / properties / variables
    circle = 2

Point.color = 'black'

Point.circle

Point.__dict__

a = Point()

b = Point()

type(a)

type(a) == Point

isinstance(a, Point)

Point.circle = 1

a.color

b.circle

a.color = 'green' # локальный аттрибут экзепляра "a" класса Point

a.__dict__

Point.type_pt = 'disc'

a.type_pt

setattr(Point, 'prop', 1)

setattr(Point, 'type_pt', 'square')

res = Point.circle

getattr(Point, 'a', False)


print(getattr(Point, 'color'))

del Point.prop

print(hasattr(Point, 'prop'))


delattr(Point, 'type_pt')

print(hasattr(a, 'circle')) # будет через нее видно но не в __dict__

print(a.__dict__)

del a.color # теперь будет браться из класса Point: будет не green, а black

# т.е. поиск устроен таким образом: сначала ищется в текущем пространстве имен, а если не находится, то берется из следующего внешнего, на который ссылается a (внешний в данном случае - это класс Point)


print(None)
