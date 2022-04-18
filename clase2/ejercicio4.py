
matriz = [  
    [1, 5, 1], 
    [2, 1, 2], 
    [3, 0, 1], 
    [1, 4, 4] 
] 

matriz_1 = matriz[slice(0, 1)][0] 
matriz_1 = matriz_1.append(sum(matriz[0])) 

matriz_2 = matriz[slice(1, 2)][0] 
matriz_2 = matriz_2.append(sum(matriz[1])) 

matriz_3 = matriz[slice(2, 3)][0] 
matriz_3 = matriz_3.append(sum(matriz[2])) 

matriz_4 = matriz[slice(3, 4)][0] 
matriz_4 = matriz_4.append(sum(matriz[3])) 

for array in matriz:
    print(array)