from abc import ABC, abstractmethod

class Animal(ABC):  # Clase abstracta - no se puede instanciar
    def __init__(self, name):
        self.name = name
        self.energy = 100
    
    @abstractmethod  # Método obligatorio para clases hijas
    def make_sound(self):
        pass
    
    # Método concreto que heredan todas las clases hijas
    def eat(self):
        self.energy += 20
        return f"🍖 {self.name} está comiendo. Energía: {self.energy}"

# Clases hijas
class Dog(Animal):
    def make_sound(self):
        return f"🐕 {self.name}: ¡Guau guau!"

class Cat(Animal):
    def make_sound(self):
        return f"🐱 {self.name}: ¡Miau miau!"

class Cow(Animal):
    def make_sound(self):
        return f"� {self.name}: ¡Muuu!"

# Ejemplo uso
if __name__ == "__main__":
    # Crear animales con nombres de animal.py
    lilo = Dog("Lilo")
    bambu = Cat("Bambú") 
    lola = Cow("Lola")
    
    print("🔊 Sonidos de los animales:")
    print(lilo.make_sound())
    print(bambu.make_sound()) 
    print(lola.make_sound())
    
    print("\n🍖 Hora de comer:")
    print(lilo.eat())
    print(bambu.eat())
    print(lola.eat())
