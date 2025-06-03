def main():

    score1 = float(input("Enter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))
    score4 = float(input("Enter score 4: "))
    score5 = float(input("Enter score 5: "))

    average = calAverage(score1, score2, score3, score4, score5)

    print("Score\t\tNumeric Grade\tLetter Grade")
    print("--------------------------------------")
    print("Score 1\t\t", score1, "\t\t", letterGrade(score1))
    print("Score 2\t\t", score2, "\t\t", letterGrade(score2))
    print("Score 3\t\t", score3, "\t\t", letterGrade(score3))
    print("Score 4\t\t", score4, "\t\t", letterGrade(score4))
    print("Score 5\t\t", score5, "\t\t", letterGrade(score5))
    print("--------------------------------------")
    print("Average Score: \t", calAverage(score1, score2, score3, score4, score5), "\t\t", letterGrade(average))

def calAverage(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average
    
def letterGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
main()