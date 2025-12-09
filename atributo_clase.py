class Animal:  # Clase simple para demostrar atributos de clase
    total_animals = 0  # 🏢 ATRIBUTO DE CLASE - compartido por todos los animales
    
    def __init__(self, name):
        self.name = name           # 👤 Atributo de instancia - cada animal tiene su propio nombre
        Animal.total_animals += 1  # Cada vez que se crea un animal, suma 1 al total


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
