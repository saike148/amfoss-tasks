# Sample Input 0

# 3 2
# expecto defend
# patronum incantation
# expecto patronum expecto
# Sample Output 0

# defend patronum defend


# Get the number of comparisons
m, n = map(int, input().split())

# Create a dictionary for mapping
mappings = {}

# Get word and mapping and store it in a dictionary
for i in range(n):
    mm, nn = input().split()
    mappings[mm] = nn

new_dict = {}
for key, value in mappings.items():
    if len(key) <= len(value):
        new_dict[key] = key
        new_dict[value] = key
    else:
        new_dict[key] = value
        new_dict[value] = value

# Get the space-separated strings
final_spell = input().split()

# Replace the input strings with values from new_dict
for i in range(m):
    if final_spell[i] in new_dict:
        final_spell[i] = new_dict[final_spell[i]]

# Print the updated strings
print(' '.join(final_spell))
