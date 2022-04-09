# Input Notas
nota_1 = input("Ingrese Primera nota: ")
nota_2 = input("Ingrese Segunda nota: ")

# Asignacion de porcentaje del valor final
nota_1 = float(nota_1) * 60 / 100
nota_2 = float(nota_2) * 40 / 100

# Suma de las notas
nota_final = (float(nota_1) + float(nota_2))

# Imprimir nota final
print("Nota final: ", float(round(nota_final, 2)))