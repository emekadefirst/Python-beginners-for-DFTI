class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def sound(self):
        pass
    
class Dog(Animal): # We just inhrited the attribute from our class named Animal
    def sound(self): # We just inhrited the method from our class named Animal
        return 'Woof'
    
class Cat(Animal):
    def sound(self):
        return 'Meow'
    
# Creatings Instance of derived classes
dog = Dog('Buddy', 'black')
cat = Cat('whisker', 'grey')

print(dog.color)


