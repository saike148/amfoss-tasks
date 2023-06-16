a = int(input())
i = 0
while a>9:
    temp=0
    while a>0:
        temp+=a%10
        a//=10
    a=temp
    i+=1
print(i)
