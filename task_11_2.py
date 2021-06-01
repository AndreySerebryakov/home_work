class Car:
    def __init__(self, name, model, year, speed=0):
        self.__name = name
        self.__model = model
        self.__year = year
        self.__speed = speed

    def up(self):
        self.__speed = self.__speed + 5
        print('скорость увеличилась на 5 и равна', self.__speed)

    def down(self):
        if self.__speed - 5 < 0:
            raise ValueError('Скорость не может быть меньше нуля')
        self.__speed = self.__speed - 5
        print('скорость уменьшилась на 5 и стала равна', self.__speed)

    def stop(self):
        self.__speed = 0
        print('остановка и скорость равна', self.__speed)

    def show(self):
        print('скорость равна', self.__speed)

    def reverse(self):
        self.__speed *= -1
        print('разворот и скорость равна', self.__speed)


car = Car('lada', '2101', 2000)

car.up()
car.up()
car.reverse()
car.down()
car.show()
car.reverse()
car.stop()
car.down()
