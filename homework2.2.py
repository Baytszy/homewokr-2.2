first = int(input('num = '))
second = int(input('num = '))
third = int(input('num = '))
if first == second and first == third:
    print(3)
elif first == second or first == third:
    print(2)
else:
    print(0)