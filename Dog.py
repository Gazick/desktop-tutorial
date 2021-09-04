class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        self.sound = sound
        return f"{self.name} says {self.sound}"


jack = Dog("Jack", 4)

print(jack.description())
print(jack.speak("Woof Woof"))
print(jack.speak("Bow Wow"))
