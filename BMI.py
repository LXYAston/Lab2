def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height** 2)
    print("Your BMI is :" + str(bmi))
    if(bmi < 18.5):
        print("Weight class: Under Weight")
    if(18.5 <= bmi <= 25.0):
        print("Weight class: Normal Weight")
    else:
        print("Weight class: Over Weight")

calculate_bmi(weight=57, height=1.73)