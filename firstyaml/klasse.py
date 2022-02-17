class Dog:
    pass
jack=Dog()
#Let's create an object of the class, and assign it the variable "jack"
#The object can also be called instance. 
#Don’t be confused if you find the words “instance” or “object” written somewhere, they always refer to the same thing.
print(type(jack))
class Dog:
    def __init__(self,name,breed,age):
        self.Name = name
        self.Breed = breed
        self.Age = age
    def __repr__(self):
        return "Name: {}, Breed: {}, Age: {}".format(self.Name,
                                           self.Breed,self.Age)

jack = Dog('Jack','Husky',5)
wuffi =Dog('Wuffi','Labrador',8)
max =Dog('Max','Labrador',7)

print(max)

