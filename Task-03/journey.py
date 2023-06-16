# Sample Input 0

# 4
# 3
# 0 1 2
# 1
# 0 3 2
# 2
# 3 1 0
# 2
# 1 3 0
# Sample Output 0

# YES
# NO
# YES
# NO

#specify the number of testcases
testcases = int(input())

for i in range(testcases):
    #specify the key to the 1st portal
    p1 = int(input())

    #specify the key to three portals
    keys = input().split()
    a = int(keys[p1-1])
    if a != 0 :
        b = int(keys[a-1])
        if b != 0:
            c = int(keys[b-1])
            if c == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")