numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def odd_even_check(list):
    even_list = []
    odd_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print('Numeros:', list, '\n')
    print('Pares:', even_list)
    print('Impares:', odd_list)


odd_even_check(numbers)
