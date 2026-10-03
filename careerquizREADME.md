# Career Quiz CLI 

An interactive command-line interface (CLI) application built in Python that guides users through a series of 10 career preference questions to determine their ideal technology career path between **Software Engineering**, **Data Science**, and **Cybersecurity**.

---

## Project Overview

The **Career Quiz CLI Tool** is designed as a lightweight, zero-dependency Python script. It presents users with 10 multiple-choice questions covering problem-solving interests, daily workday preferences, volunteer projects, and long-term career impacts. Points are dynamically aggregated in a dictionary, providing a recommended career based on the career with the highest score

---

## Key Features

* **No external Dependencies**: Uses only standard built-in Python constructs (`dict`, `list`, `tuple`, `str`, `int`, loops, and conditionals) — no external package installation required.
* **10 Career focus Questions**: Covers problem-solving preferences, technical topics, daily work environments, project types, sense of accomplishment, key skills, organizational impact (e.g., Telecel Ghana, CareerGhana), volunteering, and learning paths .
* **Input Validation**: Strips extra whitespace (`.strip()`), converts input to uppercase (`.upper()`), and uses a `while` loop to enforce valid options (`A`, `B`, or `C`) .
* **Dynamic Score Tracking**: Tracks scores in a dictionary (`scores`) and determines the top career track using `max(scores, key=scores.get)` .
* **Terminal Output**: Formatted headers, clear option listings, and an easy-to-read summary breakdown.

---

## Data Architecture & Concepts

| Data Structure / Concept | Implementation in Code |
| :--- | :--- |
| **`dict` (Dictionary)** | Tracks scores (`scores = {"Software Engineering": 0, "Data Science": 0, "Cybersecurity": 0}`) and defines question structures . |
| **`list` (List)** | Stores the 10 question dictionaries in order. |
| **`tuple` (Tuple)** | Pairs option descriptions with target career categories: `("Building interactive web applications", "Software Engineering")` [2]. |
| **`str` (String)** | Stores questions, option labels, and user inputs . |
| **Input Sanitization** | Uses `.strip().upper()` to sanitize user input . |
| **Validation Loop** | `while choice not in q["options"]:` ensures valid user entries. |

---

## Source Code (`careerquiz.py`)

