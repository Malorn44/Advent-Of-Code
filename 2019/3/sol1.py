def manhattan(pA, pB):
    return abs(pA[0] - pB[0]) + abs(pA[1] - pB[1])

pathA, pathB = open("input").read().splitlines()

# pathA = "R8,U5,L5,D3"
# pathB = "U7,R6,D4,L4"

actionsA = pathA.split(',')
actionsB = pathB.split(',')

start = (0, 0)

locSetA = {}
stepSum = 0
cur_loc = list(start)
for action in actionsA:
    direction = action[0]
    distance = int(action[1:])
    temp_loc = cur_loc
    while distance > 0:
        # print(cur_loc)
        if direction == "R":
            temp_loc[0] += 1
        elif direction == "L":
            temp_loc[0] -= 1
        elif direction == "U":
            temp_loc[1] += 1
        elif direction == "D":
            temp_loc[1] -= 1

        stepSum += 1
        if tuple(temp_loc) not in locSetA.keys():
            locSetA[tuple(temp_loc)] = stepSum
        cur_loc = temp_loc
        distance -= 1

intersections = []
stepSum = 0
cur_loc = list(start)
for action in actionsB:
    direction = action[0]
    distance = int(action[1:])
    temp_loc = cur_loc
    while distance > 0:
        # print(cur_loc)
        if direction == "R":
            temp_loc[0] += 1
        elif direction == "L":
            temp_loc[0] -= 1
        elif direction == "U":
            temp_loc[1] += 1
        elif direction == "D":
            temp_loc[1] -= 1

        stepSum += 1
        if tuple(temp_loc) in locSetA.keys():
            intersections.append((tuple(temp_loc), locSetA[tuple(temp_loc)] + stepSum))
        cur_loc = temp_loc
        distance -= 1

minDist, point = min([(manhattan((0,0),y[0]), y[0]) for y in intersections])
print(minDist, point)

minStep, point = min([(y[1], y[0]) for y in intersections])
print(minStep, point)




