# Definir variables de diferentes tipos primitivos
entero = 42
flotante = 3.1416
cadena = "Hola, soy una cadena"
booleano = True

# Concatenar la cadena con otras variables (convirtiendo si es necesario)
resultado_concatenacion = cadena + " " + str(entero) + " " + str(flotante) + " " + str(booleano)

# Límites de los enteros y flotantes en Python 
"""
En Python, el límite de los enteros depende de la plataforma en la que se ejecute. En general, los enteros en Python 3 son de precisión ilimitada, lo que significa que pueden ser tan grandes como la memoria de la máquina lo permita. Sin embargo, en la práctica, el límite se establece por la cantidad de memoria disponible.

Para los flotantes en Python, se utilizan estándares IEEE 754 de 64 bits para representar números de punto flotante. El límite superior para los números de punto flotante en Python se encuentra alrededor de 1.8 x 10^308 y el límite inferior es aproximadamente -1.8 x 10^308. Más allá de estos valores, los números se representarán como "infinito" (inf) o "negativo infinito" (-inf).

Es importante tener en cuenta que debido a limitaciones de precisión en los números de punto flotante, pueden ocurrir errores de redondeo en cálculos muy grandes o muy pequeños.
"""

# Fórmula para la suma de los primeros n números pares
n = int(input("Ingrese un número entero para n: "))  # Solicitar al usuario un valor para n
suma_pares = n * (n + 1)  # Fórmula para la suma de los primeros n números pares

# Mostrar el resultado
print("Resultado de la concatenación:", resultado_concatenacion)
print("Resultado de la suma de los primeros", n, "números pares:", suma_pares)
