
class Pet:
    """ Домашнее животное """
    legs = 4
    has_tail = True

    def __init__(self, name):
        self.name = name

    def inspect(self):
        print(self.__class__.__name__, self.name)  # ссылка на класс объекта и далее на имя класса
        print('  Всего ног:', self.legs)
        print('  Хвост присутствует -', 'да' if self.has_tail else 'нет')
        print(self.__dict__)  # подкапотный словарь атрибутов и методов


class Cat(Pet):
    """ Кошка - является Домашним Животным """

    def sound(self):
        print('Мяу!')


class Dog(Pet):
    """ Собака - является Домашним Животным """

    def sound(self):
        print('Гав!')


class Hamster(Pet):
    """ Хомячок - является Домашним Животным """

    def sound(self):
        print('Ццццццц!')  # https://goo.gl/KXoj21


pet = Pet(name="Кузя")
print(pet.__class__ is Pet)
pet.inspect()


class Bobtail(Cat):
    """ Бобтейл - является Кошкой """
    has_tail = False


my_pet = Bobtail(name = "123")
my_pet.inspect()