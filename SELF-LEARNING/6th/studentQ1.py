'''marks = { 
    "Aarav": 78, 
    "Diya": 92, 
    "Rohan": 45, 
    "Ishita": 88, 
    "Kabir": 56, 
    "Meera": 39, 
    "Arjun": 95, 
    "Saanvi": 67, 
    "Vivaan": 82, 
    "Anaya": 51 
} 
Tasks 
• Display students scoring 80 or above.  
• Count the number of students who failed (marks < 40).  
• Find the highest scorer.  
• Create a list of students scoring between 60 and 75.  
• Assign grades:  
o A: ≥ 90  
o B: 75–89  
o C: 50–74  
o F: < 50  
 
'''

marks = { 
    "Aarav": 78, 
    "Diya": 92, 
    "Rohan": 45, 
    "Ishita": 88, 
    "Kabir": 56, 
    "Meera": 39, 
    "Arjun": 95, 
    "Saanvi": 67, 
    "Vivaan": 82, 
    "Anaya": 51 
} 
#Display students scoring 80 or above.  
print("student mark above 80")

for name, score in marks.items():
    if score > 80:
        print(name, score)


