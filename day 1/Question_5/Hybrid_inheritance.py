# Code for Hybrid Inheritance in Python

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} can eat.")

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print(f"{self.name} can walk.")

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"{self.name} can swim.")

class Dolphin(Mammal, Fish):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} can speak.")

dolphin = Dolphin("dolphin")
dolphin.eat()   
dolphin.walk()  
dolphin.swim()  
dolphin.speak() 