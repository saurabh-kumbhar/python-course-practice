print("Enter weight: e.g 150-lbs or 68-kgs")
input_value = input()

weight = int(input_value.split("-")[0])
unit = input_value.split("-")[1]

if unit.lower() == "lbs":
    print(f"Weight in kgs: {weight / 2.205}")
elif unit.lower() == "kgs":
    print(f"Weight in lbs {weight * 2.205}")
else:
    print("Invalid unit")
