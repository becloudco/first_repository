def multiplicar(numero: int) -> str:
    if numero < 1:
        return "el numero debe estar entre 1 y 10"
    elif numero >= 1 and numero <=10:
        return f"El numero digitado es {numero} "
    return "Error final"

print(multiplicar(3))