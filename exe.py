'''class Car:
    def start(self):
        print("the car has started")
a = Car()

a.start()'''

'''class Car:
    def __init__ (self, brand="unknown", model="unknown"):
       self.brand = brand
       self.model= model

    def display(self):
        print(f"brand:{self.brand},model:{self.model}")


a = Car("Tata", "Nexon")
b = Car("Tesla")
c = Car()

a.display()
b.display()
c.display()


class Student:
    def __init__(self, name="Unknown", grade="N/A"):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

# Different ways to create objects
s1 = Student("Mahendra", "A")
s2 = Student("Ravi")
s3 = Student()

s1.display()
s2.display()
s3.display()

class car:
    def showinfo(self,brand=None,model=None):
        if brand and model:
            print(f"Brand:{brand},Model:{model}")
        elif brand:
            print(f"Brand:{brand}")
        else:
            print("no car info is provided")

a = car()
a.showinfo("toyota")
a.showinfo("toyota","fortunar")
a.showinfo()'''

'''class car:
    def start(self):
        print("car is started")
    def stop(self):
        print("car is stopping")
class sports_car(car):
    def turbo(self):
        print("turbo is on")

b = sports_car()
b.start()
b.turbo()
b.stop()'''

class Student:
    def __init__(self, name=None, age=None):
        if name is not None and age is not None:
            print(f"Student name: {name}, Age: {age}")
        elif name is not None:
            print(f"Student name: {name}")
        else:
            print("No student info provided")
class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return "Unsupported number of arguments"

# Constructor overloading
s1 = Student("Mahendra", 21)
s2 = Student("Mahendra")
s3 = Student()

# Method overloading
calc = Calculator()
print(calc.add(10, 20))        # Two arguments
print(calc.add(1, 2, 3))       # Three arguments
print(calc.add(5))             # Unsupported

import numpy as n
'''zeros = n.zeros((3,3))
print(zeros)
ones = n.ones((2,4))
print(ones)
full = n.full((2,3),7)
print(full)
eye = n.eye(4)
print(eye)
ar = n.arange(0,10,1)
print(ar)'''
lin = n.linspace(0,50,5)
print(lin)
a = n.array([1,2,3,4])
b= n.array([[1,2,3],[4,5,6]])
c = n.array([[[1,2],[3,4],[5,6],[7,8]]])
print(a.shape)
print(b.shape)
print(a.size)
print(a.ndim)
print(a.dtype)
print(a)
print(b)
