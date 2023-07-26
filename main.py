# Input needed to make calculation
name = input('Enter your full name')
gender = input('Enter your Gender (male or female): ')
weight = int(input('Enter your current Weight in lb: '))
height = int(input('Enter your current height in inches: '))
age = int(input('Enter your current age: '))
activity_levels = input('Enter your activity level: ')

print('full name: ', name)
print ('weigt in lb :',weight)
# Calories Calculation for Males
if gender == "male":
    x = weight * 6.23
    y = height * 12.7
    z = age * 6.8
    BMR_for_male = x + y - z + 66
    print('BMR for male:', BMR_for_male)

    if activity_levels == 'sedentary':
        Daily_calorie_need_for_maintain = BMR_for_male * 1.2

    elif activity_levels == 'light':
        Daily_calorie_need_for_maintain = BMR_for_male * 1.375

    elif activity_levels == 'moderate':
        Daily_calorie_need_for_maintain = BMR_for_male * 1.55

    elif activity_levels == 'active':
        Daily_calorie_need_for_maintain = BMR_for_male * 1.725

    print('Daily calorie need for maintenance:', Daily_calorie_need_for_maintain)

# Calories Calculation for Females
elif gender == 'female':
    t = weight * 4.3
    u = height * 4.7
    i = age * 4.7
    BMR_for_female = t + u - i + 655
    print('BMR for female:', BMR_for_female)

    if activity_levels == 'sedentary':
        Daily_calorie_need_for_maintain = BMR_for_female * 1.2

    elif activity_levels == 'light':
        Daily_calorie_need_for_maintain = BMR_for_female * 1.375

    elif activity_levels == 'moderate':
        Daily_calorie_need_for_maintain = BMR_for_female * 1.55

    elif activity_levels == 'active':
        Daily_calorie_need_for_maintain = BMR_for_female * 1.725

    print('Daily calorie need for maintenance:', Daily_calorie_need_for_maintain)




