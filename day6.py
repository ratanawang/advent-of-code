# part one
# find number of direct and indirect orbits
# objects = set()
#
#
# # only create an object if it orbits another, is orbiter
# class Object:
#     orbits = []
#     name = ""
#
#     def __init__(self, string):
#         global objects
#         self.name = string.split(")")[1]  # the orbiter
#         self.orbits.append(string.split(")")[0])  # the orbited
#         print("{} orbits {}".format(string.split(")")[1], string.split(")")[0]))
#         objects.add(self)
#
#
# while True:
#     orbit = input()
#     if orbit == "/exit":
#         break
#     else:
#         orbited = orbit.split(")")[0]
#         orbiter = orbit.split(")")[1]
#         inlist = False
#         for x in objects:
#             if x.name == orbiter:
#                 inlist = True
#         if inlist:
#             orbiter = Object(orbit)
#         else:
#             getattr(orbiter, "d_orbits").append(orbit.split(")")[0])
#             print(getattr(orbiter, "d_orbits"))


objects = {}

while True:
    orbit = input()
    if orbit == "/exit":
        break
    else:
        orbited = orbit.split(")")[0]
        orbiter = orbit.split(")")[1]
        if orbiter not in objects:
            objects[orbiter] = set()
        objects[orbiter].add(orbited)
        print("{} orbits {}".format(orbiter, objects[orbiter]))

count = 0
for x in objects:
    count += len(objects[x])
    for y in objects[x]:
        if y in objects:
            count += len(objects[y])
            for z in objects[y]:
                if z in objects:
                    count += len(objects[z])
                    for a in objects[z]:
                        if a in objects:
                            count += len(objects[a])
print(count)
