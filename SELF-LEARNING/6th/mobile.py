contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# Display names alphabetically
names = list(contacts.keys())
names.sort()

print("Contacts in Alphabetical Order:")
for name in names:
    print(name)

# Count contacts
count = 0

for name in contacts:
    count += 1

print("\nTotal Contacts:", count)

# Search contact
search_name = input("\nEnter contact name: ")

for name in contacts:
    if name == search_name:
        print("Contact Found:", contacts[name])
        break
else:
    print("Contact Not Found")

# Names starting with vowels
vowels = []

for name in contacts:
    if name[0] in "AEIOUaeiou":
        vowels.append(name)

print("\nNames Starting With Vowels:")
print(vowels)