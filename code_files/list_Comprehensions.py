#List Comprehensions
#Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# Using Loops
# final_list = []
# for i in range(0,x+1):
#     for j in range (0,y+1):
#         for k in range (0,z+1):
#             if i+j+k < n:
#                 final_list.append([i,j,k])
# print(final_list)

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) != n])