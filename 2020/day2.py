# --- Day 2: Password Philosophy ---

passwords = []
while True:
    pw = input()
    if pw != "exit":
        passwords.append(pw)
    else:
        break
valid = []
# for x in passwords:
#     y = x.split(": ")
#     letter = y[0][-1]
#     minimum = int(y[0].split("-")[0])
#     maximum = int(y[0].split("-")[1].split(" ")[0])
#     letter_count = int(y[1].count(letter))
#     if minimum <= letter_count <= maximum:
#         valid.append(x)
for x in passwords:
    y = x.split(":")
    letter = y[0][-1]
    pos_1 = int(y[0].split("-")[0])
    pos_2 = int(y[0].split("-")[1].split(" ")[0])
    if (y[1][pos_1] == letter) != (y[1][pos_2] == letter):
        valid.append(x)

print("The number of valid passwords is: " + str(len(valid)))
