#This program is a basic inventory manager []
#There's no input control just for the sake of practicing lists

inventory = []

print("Hello adventurer, you will embark on a dangerous mission what items will you choose to bring with you? ")
print("Bear in mind you only have space for three objects")
print("Selection 1: Apple, Banana, Orange")
selection1 = ["Apple", "Banana", "Orange"]
take1 = int(input())
print("You selected " + str(selection1[take1-1]))
print("Seleciton 2: Sword, Spear, Axe")
selection2 = ["Sword","Spear","Axe"]
take2 = int(input())
print("You selected " + str(selection2[take2-1]))
print("Selection 3: Heavy armor, Light armor, Mage armor")
selection3 = ["Heavy armor", "Light armor", "Mage Armor"]
take3 = int(input())
print("You selected " + str(selection3[take3-1]))
print("")
finalselection = [selection1[take1-1],selection2[take2-1],selection3[take3-1]]
#print("DEBUG: " + str(finalselection) + " LEN " + str(len(finalselection)))
print("So your composition is: " + selection1[take1-1] + ", " + selection2[take2-1] + " and " + selection3[take3-1] + ".")
print("...")
print("Are you happy with it or would you like to pick something else?")
print("...")
print("What is your choice: Pick or Leave")
choice = input()
if choice.capitalize() == 'Leave':
    pass
elif choice.capitalize() == 'Pick':
    print("Okay, I have these leftovers items: Meat, Bow, Crossbow or Staff")
    selection4 = ["Meat","Bow","Crossbow","Staff"]
    print("What would you like to pick?")
    take4 = int(input())
    print("Okay so you selected " + str(selection4[take4-1]) + ", What item would you like to drop for it?")
    print(str(selection1[take1-1]) + " " + str(selection2[take2-1]) + " " + str(selection3[take3-1]))
    drop = int(input())
    del finalselection[drop-1]
    finalselection.insert(drop-1 , selection4[take4-1])
    print("Alright! You'll final inventory then would be: " + str(finalselection))



print("...")
print("...")
print("Okay then, best of luck in your future adventure!")

