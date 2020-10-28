"""OOP examples for module 2"""

import pandas as pd
import numpy as np


class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self,shape[1]


class BareClass:
    pass


class Complex:
    def __init__(self, realpart, imagpart):
        """
        Constructor for complex numbers.
        Complex numbers have a real part and imaginary part
        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return "({}, {})".format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name):
        self.nam = str(name)
        # self.locaction = str(location)
        self.upvotes = 0

    def receive_upvotes(self):
        self.upvotes += 1

    def is_popular(self):
        return self.upvotes > 100


# class Animal:
#     """General Representation of Animals"""
#     def __init__(self, name, weight, diet_type):
#         self.name = str(name)
#         self.weight = float(weight)
#         self.diet_type = str(diet_type)

#     def run(self):
#         return "Vroom, Vroom, I go quick"

#     def eat(self, food):
#         return "Huge fan of the " + str(food)


# class Sloth(Animal):
#     def __init__(self, name, weight, diet_type, num_naps):
#         super().__init__(name, weight, diet_type)
#         self.num_naps = int(num_naps)

#     def say_something(self):
#         return "This is a sloth of typing"

#     def run(self):
#         return "Verrrrryyyy slooowwww"


# if __name__ == "__main__":
#     num1 = Complex(3, 5)
#     num2 = Complex(4, 2)
#     num1.add(num2)
#     print(num1.r, num1.i)

#     user1 = SocialMediaUser("Drew", "Nola", 101)
#     user2 = SocialMediaUser("Tori", "Biloxi", 1)
#     user3 = SocialMediaUser("D", "Seattle", upvotes=100)
#     user4 = SocialMediaUser("El", "NC", 2)
#     print("name: {}, is popular:{}".format(user2.nam, user2.is_popular, user2.up))
#     print("name: {}, is popular:{}".format(user1.nam, user2.is_popular, user1.up))
