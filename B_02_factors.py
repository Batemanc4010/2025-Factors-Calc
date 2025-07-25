import math

# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
To use this program simply enter an integer between
1 and 200. The program will show the factors of your
chosen integer.

- is a prime number (ie: it has two factors)
- is a perfect square

To exit the program, please type 'xxx'
''')

# Input checker
def num_check(question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:
        response = input(question).lower()
        if response == "xxx":
            return response
        try:
            response = int(response)
            if 1 <= response <= 200:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# Factor finder using square root optimization
def factor_finder(var_to_factor):
    factors = set()
    stop = int(math.sqrt(var_to_factor))

    for i in range(1, stop + 1):
        if var_to_factor % i == 0:
            factors.add(i)
            factors.add(var_to_factor // i)

    return sorted(factors)

# ===== Main Routine Starts Here =====

statement_generator("The Ultimate Factor Finder", "-")

# Show instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue: ")

if want_instructions == "":
    instructions()

# Main loop
while True:
    comment = ""

    # Ask user for number to factor
    to_factor = num_check("\nEnter an integer (or xxx to quit): ")

    if to_factor == "xxx":
        break

    # Special case for 1
    if to_factor == 1:
        all_factors = [1]
        comment = "One is UNITY! It only has one factor: itself."
        heading = "One is special..."
    else:
        all_factors = factor_finder(to_factor)
        heading = f"Factors of {to_factor}"

        # Prime number = 2 factors
        if len(all_factors) == 2:
            comment = f"{to_factor} is a prime number"

        # Perfect square = odd number of total factors
        elif len(all_factors) % 2 == 1:
            comment = f"{to_factor} is a perfect square"

    # Display result
    print()
    statement_generator(heading, "*")
    print("Factors:", all_factors)
    print(comment)

print("\nThank you for using the factors calculator!")