# Step 1: Get User Input
'''To actually enter a sequence of Roman numerals, we need to ask the user for input.
This can be done with the built-in input() function'''

numeral_input = input("Enter the roman numerals you want to convert: ").upper()

# Step 2: Define roman_to_int() Function
'''Now that we have the user submitting input,
let's define a roman_to_int() function to translate the Roman numerals into an integer value'''

def roman_to_int(numeral):

    '''In the function definition, we are specifying a numeral parameter that is a string
    of the Roman numeral we want to convert.'''

    # At the start, we need to create a final_answer integer variable,
    # initialized at 0, for storing our converted integer
    final_answer = 0

    # First, handle subtractive combinations
    if "CM" in numeral:
        final_answer += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        final_answer += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        final_answer += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        final_answer += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        final_answer += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        final_answer += 4
        numeral = numeral.replace("IV", "")

    '''Inside the function, let’s loop through each character in the numeral string
    and convert them to integers!'''

    # Next let's create a for loop that repeats a particular block of code
    # for all the characters of the numeral variable (our user input)
    for i in numeral:

        # Now, inside the loop, let’s use if-elif statements
        # to check Roman numeral values and add them
        if i == "M":
            final_answer += 1000
        elif i == "D":
            final_answer += 500
        elif i == "C":
            final_answer += 100
        elif i == "L":
            final_answer += 50
        elif i == "X":
            final_answer += 10
        elif i == "V":
            final_answer += 5
        elif i == "I":
            final_answer += 1

    '''The final_answer will be returned at the end of the function'''
    return final_answer


# Step 3: Call the function and print the result
print("The roman numerals you entered translates to:",
      roman_to_int(numeral_input))

"""
V        → 5
IV       → 4
IX       → 9
XII      → 12
MCMXCIV  → 1994

"""
