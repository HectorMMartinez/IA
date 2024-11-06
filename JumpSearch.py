def buscar_numero(A, T):
    izquierda = 0
    derecha = len(A) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if A[medio] == T:
            return medio  
        elif A[medio] < T:
            izquierda = medio + 1  
        else:
            derecha = medio - 1  
    return "unsuccessful"
entrada_lista = input("Ingresa una lista de números ordenada (separados por espacios): ")
A = list(map(int, entrada_lista.split()))
T = int(input("Ingresa el número que deseas buscar: "))
resultado = buscar_numero(A, T) + 1
print("Posición:", resultado if resultado != "unsuccessful" else "unsuccessful")
