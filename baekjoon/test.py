from os import remove


class Dog():
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self,name,type):
        self.name = name
        self.type = type
        Dog.num_of_dogs += 1
        Dog.birth_of_dogs += 1

    def __del__(self):
        Dog.num_of_dogs -= 1

    def bark(self):
        print('barkbark')

    @classmethod
    def get_status(slr):
        print(f'{slr.num_of_dogs}')
        print(f'{slr.birth_of_dogs}')

dog1 = Dog('1','n1')
dog2 = Dog('2','n2')
dog3 = Dog('3','n3')
dog4 = Dog('4','n4')
dog5 = Dog('5','n5')
dog4.bark()
del dog5
Dog.get_status()