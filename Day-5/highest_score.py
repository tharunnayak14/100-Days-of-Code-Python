student_scores = input("Input a list of student scores").split()
max_score = int(student_scores[0])
for score in student_scores:
    score = int(score)
    if score > max_score:
        max_score = score
print(f"Highest score is {max_score}")



