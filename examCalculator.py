# Examination Calculator
courses = ["COM311", "COM312", "COM313"]
total = 0

# loop through the course list and collect their respective values
for i in range(len(courses)):
    courses[i] = int(input("Enter score for " + courses[i] +" \n"))
    total += courses[i]
    average = total / len(courses)

# check the total score againt the pass mark range
if (total > 70):
    print("Congratulations, you made it. \n Your total mark is ", total)
    print("Average Score Obtained", average)
elif ((total < 70) and (total > 60)):
    print("Work hard next time. \n Your total mark is ", total)
    print("Average Score Obtained", average)
else:
    print ("You failed, put in more effort. \n Your total mark is ", total)
    print("Average Score Obtained", average)