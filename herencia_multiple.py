class Animal:  # Clase base con comportamientos de animal
    def __init__(self, name):
        self.name = name
        self.energy = 100
    
    def eat(self):
        self.energy += 20
        return f"🍖 {self.name} está comiendo. Energía: {self.energy}"
    
    def sleep(self):
        self.energy = 100
        return f"💤 {self.name} durmió toda la noche"


class Pet:  # Clase base con comportamientos de mascota
    def __init__(self, owner):
        self.owner = owner
        self.happiness = 50
    
    def play(self):
        self.happiness += 30
        return f"🎾 ¡Jugando! Felicidad: {self.happiness}"
    
    def show_love(self):
        return f"❤️ {self.name} ama a {self.owner}"


class Worker:  # Clase base con comportamientos de trabajador
    def __init__(self, job):
        self.job = job
        self.productivity = 0
    
    def work(self):
        self.productivity += 25
        return f"💼 {self.name} está trabajando como {self.job}. Productividad: {self.productivity}"


# HERENCIA MÚLTIPLE: Dog hereda de Animal Y Pet
class Dog(Animal, Pet):  # Hereda de DOS clases a la vez
    def __init__(self, name, owner):
        Animal.__init__(self, name)  # Inicializar parte de Animal
        Pet.__init__(self, owner)    # Inicializar parte de Pet
    
    def bark(self):
        return f"🐕 {self.name}: ¡Guau guau!"


# HERENCIA MÚLTIPLE: Cat hereda de Animal Y Pet
class Cat(Animal, Pet):  # Hereda de DOS clases a la vez
    def __init__(self, name, owner):
        Animal.__init__(self, name)  # Inicializar parte de Animal
        Pet.__init__(self, owner)    # Inicializar parte de Pet
    
    def meow(self):
        return f"🐱 {self.name}: ¡Miau miau!"


# HERENCIA MÚLTIPLE: WorkingDog hereda de Animal, Pet Y Worker
class WorkingDog(Animal, Pet, Worker):  # Hereda de TRES clases
    def __init__(self, name, owner, job):
        Animal.__init__(self, name)
        Pet.__init__(self, owner) 
        Worker.__init__(self, job)
    
    def bark(self):
        return f"🐕‍🦺 {self.name}: ¡Guau! (perro trabajador)"


# Ejemplo de herencia múltiple
if __name__ == "__main__":
    print("🧬 HERENCIA MÚLTIPLE - Ejemplo Simple\n")
    
    # Perro mascota (Animal + Pet)
    print("🐕 Creando perro mascota:")
    lilo = Dog("Lilo", "Paloma")
    
    print(lilo.bark())           # Método propio
    print(lilo.eat())            # Heredado de Animal
    print(lilo.play())           # Heredado de Pet
    print(lilo.show_love())      # Heredado de Pet
    
    print("\n" + "="*40)
    print("� Creando gata mascota:")
    bambu = Cat("Bambú", "Carlos")
    
    print(bambu.meow())          # Método propio
    print(bambu.eat())           # Heredado de Animal
    print(bambu.play())          # Heredado de Pet
    print(bambu.show_love())     # Heredado de Pet
    
    print("\n" + "="*40)
    print("�🐕‍🦺 Creando perro trabajador:")
    rex = WorkingDog("Rex", "Ana", "policía")
    
    print(rex.bark())            # Método propio
    print(rex.eat())             # Heredado de Animal
    print(rex.play())            # Heredado de Pet
    print(rex.work())            # Heredado de Worker
    print(rex.show_love())       # Heredado de Pet
    
    print(f"\n📋 RESUMEN DE HERENCIAS:")
    print(f"🐕 Lilo hereda de: {Dog.__bases__}")  # Muestra las clases padre
    print(f"� Bambú hereda de: {Cat.__bases__}")  # Muestra las clases padre
    print(f"🐕‍🦺 Rex hereda de: {WorkingDog.__bases__}")  # Muestra las clases padre
