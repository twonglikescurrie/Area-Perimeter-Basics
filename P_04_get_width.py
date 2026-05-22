# Ask user for width and loop 
# enter a number that is more than zero.

error = "Please enter a valid number/n"

while True:

    try:
        width = float(input("Width: "))

        if width > 0:
            break
        else:
            print(error)
    except ValueError:
        print(error)