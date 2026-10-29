#input
#asks for 5 inputs to be used as parameters later

#the program will not ask for the amount of days in a week
#adding the amount of full and half days negates the need for such a variable
total_days = float(input("How many school days are there in a year? "))
week_full = float(input("How many full days are in 1 week? "))
week_half = float(input("How many half days are in 1 week? "))

full_hours = float(input("\n""How many hours are in a full day? "))
half_hours = float(input("How many hours are in a half day? "))

#process
#calculates total amount of hours based on given parameters
def process(days, full, half, fullhours, halfhours):
    total_hours = (days / (half + full)) * (full * fullhours + half * halfhours) #basically "amount of weeks x hours in a week"
    return(total_hours) #returns results of previous line

#output
#concatenates processed inputs and prints result
print("\n""Based on your inputs, expect a total of " + str(process(total_days, week_full, week_half, full_hours, half_hours)) + " hours in a school year.")