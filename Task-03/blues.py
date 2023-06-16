a = int(input())
for i in range(a):
    n_elements = int(input())
    user_input=input()
    arr = list(map(int, user_input.split()))    
    counter=0

    # print(n)
    # print(arr[n-1])
    while arr and arr[0] == 0:
        arr = arr[1:]
    n=len(arr)
    for i in range(n-1):
        if arr[i]==0:
            arr[i]+=1
            arr[i-1]-=1
            counter+=1
    # print(counter)
    # print(arr)
    sum=0
    for j in range(0,n-1):
        # print(arr[j])
        sum+=arr[j]
    print(sum+counter)