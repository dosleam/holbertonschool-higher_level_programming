#!/usr/bin/python3

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        
        """
        Init
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display data"""

        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        
        """
        serialize data
        """

        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Error occurred:", e)

    @classmethod
    def deserialize(cls, filename):
        
        """
        deserialize data
        """

        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print("File not found.")
            return None
        except pickle.UnpicklingError:
            print("Error occurred while unpickling.")
            return None
        except Exception as e:
            print("Error occurred:", e)
            return None
