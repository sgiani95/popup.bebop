import re
from periodictable import core

# Create a function to get all element symbols
def get_element_symbols():
    # Fetch all element symbols from the periodic table using core.Element
    return [element.symbol for element in core.Element]

# Function to find permutations of valid atom symbols
def find_element_permutations(string):
    element_symbols = get_element_symbols()
    results = []
    
    # Helper function to recursively generate permutations
    def find_matches(start, current_permutation):
        if start == len(string):
            results.append(current_permutation)
            return
        
        # Try both 1-character and 2-character symbols (since element symbols can be 1 or 2 letters)
        for length in [1, 2]:
            if start + length <= len(string):
                symbol = string[start:start + length]
                if symbol in element_symbols:
                    find_matches(start + length, current_permutation + [symbol])
    
    # Start the recursive function
    find_matches(0, [])
    
    return results

# Example usage
input_string = "Breaking Bad"
permutations = find_element_permutations(input_string)

# Display the results
for perm in permutations:
    print(" + ".join(perm))
