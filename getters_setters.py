class Cat:  # Ejemplo de getters y setters
    def __init__(self, name, age):
        self._name = name  # Atributo protegido
        self._age = age    # Atributo protegido
        self._energy = 100 # Atributo protegido
    
    # GETTER - para obtener el valor de un atributo
    def get_name(self):
        """Getter: obtiene el nombre de la gata"""
        return f"🐱 {self._name}"
    
    def get_age(self):
        """Getter: obtiene la edad de la gata"""
        return self._age
    
    def get_energy(self):
        """Getter: obtiene la energía de la gata"""
        return self._energy
    
    # SETTER - para modificar el valor de un atributo con validación
    def set_name(self, new_name):
        """Setter: cambia el nombre con validación"""
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
            return f"✅ Nombre cambiado a: {new_name}"
        else:
            return "❌ Error: El nombre debe ser un texto válido"
    
    def set_age(self, new_age):
        """Setter: cambia la edad con validación"""
        if isinstance(new_age, int) and 0 <= new_age <= 25:
            self._age = new_age
            return f"✅ Edad cambiada a: {new_age} años"
        else:
            return "❌ Error: La edad debe ser entre 0 y 25 años"
    
    def set_energy(self, new_energy):
        """Setter: cambia la energía con validación"""
        if isinstance(new_energy, int) and 0 <= new_energy <= 100:
            self._energy = new_energy
            return f"✅ Energía cambiada a: {new_energy}"
        else:
            return "❌ Error: La energía debe ser entre 0 y 100"
    
    # Método para mostrar información completa
    def show_info(self):
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
