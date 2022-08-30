import random
min = 1
max = 6
another_roll = "yes" or "no"

while another_roll == "yes" or another_roll == "y":
    print("Rolling die")
    print("The value is: ")
    print(random.randint(min, max))
    another_roll = input("Have another roll?\n")

if another_roll == "no" or another_roll == "n":
    print("Done with rolling")
    

