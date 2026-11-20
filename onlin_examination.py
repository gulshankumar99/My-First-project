
# Project: Online Examination System
# PS No.: 55

# Step 1: Store questions in a list of dictionaries

questions = [
    {
        "question": "Q1. What is the capital of India?",
        "options": {
            "a": "Mumbai",
            "b": "New Delhi",
            "c": "Kolkata",
            "d": "Chennai"
        },
        "answer": "b"
    },
    {
        "question": "Q2. Which language is used for Python programming?",
        "options": {
            "a": "HTML",
            "b": "CSS",
            "c": "Python",
            "d": "SQL"
        },
        "answer": "c"
    },
    {
        "question": "Q3. Which data type stores multiple values?",
        "options": {
            "a": "List",
            "b": "Integer",
            "c": "Float",
            "d": "Boolean"
        },
        "answer": "b"
    },
    {
        "question": "Q4. Which keyword is used to define a function?",
        "options": {
            "a": "function",
            "b": "def",
            "c": "fun",
            "d": "define"
        },
        "answer": "b"
    },
    {
        "question": "Q5. Which function displays output in Python?",
        "options": {
            "a": "input()",
            "b": "print()",
            "c": "show()",
            "d": "display()"
        },
        "answer": "b"
    }
]


# Step 2: Function to ask questions

def conduct_exam():

    correct = 0
    wrong = 0
    skipped = 0

    print("\n========== ONLINE EXAMINATION SYSTEM ==========")
    print("Total Questions: 5")
    print("Marks per Question: 2")
    print("Total Marks: 10")
    print("Enter 's' to skip a question.")
    print("================================================")

    for i, q in enumerate(questions):

        print("\n" + q["question"])

        for key, value in q["options"].items():
            print(key + ".", value)

        # Validate user input

        while True:

            user_answer = input("Enter your answer (a/b/c/d/s): ").lower().strip()

            if user_answer in ["a", "b", "c", "d", "s"]:
                break

            else:
                print("Invalid option. Enter a, b, c, d or s to skip.")

        # Check answer

        if user_answer == "s":
            skipped += 1

        elif user_answer == q["answer"]:
            correct += 1

        else:
            wrong += 1

    return correct, wrong, skipped


# Step 3: Function to calculate result

def calculate_result(correct, wrong, skipped):

    score = correct * 2
    total_marks = 10

    percentage = (score / total_marks) * 100

    if percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return score, percentage, result


# Step 4: Function to display final result

def display_result(correct, wrong, skipped, score, percentage, result):

    print("\n========== EXAM RESULT ==========")

    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Skipped:", skipped)

    print("Score:", str(score) + "/10")
    print("Percentage: {:.2f}%".format(percentage))
    print("Result:", result)

    print("=================================")


# Step 5: Main function

def main():

    correct, wrong, skipped = conduct_exam()

    score, percentage, result = calculate_result(
        correct, wrong, skipped
    )

    display_result(
        correct, wrong, skipped,
        score, percentage, result
    )


# Step 6: Run the program

if __name__ == "__main__":
    main()
