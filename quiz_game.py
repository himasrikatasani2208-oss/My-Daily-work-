print("Welcome to the Python Quiz Game!")
print("Answer the following questions.\n")

score = 0


print("1. Python is a ____ language?")
print("a) Programming")
print("b) Cooking")
print("c) Driving")

answer = input("Enter your answer (a/b/c): ")

if answer == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is: Programming\n")


print("2. What is 5 + 3 ?")
print("a) 6")
print("b) 8")
print("c) 10")

answer = input("Enter your answer (a/b/c): ")

if answer == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is: 8\n")


print("3. Which keyword is used to define a function in Python?")
print("a) func")
print("b) def")
print("c) function")

answer = input("Enter your answer (a/b/c): ")

if answer == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is: def\n")


print("Quiz Finished!")
print("Your Final Score:", score, "/3")

if score == 3:
    print("Excellent! 🎉")
elif score == 2:
    print("Good Job 👍")
else:
    print("Keep Learning 📚")