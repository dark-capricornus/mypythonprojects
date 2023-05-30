num=int(input("Enter a value:"))
sum=0
for i in range(1,num):
    if i %3 ==0 or i%5 == 0:
        sum += i

print(sum)
