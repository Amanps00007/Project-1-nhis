import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x400")
        
        self.equation = ""
        self.input_text = tk.StringVar()

        
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        self.entry = tk.Entry(self.input_frame, textvar=self.input_text, font=('Verdana', 20), width=20, bd=5, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, ipadx=8, ipady=8)
        self.entry.pack()

    
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]

        for row_index, row in enumerate(buttons):
            for col_index, char in enumerate(row):
                btn = tk.Button(self.buttons_frame, text=char, font=('Verdana', 14), width=6, height=2,
                                command=lambda ch=char: self.on_button_click(ch))
                btn.grid(row=row_index, column=col_index, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.equation = ""
        elif char == '=':
            try:
                self.equation = str(eval(self.equation))
            except:
                self.equation = "Error"
        else:
            self.equation += char
 
        self.input_text.set(self.equation)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()