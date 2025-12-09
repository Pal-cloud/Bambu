from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Clase abstracta que define el contrato para todos los animales.
    
    No puede ser instanciada directamente. Las clases hijas deben
    implementar todos los métodos abstractos marcados con @abstractmethod.
    """
    
    def __init__(self, name):
        """
        Constructor base para todos los animales.
        
        Args:
            name (str): Nombre del animal
        """
        self.name = name
        self.energy = 100
    
    @abstractmethod
    def make_sound(self):
        """
        Método abstracto que deben implementar todas las clases hijas.
        
        Cada tipo de animal debe definir su propio sonido característico.
        
        Returns:
            str: Sonido específico del animal
        """
        pass
    
    def eat(self):
        """
        Comportamiento común heredado por todos los animales.
        
        Returns:
            str: Mensaje indicando que el animal está comiendo
        """
        self.energy += 20
        return f"🍖 {self.name} está comiendo. Energía: {self.energy}"


# Clases hijas
class Dog(Animal):
    """Implementación concreta de Animal para perros."""
    
    def make_sound(self):
        """Implementa el ladrido característico de los perros."""
        return f"🐕 {self.name}: ¡Guau guau!"

class Cat(Animal):
    """Implementación concreta de Animal para gatos."""
    
    def make_sound(self):
        """Implementa el maullido característico de los gatos."""
        return f"🐱 {self.name}: ¡Miau miau!"

class Cow(Animal):
    """Implementación concreta de Animal para vacas."""
    
    def make_sound(self):
        """Implementa el mugido característico de las vacas."""
        return f"🐄 {self.name}: ¡Muuu!"


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
