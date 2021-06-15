student_heights = input("Input a list of student heights ").split()
avg_height = 0
total_height = 0
count = 0
for height in student_heights:
    height = int(height)
    total_height += height
    count += 1

avg_height = round(total_height/count)
print(avg_height)

