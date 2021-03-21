class MyItr:
    def __init__(self, mylist):
        self.list = mylist
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list):
            self.index += 1
            if (self.index - 1) % 2 == 0 and (self.index-1) != 0:
                v = self.list[(self.index - 1)] ** 2
                return (v)
            else:
                return ("Индекс нечетный")
        else:
            raise StopIteration


itr = MyItr([1, 2, 3, 4, 5, 6])
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
