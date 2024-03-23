list = [1,2,3,4,5]
lis2 = []
for c in range(len(list)-1,-1,-1):
    lis2.append(list[c])
    print(list[c])
print(lis2)
#print(len(list)-1)
#for c in range(5-1,-1,-1):
#    print(list[c])