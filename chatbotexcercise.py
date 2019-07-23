# --- Define your functions below! ---
def intro():
    print("Welcome!")
def user_name(name):
    print("Hello " +name)
aList = []


# --- Put your main program below! ---
def main():
  while True:
      intro()
      user = input("What's your name? \n")
      user_name(user)
      answer = input("Are you enjoying your day so far? Yes or No?\n")
      if answer==("Yes"):
        print("That's fantastic to hear!\n")
      elif answer == ("No"):
        print("That sucks. Remember everyday is a new day!\n")
      answer1 = input("Do you prefer Chocolate or Vanilla Ice Cream?\n")
      if answer1 == ("Chocolate"):
        print("Yum, great choice!\n")
      elif answer1 == ("Vanilla"):
        print("Yum, great choice!\n")
      answer2 = input("What is your favorite soda to drink? Type 1 for Fanta, 2 for Sprite, 3 for Coke.\n")
      if answer2 == ("1"):
          print("You must have a sweet tooth!\n")
      elif answer2 == ("2"):
          print("oooo who would not like sprite?!!\n")
      elif answer2 == ("3"):
          print("Simple, but the best!\n")
      answer3 = input("How is your summer going? Type 1 for Good! or 2 for Ehhh.\n")
      if answer3 == ("1"):
          print("Nice!\n")
      if answer3 == ("2"):
        print("I hope it gets better!\n")
      answer4 = input("What grade are you going into this year? Type 1 for 11th grade or 2 for 12th grade?\n")
      if answer4 == ("1"):
          print("Only 2 more years of high school, but time will fly!\n")
      if answer4 == ("2"):
          print("You are almost done with high school! So exciting!\n")
      answer5 = input("What is your favorite subject in school? Type 1 for Math, 2 for Science, 3 for PE, 4 for Health or 5 for Language Arts.\n")
      if answer5 == ("1"):
         print("Cool!\n")
         print("You have completed the ChatBot! Congrats!\n")
      if answer5 == ("2"):
         print("Cool!\n")
         print("You have completed the ChatBot! Congrats!\n")
      if answer5 == ("3"):
         print("Cool!\n")
         print("You have completed the ChatBot! Congrats!\n")
      if answer5 == ("4"):
         print("Cool!\n")
         print("You have completed the ChatBot! Congrats!\n")
      if answer5 == ("5"):
          print("Cool!\n")
          print("You have completed the ChatBot! Congrats!\n")
          exit()


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
