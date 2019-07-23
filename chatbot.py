# --- Define your functions below! ---
def intro():
    print("I AM A ROBOT")
def user_name(name):
    print("hello" +name.upper)

# --- Put your main program below! ---
def main(name):
  while True:
      intro()
      user_name(user)
      user = input("What's your name? \n")
    #answer = input("(What will you say?) ")
    #print("That's cool!")
    break


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
