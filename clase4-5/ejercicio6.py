numbers_container1 = []
numbers_container2 = []
numbers_container3 = []
numbers_container4 = []
numbers_container5 = []

# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
for i in range(11):
    numbers_container1.append(i)
print(numbers_container1, "\n")

# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
for i in range(11):
    numbers_container2.append(i * -1)

numbers_container2.reverse()
print(numbers_container2, "\n")

# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
for i in range(21):
    numbers_container3.append(i)

print(numbers_container3, "\n")

# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
for i in range(21):
    if(i % 2 == 1):
        numbers_container4.append(i * -1)
numbers_container4.reverse()
print(numbers_container4, "\n")

# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
for i in range(51):
    if(i % 5 == 0):
        numbers_container5.append(i)

print(numbers_container5, "\n")