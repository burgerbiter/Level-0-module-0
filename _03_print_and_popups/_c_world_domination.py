from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    win = Tk()
    # Hide the window using the window's .withdraw() method
    win.withdraw()
    # 1. Ask the user if they know how to write code.
    q1=simpledialog.askstring(title= "Coding Experience", prompt= "Do you know how to code?")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if q1 == "yes":
        print("You will rule the world one day.")
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    else:
        print("Sign up for classes at The League.")
    # Run the window's .mainloop() method
    win.mainloop()
