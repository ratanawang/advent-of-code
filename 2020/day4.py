# --- Day 4: Passport Processing ---

passports = []
y = ""
while True:
    x = input()
    if x == "exit":
        break
    if x == "":
        passports.append(y)
        y = ""
    y += x + " "

valid = []
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


class Passport:

    ff = {}

    def process(self, passport):
        p = passport.split(" ")
        for z in p:
            if z == "":
                continue
            self.ff[z.split(":")[0]] = z.split(":")[1]

    def check_validity(self):

        byr = self.ff["byr"]
        iyr = self.ff["iyr"]
        eyr = self.ff["eyr"]
        hgt = self.ff["hgt"]
        hcl = self.ff["hcl"]
        ecl = self.ff["ecl"]
        pid = self.ff["pid"]

        if not (len(byr) == 4 and 1920 <= int(byr) <= 2002):
            return 0

        if not (len(iyr) == 4 and 2010 <= int(iyr) <= 2020):
            return 0

        if not (len(eyr) == 4 and 2020 <= int(eyr) <= 2030):
            return 0

        if not (hgt[-2:] == "cm" or hgt[-2:] == "in"):
            return 0
        if hgt[-2:] == "cm":
            if not 150 <= int(hgt[:-2]) <= 193:
                return 0
        elif hgt[-2:] == "in":
            if not 59 <= int(hgt[:-2]) <= 76:
                return 0

        if hcl[0] != "#":
            return 0
        elif hcl[0] == "#":
            hc = hcl[1:]
            if len(hc) != 6:
                return 0
            for ch in hc:
                if ch not in list("0123456789abcdef"):
                    return 0

        if ecl not in "amb blu brn gry grn hzl oth".split(" "):
            return 0

        if len(pid) != 9:
            return 0

        return 1


def check_presence(passport):
    for f in fields:
        if f not in passport:
            return 0
    return 1


for x in passports:
    if check_presence(x) == 1:
        valid.append(x)
truly_valid = 0
for x in valid:
    pp = Passport()
    pp.process(x)
    truly_valid += pp.check_validity()
print("The number of truly valid passports is: " + str(truly_valid))
