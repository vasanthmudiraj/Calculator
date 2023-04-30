import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("250x300")
        self.master.resizable(True, True)
        
        # create input field
        self.entry = tk.Entry(self.master, width=20, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # create buttons
        buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "C", "0", "=", "/"
        ]
        row = 1
        col = 0
        for button_text in buttons:
            if col == 4:
                row += 1
                col = 0
            button = tk.Button(self.master, text=button_text, width=4, height=2, font=('Arial', 12),command=lambda text=button_text: self.click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
    
    def click(self, text):
        if text == "C":
            self.entry.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, text)

root = tk.Tk()
app = Calculator(root)
root.mainloop()
