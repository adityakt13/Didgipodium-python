class Dog:
    # init is used to initialize the object
    def __init__(self, breed, age, weight, gender):
        self.breed = breed
        self.age = age
        self.weight = weight
        self.gender = gender
        print("Dog object created")


panther = Dog(breed="German Shepherd", age=11, weight=30, gender = "female")
tiger = Dog(breed='Pug', age= 3,gender = "male", weight= 15)
blacky = Dog(breed='Lebrador', age= 5, weight= 25, gender = "not defined")

print(panther.breed)
print(tiger.age)
print(panther.weight)
print(blacky.gender)