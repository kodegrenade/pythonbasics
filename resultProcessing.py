# Result Processing Python Code
first_semester_courses = ["COM311", "COM312", "COM313", "COM314", "COM315"]
second_semester_courses = ["GNS301", "STA311", "STA314", "CBS311", "OTM315"]

first_semester_total = 0
second_semester_total = 0
credit_unit_total = 26
grade_points = []

credit_units = {
    "COM311": 3, "COM312": 2, 
    "COM313": 4, "COM314": 3, 
    "COM315": 4, "GNS301": 2, 
    "STA311": 2, "STA314": 2, 
    "CBS311": 2, "OTM315": 2
}

letter_grades = {
    "A": 4.00, "AB": 3.50,
    "B": 3.25, "BC": 3.00,
    "C": 2.75, "CD": 2.50,
    "D": 2.25, "E": 2.00,
    "F": 0.00
}

grades = {}
weight_points = {}

def scoreGrade(score, course, grade_points):
    if (score >= 75 and score <= 100):
        data = { "course": course, "score": score, "grade": "A", "weight": letter_grades["A"] }
        grades[course] = data
        weight_points[course] = letter_grades["A"]
        unit = (weight_points[course] * credit_units[course])
        grade_points.append(unit)
    elif (score >= 70 and score <= 74):
        data = { "course": course, "score": score, "grade": "AB", "weight": letter_grades["AB"] }
        grades[course] = data
        weight_points[course] = letter_grades["AB"]
        unit = (weight_points[course] * credit_units[course])
        grade_points.append(unit)
    elif (score >= 65 and score <= 69):
        data = { "course": course, "score": score, "grade": "B", "weight": letter_grades["B"] }
        grades[course] = data
        weight_points[course] = letter_grades["B"]
        unit = (weight_points[course] * credit_units[course])
        grade_points.append(unit)
    elif (score >= 60 and score <= 64):
        data = { "course": course, "score": score, "grade": "BC", "weight": letter_grades["BC"] }
        grades[course] = data
        weight_points[course] = letter_grades["BC"]
        unit = (weight_points[course] * credit_units[course])
        grade_points.append(unit)
    elif (score >= 55 and score <= 59):
        data = { "course": course, "score": score, "grade": "C", "weight": letter_grades["C"] }
        grades[course] = data
        weight_points[course] = letter_grades["C"]
        unit = (weight_points[course] * credit_units[course])
        grade_points.append(unit)
    elif (score >= 50 and score <= 54):
        data = { "course": course, "score": score, "grade": "CD", "weight": letter_grades["CD"] }
        grades[course] = data
        weight_points[course] = letter_grades["CD"]
        unit = (weight_points[course] * credit_units[course])
        grade_points.append(unit)
    elif (score >= 45 and score <= 49):
        data = { "course": course, "score": score, "grade": "D", "weight": letter_grades["D"] }
        grades[course] = data
        weight_points[course] = letter_grades["D"]
        unit = (weight_points[course] * credit_units[course])
        grade_points.append(unit)
    elif (score >= 40 and score <= 44):
        data = { "course": course, "score": score, "grade": "E", "weight": letter_grades["E"] }
        grades[course] = data
        weight_points[course] = letter_grades["E"]
        unit = (weight_points[course] * credit_units[course])
        grade_points.append(unit)
    elif (score >= 0 and score <= 39):
        data = { "course": course, "score": score, "grade": "F", "weight": letter_grades["F"] }
        grades[course] = data
        weight_points[course] = letter_grades["F"]
        unit = (weight_points[course] * credit_units[course])
        grade_points.append(unit)
    return weight_points, grade_points, grades

for i in range(len(first_semester_courses)):
    course = first_semester_courses[i]
    first_semester_courses[i] = int(input("Enter examination score for " + first_semester_courses[i] + ":\n"))
    first_semester_total += first_semester_courses[i]
    mark_grade = scoreGrade(first_semester_courses[i], course, grade_points)

for k in range(len(second_semester_courses)):
    course = second_semester_courses[k]
    second_semester_courses[k] = int(input("Enter examination score for " + second_semester_courses[k] + ":\n"))
    second_semester_total += second_semester_courses[k]
    mark_grade = scoreGrade(second_semester_courses[k], course, grade_points)

grade_point_average = (sum(grade_points) / credit_unit_total)

print("\n********************************")
print("EXAMINATION RESULT")
print("********************************")
print("{:<10} {:<10} {:<10}".format("COURSE", "SCORE", "GRADE"))
for key, values in grades.items():
    print("_"*32)
    print("{:<10} {:<10} {:<10}".format(str(values["course"]), str(values["score"]), str(values["grade"])))
print("_"*32)
print("CGPA:", round(grade_point_average, 2))
print("_"*32)