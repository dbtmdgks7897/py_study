# print("*****")
# print("*****")
# print("*****")
# print("*****")
# print("*****")

# for item in range(5):
#     print("*****")

# for item in range(5):
#     print("".rjust(5,"*"))

# for item in range(5):
#     print("*" * 5)

# [print("*" * 5) for item in range(5)]

# for item in range(5):
#     for item1 in range(5):
#         print("*", end="")
#     print()

def square(num: int):
    for item in range(num):
        for item1 in range(num):
            print("*", end="")
        print()


square(6)
