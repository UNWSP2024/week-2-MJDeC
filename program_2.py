#Micah DeCaro, 9/12/24, Average Age
#Program that asks for ages of five friends and computes the average.
def average_age():
    # Get User Input
    age1=float(input('Enter your age, Friend One: '))
    age2=float(input('Enter your age, Friend Two: '))
    age3=float(input('Enter your age, Friend Three: '))
    age4=float(input('Enter your age, Friend Four: '))
    age5=float(input('Enter your age, Friend Five: '))
    # Sum ages
    sum=(age1+age2+age3+age4+age5)
    # Average the ages
    final_average=sum/5.0

    # Print the results
    print(final_average)
# Line which calls the above function.
average_age()
