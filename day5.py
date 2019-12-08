# part one (built off of day2.py)


def add_store():
    temp = "0"*(5 - len(str(nums[index]))) + str(nums[index])
    if temp[-3] == "0" and temp[-4] == "0":  # position mode
        nums[nums[index + 3]] = nums[nums[index + 1]] + nums[nums[index + 2]]
    elif temp[-3] == "1" and temp[-4] == "0":  # 1st parameter in immediate mode
        nums[nums[index + 3]] = nums[index + 1] + nums[nums[index + 2]]
    elif temp[-3] == "0" and temp[-4] == "1":  # 2nd parameter in immediate mode
        nums[nums[index + 3]] = nums[nums[index + 1]] + nums[index + 2]
    elif temp[-3] == "1" and temp[-4] == "1":  # both parameters in immediate mode
        nums[nums[index + 3]] = nums[index + 1] + nums[index + 2]
    if nums[index] != int(temp):
        return index
    return 4


def multiply_store():
    temp = "0"*(5 - len(str(nums[index]))) + str(nums[index])
    if temp[-3] == "0" and temp[-4] == "0":  # position mode
        nums[nums[index + 3]] = nums[nums[index + 1]] * nums[nums[index + 2]]
    elif temp[-3] == "1" and temp[-4] == "0":  # 1st parameter in immediate mode
        nums[nums[index + 3]] = nums[index + 1] * nums[nums[index + 2]]
    elif temp[-3] == "0" and temp[-4] == "1":  # 2nd parameter in immediate mode
        nums[nums[index + 3]] = nums[nums[index + 1]] * nums[index + 2]
    elif temp[-3] == "1" and temp[-4] == "1":  # both parameters in immediate mode
        nums[nums[index + 3]] = nums[index + 1] * nums[index + 2]
    if nums[index] != int(temp):
        return index
    return 4


def store():
    nums[nums[index + 1]] = int(input("Enter a number: "))
    return 2


def grab():
    print(nums[nums[index + 1]])
    return 2


def jump_if_true():
    temp = "0" * (5 - len(str(nums[index]))) + str(nums[index])
    if temp[-3] == "0" and temp[-4] == "0":  # position mode
        if nums[nums[index + 1]] != 0:
            return nums[nums[index + 2]]
    elif temp[-3] == "1" and temp[-4] == "0":  # 1st parameter in immediate mode
        if nums[index + 1] != 0:
            return nums[nums[index + 2]]
    elif temp[-3] == "0" and temp[-4] == "1":  # 2nd parameter in immediate mode
        if nums[nums[index + 1]] != 0:
            return nums[index + 2]
    elif temp[-3] == "1" and temp[-4] == "1":  # both parameters in immediate mode
        if nums[index + 1] != 0:
            return nums[index + 2]
    return index + 3


def jump_if_false():
    temp = "0" * (5 - len(str(nums[index]))) + str(nums[index])
    if temp[-3] == "0" and temp[-4] == "0":  # position mode
        if nums[nums[index + 1]] == 0:
            return nums[nums[index + 2]]
    elif temp[-3] == "1" and temp[-4] == "0":  # 1st parameter in immediate mode
        if nums[index + 1] == 0:
            return nums[nums[index + 2]]
    elif temp[-3] == "0" and temp[-4] == "1":  # 2nd parameter in immediate mode
        if nums[nums[index + 1]] == 0:
            return nums[index + 2]
    elif temp[-3] == "1" and temp[-4] == "1":  # both parameters in immediate mode
        if nums[index + 1] == 0:
            return nums[index + 2]
    return index + 3


def less_than():
    temp = "0" * (5 - len(str(nums[index]))) + str(nums[index])
    if temp[-3] == "0" and temp[-4] == "0":  # position mode
        if nums[nums[index + 1]] < nums[nums[index + 2]]:
            nums[nums[index + 3]] = 1
        else:
            nums[nums[index + 3]] = 0
    elif temp[-3] == "1" and temp[-4] == "0":  # 1st parameter in immediate mode
        if nums[index + 1] < nums[nums[index + 2]]:
            nums[nums[index + 3]] = 1
        else:
            nums[nums[index + 3]] = 0
    elif temp[-3] == "0" and temp[-4] == "1":  # 2nd parameter in immediate mode
        if nums[nums[index + 1]] < nums[index + 2]:
            nums[nums[index + 3]] = 1
        else:
            nums[nums[index + 3]] = 0
    elif temp[-3] == "1" and temp[-4] == "1":  # both parameters in immediate mode
        if nums[index + 1] < nums[index + 2]:
            nums[nums[index + 3]] = 1
        else:
            nums[nums[index + 3]] = 0
    if nums[index] != int(temp):
        return index
    return 4


