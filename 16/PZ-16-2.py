# Создайте класс "Животное", который содержит информацию о виде и возрасте
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе. 

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def info(self):
        print(f"Species: {self.species}, Age: {self.age}")


class Dog(Animal):
    def __init__(self, age, breed):
        super().__init__("Dog", age)
        self.breed = breed

    def info(self):
        super().info()
        print(f"Breed: {self.breed}")


class Cat(Animal):
    def __init__(self, age, breed):
        super().__init__("Cat", age)
        self.breed = breed

    def info(self):
        super().info()
        print(f"Breed: {self.breed}")


dog = Dog(3, "Labrador")
cat = Cat(5, "Siamese")

dog.info()
print()
cat.info()