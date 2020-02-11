def intcodeCalculator(num1, num2, intcode):
    intcode[1] = num1
    intcode[2] = num2
    
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
    
    return intcode[0]

intcode = [int(x) for x in open("input").read().split(",")]


for i in range(100):
    for j in range(100):
        if intcodeCalculator(i, j, intcode[:]) == 19690720:
            print(100 * i + j)
            break



