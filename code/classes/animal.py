# 1. напишите класс "Dog", собаки лают
# 2. напишите класс "Cat", кошечки мяукают
# 3. обобщите??

class Animal:
    def say(self):
        print("Saying smth...")

    def say_animal(self, greeting):
        print(f"{greeting} from animal!")

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def order():
        print("Хищные")

    def say(self):
        print(f"{self.name}: Woof!")

class Cat:
    def __init__(self, name):
        self.name = name

    def say(self):
        print(f"{self.name}: Meow!")


Dog.order()

# dog = Dog("Бонк", "Black")
# dog2 = Dog("Бобик", "Yellow")
# cat = Cat("Пушок")
# dog.say_animal("Hi")
# print(dog.name)
# cat.say()
# dog.say()

# animals = [
# Dog("Бонк", "Black"),
# Cat("Пушок")
# ]

# for animal in animals:
#     animal.say()

# value = 43
# hello = f"Hello {value - 1}"
# print(hello)