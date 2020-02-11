intcode = [int(x) for x in open("input").read().split(",")]

intcode[1] = 12
intcode[2] = 2

for i in range(0, len(intcode), 4): 
    if intcode[i] == 99:
        break

    n1 = intcode[intcode[i+1]]
    n2 = intcode[intcode[i+2]]
    loc = intcode[i+3]


    if intcode[i] == 1:
        intcode[loc] = n1 + n2
    elif intcode[i] == 2:
        intcode[loc] = n1 * n2

print(intcode[0])








