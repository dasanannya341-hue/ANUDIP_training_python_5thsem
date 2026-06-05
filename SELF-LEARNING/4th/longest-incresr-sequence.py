#Accept N numbers one by one and find the length of the longest continuous increasing sequence.
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
max_length = 1
current_length = 1
for i in range(1, n):
    if numbers[i] > numbers[i - 1]:
        current_length += 1
    else:
        max_length = max(max_length, current_length)
        current_length = 1
max_length = max(max_length, current_length)
print("Length of the longest continuous increasing sequence:", max_length)