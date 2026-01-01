class Point:
    color = 'red'
    circle = 2

    def set_coords_noself():
        print("Вызов метода set_coords")

    def set_coords(self):
        print("Вызов метода set_coords" + str(self))

print(Point.set_coords_noself)

Point.set_coords_noself()

pt = Point()

print(pt.set_coords_noself)

# pt.set_coords_noself() # будет ошибка, потому что не передали параметр self, когда определяли

# интерпретатор Python когда вызывает тот или иной метод через объект класса делает одну такую вещь: автоматически вместо аргумента подставляет параметр self
# этот параметр self является ссылкой на экземляр класса Point (т.е. в данном случае на pt)
# и так происходит всегда, если методы объявляем как функции внутри класса 


pt.set_coords() # тут все теперь ок с self

Point.set_coords(pt) # эквивалент pt.set_coords()




print(None)

