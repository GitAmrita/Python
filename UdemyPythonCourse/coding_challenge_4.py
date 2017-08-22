def get_user_input():
    weight = input("Enter weight: ")
    height = input("Enter height: ")
    return float(weight), float(height)


def calculate_bmi():
    values = get_user_input()
    weight = values[0]
    height = values[1]
    bmi = weight/height**2
    return bmi

print calculate_bmi()