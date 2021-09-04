class Cat:
    def __init__(self, name, breed="pers", age=1, color="white"):
        print("Hello new object is", self, name, breed, age, color)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color


Kelly = Cat("Kelly")
print(Kelly)
