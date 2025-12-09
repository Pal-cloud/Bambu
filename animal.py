class Animal:
    """
    Representa un animal básico con capacidades de comunicación.
    
    Esta clase demuestra los conceptos fundamentales de POO:
    - Encapsulación de datos (atributos)
    - Comportamiento (métodos)
    - Instanciación de objetos
    """
    
    def __init__(self, name, animal_type):
        """
        Inicializa un nuevo animal.
        
        Args:
            name (str): Nombre del animal
            animal_type (str): Tipo de animal (perro, gato, vaca, etc.)
        """
        self.name = name
        self.animal_type = animal_type
        self.energy = 100

    def make_sound(self):
        """
        Produce el sonido característico según el tipo de animal.
        
        Returns:
            str: Mensaje con el sonido específico del animal
        """
        if self.animal_type == "perro":
            return f"🐕 {self.name}: ¡Guau guau!"
        elif self.animal_type == "gato":
            return f"🐱 {self.name}: ¡Miau miau!"
        elif self.animal_type == "vaca":
            return f"🐄 {self.name}: ¡Muuu!"
        else:
            return f"🐾 {self.name} hace un sonido extraño"


# Ejemplo sonido
if __name__ == "__main__":
    print("🐾 ¡Bienvenido a la granja!\n")
    
    # Crear tres animales diferentes
    lilo = Animal("Lilo", "perro")  # Lilo es un perro
    bambu = Animal("Bambú", "gato") # Bambú es una gata
    lola = Animal("Lola", "vaca")   # Lola es una vaca
    
    print("🏠 Animales en la granja:")
    print(f"   🐕 Perro: {lilo.name}")
    print(f"   🐱 Gato: {bambu.name}")
    print(f"   🐄 Vaca: {lola.name}")
    
    print("\n" + "="*40)
    print("🔊 ¡Escuchemos a los animales!")
    print(lilo.make_sound())
    print(bambu.make_sound())
    print(lola.make_sound())
