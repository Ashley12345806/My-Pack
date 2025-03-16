# Parent class
class Animal:
    def __init__(self, name, species, age, habitat,color, size, sound):
        self.name = name
        self.species = species
        self.age = age
        self.habitat = habitat
        self.color = color
        self.size = size
        self.sound = sound

    def display_basic_info(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"

# Child class inheriting from parent class
class Mammal(Animal):
    def __init__(self, name, species, age, habitat, color, size, sound, fur_type,):
        super().__init__(name, species, age, habitat, color, size, sound)
        self.fur_type = fur_type

    def display_mammal_info(self):
        return f"Fur Type: {self.fur_type}"

# Another child class inheriting from Mammal
class Carnivore(Mammal):
    def __init__(self, name, species, age, habitat, color, size, sound, fur_type, hunting_style):
        super().__init__(name, species, age, habitat, color, size, sound, fur_type)
        self.hunting_style = hunting_style

    def display_carnivore_info(self):
        return f"Hunting Style: {self.hunting_style}"

# Another class extending Carnivore
class BigCat(Carnivore):
    def __init__(self, name, species, age, habitat, diet, color, sound, fur_type, hunting_style, roar_volume):
        super().__init__(name, species, age, habitat, diet, color, sound, fur_type,hunting_style)
        self.roar_volume = roar_volume

    def display_bigcat_info(self):
        return f"Roar Volume: {self.roar_volume} dB"

# Final class inheriting from BigCat with at least 5 methods
class Lion(BigCat):
    def __init__(self, name, species, age, habitat, color, size, sound, fur_type, hunting_style, roar_volume, pride_size):
        super().__init__(name, species, age, habitat, color, size, sound, fur_type, hunting_style, roar_volume)
        self.pride_size = pride_size

    def display_pride_size(self):
        return f"Pride Size: {self.pride_size}"

    def make_sound(self):
        return f"{self.name} says: {self.sound}"

    def display_lion_territory(self):
        return f"Lion named {self.name} roams the {self.habitat}."

    def hunt_prey(self):
        return f"{self.name} is hunting using {self.hunting_style} style."

    def display_color(self):
        return f"{self.name} primarily eats: {self.color}"

# Example usage
lion = Lion(
    name="Simba",
    species="Panthera leo",
    age=5,
    habitat="Savannah",
    color="Brown",
    size="Large",
    sound="Roar",
    fur_type="Short",
    hunting_style="Stalking and ambush",
    roar_volume=114,
    pride_size=12
)

# Access Lion-specific and inherited methods
print(lion.display_basic_info())
print(lion.display_mammal_info())
print(lion.display_carnivore_info())
print(lion.display_bigcat_info())
print(lion.display_pride_size())
print(lion.make_sound())
print(lion.display_lion_territory())
print(lion.hunt_prey())
print(lion.display_color())
