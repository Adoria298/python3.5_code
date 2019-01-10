from isbn_app import *
from tkinter import *
from tkinter.ttk import *

WINTITLE = "CheckGenISBN"

class ISBN_GUI(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.master = master

        self.isbn_mode = IntVar()
        
        self.create_widgets()

    def create_widgets(self):
        # mode
        self.isbn_mode_lbl = Label(self, text="Mode:")
        self.isbn_mode_lbl.grid(column=0, row=0)
        
        self.isbn_mode_radio_10 = Radiobutton(text="10", variable=self.isbn_mode, value=10)
        self.isbn_mode_radio_10.grid(column=1, row=0)

        self.isbn_mode_radio_13 = Radiobutton(text="13", variable=self.isbn_mode, value=13)
        self.isbn_mode_radio_13.grid(column=2, row=0)

        # isbn entry
        self.isbn_lbl = Label(self, text="ISBN:")
        self.isbn_lbl.grid(column=0, row=1)

        self.isbn_entry = Entry(self)
        self.isbn_entry.grid(column=1, row=1, columnspan=2)

        # submit button
        self.submit_btn = Button(self, text="Go!", command=self.gen_isbn)
        self.submit_btn.grid(column=0, row=2)

    def gen_isbn(self):
        if self.isbn_mode.get() == 10:
            gen_func = gen_isbn_10_check_digit
        elif self.isbn_mode.get() == 13:
            gen_func = gen_isbn_13_check_digit

        self.isbn_incomplete = self.isbn_entry.get()
        valid, reason = validate_isbn(self.isbn_incomplete, self.isbn_mode.get())
        if valid:
            self.checksum = str(gen_func(self.isbn_incomplete))
            messagebox.showinfo(WINTITLE, "checksum: " + self.checksum)
        else:
            messagebox.showerror(WINTITLE, "ISBN invalid: " + reason)
        

root = Tk()
root.title(WINTITLE)
main = ISBN_GUI(root)
root.mainloop()
