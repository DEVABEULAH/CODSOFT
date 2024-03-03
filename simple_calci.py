def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    if num_2 == 0:
        raise ValueError("Cannot divide by zero")
    return num_1 / num_2
def remainder(num_1, num_2):
    return num_1 % num_2

print("Select operation:")
print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")
print("5) Remainder")

while True:
    option = input("Enter choice (1 2 3 4 5): ")

    if option in ('1', '2', '3', '4', '5'):
        N_1 = float(input("Enter first number: "))
        N_2 = float(input("Enter second number: "))

        if option == '1':
            print(N_1, "+", N_2, "=", add(N_1, N_2))

        elif option == '2':
            print(N_1, "-", N_2, "=", subtract(N_1, N_2))

        elif option == '3':
            print(N_1, "*", N_2, "=", multiply(N_1, N_2))

        elif option == '4':
            try:
                print(N_1, "/", N_2, "=", divide(N_1, N_2))
            except ValueError as e:
                print(e)
                continue
        elif option == '5':
            print(N_1, "%", N_2, "=", remainder(N_1, N_2))
         # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (YES/NO): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
