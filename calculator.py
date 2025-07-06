import tkinter as tk

expression = ""

def press(value):
    global expression
    expression += str(value)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression.replace("×", "*").replace("÷", "/")))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def key_event(event):
    key = event.char
    if key in "0123456789.+-*/":
        press(key)
    elif key == "\r":  # Enter
        equal()
    elif key == "\x08":  # Backspace
        backspace()

# Main window
root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("330x520")  # Increased height
root.configure(bg="#1e1e1e")
root.resizable(False, False)
root.bind("<Key>", key_event)

input_text = tk.StringVar()

# Entry field
entry = tk.Entry(
    root, textvariable=input_text, font=('Arial', 24),
    bd=6, relief='ridge', justify='right', bg="#2b2b2b", fg="white"
)
entry.pack(fill='both', ipady=10, padx=10, pady=10)

# Buttons layout
buttons = [
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C', '⌫', '', '']
]

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(expand=True, fill='both', padx=10, pady=(0, 10))

def create_button(text, row, col):
    if not text:
        return
    if text == '=':
        command = equal
        bg, fg = "#00adb5", "white"
    elif text == 'C':
        command = clear
        bg, fg = "#ff5722", "white"
    elif text == '⌫':
        command = backspace
        bg, fg = "#607d8b", "white"
    else:
        command = lambda x=text: press(x)
        bg, fg = "#333333", "#ffffff"

    btn = tk.Button(
        btn_frame, text=text, command=command,
        font=('Arial', 18), bd=0, bg=bg, fg=fg,
        activebackground="#555"
    )
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Add buttons and configure grid
for i, row in enumerate(buttons):
    btn_frame.grid_rowconfigure(i, weight=1)
    for j, text in enumerate(row):
        btn_frame.grid_columnconfigure(j, weight=1)
        create_button(text, i, j)

root.mainloop()
