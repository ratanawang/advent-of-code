# --- Day 1: Report Repair ---

nums = []
while True:
    x = input()
    if x != "exit":
        nums.append(int(x))
    else:
        break
# for x in nums:
#     y = 2020 - x
#     if y in nums:
#         print("The code is: " + str(x * y))
#         break
for x in range(0, len(nums) - 1):
    for y in range(x + 1, len(nums)):
        z = 2020 - (nums[x] + nums[y])
        if z in nums:
            print("The code is: " + str(nums[x] * nums[y] * z))
            break
