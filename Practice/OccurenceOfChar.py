from collections import Counter

def character_occurrences(s):
    return Counter(s)

# Example usage
input_string = "hello world"
result = character_occurrences(input_string)

# Display the result
for char, count in result.items():
    print(f"'{char}': {count}")
