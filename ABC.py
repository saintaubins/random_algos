# model for abc
from abc import ABC, abstractmethod
import collections

# class Entertainer(ABC):
#     @abstractmethod
#     def sing(self, song):
#         pass

#     @abstractmethod
#     def dance(self):
#         pass

class Visible(ABC):
    # Mixin class that reveals calculation details

    @abstractmethod
    def calc(self, x):
        return 0

    def show(self, x):
        result = self.calc(x)
        print(f'Called calc() with {x} giving {result}')

class Calculator(Visible):
    def __init__(self, factor):
        self.factor = factor

    def calc(self, x):
        return x * self.factor

double = Calculator(2)
y = double.calc(5)
y = double.show(5)

# class ListBasedSet(collections.abc.Set):
#     ''' Alternate set implementation favoring space over speed
#         and not requiring the set elements to be hashable. '''
#     def __init__(self, iterable):
#         self.elements = lst = []
#         for value in iterable:
#             if value not in lst:
#                 lst.append(value)
        
#     def __iter__(self):
#         return iter(self.elements)

#     def __contains__(self, value):
#         return value in self.elements

#     def __len__(self):
#         return len(self.elements)

# s1 = ListBasedSet('abcdef')
# s2 = ListBasedSet('defghi')
# overlap = s1 & s2        # The __and__() method is supported automatically
# print(overlap)

dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
dataEngineer = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])
print(f'intersection : {dataScientist & dataEngineer}')   # intersection between 2 sets
print('union : ',dataScientist | dataEngineer)   # union between 2 sets
print('difference : ' ,dataScientist - dataEngineer)   # difference between 2 sets
print('symmetric difference : ' ,dataScientist ^ dataEngineer) # symmetric difference between 2 sets
