print("===== MATHEMATICAL CALCULATOR =====")
print("Operations: +, -, *, /, %, **")
while True:
    calculation = input("\nEnter calculation: ")
    try:
        result = eval(calculation)
        print("Result =", result)
    except:
        print("Invalid input")
        continue
    option = input("\nEnter C to clear or OFF to turn off: ").upper()
    if option == "OFF":
        print("Calculator turned off.")
        break
    elif option == "C":
        continue
    else:
        print("Invalid option. Calculator turned off.")
        break