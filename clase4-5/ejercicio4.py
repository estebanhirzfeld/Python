number_container = []
number_range =  int(input("ingrese cuantos numeros desea ingresar: "))

for i in range(number_range):
    input_number = int(input("Ingrese numero: "))
    number_container.append(input_number)

result = sum(number_container) / len(number_container)

print("suma aritmetica:", result)