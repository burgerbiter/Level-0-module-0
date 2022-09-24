from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    win = Tk()
    # Make a new window variable, window = Tk()
    win.withdraw()
    # Hide the window using the window's .withdraw() method
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    rando = random.randInt(0, 3)
    # 2. Print your variable to the console
    print(rando)
    # 3. Get the user to enter something that they think is awesome
    q = simpledialog.askstring(title="Cool", prompt= "What is something you think is awesome?")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if rando == 0:
        print("That's awesome!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    elif rando == 1:
        print("That's alright I guess.")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    elif rando == 2:
        print("That's boring.")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    elif rando == 3:
        print("You do you.")
    # Run the window's .mainloop() method
    win.mainloop()
