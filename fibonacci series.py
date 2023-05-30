num=int(input("Prompt:"))

fibo1=0
fibo2=1
print(fibo1)
print(fibo2)
for i in range(2,num):
    next_fibo = fibo1 + fibo2
    fibo1=fibo2
    fibo2=next_fibo
    print(next_fibo)

