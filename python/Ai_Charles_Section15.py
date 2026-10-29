#processes input; calculates hours
#multiplies week by weekly hours
#returns results (as float)
def process(days, full, half, fullhours, halfhours):
    total_hours = (days / week_length) * (full * fullhours + half * halfhours)
    return(total_hours)


#asks for 5 inputs to be used as parameters later
#the program will not ask for the amount of days in a week
#it will instead be created through the addition of week_full and week_half
total_days = float(input("How many school days are there in a year? "))
week_full = float(input("How many full days are in 1 week? "))
week_half = float(input("How many half days are in 1 week? "))
week_length = (week_full + week_half)
full_hours = float(input("\n""How many hours are in a full day? "))
half_hours = float(input("How many hours are in a half day? "))


#calls process function
total_hours = process(total_days, week_full, week_half, full_hours, half_hours)

#output
#concatenates processed inputs and prints result
print("\n""Based on your inputs, expect a total of " + str(total_hours) + " hours in a school year.")

exit() #exit
