# part one

# take in input, convert to a list of nums
nums = list(input("Enter the list of numbers: "))
pos = 0
base = ["0", "1", "0", "-1"]

# base pattern: 0, 1, 0, -1
# method 1: multiply each base pattern element by the index + 1 of the element
# make enough base pattern elements to pair up with all of the original elements
# skip the first value


def find_base_pattern(index):
    new_base = []
    for x in base:
        for y in range(0, index):
            new_base.append(x)
    print(new_base)


# method 2: calculates new pattern's digit:
# takes in arguments of original pattern, base pattern (1)
# returns the last digit of the calculated number


# while index < len(nums):
#     pass

find_base_pattern(pos)
