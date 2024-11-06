L = []

print("Ingresa números para agregar a la lista. Dale al ENTER para finalizar")

while True:
    E = input("Ingresa un número: ")
    if E.lower() == "":
        break 
    try:
        N = float(E)
        L.append(N)
    except ValueError:
        print("Por favor, ingresa un número válido.")

L.sort()

print("Lista de números ordenada:", L)