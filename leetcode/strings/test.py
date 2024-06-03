

string = "-+5e3.5"
letters = "eE."
letters1 = "-+"
nosign = string.lstrip("+-")

char1 = "".join(char for char in nosign if char not in letters1)

print(char1)

exp1 = char1.find("e")+1
exp2 = char1.find("E")+1

try:
    int(char1[exp1])
    int(char1[exp2])
except:
    print("no")

    



print("".join(char for char in char1 if char not in letters))