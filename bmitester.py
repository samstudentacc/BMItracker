from tracker import BMI
import bmitester

#first benchmark, make the calculation
def testcalc():
    weight = float(180)
    height = float(72)
    bmitest = BMI(weight,height,0)

    kg = weight * 0.45
    meters = height * 0.025
    msquare = meters * meters
    expectedbmi = kg / msquare

    assert bmitest.calcBMI() == expectedbmi

#second benchmark, label what type user is
def testlabel():
    # OFF points: 18.4, 18.4, 25, 24.9, 30, 29.9
    # ON points: 18.5, 18.5, 24.9, 25, 29.9, 30
    offpoints = [18.4,18.4,25,24.9,30,29.9]
    onpoints = [18.5,18.5,24.9,25,29.9,30]
    feedbackoff = []
    feedbackon = []
    for i in range(len(offpoints)):
        userbmioff = BMI(0, 0, offpoints[i])
        userbmion = BMI(0, 0, onpoints[i])
        classoff = userbmioff.getBMIrange()
        classon = userbmion.getBMIrange()

        feedbackoff.append(classoff)
        feedbackon.append(classon)

    #OFF points: under, under, over, normal, obese, over
    #ON points: normal, normal, normal, over, over, obese
    assert feedbackoff[0] == "Underweight"
    assert feedbackoff[1] == "Underweight"
    assert feedbackoff[2] == "Overweight"
    assert feedbackoff[3] == "Normal-weight"
    assert feedbackoff[4] == "Obese"
    assert feedbackoff[5] == "Overweight"
    assert feedbackon[0] == "Normal-weight"
    assert feedbackon[1] == "Normal-weight"
    assert feedbackon[2] == "Normal-weight"
    assert feedbackon[3] == "Overweight"
    assert feedbackon[4] == "Overweight"
    assert feedbackon[5] == "Obese"