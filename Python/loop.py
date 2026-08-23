# n = int(input('n: '))

# for i in range(n):
#     print('Hello World')

# for i in range(1,n+1):
#     print(i)

# for i in range(n,0,-1):
#     print(i)

# for i in range(n,n*10+1,n):
#     print(i)


n = int(input('n: '))
# sum = 0
# for i in range(n):
#     sum = sum + i
# print(sum)

# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2==0:
#         even = even +1;
#     else:
#         odd = odd + 1;
# print(f"Your even number is {even} and your odd number is  {odd}")


copy = n
rev = 0 

while n>0:
    rev = rev * 10 + n%10
    n = n//10

if copy == rev:
    print("its a palindromic number")
else:
    print('Not a palindromic number')

