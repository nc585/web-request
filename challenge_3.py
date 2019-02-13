# https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.json
# goal: calculate average grade

import json
import requests # because it is a third party package, need to install it using pip from command line
import statistics 

request_url = "https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.json"

response = requests.get(request_url)

parsed_response = json.loads(response.text) #converts to dictionary

grades = [] #can use list functions to do calculations

for student in parsed_response["students"]:
    grades.append(student["finalGrade"])

avg_grade = statistics.mean(grades)

print("THE AVERAGE GRADE IS: " + str(avg_grade))

#print(statistics.mean(grades))