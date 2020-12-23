# --- Day 3: Toboggan Trajectory ---

map = []
while True:
    row = input()
    if row != "exit":
        map.append(list(row))
    else:
        break
map_width = len(map[0])


def count_trees(right, down):
    trees = 0
    col = 0
    for row in range(0, len(map), down):
        if map[row][col] == "#":
            trees += 1
        col += right
        if col >= map_width:
            col -= map_width
    print(f"Right {right}, down {down}: {trees}")
    return trees


answer = count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2)
print("The code is: " + str(answer))
