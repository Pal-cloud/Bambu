class Animal:  # Clase simple para representar animales
    """
    Clase que representa un animal con nombre y tipo.
    """
    def __init__(self, name, animal_type):  # Constructor - se ejecuta al crear el animal
        self.name = name           # Nombre del animal
        self.animal_type = animal_type  # Tipo de animal (perro, gato, etc.)
        self.energy = 100         # Energía inicial del animal

    def make_sound(self):  # Método para que el animal haga ruido
        if self.animal_type == "perro":
            return f"� {self.name} dice: ¡Guau guau!"
        elif self.animal_type == "gato":
            return f"🐱 {self.name} dice: ¡Miau miau!"
        elif self.animal_type == "vaca":
            return f"🐄 {self.name} dice: ¡Muuu!"
        else:
            return f"🐾 {self.name} hace un sonido extraño"

# Ejemplo sonido
if __name__ == "__main__":
    print("� ¡Bienvenido a la granja!\n")
    
    # Crear tres animales diferentes
    my_dog = Animal("Lilo", "perro")
    my_cat = Animal("Bambú", "gato") 
    my_cow = Animal("Lola", "vaca")
    
    print("� Animales en la granja:")
    print(f"   🐕 Perro: {my_dog.name}")
    print(f"   🐱 Gato: {my_cat.name}")
    print(f"   🐄 Vaca: {my_cow.name}")
    
    print("\n" + "="*40)
    print("� ¡Escuchemos a los animales!")
    print(my_dog.make_sound())
    print(my_cat.make_sound())
    print(my_cow.make_sound())
