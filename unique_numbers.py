x = [1, 4, 7, 6, 6, 2, 8, 12, 4]
unique_x = []

for i_elem in x:
    if i_elem not in unique_x:
        unique_x.append(i_elem)

print(x, unique_x, sep='\n')
