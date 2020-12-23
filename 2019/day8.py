# part one

import textwrap
from collections import Counter

layers = textwrap.wrap(input(), 150)
print(layers)
zeros = {}

for i in range(0, len(layers)):
    count = Counter(layers[i])
    print("count of character frequency in layer {} is: ".format(i) + str(count))
    zeros[i] = count["0"]

key_list = list(zeros.keys())
value_list = list(zeros.values())

lowest = key_list[value_list.index(min(value_list))]
print("layer {} has the lowest number of zeros".format(lowest))

count_lowest = Counter(layers[lowest])
print("it has {} 1's and {} 2's".format(count_lowest["1"], count_lowest["2"]))

# part two

result = []
while len(result) < 150:
    for i in range(0, len(layers)):
        if int(layers[i][len(result)]) < 2:
            result.append(layers[i][len(result)])
            break

print(result)
result = textwrap.wrap("".join(result), 25)
for i in result:
    print(i)
