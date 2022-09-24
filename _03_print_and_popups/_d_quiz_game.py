from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    win = Tk()
    # Hide the window using the window's .withdraw() method
    win.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    q1 = simpledialog.askstring(title= "Q1", prompt= "What is your name, Joe?")
    #      // 2.  Ask the user a question 
    if q1 == "Joe":
    #      // 3.  Use an if statement to check if their answer is correct
        print("Hardly a difficult question.")
        str(score + 1)
    #      // 4.  if the user's answer was correct, add one to their score
    else:
        print("Whatever you say, Joe.")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    print("Anyway, Joe, we'll be starting soon.")
    q2 = simpledialog.askstring(title="Q2", prompt="Let's start with something easy. What's 43 times 13?")
    if q2 == "559":
        print("You searched up the answer, didn't you? Fail.")
        str(score + 1)
    else:
        print("I'm disappointed in you. You can't even do simple multiplication. Fail.")


    # Run the window's .mainloop() method
    print("Final score: Fail")
    win.mainloop()
