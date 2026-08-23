"Count of occurance of each elements in the list"
# a = [3,3,3,2,2,2,5,5,5,4,4,1,1,1,6]

# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)

"add the values of common elements in two dictory"

d1 = {1:10,2:20,3:30,4:40}
d2 = {4:50,6:60,1:70,8:80}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)

