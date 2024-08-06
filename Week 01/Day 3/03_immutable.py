# Immutability: Strings cannot be changed, any operation returns a new string
original = "Hello"
modified = original.replace("H", "J")
print(original)  # Output: "Hello"
print(modified)  # Output: "Jello"