class Animal:
    num_of_animals =0
    def __init__(self):
        Animal.num_of_animals=Animal.num_of_animals +1
    def voice(self):
        pass

    def print_num_of_animals():
        print(Animal.num_of_animals)

    print_num_of_animals=staticmethod(print_num_of_animals)

class Dog(Animal):
    def voice(self):
        print('wow')

class Cat(Animal):
    def voice(self):
        print('meow')

class Fish(Animal):
    def voice(self):
        print('blob-blob')

doggy = Dog()
murka = Cat()
fishka = Fish()

doggy.voice()
murka.voice()
fishka.voice()

Animal.print_num_of_animals()
doggy.print_num_of_animals()