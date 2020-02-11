
def recursiveFuelCalc(mass):
    required_fuel = (mass // 3) - 2
    if required_fuel <= 0:
        return 0
    return required_fuel + recursiveFuelCalc(required_fuel)


mass_list = [int(line) for line in open("input").read().splitlines()]

required_fuel = 0
for mass in mass_list:
    required_fuel += recursiveFuelCalc(mass)

print(required_fuel)
