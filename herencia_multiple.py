class Animal:
    """
    Clase base que proporciona comportamientos biológicos fundamentales.
    
    Define las necesidades básicas que comparten todos los seres vivos:
    alimentación, descanso y gestión de energía.
    """
    
    def __init__(self, name):
        """
        Inicializa las características básicas de cualquier animal.
        
        Args:
            name (str): Nombre del animal
        """
        self.name = name
        self.energy = 100
    
    def eat(self):
        """Incrementa energía mediante alimentación."""
        self.energy += 20
        return f"🍖 {self.name} está comiendo. Energía: {self.energy}"
    
    def sleep(self):
        """Restaura completamente la energía mediante el descanso."""
        self.energy = 100
        return f"💤 {self.name} durmió toda la noche"


class Pet:
    """
    Clase base que define comportamientos típicos de mascotas.
    
    Gestiona la relación afectiva entre la mascota y su dueño,
    incluyendo actividades recreativas y vínculos emocionales.
    """
    
    def __init__(self, owner):
        """
        Establece la relación mascota-dueño.
        
        Args:
            owner (str): Nombre del dueño de la mascota
        """
        self.owner = owner
        self.happiness = 50
    
    def play(self):
        """Incrementa felicidad a través del juego."""
        self.happiness += 30
        return f"🎾 ¡Jugando! Felicidad: {self.happiness}"
    
    def show_love(self):
        """Expresa afecto hacia el dueño."""
        return f"❤️ {self.name} ama a {self.owner}"


class Worker:
    """
    Clase base para animales con capacidades laborales.
    
    Define comportamientos relacionados con actividades productivas
    o servicios especializados que puede realizar el animal.
    """
    
    def __init__(self, job):
        """
        Asigna una función laboral específica.
        
        Args:
            job (str): Tipo de trabajo que realiza el animal
        """
        self.job = job
        self.productivity = 0
    
    def work(self):
        """Ejecuta las tareas asignadas según su especialización."""
        self.productivity += 25
        return f"💼 {self.name} está trabajando como {self.job}. Productividad: {self.productivity}"


# HERENCIA MÚLTIPLE: Dog hereda de Animal Y Pet
class Dog(Animal, Pet):
    """
    Perro doméstico que combina naturaleza animal con comportamiento de mascota.
    
    Hereda de:
        Animal: Necesidades biológicas básicas
        Pet: Comportamientos afectivos y recreativos
    """
    
    def __init__(self, name, owner):
        """
        Inicializa perro con características de animal y mascota.
        
        Args:
            name (str): Nombre del perro
            owner (str): Nombre del dueño
        """
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
    
    def bark(self):
        """Comportamiento específico de ladrido."""
        return f"🐕 {self.name}: ¡Guau guau!"


# HERENCIA MÚLTIPLE: Cat hereda de Animal Y Pet
class Cat(Animal, Pet):
    """
    Gato doméstico que combina instintos salvajes con vida hogareña.
    
    Hereda de:
        Animal: Necesidades biológicas básicas  
        Pet: Comportamientos afectivos (aunque más independientes)
    """
    
    def __init__(self, name, owner):
        """
        Inicializa gato con características de animal y mascota.
        
        Args:
            name (str): Nombre del gato
            owner (str): Nombre del dueño
        """
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
    
    def meow(self):
        """Comportamiento específico de maullido."""
        return f"🐱 {self.name}: ¡Miau miau!"


# HERENCIA MÚLTIPLE: WorkingDog hereda de Animal, Pet Y Worker
class WorkingDog(Animal, Pet, Worker):
    """
    Perro de trabajo que combina tres aspectos: animal, mascota y trabajador.
    
    Ejemplo de herencia múltiple completa que integra:
        Animal: Necesidades biológicas
        Pet: Vínculos afectivos 
        Worker: Capacidades laborales especializadas
    """
    
    def __init__(self, name, owner, job):
        """
        Inicializa perro de trabajo con todas sus facetas.
        
        Args:
            name (str): Nombre del perro
            owner (str): Nombre del dueño/entrenador
            job (str): Especialización laboral (policía, rescate, etc.)
        """
        Animal.__init__(self, name)
        Pet.__init__(self, owner) 
        Worker.__init__(self, job)
    
    def bark(self):
        """Ladrido profesional de perro de trabajo."""
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
