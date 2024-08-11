# Create the dictionary
emp= {
    "id": 1,
    "name": "John",
    "designation": "Developer",
    "salary": 8000
}

print("Original dictionary:")
print(emp)

# Delete the designation key
del emp["designation"]

print("\nDictionary after deleting designation key:")
print(emp)

# Update the name
emp["name"] = "Jane"

print("\nDictionary after updating name:")
print(emp)