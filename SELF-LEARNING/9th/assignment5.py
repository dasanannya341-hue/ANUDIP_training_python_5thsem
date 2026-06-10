'''Assignment 5: News Article Text Analyzer 
Problem Statement 
A news agency wants to analyze the content of an article. 
Use a paragraph containing at least 300 words. 
Requirements 
1. Count total characters.  
2. Count total words.  
3. Count total sentences.  
4. Count vowels and consonants.  
5. Find longest word.  
6. Find shortest word.  
7. Find the most frequent word.  
8. Create a dictionary of word frequencies.  
9. Display words appearing only once.  
10. Display words appearing more than 5 times.  
11. Count words starting with each alphabet.  
12. Display all unique words.  
Challenge 
Generate a complete text summary: 
Total Words 
Total Sentences 
Average Word Length 
Most Frequent Word 
Vocabulary Size'''


# News Article Text Analyzer

article = """
Technology is transforming the world at an unprecedented pace. In recent years,
artificial intelligence has become one of the most discussed technologies.
Many industries are adopting artificial intelligence to improve efficiency,
reduce costs, and enhance customer experiences. The healthcare sector uses
artificial intelligence for disease prediction and medical imaging. The
education sector uses technology to provide online learning opportunities.
Businesses are investing heavily in technology because it helps them remain
competitive in a rapidly changing market.

Governments are also focusing on digital transformation. Smart cities are
being developed using advanced technology and data analytics. Public services
are becoming more accessible through online platforms. Citizens can now access
important information quickly and efficiently. Technology is improving
communication, transportation, and financial services. Digital payment systems
have simplified transactions for millions of people.

Despite these advantages, technology also presents challenges. Data privacy and
cybersecurity have become major concerns. Organizations must protect sensitive
information from cyber attacks. Individuals should be aware of online threats
and follow safe internet practices. Technology companies are investing in
security measures to build trust among users.

Artificial intelligence continues to evolve and influence various aspects of
daily life. Researchers are exploring new applications of artificial
intelligence in agriculture, manufacturing, and environmental protection.
Technology has created opportunities for innovation and economic growth.
Experts believe that technology will continue to shape the future of society.
Responsible use of technology is essential to ensure sustainable development
and long-term benefits for humanity. Technology, technology, technology,
technology, technology, technology.
"""

# Total characters
total_characters = len(article)

# Total words
words = article.lower().split()
total_words = len(words)

# Total sentences
total_sentences = article.count(".") + article.count("?") + article.count("!")

# Count vowels and consonants
vowels = 0
consonants = 0

for ch in article.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Find longest and shortest word
clean_words = []

for word in words:
    word = word.strip(".,!?;:()")
    clean_words.append(word)

longest_word = clean_words[0]
shortest_word = clean_words[0]

for word in clean_words:
    if len(word) > len(longest_word):
        longest_word = word

    if len(word) < len(shortest_word):
        shortest_word = word

# Word frequency dictionary
frequency = {}

for word in clean_words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Most frequent word
most_word = ""
most_count = 0

for word in frequency:
    if frequency[word] > most_count:
        most_count = frequency[word]
        most_word = word

# Words appearing only once
print("Words Appearing Only Once:")
for word in frequency:
    if frequency[word] == 1:
        print(word)

# Words appearing more than 5 times
print("\nWords Appearing More Than 5 Times:")
for word in frequency:
    if frequency[word] > 5:
        print(word, ":", frequency[word])

# Count words starting with each alphabet
alphabet_count = {}

for word in frequency:
    first = word[0]

    if first in alphabet_count:
        alphabet_count[first] += 1
    else:
        alphabet_count[first] = 1

print("\nWords Starting With Each Alphabet:")
for key in alphabet_count:
    print(key, ":", alphabet_count[key])

# Unique words
print("\nUnique Words:")
for word in frequency:
    print(word)

# Average word length
total_length = 0

for word in clean_words:
    total_length += len(word)

average_word_length = total_length / total_words

# Vocabulary size
vocabulary_size = len(frequency)

# Final Summary Report
print("\n===== NEWS ARTICLE SUMMARY =====")
print("Total Characters :", total_characters)
print("Total Words :", total_words)
print("Total Sentences :", total_sentences)
print("Vowels :", vowels)
print("Consonants :", consonants)
print("Longest Word :", longest_word)
print("Shortest Word :", shortest_word)
print("Most Frequent Word :", most_word)
print("Frequency :", most_count)
print("Average Word Length :", round(average_word_length, 2))
print("Vocabulary Size :", vocabulary_size)