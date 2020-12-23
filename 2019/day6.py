# part one
# find number of direct and indirect orbits


def add_stuff(amount):
    global count
    count += amount


def count_stuff(key):
    if len(objects[key]) > 0:
        add_stuff(len(objects[key]))
        for y in objects[key]:
            count_stuff(y)


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
        if orbited not in objects:
            objects[orbited] = set()
        objects[orbiter].add(orbited)
        print("{} orbits {}".format(orbiter, objects[orbiter]))

count = 0
for x in objects:
    count_stuff(x)
print(count)
