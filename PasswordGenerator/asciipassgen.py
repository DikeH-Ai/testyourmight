import random
"""
    A random thought of using the random module and ascii values
    to generate passwords
"""

"""
    Strong password specifications:
        6-12 characters long 
        Upper and lowwer case letters
        Digits
        special characters 
""" 
def asciipassgen():
    # create a password variable to an empty string
    password = ""  
    # setup a for loop withing the range of random 7, 17
    num = random.choice(range(7,17))
    lowerval = 0
    upperval = 0
    spcVal = 0
    while True:
        if len(password) == num:
            break
    #     each loop calls the random function to select a number within the range of all ascii characters
        asciiVal = random.choice(range(20,126))
        if asciiVal == 32:
            continue

        if len(password) > 4:
            for i in password:
                if i.islower():
                    lowerval += 1
                elif i.isupper():
                    upperval += 1
                elif not i.isspace():
                    spcVal += 1
            if lowerval < 2:
                continue
            if upperval < 2:
                continue
            if spcVal < 2:
                continue
    # append to the empty string
        password += chr(asciiVal)
    print(password)

if __name__ == "__main__":
    asciipassgen()