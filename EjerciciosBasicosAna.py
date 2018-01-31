#### Ejercicio 1 ####
print("Hola Mundo")
print("\n")

#### Ejercicio 2 ####
num1 = 134
num2 = 431
print('La suma es:', num1 + num2)
print("\n")

#### Ejercicio 3 ####
precioProducto = 100
precioIva = 21
precioTotal = precioProducto * precioIva / 100
print("Precio total del producto con IVA: " + str(precioTotal + precioProducto), "euros")
print("\n")

#### Ejercicio 4 ####
a = "Hola"
b = "mundo"
c = 87
d = 2.33145

# a)
print('"', a, b, '"')
# sin comillas
print(a, b)
print("\n")
# b)
print('"-' + a + "-" + b + '-"')
# sin comillas
print("-" + a + "-" + b + "-")
print("\n")

# c)
print('"C:\\Users\\' + b + '.exe"')
# sin comillas
print("C:\\Users\\" + b + ".exe")
print("\n")

# d)
print('"El resultado es: ' + str(c) + '"')
# sin comillas
print("El resultado es: " + str(c))
print("\n")

# e)
print('"El resultado es: ' + str(c) + 'min( ' + str(c * 60) + ' seg)' + '"')
# sin comillas
print("El resultado es: " + str(c) + " min(" + str(c * 60) + "seg)")
print("\n")

# f)
print('"'"La temepratura es: " + str(round(d, 1)) + '"')
# sin comillas
print("La temperatura es: " + str(round(d, 1)))
print("\n")

####Ejercicio 5####
palabra = input("Indique la frase para dar la vuelta: ")
print(''.join(reversed(palabra)))

input("Pulse intro para salir")
    
    

