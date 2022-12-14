# This is a really simple program that makes a choice when one is feeling indecisive
# It starts by asking how many choices there are, then it asks you to list the choices
# using a comma. When that is done, it randomly selects a choice for you

import random

print("welcome")

print("how many options are we dealing with?")
amount = input()

if amount.isdigit():
    amount = int(amount)
else:
    print("Choose a number with no spaces next time")
    quit()
    
print("What %d options would you like to randomize? separate them using commas" % amount)
options = input()
list1 = options.split(",")

if len(list1)<amount:
    print("insufficient text")
    quit()
elif len(list1)>amount:
    print("too much text")
    quit()
    
print("we will now make a random choice for you")

choice = random.randrange(amount)
print(list1[choice])
