import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.notes = []
    
    def create_widgets(self):
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.message = tk.Label(self.master, text=' TODO ' ,font='none 18', bg='dark slate blue').pack(side=tk.TOP, padx=5, pady=5  , fill=tk.BOTH )

        self.input_msg = tk.Label(self.master, text=' Text Input ', font='none 14', bg='slate blue').pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)

        self.text_input = tk.Entry(self.master, font='none 12 bold', bg='azure3')

        self.text_input.pack(side=tk.TOP, padx=5 , pady= 5 , ipady=3 , fill=tk.BOTH)
        self.text_input.focus()
        
        self.btn = tk.Button(self.master, text=' Add Note ', font='none 12', command=self.on_click , bg='royal blue').pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)

        self.note_msg = tk.Label(self.master, text=' Items ' ,font='none 18', bg='dark slate blue').pack(side=tk.TOP, padx=5, pady=5  , fill=tk.BOTH)

        self.note_table = tk.Listbox(self.master, font='none 12 bold' , height=20, width=35, bg='sky blue1')
        self.note_table.pack(side=tk.TOP, padx=5, pady=5  , fill=tk.BOTH)
        self.note_table.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.note_table.yview)

        self.btn = tk.Button(self.master, text=' Clear Notes ', font='none 14', command=self.clear , bg='brown1' , fg='white')
        self.btn.pack(side=tk.BOTTOM, padx=5, pady=5  , fill=tk.BOTH)
    
    def on_click(self):
        self.text = self.text_input.get()
        if len(self.text) > 0:
            self.note_table.delete(0, tk.END)
            self.notes.append(self.text)
            for i, n in enumerate(self.notes):
                self.note_table.insert(i, f'{i + 1} : {n}')
        else:
            self.note_table.delete(0, tk.END)
            self.note_table.insert(0, 'Please Enter Some Text')
    
    def clear(self):
        self.notes = []
        self.note_table.delete(0, tk.END)



def main():
    root = tk.Tk()
    root.title('Simple TODO App')
    app = App(master=root)
    app.master.iconbitmap('todo.ico')
    app.mainloop()

if __name__=='__main__':
    main()
