import re #import regular expression library

message = "Puoi trovarmi al 333-6942011 oppure al 338-7774201 o al 347-6969421"

#method 1 it finds only the first phone number in a given string
src_pattern = re.compile(r"\d\d\d-\d\d\d\d\d\d\d") #pattern recognition \d means digit 0-9 and then it looks for a dash between digit 3 and 4
try:
    mo = src_pattern.search(message) #find first recognized pattern (first number), mo stands for matched object
    print(mo.group()) #this prints out only the object than just print(mo) what is found (c)
    print(mo)
except AttributeError:
    print("Didn't find any phone numbers")

#method 2 finds all the phone numbers in a given string

print(src_pattern.findall(message)) #method findall




