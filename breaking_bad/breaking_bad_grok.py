import periodictable

# Get all element symbols from periodictable
element_symbols = [str(elem) for elem in periodictable.elements]
# Convert to a set for faster lookup, include both raw and lowercase for flexibility
element_set = set(symbol.lower() for symbol in element_symbols) | set(element_symbols)

def find_element_splits(input_string):
    found_splits = []
    text = input_string.lower()  # Case-insensitive matching
    
    # Check for 2-letter symbols first
    for i in range(len(text) - 1):
        substring = text[i:i+2]
        if substring in element_set:
            element = substring.capitalize()
            # Get atomic number
            atomic_number = periodictable.elements.symbol(element).number
            remainder = input_string[i + len(element):].strip()
            found_splits.append(f"{element}^{atomic_number} | {remainder}")
    
    # Check for 1-letter symbols, avoiding overlaps with 2-letter ones
    for i in range(len(text)):
        substring = text[i:i+1]
        if substring in element_set:
            # Check if this position is part of a 2-letter element already found
            is_overlap = any(i >= split[0] and i < split[0] + 2 for split in [(s.index('|') - len(s.split('|')[0].strip()), s) for s in found_splits])
            if not is_overlap:
                element = substring.capitalize()
                # Get atomic number
                atomic_number = periodictable.elements.symbol(element).number
                remainder = input_string[i + len(element):].strip()
                found_splits.append(f"{element}^{atomic_number} | {remainder}")
    
    return found_splits

# Test with "Breaking Bad"
input_string = "Chemical Safety"
splits = find_element_splits(input_string)
print(f"Input string: {input_string}")
print("Element splits found:")
for split in sorted(splits):  # Sort for consistent output
    print(split)
print(f"Number of distinct splits: {len(splits)}")