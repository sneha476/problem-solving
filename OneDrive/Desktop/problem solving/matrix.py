l1=[[1,2],[3,4]]
l2=[[3,4],[2,1]]
l3=[]
# for i in range(len(l1)):
#     l=[]
#     for j in range(len(l1[i])):
#             mul=(l1[i]*l2[j])+(l1[i]*l2[j])
#             l.append(mul)
#     l3.append(l)
# print(l3)
# for i in range(len(l3)):
#     for j in range(len(l3[i])):
#         print(l3[i][j],end="  ")
#     print()
for i in range(len(l1)):
    l=[]
    for j in range(len(l1[i])):
        add=0
        for k in range(len(l1[i])):
            add=add+(l1[i][k]*l2[k][j])
        l.append(add)
    l3.append(l)
print(l3)


