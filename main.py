# gather initial user information


# Conversions
lbToKg = 0.45359237
inToCm = 2.54
kgToCal = 7700

done = False
while not done:
    firstName = input('Enter first name: ')
    lastName = input('Enter last name: ')
    age = int(input('Enter Age: '))
    gender = input('Enter gender (M/F): ')
    units = input("Do you use kg or lbs? ")
    if units.lower() == 'kg':
        weight = float(input('Enter Weight: '))
        height = float(input('Enter Height in cm: '))
    else:
        weight = float(input('Enter Weight: ')) * lbToKg
        heightFeet = (input('Enter Height (ft-in): ')).split('-')
        height = ((int(heightFeet[0]) * 12) + int(heightFeet[1])) * inToCm

    if gender.lower() == 'm':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    print('first name:', firstName, 'last name:', lastName, 'age:', age, 'height:', round(height, 2), 'weight:',
          round(weight, 2), 'BMR:', round(bmr, 2))

    correct = input('Does this look right? (Y/N): ')
    if correct.lower() == 'y':
        done = True
    else:
        done = False

# Set goals
goals = False

while not goals:
    goalLoss = input("Do you wish to maintain weight, lose fat, lose extreme amount of fat (M/L/E): ")
    if goalLoss.lower() == 'm':
        print("Keep on doin' what your doin':)")
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
