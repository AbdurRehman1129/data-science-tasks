quiz = {
"Question": 
    {1: "What is the capital city of Pakistan? ",
    2: "Who is the founder of Pakistan?",
    3: "What is the national flower of Pakistan? ",
    4: "Which of the following is the national animal of Pakistan?",
    5: "In which year did Pakistan become an independent country? "},
"Option":   
    {1: ["A - Lahore", "B - Karachi", "C - Islamabad", "D - Peshawar"],
    2: ["A - Iqbal", "B - Benazir", "C - Quaid-e-Azam", "D - Sir Syed"],
    3: ["A - Rose", "B - Jasmine", "C - Lily", "D - Sunflower"],
    4: ["A - Leopard", "B - Tiger", "C - Markhor", "D - Elephant "],
    5: ["A - 1947", "B - 1950", "C - 1930", "D - 1965"]},
"Answer":   
    {1: "C", 2: "C", 3: "B", 4: "C", 5: "A"},
}
x = 0
score = 0
print("""
            QUIZ ABOUT PAKISTAN
       
NOTE: There will be five questions in this quiz.
Each correct answer worth 10 Scores.
Result will be displayed at END of quiz.""")
for values in quiz["Question"].values():
    x = x+1
    print(f"\nQuestion {x}: {values}")
    for values in quiz["Option"][x]:
        print(values)
    Answer = input("Enter your choice (A, B, C, D) : ").upper()
    if Answer == quiz["Answer"][x]:
        score += 10
    else:
        score = score

if score > 0:
    print(f"\nYOU SCORED {score}\n")
else:
    print(f"\nALL ANSWERS ARE INCORRECT! TRY AGAIN\n")
