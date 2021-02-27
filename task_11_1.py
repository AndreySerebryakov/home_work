class Dog:
    def __init__(self, name, age, weight):
        self.__name = name
        self.__age = age
        self.__weight = weight

    def say(self, word):
        print(f'{word} {self.__name}')

    def run(self, word):
        print(f'{word} {self.__name}')


dog = Dog('Sparky', 10, 5)
dog.say('Woof!')
dog.run('Run')
print(dog._Dog__name)


class Cat:
    def __init__(self, name, age, weight):
        self.__name = name
        self.__age = age
        self.__weight = weight

    def say(self, word):
        print(f'{word} {self.__name}')

    def say1(self, word):
        print(f'{word}')


cat = Cat('Tom', 1, 4)
cat.say('Meow')
cat.say1('Mrrr')
print(cat._Cat__name)


class Rabbit:
    def __init__(self, name, age, weight):
        self.__name = name
        self.__age = age
        self.__weight = weight

    def run(self, word):
        print(f'{word}')

    def eat(self, word):
        print(f'{word}')


rabbit = Rabbit('Rom', 2, 3)
rabbit.run('Run')
rabbit.eat('Eat carrot')
print(rabbit._Rabbit__name)

class Turtle:
    def __init__(self, name, age, weight):
        self.__name = name
        self.__age = age
        self.__weight = weight

    def swim(self, word):
        print(f'{word}')

    def crawl(self, word):
        print(f'{word}')


turtle = Turtle('Leo', 40, 15)
turtle.swim('Swim')
turtle.crawl('Crawl')
print(turtle._Turtle__name)

class Dino:
    def __init__(self, name, age, weight):
        self.__name = name
        self.__age = age
        self.__weight = weight

    def say(self, word):
        print(f'{word}')

    def walk(self, word):
        print(f'{word}')


dino = Dino('Rex', 4, 150)
dino.say('Arght')
dino.walk('Walk')
print(dino._Dino__name)