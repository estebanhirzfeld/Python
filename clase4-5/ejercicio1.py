number_1 = int(input("Ingrese primer numero: "))
number_2 = int(input("Ingrese segundo numero: "))

print(
    "\n"
    "1. Suma\n"
    "2. Resta\n"
    "3. Multiplicacion\n"
    "4. Division\n"
    "5. Salir\n"
)

option = int(input("Ingrese la operacion que desea realizar: "))

if (option == 1):
    print("(SUMA) El resultado es:", number_1 + number_2)
elif (option == 2):
    print("(RESTA) El resultado es:", number_1 - number_2)
elif (option == 3):
    print("(MULTIPLICACION) El resultado es:", number_1 * number_2)
elif (option == 4):
    print("(DIVISION) El resultado es:", number_1 / number_2)
else:
    print("Opcion invalida")

