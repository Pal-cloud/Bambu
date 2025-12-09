class Animal:  # Ejemplo de atributos públicos, protegidos y privados
    def __init__(self, name, age):
        # ATRIBUTO PÚBLICO - accesible desde cualquier lugar
        self.name = name  # Sin guiones bajos = público
        
        # ATRIBUTO PROTEGIDO - para uso interno y clases hijas
        self._age = age  # Un guión bajo = protegido
        
        # ATRIBUTO PRIVADO - solo para uso interno de esta clase
        self.__secret_id = 12345  # Dos guiones bajos = privado
    
    # MÉTODO PÚBLICO - accesible desde cualquier lugar
    def get_info(self):
        return f"🐾 {self.name} tiene {self._age} años"
    
    # MÉTODO PROTEGIDO - para uso interno y clases hijas
    def _calculate_energy(self):
        return self._age * 10
    
    # MÉTODO PRIVADO - solo para uso interno de esta clase
    def __generate_secret(self):
        return f"Secreto: {self.__secret_id}"
    
    # MÉTODO PÚBLICO que usa el método privado
    def show_secret(self):
        return self.__generate_secret()


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
