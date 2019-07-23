f = open("dictionary.txt","r")
print("Let me ask you something!")
print("Can your password survive a dictionary attack?\n")
test_passwords = input("Please type in a trial password: ").strip()
lineList= [line.rstrip('\n') for line in f]

def init(test_passwords):
    if test_passwords in lineList:
        return False
    elif test_passwords not in lineList:
        return True

result = init(test_passwords)

if result == False:
    print("You are at risk!")
elif result == True:
    print("You are safe!")
