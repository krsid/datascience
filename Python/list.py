"fetch the Negative and postive number"
# l = [23,-44,89,90,-44,0, 34, -56]

# for i in l:
#     if i >= 0:
#         print(i)

# for i in l:
#     if i<=0:
#         print(i)

"Find the largest number from the list and its indexing"
# l = [23,43,645,26,87,982]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f'Your largest number is {largest} at the index {index}')

"Find the second largest value from the list"

# l = [21,23,43,25,64, 56,]

# largest = l[0]
# sec_lar = l[0]

# for i in l:
#     if i > largest:
#         sec_lar = largest
#         largest = i
#     elif i > sec_lar:
#         sec_lar = i

# print(largest, sec_lar)

"check if the list is sorted or not"

l = [2,3,4,8,6,7]

for i in range(len(l)-1):
    if l[i] < l[i+1]:
        continue
    else:
        print("List is not sorted")
        break
else:
    print("Your list is sorted")
