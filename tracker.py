#C:\Users\backu\PycharmProjects\BMItracker\tracker.py

print("BMI Tracker 1.0")

'''print("Please input your weight in pounds")
uwieght = input()
print("Please input your height in inches")
uheight = input()'''


class BMI:
    def __init__(self, weight, height, bmi):
        self.weight = float(weight)
        self.height = float(height)
        self.bmi = float(bmi)

    def calcBMI(self):
        #formula for BMI
        kg = self.weight * 0.45
        meters = self.height * 0.025
        msquare = meters * meters
        bmi = kg/msquare
        self.bmi = bmi
        return bmi

    # E = 0.1
    def getBMIrange(self):
        if self.bmi == 0:
            return "Error: run calcBMI()"
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi <= 24.9:
            return "Normal-weight"
        elif 25 <= self.bmi <= 29.9:
            return "Overweight"
        elif self.bmi >= 30:
            return "Obese"
        else:
            return "Error"