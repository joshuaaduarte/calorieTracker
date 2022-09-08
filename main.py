# imports 
import csv #used to manipulate csv files
import os
import os.path # used to check if files exist 
# gather initial user information

# Basic Functions
def clear():
    os.system('cls')

# Conversions
lbToKg = 0.45359237
kgTolb = 1/lbToKg
inToCm = 2.54
cmToIn = 1/inToCm
kgToCal = 7700

# ask user to input their first and last name
firstName = input('Enter first name: ')
lastName = input('Enter last name: ')

clear()

# check if previous csv file exists
if os.path.exists('{}_{}.csv'.format(firstName.lower(), lastName.lower())) == True:
    done = True
    goals = True
    print('Welcome Back! Your file already exists.')
else:
    done = False
    goals = False

# asks user for data if csv does not exist
while not done:

    age = int(input('Enter Age: '))

    # ensures input is either m or f
    genderTextOk = False
    while genderTextOk == False:
        gender = input('Enter gender (M/F): ')
        if gender.lower() == 'm':
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
            genderTextOk = True
        elif gender.lower() == 'f':
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        else: 
            print('Input Invalid. Please try again')

    # ensures input is either 1 or 2
    unitTextOk = False
    while unitTextOk == False:
        units = input("Do you use kg or lbs?(1/2) ")
        if units == '1':
            unitTextOk == True
            weight = float(input('Enter Weight: '))
            height = float(input('Enter Height in cm: '))
        elif units == '2':
            unitTextOk == True
            weight = float(input('Enter Weight: ')) * lbToKg
            heightFeet = (input('Enter Height (ft-in): ')).split('-')
            height = ((int(heightFeet[0]) * 12) + int(heightFeet[1])) * inToCm
        else:
            print('Input Invalid. Please try again')

    
    

    print('first name:', firstName, 'last name:', lastName, 'age:', age, 'height:', round(height, 2), 'weight:',
          round(weight, 2))

    correct = input('Does this look right? (Y/N): ')
    if correct.lower() == 'y':
        done = True
    else:
        done = False

# Set goals if csv does not exist
while not goals:
    goalLoss = input("Do you wish to maintain weight, lose fat, lose extreme amount of fat (M/L/E): ")
    if goalLoss.lower() == 'm':
        print("Eat ", bmr, ' calories per day!')
    else:
        if units.lower() == 'kg':
            goalWeight = float(input('Enter goal weight: '))
        else:
            goalWeight = float(input('Enter goal weight: ')) * lbToKg

        caloriesToBurn = (weight - goalWeight) * kgToCal

        if goalLoss.lower() == 'l':
            dailyCalorieIntake = bmr * 0.8
        else:
            dailyCalorieIntake = bmr * 0.6

        weeksToGo = caloriesToBurn / (7 * dailyCalorieIntake)
        if units.lower() == 'kg':
            print('You can get to ', goalWeight, 'kilograms in ', weeksToGo, 'weeks at ', dailyCalorieIntake,
                  'calories per day!')
        else:
            print('You can get to ', goalWeight / lbToKg, 'pounds in ', weeksToGo, 'weeks at ', dailyCalorieIntake,
                  'calories per day!')
    goals = True


# store information within a csv file 
# create csv file 
if os.path.exists('{}_{}.csv'.format(firstName.lower(), lastName.lower())) == False:
    header = ['First Name', ' Last Name', 'Gender','Age', 'Height', 'Weight', 'BMR', 'Goal Weight','Daily Caloric Intake', 'Preferred Units']
    data = [firstName, lastName, gender, age, height, weight, bmr, goalWeight, dailyCalorieIntake, units]
    with open('{}_{}.csv'.format(firstName.lower(), lastName.lower()), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(data)

