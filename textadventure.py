print("start")
print("Deep in the woods, there is a castle. In that castle , you are fighting against a powerful, fire-breathing dragon. With all your might, you dodge the balls of fire shot at you from the dragon's mouth, with your sword.")
answer = input("Press 1, continue to defend yourself or 2, look for an escape. Along the way, you will need to find a door that leads you out of the castle.")
if answer == "1":
    answer2 = str(input("Right Door or Left Door? Be careful which door you choose! One can lead you to your death trap and one can save you...\n press to continue"))
    print("Good choice! The right door leads to outside of the castle.")
elif answer == "2":
    answer2= str(input("You lead yourself into the dragon's dungeon!\n press to continue"))
    print("Find a way to escape before the dragon catches you in there!!")
answer = input("Now your job is to quickly make your escape. Type 1 for a temporary blinding potion that will blind the dragon to make your escape or Type 2 for a plastic toy to throw at the dragon as a distraction.")
if answer == "1":
    answer3 = str(input("You chose the temporary blinding potion! Now on your back left pocket, open the cap of the potion and throw it at the dragon! But, Hurry!!!!"))
    print("The dragon is blinded by the potion and you begin to run away.\n press enter to continue")
elif answer == "2":
    answer4 = str(input("Wave the toy around the dragon's face.\n press to continue"))
    print("The dragon becomes distracted and you throw it at the creature. This is your chance to look for an exit!")
answer=input("You have escaped the dragon! As you are running out the castle, you encounter two paths that lead back to the village. Press 1, save a princess from being held captive by a troll and find love or Press 2 to swim with the sharks and risk your life again.")
if answer == "2":
    answer5= str(input("Jump into the water and swim, swim, swim like your life depends on it. Beware, these sharks BITE!!!!!! \n press to continue"))
    print("You swim, swim, and swim like your life depends on it!")
    print("You managed to stay alive! Congratulations!\n press to continue")
elif answer == "1":
    answer6= str(input("You walk towards the troll and the princess with your sword in your hand before threatening the troll to stay away from your love. \n press enter to continue"))
    print("You save her and you guys live happily every after!")
    print("Goodbye!")
    exit()
