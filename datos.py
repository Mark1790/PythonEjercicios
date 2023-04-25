# Solicitar información personal
nombre = input("Por favor, ingresa tu nombre completo: ")

# Verificar si el nombre ingresado contiene solo letras y espacios
while not nombre.replace(' ', '').isalpha():
    nombre = input("Por favor, ingresa un nombre válido (solo letras y espacios): ")

# Solicitar información adicional
edad = input("Por favor, ingresa tu edad: ")
telefono = input("Por favor, ingresa tu número de teléfono: ")
correo = input("Por favor, ingresa tu correo electrónico: ")

# Imprimir resumen de la información ingresada
print("\nResumen de la información ingresada:")
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Teléfono: ", telefono)
print("Correo electrónico: ", correo)

