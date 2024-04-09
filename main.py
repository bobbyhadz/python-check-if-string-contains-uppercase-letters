# Check if a string contains any Uppercase letters in Python

my_str = 'Bobby'

contains_uppercase = any(char.isupper() for char in my_str)
print(contains_uppercase)  # 👉️ True

if contains_uppercase:
    # 👇️ this runs
    print('The string contains uppercase letters')
else:
    print('The string does NOT contain any uppercase letters')

# --------------------------------------------------

# ✅ Extract the uppercase letters from a string
my_str = 'BOBBYhadz123'

only_upper = ''.join(char for char in my_str if char.isupper())
print(only_upper)  # 👉️ BOBBY

only_upper = [char for char in my_str if char.isupper()]
print(only_upper)  # 👉️ ['B', 'O', 'B', 'B', 'Y']
