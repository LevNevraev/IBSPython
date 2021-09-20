class Animal:
    def voice(self):
        pass

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