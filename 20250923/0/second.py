numbers = [i for i in range(5, 16)]
letters = [j for j in "abcdefghijk"]
print(numbers, letters)
numbers[4:8] = letters[-5:]
print(numbers, letters)
