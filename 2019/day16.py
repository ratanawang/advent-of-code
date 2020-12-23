# part one and part two

# take in input, convert to a list of nums
input_signal = (list(input("Enter the list of numbers: ")))
new_input = []
pos = 0
base = ["0", "1", "0", "-1"]
count = 0
offset = int("".join(input_signal[0:7]))
answer = []


# base pattern: 0, 1, 0, -1
# method 1: multiply each base pattern element by the index + 1 of the element
def find_base_pattern(index):
    new_base = []
    for x in base:
        for y in range(0, index):
            new_base.append(x)
    return new_base


# method 2: makes base pattern long enough to match pattern
# skips first element
def lengthen(base_pattern):
    while len(base_pattern) < len(input_signal) + 1:
        base_pattern *= 2
    base_pattern = base_pattern[1::]
    return base_pattern


# method 3: calculates new pattern's digit:
# takes in arguments of original pattern, base pattern (1)
# returns the last digit of the calculated number
def digit(pattern, base_pattern):
    res = 0
    for i in range(0, len(pattern)):
        res += int(pattern[i]) * int(base_pattern[i])
    res = int(str(res)[-1])
    return res


while count < 100:
    pos = 0
    while pos < len(input_signal):
        bp = lengthen(find_base_pattern(pos + 1))  # index 0, element 1
        new_input.append(digit(input_signal, bp))
        pos += 1
    print(new_input)
    input_signal = [x for x in new_input]
    answer = [x for x in new_input]
    new_input.clear()
    count += 1

print(answer)
print(answer[offset:offset + 8])
