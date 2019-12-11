# part one
# find number of direct and indirect orbits


class Object:
    d_orbits = []
    i_orbits = []
    name = ""

    def __init__(self, string):
        self.name = string.split(")")[1]  # the orbiter
        self.d_orbits.append(string.split(")")[0])  # the orbited
        print("{} orbits {}".format(self.name, string.split(")")[0]))


# converts data with numbers into readable strings
def converter(string):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for i in string:
        if i.isdigit():
            string.replace(i, alphabet[i])
    return string


while True:
    orbit = input()
    if orbit == "/exit":
        break
    else:
        orbit = converter(orbit)
        orbiter = orbit.split(")")[1]
        if not isinstance(orbiter, Object):
            orbiter = Object(orbit)
        else:
            orbiter.d_orbits.append(orbit.split(")")[0])
