# Ask user for width and loop 
# enter a number that is more than zero.

def num_check(question):
        
    error = "Please enter a valid number/n"

    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error) 




# Main routine goes here
for item in range (0, 2):
    width = num_check("Width: ")
    print(width)

print()

for item in range (0, 2):
    height = num_check("Height: ")
    print(height)