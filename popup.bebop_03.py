import tkinter as tk

def create_mockup_window(window_title, a1_text, a2a4_text, b1_text, b2_text, b3_text):
    # Create the root window
    root = tk.Tk()
    root.title(window_title)  # Set the window title dynamically
    root.geometry("400x200")  # Set the window size

    # Create a main frame to hold everything
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Create two rows of frames (top and bottom)
    top_frame = tk.Frame(main_frame, bg="white")  # Set background color of top_frame to white
    top_frame.pack(fill=tk.BOTH, expand=True)  # Fill the remaining space (top row)
    
    bottom_frame = tk.Frame(main_frame)
    bottom_frame.pack(side=tk.BOTTOM, pady=10)  # Stick to the bottom (bottom row)
    
    # Hardcoding labels for the top row (A1, A2-A4 merged, A5)
    label_A1 = tk.Label(top_frame, text=a1_text, font=("Arial", 25), bg="white")
    label_A1.grid(row=0, column=0, padx=5, sticky="nsew")
    
    # Create a frame for A2, A3, and A4 combined with a white background
    merged_frame_A2_A4 = tk.Frame(top_frame, width=30, height=2, bg="white")
    merged_frame_A2_A4.grid(row=0, column=1, columnspan=3, padx=5, sticky="nsew")  # Span 3 columns
    
    # Add a label inside the merged frame
    merged_label = tk.Label(merged_frame_A2_A4, text=a2a4_text, justify="left", width=30, height=2, bg="white")
    merged_label.pack(fill=tk.BOTH, expand=True)
    
    label_A5 = tk.Label(top_frame, text="", width=10, height=2, bg="white")
    label_A5.grid(row=0, column=4, padx=5, sticky="nsew")

    # Make the grid cells expand (equal size for all columns)
    for i in range(3):
        top_frame.grid_columnconfigure(i, weight=1)  # Ensure equal width for all columns
    
    # Vertically center the A row by configuring rows inside top_frame
    top_frame.grid_rowconfigure(0, weight=1)  # Ensure the row takes up available vertical space

    # Hardcoding buttons for the bottom row (B1, B2, B3)
    def on_button_click(button_name):
        print(f"{button_name} button clicked!")

    # Bottom row buttons with passed text for B1, B2, and B3
    button_B1 = tk.Button(bottom_frame, text=b1_text, underline=0, width=10, height=1, command=lambda: on_button_click("B1"))
    button_B1.grid(row=0, column=0, padx=5)
    
    button_B2 = tk.Button(bottom_frame, text=b2_text, underline=0, width=10, height=1, command=lambda: on_button_click("B2"))
    button_B2.grid(row=0, column=1, padx=5)
    
    button_B3 = tk.Button(bottom_frame, text=b3_text, underline=0, width=10, height=1, command=lambda: on_button_click("B3"))
    button_B3.grid(row=0, column=2, padx=5)

    # Run the application
    root.mainloop()

# Example usage of the function with custom text and window title
# create_mockup_window("#001", " ℹ️", "Press OK to continue...", "Yes", "No", "Cancel")
# create_mockup_window("#2番目", " 絵文字", "ロスト・イン・トランスレーション.", "はい", "いいえ", "キャンセル")


# create_mockup_window("#002", " ⚠️", "Do you accept all conditions?", "Yes", "No", "100 pages")

