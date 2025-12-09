class Cat:
    """
    Implementa control de acceso tradicional con getters y setters.
    
    Demuestra validación de datos y encapsulación usando métodos
    explícitos para leer y modificar atributos protegidos.
    """
    
    def __init__(self, name, age):
        """
        Inicializa gata con atributos protegidos.
        
        Args:
            name (str): Nombre de la gata
            age (int): Edad inicial en años
        """
        self._name = name
        self._age = age
        self._energy = 100

    def get_name(self):
        """Obtiene nombre con formato decorativo."""
        return f"🐱 {self._name}"
    
    def get_age(self):
        """Obtiene edad actual."""
        return self._age
    
    def get_energy(self):
        """Obtiene nivel de energía actual."""
        return self._energy

    def set_name(self, new_name):
        """
        Modifica nombre con validación de entrada.
        
        Args:
            new_name (str): Nuevo nombre propuesto
            
        Returns:
            str: Mensaje de éxito o error
        """
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
            return f"✅ Nombre cambiado a: {new_name}"
        else:
            return "❌ Error: El nombre debe ser un texto válido"
    
    def set_age(self, new_age):
        """
        Modifica edad con validación de rango.
        
        Args:
            new_age (int): Nueva edad propuesta
            
        Returns:
            str: Mensaje de éxito o error
        """
        if isinstance(new_age, int) and 0 <= new_age <= 25:
            self._age = new_age
            return f"✅ Edad cambiada a: {new_age} años"
        else:
            return "❌ Error: La edad debe ser entre 0 y 25 años"
    
    def set_energy(self, new_energy):
        """
        Modifica energía con validación de límites.
        
        Args:
            new_energy (int): Nuevo nivel de energía
            
        Returns:
            str: Mensaje de éxito o error
        """
        if isinstance(new_energy, int) and 0 <= new_energy <= 100:
            self._energy = new_energy
            return f"✅ Energía cambiada a: {new_energy}"
        else:
            return "❌ Error: La energía debe ser entre 0 y 100"

    def show_info(self):
        """
        Resumen completo del estado actual.
        
        Returns:
            str: Información formateada de todos los atributos
        """
        return f"🐱 {self._name} - Edad: {self._age} años - Energía: {self._energy}"


# Ejemplo de getters y setters
if __name__ == "__main__":
    print("🔧 GETTERS Y SETTERS - Control de Acceso\n")
    
    # Crear gata
    bambu = Cat("Bambú", 2)
    
    print("📖 USANDO GETTERS (obtener valores):")
    print(f"   Nombre: {bambu.get_name()}")
    print(f"   Edad: {bambu.get_age()} años")
    print(f"   Energía: {bambu.get_energy()}")
    print(f"   Info completa: {bambu.show_info()}")
    
    print("\n🛠️ USANDO SETTERS (modificar con validación):")
    
    print("\n✅ Cambios válidos:")
    print(f"   {bambu.set_name('Bambú Princesa')}")
    print(f"   {bambu.set_age(3)}")
    print(f"   {bambu.set_energy(80)}")
    print(f"   Resultado: {bambu.show_info()}")
    
    print("\n❌ Intentos de cambios inválidos:")
    print(f"   {bambu.set_name('')}")  # Nombre vacío
    print(f"   {bambu.set_age(-5)}")   # Edad negativa
    print(f"   {bambu.set_age(30)}")   # Edad muy alta
    print(f"   {bambu.set_energy(150)}")  # Energía muy alta
    print(f"   {bambu.set_energy(-10)}")  # Energía negativa
    
    print(f"\n📊 Estado final: {bambu.show_info()}")
    
    print("\n🎯 COMPARACIÓN:")
    print("   🚫 Acceso DIRECTO: bambu._age = -999  (sin validación)")
    print("   ✅ Con SETTER: bambu.set_age(-999)     (con validación)")
    
    print("\n📋 VENTAJAS DE GETTERS Y SETTERS:")
    print("   🛡️ VALIDACIÓN: Solo permite valores válidos")
    print("   🔒 CONTROL: Puedes añadir lógica especial")
    print("   📝 CONSISTENCIA: Formato uniforme de datos")
    print("   🐛 DEPURACIÓN: Más fácil encontrar errores")
