def clasificar_edad():
    try:
        edad = int(input("Ingrese su edad: "))
        
        if edad < 0:
            print("La edad no puede ser negativa.")
        elif edad <= 12:
            print("Eres un infante.")
        elif edad <= 18:
            print("Eres un adolescente.")
        elif edad <= 45:
            print("Eres un mayor joven.")
        elif edad <= 100:
            print("Eres un anciano.")
        else:
            print("¿En serio tienes esa edad?")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Ejecutar la función
clasificar_edad()