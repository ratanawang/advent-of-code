# part one + part two
valid = []
okay = True
for i in range(265275, 781584):
    okay = True
    for a in range(0, 5):
        if int(str(i)[a]) > int(str(i)[a+1]):
            okay = False
    if okay:
        valid.append(i)
print(valid)
for p in range(0, 5):
    for x in valid:
        okay = False
        for y in range(0, 5):
            if int(str(x)[y]) == int(str(x)[y+1]):
                temp = int(str(x)[y])
                if str(temp)*2 in str(x) and str(temp)*3 not in str(x):
                    okay = True
        if not okay:
            valid.remove(x)
print(valid)
print(len(valid))

