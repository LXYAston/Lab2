def calculate_bmi(height, weight):
    print("Height = " , height)
    print("Weight = " + str(weight))
    bmi = weight/(height ** 2)
    print("Your BMI is :" + str(bmi))
    if bmi < 18.5:
        print("Weight class: Under Weight")
    elif bmi > 25.0:
        print("Weight class: Over Weight")
    else:
        print("Weight class: Normal Weight")    

calculate_bmi(weight=57, height=1.73)
calculate_bmi(weight=97, height=1.73)
calculate_bmi(weight=37, height=1.73)
