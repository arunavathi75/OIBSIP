print("===== BMI Calculator =====")

while True:
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than 0.")
            continue

        bmi = weight / (height ** 2)

        print("\nYour BMI is:", round(bmi, 2))

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal Weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

        break

    except ValueError:
        print("Invalid input! Please enter numeric values only.")