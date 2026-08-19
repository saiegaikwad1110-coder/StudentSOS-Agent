def quiz():
    """Run a 5-question multiple-choice quiz"""

    # Initialize score
    score = 0

    # Quiz questions
    questions = [
        {
            "question": "What is the correct way to create a variable in Python?",
            "options": ["var x = 5", "x = 5", "5 = x", "declare x = 5"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a valid Python data type?",
            "options": ["integer", "string", "boolean", "All of the above"],
            "answer": "D"
        },
        {
            "question": "What does the input() function do?",
            "options": [
                "Outputs text",
                "Gets user input as a string",
                "Creates a variable",
                "Performs calculations"
            ],
            "answer": "B"
        },
        {
            "question": "Which symbol is used for addition in Python?",
            "options": ["add", "++", "+", "&"],
            "answer": "C"
        },
        {
            "question": "What will print(5 / 2) output in Python 3?",
            "options": ["2", "2.5", "2.0", "Error"],
            "answer": "B"
        }
    ]

    # Run each question
    for i in range(len(questions)):

        print(f"\n--- Question {i + 1} of {len(questions)} ---")
        print(questions[i]["question"])

        # Display options
        option_letters = ["A", "B", "C", "D"]

        for j in range(len(questions[i]["options"])):
            print(f"{option_letters[j]}. {questions[i]['options'][j]}")

        # Get answer
        user_answer = input("\nYour answer (A/B/C/D): ").upper()

        # Check answer
        if user_answer == questions[i]["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! Correct answer is {questions[i]['answer']}.")

    # Final result
    print("\n" + "=" * 40)
    print(f"Quiz Complete! Your Score: {score}/{len(questions)}")

    # Percentage
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage}%")

    # Feedback
    if score == len(questions):
        print("Perfect! You're a Python expert!")
    elif score >= 4:
        print("Great job! You know Python well!")
    elif score >= 3:
        print("Good effort! Keep learning!")
    else:
        print("Keep practicing and you'll improve!")

    print("=" * 40)


# Run quizs
if __name__ == "__main__":
    quiz()