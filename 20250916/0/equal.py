index = 1
count = 0
while n := int(input()):
    if n == index:
        count += 1
    index += 1

print(count)
