print("Welcome to BMI calculator.")


Gender = input("Put in your gender: ")
Weight = input("Put in your weight in KG: ")
Height = input("Put in your height in CM: ")

Weight = float(Weight)
Height = float(Height)

Height_Squared = Height * Height
BMI = Weight / Height_Squared
BMI_Formula_Completed = BMI * 10000


BMI_Formula_Completed = str(BMI_Formula_Completed)

print("You have a BMI score of " + BMI_Formula_Completed + ".")

BMI_Formula_Completed = float(BMI_Formula_Completed)

if BMI_Formula_Completed <= 18.4:
    print("You are underweight, your health risk is malnutrition risk.")
elif BMI_Formula_Completed <= 18.5:
    print("You are normal weight, your health risk is low risk.")
elif BMI_Formula_Completed <= 25:
    print("You are overweight, your health risk is enhanced risk.")
elif BMI_Formula_Completed >= 30:
    print("You are moderately obese , your health risk is medium risk.")
elif BMI_Formula_Completed >= 35:
    print("You are severely obese , your health risk is high risk.")
elif BMI_Formula_Completed >= 40:
    print("You are very severley obese , your health risk is very high risk.")

#over weight
var = [23.7,22.4,29.4]
dict ={}
for x in var:
    if x not in dict:
        dict[x]=" BMI_OverWeight"
    else:
        dict[x]="BMI_Category"

print(dict)