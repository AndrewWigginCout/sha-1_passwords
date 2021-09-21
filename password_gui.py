def main():
    def click():
        ui=I.get(1.0,tk.END)
        if len(ui)>0: ui=ui[0:-1]
        O.delete(1.0,tk.END)
        O.insert(tk.END,make(ui))
    import tkinter as tk
    import tkinter.scrolledtext as scrolledtext
    root=tk.Tk()
    root.geometry("600x400")
    root.title("Alex's password maker")
    font=('consolas',16)
    
    I=tk.scrolledtext.ScrolledText(root,height=4,width=50)
    I['font'] = font
    I.pack(expand=True,fill="both")
    
    button=tk.Button(root,text="Hash", command=click, font=font, height=3, width=50)
    button.pack()
    
    O=scrolledtext.ScrolledText(root)
    O['font'] = font
    O.pack(expand=True,fill="both")
    
    
    root.mainloop()

from sha1password import make
if __name__ == '__main__':
    main()
