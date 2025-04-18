grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Accessing values using keys
print(grades["Alice"])  # It will show 85 (we access Alice's grade using her name as the key)

# Adding a new key-value pair
grades["David"] = 92  # this adds 'David' as a new key with 92 as the value

print(grades)  # It will show {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}

# Updating an existing value
grades["Bob"] = 95  # this updates Bob's grade from 90 to 95

print(grades)  # It will show {'Alice': 85, 'Bob': 95, 'Charlie': 78, 'David': 92}

# Using keys() to get all the keys in the dictionary
print(grades.keys())  # It will show dict_keys(['Alice', 'Bob', 'Charlie', 'David'])

# Using values() to get all the values in the dictionary
print(grades.values())  # It will show dict_values([85, 95, 78, 92])

# Output

"""
85
{'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}
{'Alice': 85, 'Bob': 95, 'Charlie': 78, 'David': 92}
dict_keys(['Alice', 'Bob', 'Charlie', 'David'])
dict_values([85, 95, 78, 92])
"""
