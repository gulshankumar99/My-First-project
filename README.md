# Online Examination System

**PS No.:** 55

A simple command-line multiple-choice examination system written in Python. It presents questions one at a time, validates the user's input, and displays a scored result at the end.

## Features

- Multiple-choice questions (options a–d) stored as a list of dictionaries
- Input validation: only `a`, `b`, `c`, `d`, or `s` are accepted
- Option to skip a question with `s`
- Automatic scoring (2 marks per correct answer, no negative marking)
- Final report showing correct, wrong, and skipped counts, score, percentage, and Pass/Fail status
- Clean, modular structure using separate functions for each stage

## Requirements

- Python 3.6 or higher
- No external libraries required

## How to Run

```bash
python onlin_examination.py
```

## How It Works

1. The exam displays a header with the total questions and marks.
2. Each question is shown with its options.
3. Enter your answer (`a`/`b`/`c`/`d`), or `s` to skip. Invalid input prompts you again.
4. After the last question, the result summary is displayed.

## Scoring Rules

| Item                | Value        |
|---------------------|--------------|
| Total questions     | 5            |
| Marks per question  | 2            |
| Total marks         | 10           |
| Negative marking    | None         |
| Skipped questions   | 0 marks      |
| Pass percentage     | 40% or above |

## Sample Output

```
========== ONLINE EXAMINATION SYSTEM ==========
Total Questions: 5
Marks per Question: 2
Total Marks: 10
Enter 's' to skip a question.
================================================

Q1. What is the capital of India?
a. Mumbai
b. New Delhi
c. Kolkata
d. Chennai
Enter your answer (a/b/c/d/s): b

...

========== EXAM RESULT ==========
Correct: 4
Wrong: 1
Skipped: 0
Score: 8/10
Percentage: 80.00%
Result: Pass
=================================
```

## Code Structure

| Function             | Purpose                                                        |
|----------------------|----------------------------------------------------------------|
| `questions`          | List of dictionaries holding each question, options, and answer |
| `conduct_exam()`     | Asks questions, validates input, and tallies correct/wrong/skipped |
| `calculate_result()` | Computes score, percentage, and Pass/Fail                      |
| `display_result()`   | Prints the final result summary                                |
| `main()`             | Runs the exam from start to finish                             |

## Adding or Editing Questions

Add a new dictionary to the `questions` list:

```python
{
    "question": "Q6. Your question here?",
    "options": {
        "a": "Option A",
        "b": "Option B",
        "c": "Option C",
        "d": "Option D"
    },
    "answer": "a"
},
```

If you change the number of questions, also update the hardcoded values in `conduct_exam()` (the header text) and `calculate_result()` (`total_marks`), as well as the `/10` in `display_result()`.

## Possible Improvements

- Calculate total questions and marks automatically from the `questions` list
- Shuffle question and option order
- Add a timer for the exam
- Save results to a file or database
- Add user login and multiple exam sets
- Build a GUI or web version

## Author

Add your name here.
