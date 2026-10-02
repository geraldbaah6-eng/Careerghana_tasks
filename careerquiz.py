def runcareerquiz():
    print("<=== Welcome to the CPath Quiz ===>")
    print("Answer the questions below to find your recommended career path!\n") 

    #A Score tracker for each career category

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
                "C": ("Becoming proficient in ethical hacking and Penetration testing ", "Cybersecurity") 
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

    # Printing the  final recommendation 
    print("-" * 40) 
    print(f"RECOMMENDED CAREER PATH: {recommended_path}") 
    print("-" * 40) 
    print(f"Summary breakdown: {scores}\n") 

if __name__ == "__main__": 
    runcareerquiz()