def calculator():
    ask = (
        input("\n\nWhat do you wanna do select the operation please from DMAS:")
        .lower()
        .strip()
    )

    num1 = input("\nEnter the first number (Is the divisor if selected D):")
    num2 = input("Enter the second number (Is the dividend if selected D):")

    if num1.isnumeric() and num2.isnumeric():
        num1 = float(num1)
        num2 = float(num2)

    divide = lambda: print(f"\nThe Quotient is:{num2/num1}\n")

    multiply = lambda: print(f"\nThe Product is:{num1*num2}\n")

    add = lambda: print(f"\nThe Sum is:{num1+num2}\n")

    subtract = lambda: print(f"\nThe Difference is:{num1-num2}\n")

    if ask == "d" or ask == "divide":
        divide()

    elif ask == "m" or ask == "multiply":
        multiply()

    elif ask == "a" or ask == "add":
        add()

    elif ask == "s" or ask == "subtract":
        subtract()

    else:
        print(
            "Invalid operation selected. Please choose from DMAS (Divide, Multiply, Add, Subtract)."
        )


if __name__ == "__main__":
    calculator()

    while True:
        again = (
            input("Do you want to do another calculation? (yes/no): ").strip().lower()
        )

        if again == "yes":
            calculator()

        elif again == "no":
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
