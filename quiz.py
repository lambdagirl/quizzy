import sqlite3
class Quession:
    def __init__(self, id, prompt, choices,answer):
        self.prompt = id
        self.prompt = prompt
        self.answer = answer
        self.choices = choices

class User:
    def __init__(self, id, nickname, score,):
        self.prompt = id
        self.prompt = prompt
        self.answer = answer
        self.choices = choices

def get_question():
    db_conn = sqlite3.connect('quizzy.db');
    cursor = db_conn.cursor();
    _sql = """SELECT question_id, question, correct_choice, choice1,
    choice2, choice3 FROM question;"""
    cursor.execute(_sql);
    question_data = cursor.fetchall()
    cursor.close();        # Close the database connection
    db_conn.close();
    print(question_data)
    return question_data

q_data = get_question()

questions = []
for i in range(len(q_data)):
    questions.append(Quession(q_data[i][1],q_data[i][2:6],q_data[i][2]))


def run_test(questions):
    score = 0
    for question in questions:
        print(question.prompt, question.choices)
        user_answer = input("Choice")
        print("correct answer is ",question.answer)
        if user_answer == question.answer:
            score += 1
    print("You got " + str(score) + '/' + str(len(questions)))

run_test(questions)
