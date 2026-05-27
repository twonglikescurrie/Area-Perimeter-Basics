# Function goes here
def num_check(question):

    error = "Please enter a number greater than zero\n"

    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine starts here...

keep_going = ""

while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    length = num_check("Length: ")
    cost = num_check("Cost per meter: $")

    # Calculate perimeter and price for the fence
    perimeter = 2 * (width + length)

    price = perimeter * cost

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input("\nPress <enter> to keep going or any key to quit: ")

print()
print("Thank you for using the calculator")