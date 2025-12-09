class Cat:  # Ejemplo pytónico de getters y setters con @property
    def __init__(self, name, age):
        self._name = name  # Atributo protegido
        self._age = age    # Atributo protegido
        self._energy = 100 # Atributo protegido
    
    # GETTER PYTÓNICO - usando @property
    @property
    def name(self):
        """Getter pytónico: obtiene el nombre como si fuera un atributo"""
        return f"🐱 {self._name}"
    
    @property
    def age(self):
        """Getter pytónico: obtiene la edad"""
        return self._age
    
    @property
    def energy(self):
        """Getter pytónico: obtiene la energía"""
        return self._energy
    
    # SETTER PYTÓNICO - usando @nombre.setter
    @name.setter
    def name(self, new_name):
        """Setter pytónico: cambia el nombre con validación"""
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("❌ El nombre debe ser un texto válido")
    
    @age.setter
    def age(self, new_age):
        """Setter pytónico: cambia la edad con validación"""
        if isinstance(new_age, int) and 0 <= new_age <= 25:
            self._age = new_age
        else:
            raise ValueError("❌ La edad debe ser entre 0 y 25 años")
    
    @energy.setter
    def energy(self, new_energy):
        """Setter pytónico: cambia la energía con validación"""
        if isinstance(new_energy, int) and 0 <= new_energy <= 100:
            self._energy = new_energy
        else:
            raise ValueError("❌ La energía debe ser entre 0 y 100")
    
    # Método para mostrar información completa
    def show_info(self):
        return f"🐱 {self._name} - Edad: {self._age} años - Energía: {self._energy}"


# Ejemplo pytónico de properties
if __name__ == "__main__":
    print("🐍 PROPERTIES PYTÓNICAS - Decorador @property\n")
    
    # Crear gata
    bambu = Cat("Bambú", 2)
    
    print("📖 USANDO PROPERTIES (como atributos normales):")
    print(f"   Nombre: {bambu.name}")      # Se ve como atributo, pero es un getter
    print(f"   Edad: {bambu.age} años")    # Se ve como atributo, pero es un getter
    print(f"   Energía: {bambu.energy}")   # Se ve como atributo, pero es un getter
    print(f"   Info completa: {bambu.show_info()}")
    
    print("\n🛠️ MODIFICANDO CON PROPERTIES (como asignaciones normales):")
    
    print("\n✅ Cambios válidos:")
    try:
        bambu.name = "Bambú Princesa"     # Se ve como asignación, pero es un setter
        print(f"   ✅ Nombre cambiado a: {bambu._name}")
        
        bambu.age = 3                     # Se ve como asignación, pero es un setter
        print(f"   ✅ Edad cambiada a: {bambu.age} años")
        
        bambu.energy = 80                 # Se ve como asignación, pero es un setter
        print(f"   ✅ Energía cambiada a: {bambu.energy}")
        
        print(f"   Resultado: {bambu.show_info()}")
    except ValueError as e:
        print(f"   {e}")
    
    print("\n❌ Intentos de cambios inválidos:")
    
    # Nombre vacío
    try:
        bambu.name = ""
    except ValueError as e:
        print(f"   {e}")
    
    # Edad negativa
    try:
        bambu.age = -5
    except ValueError as e:
        print(f"   {e}")
    
    # Edad muy alta
    try:
        bambu.age = 30
    except ValueError as e:
        print(f"   {e}")
    
    # Energía muy alta
    try:
        bambu.energy = 150
    except ValueError as e:
        print(f"   {e}")
    
    # Energía negativa
    try:
        bambu.energy = -10
    except ValueError as e:
        print(f"   {e}")
    
    print(f"\n📊 Estado final: {bambu.show_info()}")
    
    print("\n🎯 COMPARACIÓN DE SINTAXIS:")
    print("   🐍 PYTÓNICO:     bambu.age = 5      (limpio y natural)")
    print("   📝 TRADICIONAL:  bambu.set_age(5)   (más verboso)")
    print("   🐍 PYTÓNICO:     print(bambu.age)   (como un atributo)")
    print("   📝 TRADICIONAL:  print(bambu.get_age())  (llamada a método)")
    
    print("\n📋 VENTAJAS DE @property:")
    print("   🎨 SINTAXIS LIMPIA: Se usa como atributos normales")
    print("   🛡️ VALIDACIÓN: Mantiene toda la validación")
    print("   🔄 COMPATIBILIDAD: Fácil migración desde atributos públicos")
    print("   📖 LEGIBILIDAD: Código más natural y fácil de leer")
