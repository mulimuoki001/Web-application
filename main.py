import requests
import random
import tkinter as tk


def trivia_questions(amount=5, category=9, difficulty="medium", type="multiple"):
    url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "category": category,
        "difficulty": difficulty,
        "type": type,
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data["response_code"] == 0:
        return data["results"]
    else:
        return []


def answer_checker(question, option, score):
    if option == question["correct_answer"]:
        feedback = "Congratulations!! Correct answer"
        score["text"] = f"Score: {int(score['text'].split(': ')[1]) + 1}"
    else:
        feedback = f"Wrong! The correct answer is: {question['correct_answer']}"
    feedback_label["text"] = feedback


def nxt_question():
    global current_question_index
    if current_question_index < len(questions) - 1:
        current_question_index += 1
        display_question(current_question_index)
    else:
        feedback_label[
            "text"
        ] = f"Game Over!! your total score is:  {score['text'].split(': ')[1]}/{len(questions)}"


def display_question(index):
    if 0 <= index < len(questions):
        question = questions[index]
        qstn_label["text"] = question["question"]
        options = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(options)
        for i, option in enumerate(options):
            option_buttons[i]["text"] = option


# Creates the main window
window = tk.Tk()
window.title("TRIVIA GAME!!!")


qstn_label = tk.Label(window, text="Karibu to Trivia Game!!!", font=("Arial", 14))
qstn_label.pack(pady=11)

score = tk.Label(window, text="score: 0", font=("Arial", 12))
score.pack(pady=10)

feedback_label = tk.Label(window, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

option_buttons = []
for _ in range(4):
    button = tk.Button(
        window,
        text="",
        font=("Arial", 10),
        width=50,
        command=lambda: answer_checker(
            questions[current_question_index], button["text"], score
        ),
    )
    button.pack(pady=20)
    option_buttons.append(button)
    next_button = tk.Button(
        window, text="Next", font=("Arial", 12), width=25, command=nxt_question
    )
next_button.pack(pady=10)
questions = trivia_questions(
    amount=10, category=9, difficulty="medium", type="multiple"
)
current_question_index = 0

# Show the first question


display_question(current_question_index)

# Start the GUI event loop
window.mainloop()
