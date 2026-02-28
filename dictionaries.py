dog = {"name": "zoro", "age": 5, "breed": "labrador"}
print(dog["name"])  # Accessing value using key
dog["age"] = 6  # Modifying value of an existing key
print(dog)
print(dog.get("color", "black"))  # Accessing value using get() method with default value
print(dog.pop("breed"))  # Removing a key-value pair using pop() method
print(dog)
print("color" in dog)  # Checking if a key exists in the dictionary
print(list(dog.items()))  # Getting a list of all keys in the dictionary    