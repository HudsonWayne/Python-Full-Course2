weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds(K or L): ")

if unit.upper() == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit.upper() == "L":
    weight = weight / 2.205
    unit = "kgs."
else:
    print(f"Invalid {unit}")
    print(f"Your weight is {weight}")