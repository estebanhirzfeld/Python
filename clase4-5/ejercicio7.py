list_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
list_2 = ["h",'o','l','a',' ', 'l','u','n','a']

container_1 = []
container_2 = []

for char in list_1:
    if (char in list_2):
        container_1.append(char)

for char in container_1:
    if char not in container_2:
        container_2.append(char)

print(container_2)


