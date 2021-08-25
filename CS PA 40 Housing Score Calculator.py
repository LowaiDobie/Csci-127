#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 28, 2020
#This program prints: Housing Score Calculator


answers=[]
def computeScore(answers):
    score=0
    
    score+=answers[0]
    
    if answers[1]>23:
        score+=1
    
    if answers[2]=="Yes":
        score-=1
    
    score+=answers[3]
    
    if answers[4]>3.5:
        score+=1
    
    return score
def main():
    print("-----------------------------------")
    print("HOUSING SCORE CALCULATOR")
    print("-----------------------------------")
    print()
    print("QUESTION 1")
    answers.append(int(input("What year are you?(1,2,3,4): ")))

    print("QUESTION 2")
    answers.append(int(input("How old are you?: ")))

    print("QUESTION 3")
    answers.append(input("Are you currently on probation? (Yes or No): "))

    print("QUESTION 4")
    answers.append(int(input("Are you Part-time or Full-time? (0 or 1): ")))

    print("QUESTION 5")
    answers.append(float(input("What is your GPA?: ")))
    score=computeScore(answers)
    print()
    print("-----------------------------------")
    print("Your housing score is: ",score)
    print("-----------------------------------")

if __name__ == "__main__":
    main()

