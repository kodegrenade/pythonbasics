# Program to compute student score in five courses
name = str(input("Enter your name: \n"))
matric_no = str(input("Enter your matric number: \n"))
com311 = int(input("Enter score for COM311: \n"))
com312 = int(input("Enter score for COM312: \n"))
com313 = int(input("Enter score for COM313: \n"))
com314 = int(input("Enter score for COM314: \n"))
com315 = int(input("Enter score for COM315: \n"))
total = com311 + com312 + com313 + com314 + com315
average = total / 5
print(name +",", "Your total score in all courses is: ", total)
print("The average score for all courses is:", average)