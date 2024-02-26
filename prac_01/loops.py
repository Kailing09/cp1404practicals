for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
for i in range(10, 101, 10):
    print(i, end=' ')
print()

#b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c
password = input('Enter your password: ')
stars = '*' * len(password)
print(stars)

#d
password = input('Enter your password: ')
for i in range(1, len(password) + 1):
    stars = '*' * i
    print(stars)

