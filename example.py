#name = input("What's your name? \n")
#print("Hello, "+name+"!")
done=True
#number = 5.00
#print(done)
#print(type(done))
#print(type(number))
#def arewedone():
    #if done == True:
        #print("we finished")
    #else:
        #print("not finished")

#count = 0
#while done == False:
    #arewedone()
    #print("infinite loop")
    #count +=1
    #if count > 5:
        #done = True
        #print("i'm free")
#for i in range (1,5):
    #print(i)

number = "10"
tries = 3
while tries>0:
    first = input("From numbers 10-20, what is your guess?")
    if (first == number):
        print("You are correct!")
        tries +=1
    else:
        second = input("Two more tries. Again, from numbers 10-20, what is your guess?")
        tries -=1
    if (second == number):
        print("You are correct!")
        tries -=1
    else:
        third = input("Last chance. From numbers 10-20, what is your guess?")
        tries -=1
    if (third == number):
        print("You are correct! Bye.")
        tries -=1
    else:
        third = input("Maybe next time!")
        tries -=1
