def main():
    grade = int(input ("What's your CIS102 grade?"))
    if grade == 100:
       print ('A. Super Star!')
    elif grade < 100 and grade >= 90:
       print ('B. Great job!')
    elif grade < 90 and grade >= 80:
       print ('C. Good job!')
    elif grade < 80 and grade >= 70:
       print ('D. Do better next time!')
    elif grade < 70 and grade >= 20:
       print ('F. Talk to me after class')
    elif grade < 20 and grade >= 0:
       print ('Quit already')
    else: 
       print('Wrong input')
main()