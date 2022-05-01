while True:
    input_number = int(input("Ingrese un numero Impar: "))
    if(input_number % 2 == 0):
        print("El numero ingresado es par, intente nuevamente")
    else:
        print("El numero ingresado es impar, fin del programa")
        break