def equals():
    temp = "0" * (5 - len(str(nums[index]))) + str(nums[index])
    if temp[-3] == "0" and temp[-4] == "0":  # position mode
        if nums[nums[index + 1]] == nums[nums[index + 2]]:
            nums[nums[index + 3]] = 1
        else:
            nums[nums[index + 3]] = 0
    elif temp[-3] == "1" and temp[-4] == "0":  # 1st parameter in immediate mode
        if nums[index + 1] == nums[nums[index + 2]]:
            nums[nums[index + 3]] = 1
        else:
            nums[nums[index + 3]] = 0
    elif temp[-3] == "0" and temp[-4] == "1":  # 2nd parameter in immediate mode
        if nums[nums[index + 1]] == nums[index + 2]:
            nums[nums[index + 3]] = 1
        else:
            nums[nums[index + 3]] = 0
    elif temp[-3] == "1" and temp[-4] == "1":  # both parameters in immediate mode
        if nums[index + 1] == nums[index + 2]:
            nums[nums[index + 3]] = 1
        else:
            nums[nums[index + 3]] = 0
    if nums[index] != int(temp):
        return index
    return 4


nums = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1102, 46, 47, 225, 2, 122, 130, 224, 101, -1998, 224, 224, 4,
        224, 1002, 223, 8, 223, 1001, 224, 6, 224, 1, 224, 223, 223, 1102, 61, 51, 225, 102, 32, 92, 224, 101, -800,
        224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 1, 224, 1, 223, 224, 223, 1101, 61, 64, 225, 1001, 118, 25, 224,
        101, -106, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 1, 224, 224, 1, 224, 223, 223, 1102, 33, 25, 225, 1102, 73,
        67, 224, 101, -4891, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 4, 224, 1, 224, 223, 223, 1101, 14, 81,
        225, 1102, 17, 74, 225, 1102, 52, 67, 225, 1101, 94, 27, 225, 101, 71, 39, 224, 101, -132, 224, 224, 4, 224,
        1002, 223, 8, 223, 101, 5, 224, 224, 1, 224, 223, 223, 1002, 14, 38, 224, 101, -1786, 224, 224, 4, 224, 102, 8,
        223, 223, 1001, 224, 2, 224, 1, 223, 224, 223, 1, 65, 126, 224, 1001, 224, -128, 224, 4, 224, 1002, 223, 8, 223,
        101, 6, 224, 224, 1, 224, 223, 223, 1101, 81, 40, 224, 1001, 224, -121, 224, 4, 224, 102, 8, 223, 223, 101, 4,
        224, 224, 1, 223, 224, 223, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105,
        227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105,
        1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101,
        294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0,
        0, 1105, 1, 99999, 1008, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 329, 1001, 223, 1, 223, 107, 677, 677,
        224, 102, 2, 223, 223, 1005, 224, 344, 101, 1, 223, 223, 1107, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 359,
        1001, 223, 1, 223, 1108, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 374, 101, 1, 223, 223, 107, 226, 226, 224,
        1002, 223, 2, 223, 1005, 224, 389, 1001, 223, 1, 223, 108, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 404,
        1001, 223, 1, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 419, 1001, 223, 1, 223, 1107, 677, 226,
        224, 102, 2, 223, 223, 1005, 224, 434, 1001, 223, 1, 223, 108, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 449,
        1001, 223, 1, 223, 8, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 464, 1001, 223, 1, 223, 1007, 677, 226, 224,
        1002, 223, 2, 223, 1006, 224, 479, 1001, 223, 1, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 494,
        1001, 223, 1, 223, 1107, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 509, 101, 1, 223, 223, 1108, 226, 677,
        224, 102, 2, 223, 223, 1005, 224, 524, 1001, 223, 1, 223, 7, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 539,
        1001, 223, 1, 223, 8, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 554, 101, 1, 223, 223, 107, 677, 226, 224,
        102, 2, 223, 223, 1006, 224, 569, 1001, 223, 1, 223, 7, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 584, 1001,
        223, 1, 223, 1008, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 599, 101, 1, 223, 223, 1108, 677, 226, 224, 102,
        2, 223, 223, 1006, 224, 614, 101, 1, 223, 223, 7, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 629, 1001, 223, 1,
        223, 8, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 644, 101, 1, 223, 223, 1007, 226, 226, 224, 102, 2, 223,
        223, 1005, 224, 659, 101, 1, 223, 223, 108, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 674, 1001, 223, 1, 223,
        4, 223, 99, 226]

index = 0
while index < (len(nums) - 2):
    if nums[index] % 100 == 1:
        index += add_store()
    elif nums[index] % 100 == 2:
        index += multiply_store()
    elif nums[index] % 100 == 3:
        index += store()
    elif nums[index] % 100 == 4:
        index += grab()
    elif nums[index] % 100 == 5:
        index = jump_if_true()
    elif nums[index] % 100 == 6:
        index = jump_if_false()
    elif nums[index] % 100 == 7:
        index += less_than()
    elif nums[index] % 100 == 8:
        index += equals()
    elif nums[index] % 100 == 99:
        index = len(nums)
