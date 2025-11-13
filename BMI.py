def calculate_bmi(height, weight):
    print("Height: ", height) #can also use str(height) instead of ,height 
    print("weight: ", weight)
    weightno = 0
    bmi = weight/height**2
    if bmi < 18.5:
        weightno = -1
        weightclass = "under weight"
    if bmi > 25.0:
        weightno = 1
        weightclass = "over weight"
    else:
        weightno = 0
        weightclass = "normal weight"
    print("bmi : ",bmi, "weight class:", weightclass, "value: ",weightno)
    return weightno

print(calculate_bmi(1.67, 70))
