mass_list = open("input").read().splitlines()


fuel_sum = 0

for mass in mass_list:
    temp = int(mass)
    temp = temp // 3
    temp -= 2
    fuel_sum += temp

print(fuel_sum)

