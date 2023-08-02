

x = 1
y = 1
z = 1
n = 2

list_xyz = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ]

# for i in list_xyz: 
#     if i[0]+i[1]+i[2] == n:
#         list_xyz.remove(i)

print(list_xyz)