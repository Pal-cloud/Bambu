class Animal:
    """
    Demuestra los tres niveles de visibilidad en Python.
    
    Convenciones de visibilidad:
    - público: acceso libre (sin _)
    - protegido: uso interno preferido (_)  
    - privado: acceso restringido (__)
    """
    
    def __init__(self, name, age):
        """
        Inicializa animal con diferentes niveles de visibilidad.
        
        Args:
            name (str): Nombre público del animal
            age (int): Edad protegida del animal
        """
        self.name = name                    # Público - acceso libre
        self.energy = 100                   # Público - acceso libre
        self._age = age                     # Protegido - uso interno preferido
        self.__secret_id = 12345            # Privado - acceso muy restringido

    def _calculate_energy(self):
        """
        Método protegido para cálculos internos.
        
        Returns:
            int: Energía calculada basada en la edad
        """
        return self._age * 10

    def __generate_secret(self):
        """Método privado solo para uso interno de esta clase."""
        return f"Secreto: {self.__secret_id}"

    def show_secret(self):
        """
        Única forma pública de acceder a datos privados.
        
        Returns:
            str: ID secreto del animal
        """
        return self.__generate_secret()

    def get_info(self):
        """
        Información completa usando todos los niveles de acceso.
        
        Returns:
            str: Información formateada del animal
        """
        return f"🐾 {self.name} tiene {self._age} años"


class Cat(Animal):  # Clase hija para probar herencia
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed  # Público
    
    def meow_with_info(self):
        # ✅ Puede acceder a público y protegido
        energy = self._calculate_energy()  # Método protegido
        return f"� {self.name} (raza: {self.breed}) maúlla con energía: {energy}"
    
    def try_access_private(self):
        # ❌ NO puede acceder a atributos privados directamente
        try:
            return self.__secret_id  # Esto dará error
        except AttributeError:
            return "❌ No puedo acceder al atributo privado __secret_id"


# Ejemplo de visibilidad de atributos
if __name__ == "__main__":
    print("🔐 ATRIBUTOS: PÚBLICO, PROTEGIDO Y PRIVADO\n")
    
    # Crear objetos
    bambu = Cat("Bambú", 2, "Persa")
    
    print("✅ ATRIBUTOS PÚBLICOS (accesibles desde fuera):")
    print(f"   Nombre: {bambu.name}")  # ✅ Funciona
    print(f"   Raza: {bambu.breed}")   # ✅ Funciona
    print(f"   Info: {bambu.get_info()}")  # ✅ Funciona
    
    print("\n⚠️ ATRIBUTOS PROTEGIDOS (no deberías acceder, pero puedes):")
    print(f"   Edad: {bambu._age}")  # ⚠️ Funciona pero NO es recomendado
    print(f"   Energía: {bambu._calculate_energy()}")  # ⚠️ Funciona pero NO recomendado
    
    print("\n❌ ATRIBUTOS PRIVADOS (no accesibles desde fuera):")
    try:
        print(f"   ID secreto: {bambu.__secret_id}")  # ❌ Error
    except AttributeError as e:
        print(f"   Error: {e}")
    
    print(f"   Pero sí puedo usar método público: {bambu.show_secret()}")  # ✅ Funciona
    
    print("\n� DESDE LA CLASE HIJA:")
    print(f"   {bambu.meow_with_info()}")  # ✅ Usa protegido
    print(f"   {bambu.try_access_private()}")  # ❌ No puede acceder a privado
    
    print("\n📋 RESUMEN:")
    print("   🟢 público: self.name → accesible desde cualquier lugar")
    print("   🟡 _protegido: self._age → para uso interno y clases hijas") 
    print("   🔴 __privado: self.__secret_id → solo para uso interno")
