# Паттерн "Моносостояние"
class TheadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }
    def __init__(self):
        self.__dict__ = self.__shared_attrs

# в каждом экземпляре будут одни и те же свойства

th1 = TheadData()
th2 = TheadData()



th2.id = 3 # появится и в th1
th1.attr_new = 'new_attr' # появится и в th2



print(None)