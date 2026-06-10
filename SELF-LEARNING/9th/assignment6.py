'''Assignment 6: Student Resume Analyzer 
Problem Statement 
A student enters a resume as plain text (Name, Skills, Education, Projects, Achievements). 
The system should: 
1. Count total words.  
2. Count total characters.  
3. Extract email IDs.  
4. Extract phone numbers.  
5. Count skills mentioned.  
6. Find repeated keywords.  
7. Identify the most frequently used word.  
8. Generate a skill frequency report.  
9. Detect duplicate skills.  
10. Create a summary dashboard.  
Expected Output 
Resume Analysis Report 
 
Total Words: 420 
Total Characters: 2650 
 
Email Found: 1 
Phone Numbers Found: 1 
 
Most Frequent Skill: Python 
 
Top 5 Keywords: 
Python 
SQL 
React 
Java 
Communication'''

# Student Resume Analyzer

resume = """
Name: Anuj Sharma
Email: anuj123@gmail.com
Phone: 9876543210

Education:
B.Tech in Computer Science

Skills:
Python SQL React Java Communication Python SQL

Projects:
Library Management System
Employee Payroll System
Student Result Processing System

Achievements:
Winner of Coding Competition
Completed Python Certification
Strong Communication and Leadership Skills
"""

# Total words
words = resume.split()
total_words = len(words)

# Total characters
total_characters = len(resume)

# Extract Email IDs
emails = []

for word in words:
    if "@" in word and "." in word:
        emails.append(word)

# Extract Phone Numbers
phones = []

for word in words:
    if word.isdigit() and len(word) == 10:
        phones.append(word)

# Skills List
skills = ["Python", "SQL", "React", "Java", "Communication"]

skill_frequency = {}

for skill in skills:
    count = resume.lower().count(skill.lower())

    if count > 0:
        skill_frequency[skill] = count

# Find repeated keywords
print("Repeated Keywords:")
for skill in skill_frequency:
    if skill_frequency[skill] > 1:
        print(skill, ":", skill_frequency[skill])

# Most frequent skill
most_skill = ""
max_count = 0

for skill in skill_frequency:
    if skill_frequency[skill] > max_count:
        max_count = skill_frequency[skill]
        most_skill = skill

# Word Frequency Dictionary
word_frequency = {}

for word in words:

    word = word.strip(":,.").lower()

    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Most frequently used word
most_word = ""
word_count = 0

for word in word_frequency:
    if word_frequency[word] > word_count:
        word_count = word_frequency[word]
        most_word = word

# Duplicate Skills
print("\nDuplicate Skills:")
for skill in skill_frequency:
    if skill_frequency[skill] > 1:
        print(skill)

# Top 5 Keywords
sorted_keywords = sorted(word_frequency.items(),
                         key=lambda x: x[1],
                         reverse=True)

# Summary Dashboard
print("\n===== RESUME ANALYSIS REPORT =====")

print("Total Words :", total_words)
print("Total Characters :", total_characters)

print("\nEmail Found :", len(emails))
for email in emails:
    print(email)

print("\nPhone Numbers Found :", len(phones))
for phone in phones:
    print(phone)

print("\nMost Frequent Skill :", most_skill)

print("\nMost Frequently Used Word :", most_word)

print("\nSkill Frequency Report")
for skill in skill_frequency:
    print(skill, ":", skill_frequency[skill])

print("\nTop 5 Keywords")
for item in sorted_keywords[:5]:
    print(item[0], ":", item[1])