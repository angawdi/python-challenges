# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calculation():
    cal = input('What calculation would you like to do? (add, sub, mult, div)')
    try:
        num1 = int(input('What is the number 1?'))
        num2 = int(input('What is the number 2?'))
    except:
        print('It is not a number')
    result = 0;
    if (cal == 'add'):
        result = num1 + num2
    elif (cal == 'sub'):
        result = num1 - num2
    elif (cal == 'mult'):
        result = num1*num2
    elif (cal == 'div'):
        result = num1/num2
    
    
    print('Your result is: ', result);
