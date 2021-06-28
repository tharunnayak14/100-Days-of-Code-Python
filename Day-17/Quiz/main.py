from question_data import question_data
from quiz_brain import QuizBrain

questions = question_data


class NewQuestion:
    def __init__(self, text, answer):
        # question = random.choice(questions)
        self.text = text
        self.answer = answer


# que_1 = NewQuestion("question", "answer")
# print(que_1.text, que_1.answer)



question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(NewQuestion(question_text, question_answer))

# print(question_bank)
Quiz = QuizBrain(question_bank)
while Quiz.still_has_questions():
    Quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {Quiz.score}/{len(Quiz.question_list)}")