# Task 2: List Slicing and Reversing

# 1. Creates a list of numbers from 1 to 10
original_list = list(range(1, 11))
print(f"Original list: {original_list}")

# 2. Extracts the first five elements from the list using slicing
# Syntax: [start:stop]
extracted_elements = original_list[0:5]

# 3. Reverses these extracted elements
# Syntax: [::-1] is a common way to reverse a list
reversed_elements = extracted_elements[::-1]

# 4. Prints both the extracted list and the reversed list
print(f"Extracted first five elements: {extracted_elements}")
print(f"Reversed extracted elements: {reversed_elements}")