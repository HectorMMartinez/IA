#Problema 3
def Romanos(Romano):
    ValoresRomanos={
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000  
    }

    Valor=0
    L=len(Romano)

    for i in range(L):
        if i < L - 1 and ValoresRomanos[Romano[i]] < ValoresRomanos[Romano[i+1]]:
            Valor -= ValoresRomanos[Romano[i]]
        else:
            Valor += ValoresRomanos[Romano[i]]
    return Valor

print("Ingrese un numero romano que quiera decifrar")
Romano=input("Valor romano:")
Valor=Romanos(Romano)
print("Entrada: ",Romano)
print("Salida: ", Valor)
