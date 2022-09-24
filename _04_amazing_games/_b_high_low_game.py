from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    #8print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        ans = simpledialog.askinteger(title="guess", prompt="Guess a number between 1 and 100.")
        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
        if ans == random_num:
            print("you won")
            sys.exit(0)
        # 7. if the guess is high
        elif ans >= random_num:
            # 8. Tell them it's too high
            print("Too high")
        # 9. Else if the guess is low
        elif ans <= random_num:
            # 10. Tell them it's too low
            print("Too low")
    #11. Outside of the loop, tell the user they lost
    print("You lost")
    window.mainloop()
