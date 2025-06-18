import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#2D2929")

# Create Entry widget for display
display = tk.Entry(root,
            font=("Arial", 24),
            borderwidth=3,
            relief="ridge",
            justify="right",
            fg = 'white',
            bg="#201E1E",
            insertbackground="white"
        )
display.pack(padx=10, pady=20, fill='both')

btns_frame = tk.Frame(root, bg="#201E1E")
btns_frame.pack()

# Button style
btn_config = {
    "font": ("Arial", 18),
    "bg": "#333333",  # dark gray buttons
    "fg": "white",
    "width": 5,
    "height": 2,
    "bd": 0,
    "highlightthickness": 0
}

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]
# Create buttons in grid
def on_button_click(symbol):
    if symbol == "C":
        display.delete(0, tk.END)  # Clear display
    elif symbol == "=":
        try:
            result = eval(display.get())  # Evaluate expression
            display.delete(0, tk.END)
            display.insert(0, str(result))  # Show result
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, symbol)  # Add symbol to display

for row_index, row in enumerate(buttons):
    for col_index, symbol in enumerate(row):
        btn = tk.Button(btns_frame, text=symbol, command=lambda s=symbol: on_button_click(s), **btn_config)
        btn.grid(row=row_index, column=col_index, padx=5, pady=5)


# Run the app
root.mainloop()
