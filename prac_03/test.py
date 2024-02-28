# with open("ok.txt", 'r') as my_file:
#     contents = my_file.read()
#     words = contents.split()
#     for word in words:
#         print(word)
#

# with open("ok.txt", "r") as my_file:
#     contents = my_file.readlines()
#     print(contents)

# with open("ok.txt", "r") as my_file:
#     for line in my_file:
#         part = line.strip().split(",")
#         name = part[0]
#         notsure = part[1]
#         yr = part[2]
#         print(name, notsure, yr[0::-2])


# with open("ok.txt", 'r') as my_file:
#     for line in my_file:
#         print(line)




#exeptions
valid_input = False
while not valid_input:
    try:
        age = int(input("Enter your age: "))
        valid_input = True
    except ValueError:
        print("Invalid")
    else:
        print(f"next year u will be {age + 1}")
    finally:
        print("good try")

iif not i
