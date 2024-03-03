name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

with open('name.txt', 'r') as file:
    name = file.read()
print(f"Your name is {name}")

with open('numbers.txt', 'w') as file:
    file.writelines(['17\n', '42\n', '400\n'])

with open('numbers.txt', 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
print(number1 + number2)

total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)
print(total)
