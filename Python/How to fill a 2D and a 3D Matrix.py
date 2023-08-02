


x = 1
y = 1
z = 1


list_x = [x for x in range(x+1)]
list_y = [y for y in range(y+1)]
list_z = [z for z in range(z+1)]


# #here's how a 2D matrix is populated:

# final = []

# for i in list_x:
#     temp = []
    
#     for j in list_y:
#         temp.append([i,j])
        
    
#     final.append(temp)

# for i in final:
#     print(i)


#Let's try with a 3D:

final = []

for i in list_x:
    temp = []
    
    for j in list_y:

        for k in list_z:

            temp.append([i,j,k])
        
    
    final.append(temp)

for i in final:
    print(i)