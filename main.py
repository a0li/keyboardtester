import tkinter as tk
from tkinter import messagebox

def newfunction(keysinput):
    allkeys = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", '#', '\\', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
    keys = keysinput
    l = list(keys)
    actualkeylength = 0
    for l in l:
        for c in allkeys:
            if c == l:
                actualkeylength = actualkeylength + 1
                del allkeys[allkeys.index(c)]

    keysworking = (str(int(((actualkeylength / 48) * 100))) + "%")
    keysnotworking = str(100-(int(((actualkeylength / 48) * 100)))) + "%"
    if actualkeylength == 48:
        keysnotpressed = ("All keys pressed!")
    else:
        keysnotpressed = ('Keys not pressed: \n',*allkeys)
    return keysworking, keysnotworking, keysnotpressed


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("360x130")
        self.label = tk.Label(self, text="48 typable characters on a keyboard. \n Check that all the keys on your keyboard work. \n Will return the keys which have not been pressed.")
        self.label.pack()
        self.label2 = tk.Label(self, text="Enter keys")
        self.label2.pack()
        self.entry = tk.Entry(self, width="55")
        self.entry.pack()

        self.button = tk.Button(self, text="Test", command=self.on_button, width="23")
        self.button.pack()

        self.title("Keyboard Checker")

    def on_button(self):
        keysinput = self.entry.get()
        result = newfunction(keysinput)

        messagebox_info = (
            "Percent of keys working: {}\n"
            "Percent of keys NOT working: {}\n"
            "{}").format(
            result[0], result[1], result[2])

        msg = messagebox.showinfo("Result", messagebox_info)

app = GUI()
app.resizable(False, False)
app.mainloop()