```python
def runcareerquiz():
    print("<=== Welcome to the CPath Quiz ===>")
    print("Answer the questions below to find your recommended career path!\n")

    # Score tracker for each career category
    scores = {
        "Software Engineering": 0,
        "Data Science": 0,
        "Cybersecurity": 0
    }

    # Ten Multiple choice questions
    questions = [
        {
            "prompt": "1. What kind of problem do you enjoy solving most?",
            "options": {
                "A": ("Building interactive web applications", "Software Engineering"),
                "B": ("Analyzing trends and finding patterns in numbers", "Data Science"),
                "C": ("Identifying security flaws and protecting systems", "Cybersecurity")
            }
        },
        {
            "prompt": "2. Which topic interests you the most?",
            "options": {
                "A": ("Object-oriented programming and software design", "Software Engineering"),
                "B": ("Statistics, charts, and predictive modeling", "Data Science"),
                "C": ("Encrypting algorithms and network protocols", "Cybersecurity")
            }
        },
        {
            "prompt": "3. How would you like to spend your ideal workday?",
            "options": {
                "A": ("Developing new features for a product", "Software Engineering"),
                "B": ("Monitoring network activity and auditing system security", "Cybersecurity"),
                "C": ("Working with large datasets to extract insights", "Data Science")
            }
        },
        {
            "prompt": "4. Which project sounds most exciting to build?",
            "options": {
                "A": ("A vulnerability scanner for web servers", "Cybersecurity"),
                "B": ("A dashboard visualizing global trends", "Data Science"),
                "C": ("A full-stack mobile or desktop app", "Software Engineering")
            }
        },
        {
            "prompt": "5. What result gives you the greatest sense of accomplishment?",
            "options": {
                "A": ("Shipping functional software to active users", "Software Engineering"),
                "B": ("Defending a infrastructure network against cyber threats", "Cybersecurity"),
                "C": ("Discovering a key insight hidden inside complex data", "Data Science")
            }
        },
        {
            "prompt": "6. Which skill do you want to master the most?",
            "options": {
                "A": ("Building predictive models and machine learning algorithms", "Data Science"),
                "B": ("Writing clean and efficient code", "Software Engineering"),
                "C": ("Implementing advanced security measures and protocols", "Cybersecurity")
            }
        },
        {
            "prompt": "7. What kind of team environment do you prefer?",
            "options": {
                "A": ("Coordinating with IT and security teams to protect CareerGhana's Database systems", "Cybersecurity"),
                "B": ("Working with data analysts and statisticians to solve problems facing Telecel Ghana", "Data Science"),
                "C": ("Collaborating with other developers to build new softwares for CareerGhana", "Software Engineering")
            }
        },
        {
            "prompt": "8. Which project would you like to work on as a volunteer?",
            "options": {
                "A": ("Teach students the basics of programming", "Software Engineering"),
                "B": ("Teach students in a local school about emerging trends in modern-day security", "Cybersecurity"),
                "C": ("Help a local organization analyze data and discover meaningful insights", "Data Science")
            }
        },
        {
            "prompt": "9. What kind of impact do you want to make in your career?",
            "options": {
                "A": ("Creating innovative software solutions that improve user experiences", "Software Engineering"),
                "B": ("Driving data-informed decisions that shape business strategies", "Data Science"),
                "C": ("Safeguarding digital assets and protecting sensitive information", "Cybersecurity")
            }
        },
        {
            "prompt": "10. Which learning path appeals to you the most?",
            "options": {
                "A": ("Mastering programming languages and software development frameworks", "Software Engineering"),
                "B": ("Gaining expertise in statistical analysis and machine learning techniques", "Data Science"),
                "C": ("Becoming proficient in ethical hacking and Penetration testing", "Cybersecurity")
            }
        }
    ]

    # Question and input loop
    for q in questions:
        print(q["prompt"])

        for option, (desc, _) in q["options"].items():
            print(f" [{option}] {desc}")

        choice = input("Select an option (A, B, or C): ").strip().upper()
        while choice not in q["options"]:
            choice = input("Invalid option. Please enter A, B, or C: ").strip().upper()

        selectedcategory = q["options"][choice][1]
        scores[selectedcategory] += 1
        print()

    # Determining the recommended career path based on highest score
    recommended_path = max(scores, key=scores.get)

    # Printing the final recommendation
    print("-" * 40)
    print(f"RECOMMENDED CAREER PATH: {recommended_path}")
    print("-" * 40)
    print(f"Summary breakdown: {scores}\n")

if __name__ == "__main__":
    runcareerquiz()
```

---

## How to Run the Script

### Prerequisites
 Python 3.x installed on your machine.

### Execution Steps
1. Save the code into a file named `careerquiz.py`.
2. Open your terminal or command prompt in that directory.
3. Run the command:

* **Windows**:
  ```powershell
  py careerquiz.py
  ```
* **macOS / Linux**:
  ```bash
  python3 careerquiz.py
  ```

---

## Example Terminal Output

```text
<=== Welcome to the CPath Quiz ===>
Answer the questions below to find your recommended career path!

1. What kind of problem do you enjoy solving most?
 [A] Building interactive web applications
 [B] Analyzing trends and finding patterns in numbers
 [C] Identifying security flaws and protecting systems
Select an option (A, B, or C): A

... [Questions 2–10] ...

----------------------------------------
RECOMMENDED CAREER PATH: Software Engineering
----------------------------------------
Summary breakdown: {'Software Engineering': 6, 'Data Science': 2, 'Cybersecurity': 2}
```

---

## Customization Guide

### Adding an 11th Question
To extend the quiz, append a new dictionary item to the `questions` list:

```python
{
    "prompt": "11. Your custom question prompt here?",
    "options": {
        "A": ("Description for Software Engineering", "Software Engineering"),
        "B": ("Description for Data Science", "Data Science"),
        "C": ("Description for Cybersecurity", "Cybersecurity")
    }
}
```

### Adding a New Track (e.g., DevOps)
1. Add `"DevOps": 0` to `scores`.
2. Add a `"D"` key with `("Description", "DevOps")` to each question dictionary in `questions`.
3. Update the prompt to accept `"A, B, C, or D"`.
