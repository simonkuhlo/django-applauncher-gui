import tkinter as tk

window = tk.Tk(screenName="Basic GUI", baseName="Basic GUI 2", className="Basic GUI 3")
greeting = tk.Label(text="\n-----------------\n  |  Hi, this is a very basic GUI-Window.  |  \n-----------------\n")
greeting.pack()


if __name__ == "__main__":
    window.mainloop()