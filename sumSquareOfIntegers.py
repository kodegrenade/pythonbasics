# Week 6 Exercise 1
total = 0
x = 0
number = 200
last_number = 0
while True:
    x = x + 1
    y = x ** 2
    total = total + y    
    if total >= number:
        last_number = x
        break
print("Final Total:", total)
print("Last Number added:", last_number)