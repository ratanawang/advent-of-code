import math

# part one
masses = []
fuel = []
total_fuel = 0
while True:
    mass = input()
    if mass != "/exit":
        masses.append(int(mass))
    else:
        break
# for x in masses:
#     fuel.append(math.floor(x/3)-2)

# part two
for x in masses:
    total_fuel += math.floor(x / 3) - 2
    x = math.floor(x/3)-2
    while math.floor(x/3)-2 > 0:
        total_fuel += math.floor(x/3)-2
        x = math.floor(x/3)-2
print(total_fuel)
