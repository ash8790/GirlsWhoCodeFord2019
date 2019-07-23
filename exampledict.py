f = open("dictionary.txt","r")
print("Let me ask you something!")
print("Can your password survive a dictionary attack?\n")

test_passwords = input("Please type in a trial password: ").strip()
dictionary = [line.rstrip('\n') for line in f]

while True:
    if test_passwords in dictionary:
        print("Not a good sign. You should start changing your password now...")
        break
    elif test_passwords not in dictionary:
        print("Wooooh, what a relief! You are safe! Yayay!!")
        break

if len(test_passwords) < 10:
    print("You should have typed a longer password. Try again!")
else:
    print("You got it! A sufficent amount of letters to keep your password private.")
