class Cat:
    """
    Implementa control de acceso pytónico usando decorador @property.
    
    Demuestra la forma elegante y natural de Python para getters/setters
    que permite sintaxis de atributo con validación incorporada.
    """
    
    def __init__(self, name, age):
        """
        Inicializa gata usando properties para validación automática.
        
        Args:
            name (str): Nombre de la gata
            age (int): Edad inicial en años
        """
        self._name = name
        self.age = age  # Usa el setter automáticamente
        self._energy = 100

    @property
    def name(self):
        """Property para obtener nombre con formato decorativo."""
        return f"🐱 {self._name}"
    
    @name.setter
    def name(self, value):
        """
        Valida y asigna nuevo nombre.
        
        Args:
            value (str): Nuevo nombre propuesto
            
        Raises:
            ValueError: Si el nombre no es válido
        """
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("El nombre debe ser un texto válido")
        self._name = value

    @property  
    def age(self):
        """Property para obtener edad actual."""
        return self._age
    
    @age.setter
    def age(self, value):
        """
        Valida y asigna nueva edad.
        
        Args:
            value (int): Nueva edad propuesta
            
        Raises:
            ValueError: Si la edad está fuera del rango válido
        """
        if not isinstance(value, int) or not (0 <= value <= 25):
            raise ValueError("La edad debe ser un entero entre 0 y 25")
        self._age = value

    @property
    def energy(self):
        """Property para obtener nivel de energía actual."""
        return self._energy
    
    @energy.setter
    def energy(self, value):
        """
        Valida y asigna nuevo nivel de energía.
        
        Args:
            value (int): Nuevo nivel de energía
            
        Raises:
            ValueError: Si la energía está fuera del rango válido
        """
        if not isinstance(value, int) or not (0 <= value <= 100):
            raise ValueError("La energía debe ser un entero entre 0 y 100")
        self._energy = value

    def show_info(self):
        """
        Resumen completo usando properties.
        
        Returns:
            str: Información formateada de todos los atributos
        """
        return f"{self.name} - Edad: {self.age} años - Energía: {self.energy}"


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
