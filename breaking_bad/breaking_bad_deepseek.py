import tkinter as tk
from tkinter import messagebox
import periodictable

# Dictionary mapping letters to chemical elements
element_symbols = {
    'A': 'Al', 'B': 'Br', 'C': 'C', 'D': 'Dy', 'E': 'Es', 'F': 'F', 'G': 'Ge',
    'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'Li', 'M': 'Mn', 'N': 'N',
    'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'Ra', 'S': 'S', 'T': 'Ti', 'U': 'U',
    'V': 'V', 'W': 'W', 'X': 'Xe', 'Y': 'Y', 'Z': 'Zn'
}

# List of all valid chemical symbols
valid_symbols = set(element_symbols.values())

# Function to generate all possible splits of the input text
def generate_combinations(text):
    if not text:
        return [[]]
    combinations = []
    # Try 2-letter symbols first
    if len(text) >= 2:
        symbol = text[:2].title()
        if symbol in valid_symbols:
            for rest in generate_combinations(text[2:]):
                combinations.append([symbol] + rest)
    # Try 1-letter symbols
    symbol = text[0].upper()
    if symbol in valid_symbols:
        for rest in generate_combinations(text[1:]):
            combinations.append([symbol] + rest)
    # If no valid symbols, treat the character as-is
    if not combinations:
        combinations.append([text[0]])
        for rest in generate_combinations(text[1:]):
            combinations.append([text[0]] + rest)
    return combinations

# Function to find the best combination
def find_best_combination(text):
    combinations = generate_combinations(text)
    if not combinations:
        return list(text)  # Fallback: return individual characters
    # Prioritize combinations with the most elements
    best = max(combinations, key=lambda x: len(x))
    # If there's a tie, prioritize longer symbols
    best = max(combinations, key=lambda x: (len(x), sum(len(s) for s in x)))
    return best

# Function to convert text to chemical symbols (advanced)
def text_to_elements_advanced(text):
    return ' '.join(find_best_combination(text))

# Function to get element details
def get_element_details(symbol):
    try:
        element = periodictable.elements.symbol(symbol)
        return f"Element: {element.name}\nAtomic Number: {element.number}\nAtomic Mass: {element.mass}"
    except:
        return f"No data found for {symbol}"

# GUI Application
class BreakingBadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Breaking Bad Logo Generator")
        self.root.geometry("400x300")

        # Label
        self.label = tk.Label(root, text="Enter Text:", font=("Arial", 14))
        self.label.pack(pady=10)

        # Text Entry
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10)

        # Convert Button
        self.convert_button = tk.Button(root, text="Convert to Elements", command=self.convert_text)
        self.convert_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Courier", 16), fg="green")
        self.result_label.pack(pady=20)

        # Details Button
        self.details_button = tk.Button(root, text="Show Element Details", command=self.show_details)
        self.details_button.pack(pady=10)

    # Function to convert text and display result
    def convert_text(self):
        input_text = self.entry.get()
        if not input_text:
            messagebox.showwarning("Input Error", "Please enter some text!")
            return
        output = text_to_elements_advanced(input_text)
        self.result_label.config(text=output)

    # Function to show element details
    def show_details(self):
        result_text = self.result_label.cget("text")
        if not result_text:
            messagebox.showwarning("Error", "No conversion result to analyze!")
            return
        symbols = result_text.split()
        details = ""
        for symbol in symbols:
            if symbol in valid_symbols:
                details += get_element_details(symbol) + "\n\n"
        if details:
            messagebox.showinfo("Element Details", details)
        else:
            messagebox.showinfo("Element Details", "No valid elements found!")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BreakingBadApp(root)
    root.mainloop()