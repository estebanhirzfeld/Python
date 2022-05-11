def recortar(number, min, max):
    if number < min:
        return min
    if number > max:
        return max
    return number

print(recortar(5,0,10))
