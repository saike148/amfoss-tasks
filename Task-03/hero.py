cities = int(input()) 

for _ in range(cities):
    n = int(input())  #no of heroes
    levels = list(map(int, input().split()))  #level of heroes
    zero_count = levels.count(0)  #0 level heroes
    if 0 in levels:
        levels.remove(0)  #remove one zero
        print(n - zero_count)  #minimum
    elif len(set(levels)) == n:
        print(n + 1)
    else:
        print(n)  #diff levels