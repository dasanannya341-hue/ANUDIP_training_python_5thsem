'''Assignment 3: Chat Message Analytics Dashboard 
Problem Statement 
A messaging application wants to analyze chat messages. 
Store at least 20 chat messages in a list. 
Requirements 
For each message: 
1. Count total words.  
2. Count total characters.  
3. Count vowels and consonants.  
4. Find longest word.  
5. Find shortest word.  
6. Count occurrence of each word.  
7. Display repeated words.  
8. Display words starting with vowels.  
9. Display words longer than 5 characters.  
10. Create a dictionary containing word frequencies.  
Challenge 
Generate a report showing: 
Most Frequently Used Word 
Longest Message 
Shortest Message 
Average Words Per Message'''

# Chat Message Analytics Dashboard

messages = [
    "Hello how are you",
    "I am doing great today",
    "Python programming is fun",
    "Let's complete the assignment",
    "Good morning everyone",
    "Have a wonderful day",
    "Learning Python is interesting",
    "Data science is amazing",
    "Machine learning is powerful",
    "Artificial intelligence is growing",
    "Keep practicing coding daily",
    "Success comes with consistency",
    "Always believe in yourself",
    "Hard work beats talent",
    "Never stop learning new things",
    "Coding improves problem solving",
    "Teamwork makes projects successful",
    "Communication is very important",
    "Practice makes a person perfect",
    "Stay focused on your goals"
]

word_frequency = {}

total_words_all = 0

longest_message = messages[0]
shortest_message = messages[0]

# Process each message
for msg in messages:

    print("\nMessage :", msg)

    words = msg.split()

    # Count words
    word_count = len(words)
    total_words_all += word_count

    # Count characters
    char_count = len(msg)

    # Count vowels and consonants
    vowels = 0
    consonants = 0

    for ch in msg.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    # Find longest word
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    # Find shortest word
    shortest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word

    # Word frequency dictionary
    for word in words:
        word = word.lower()

        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    print("Total Words :", word_count)
    print("Total Characters :", char_count)
    print("Vowels :", vowels)
    print("Consonants :", consonants)
    print("Longest Word :", longest_word)
    print("Shortest Word :", shortest_word)

    # Longest and shortest message
    if len(msg) > len(longest_message):
        longest_message = msg

    if len(msg) < len(shortest_message):
        shortest_message = msg

# Display repeated words
print("\n===== Repeated Words =====")

for word in word_frequency:
    if word_frequency[word] > 1:
        print(word, ":", word_frequency[word])

# Words starting with vowels
print("\n===== Words Starting With Vowels =====")

for word in word_frequency:
    if word[0].lower() in "aeiou":
        print(word)

# Words longer than 5 characters
print("\n===== Words Longer Than 5 Characters =====")

for word in word_frequency:
    if len(word) > 5:
        print(word)

# Display word frequency dictionary
print("\n===== Word Frequency Dictionary =====")
print(word_frequency)

# Most frequently used word
max_word = ""
max_count = 0

for word in word_frequency:
    if word_frequency[word] > max_count:
        max_count = word_frequency[word]
        max_word = word

# Average words per message
average_words = total_words_all / len(messages)

# Final Report
print("\n===== CHAT ANALYTICS REPORT =====")
print("Most Frequently Used Word :", max_word)
print("Frequency :", max_count)

print("\nLongest Message :")
print(longest_message)

print("\nShortest Message :")
print(shortest_message)

print("\nAverage Words Per Message :", average_words)