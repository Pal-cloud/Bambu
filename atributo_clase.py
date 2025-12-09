class Animal:
    """
    Demuestra la diferencia entre atributos de clase e instancia.
    
    Atributos de clase:
        total_animals (int): Contador global compartido por todas las instancias
    """
    
    total_animals = 0  # Atributo de clase - compartido por todos los animales
    
    def __init__(self, name):
        """
        Crea un animal e incrementa automáticamente el contador global.
        
        Args:
            name (str): Nombre único del animal
        """
        self.name = name  # Atributo de instancia - único para cada objeto
        Animal.total_animals += 1  # Modifica el atributo de clase


# Ejemplo súper simple de atributo de clase
if __name__ == "__main__":
    print("📊 ATRIBUTO DE CLASE - Ejemplo Simple\n")
    
    print(f"Inicio - Total animales: {Animal.total_animals}")
    
    print("\n🐾 Creando animales...")
    lilo = Animal("Lilo")  # Lilo es un perro
    print(f"Creado Lilo (perro) - Total: {Animal.total_animals}")
    
    bambu = Animal("Bambú")  # Bambú es una gata
    print(f"Creado Bambú (gata) - Total: {Animal.total_animals}")
    
    lola = Animal("Lola")  # Lola es una vaca
    print(f"Creado Lola (vaca) - Total: {Animal.total_animals}")
    
    print(f"\n✨ RESULTADO:")
    print(f"🏢 Animal.total_animals = {Animal.total_animals}  (desde la clase)")
    print(f"� lilo.name = {lilo.name}  (perro)")
    print(f"� bambu.name = {bambu.name}  (gata)")
    print(f"� lola.name = {lola.name}  (vaca)")
