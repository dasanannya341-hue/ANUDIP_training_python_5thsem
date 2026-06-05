#program to remove duplicate elements from a list
#creating a list with duplicate elements
numbers=[]
print("Enter 10 numbers:")
for i in range(10):
    num=int(input())
    numbers.append(num)
print("List with duplicates: ", numbers)
E=int(input("Enter number to remove duplicates: "))
#finding the index of the element to be removed
frequency = numbers.count(E)
if frequency == 0:
    print("Element not found in the list.")
elif frequency == 1:
    print("Element is not a duplicate.")
else:
    #revwersing the list to remove duplicates from the end
    numbers.reverse()
    for i in range(1, frequency):
        numbers.remove(E)
    #reversing the list again to restore original order
    numbers.reverse()
    print("List after removing duplicates: ", numbers)
    