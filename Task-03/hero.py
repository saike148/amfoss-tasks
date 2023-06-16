cities = int(input())  # Read the number of cities

for _ in range(cities):
    n = int(input())  # Read the number of heroes in the city
    levels = list(map(int, input().split()))  # Read the levels of heroes
    
    zero_count = levels.count(0)  # Count the number of heroes with level zero
    
    if 0 in levels:
        levels.remove(0)  # Remove one occurrence of zero from the list
        print(n - zero_count)  # Print the minimum mana required
    elif len(set(levels)) == n:
        print(n + 1)  # All heroes have the same level, so print n + 1
    else:
        print(n)  # Heroes have different levels, so print the original number of heroes
