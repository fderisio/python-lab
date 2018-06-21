def bmi_result(num):
    if num < 18.5:
        print('Underweight')
    if 18.5 >= num <= 25:
        print('Normal')
    if num > 25:
        return 'Overweight'


class KgException:
    pass


class CmException:
    pass


def bmi_calculator():
    while True:
        try:
            height = int(input('What is your height (in CM)?'))
            weight = float(input('What is your weight (in KG)?'))
            break
        except ValueError:
            print('Please enter a valid number.')
    bmi = round(weight / ((height / 100) ** 2), 2)
    print('Your BMI is:', bmi, bmi_result(float(bmi)))
    return bmi


bmi_calculator()
