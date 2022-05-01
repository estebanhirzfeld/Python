allowed_numbers = numeros = [1, 3, 6, 9]

while True:
    input_number = int(input("Ingrese un numero entero del 0 al 9: "))

    if(input_number > 9 or input_number < 0):
        print("Numero invalido, intente nuevamente")

    elif(input_number in allowed_numbers):
        print("El numero es valido y fue encontrado en la lista")
        break
    
    elif(input_number not in allowed_numbers):
        print("El numero es valido, pero no fue encontrado en la lista")
        break

