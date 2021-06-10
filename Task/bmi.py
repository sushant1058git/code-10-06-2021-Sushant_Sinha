import json
from prettytable import PrettyTable

# Reading JSON Files
data = json.load(open('sample.json'))

# Creating Table
myTable = PrettyTable()

# Defining Fields
myTable.field_names = ["BMI", "BMI_Category", "Health_Risk"]

count = 0


def person_data(height, weight):
    bmi = weight / (height / 100) ** 2
    bmi = round(bmi, 2)
    return bmi


# Passing each record one by one
for person in data['record']:
    BMI = person_data(person['HeightCm'], person['WeightKg'])

    if BMI <= 18.4:
        BMI_Category = "underweight"
        Health_Risk = "Malnutrition"
        myTable.add_row([BMI, BMI_Category, Health_Risk])

    elif 18.5 <= BMI <= 24.9:
        BMI_Category = "Normal Weight"
        Health_Risk = "Low Risk"
        myTable.add_row([BMI, BMI_Category, Health_Risk])

    elif 25 <= BMI <= 29.9:
        BMI_Category = "Overweight"
        Health_Risk = "Enhanced Health risk"
        myTable.add_row([BMI, BMI_Category, Health_Risk])
        count += 1

    elif 30 <= BMI <= 34.9:
        BMI_Category = "Moderately Obese"
        Health_Risk = "Medium Health Risk"
        myTable.add_row([BMI, BMI_Category, Health_Risk])

    elif 35 <= BMI <= 39.9:
        BMI_Category = " Severely Obese"
        Health_Risk = "High Health Risk"
        myTable.add_row([BMI, BMI_Category, Health_Risk])

    else:
        BMI_Category = " Very Severely Obese"
        Health_Risk = "Very High Health Risk"
        myTable.add_row([BMI, BMI_Category, Health_Risk])

# Printing complete Table
print(f" Person Details :\n {myTable}")

# Printing number of overweight person
print(f"Total number of Overweight people is : {count}")
