#allows time delays (in seconds)
#the delays do absolutely nothing, but i'm keeping them because they look visually appealing.
import time

#set up variables
gradeCounter = 0

#introduction & instructions
print("Hello, welcome to the Archbishop MacDonald eligibility determinator.")
time.sleep(1)
print("This program will calculate your grades to see if they're high enough.")
time.sleep(1)
print("Enter your grades below when prompted, as an integer. Do not include percentages.""\n")
time.sleep(1)

#sets variables to integer version of user inputs
math = int(input("Please enter your math grade: "))
social = int(input("Please enter your social studies grade: "))
science = int(input("Please enter your science grade: "))
english = int(input("Please enter your english grade: "))
religion = int(input("Please enter your religion grade: "))

#gives info.
print("\n" "Calculating grades... ")
print("A minimum of 75% or above in all inputted grades is required.""\n")
time.sleep(1)

#grade list + names
classes = [
    math,
    social,
    science,
    english,
    religion,

    #variants of the subject names for the results sequence
    "math", "social studies", "science", "English", "religion",
    "Math", "Social studies", "Science", "English", "Religion"
]

#grade determination
#checks each grade, determines if they meet criteria
for i in range(5):
    #locates item on list and gets input and associated name
    print(str(classes[gradeCounter + 10]) + " = " + str(classes[gradeCounter]) + "%")
    time.sleep(.5)
    #loop will continue if grade is >= to 75
    #exits program is grade is less than 75
    if classes[gradeCounter] >= 75:
        print("Congratulations, your " + str(classes[gradeCounter + 5]) + " grade is high enough!")     
    else:
        accepted = 0
        print("Sorry, your " + str(classes[gradeCounter + 5]) + " grade is too low.")
        
        #rejected results
        time.sleep(1.5)
        print("\n""You are not eligible for acceptance into Archbishop MacDonald.")
        time.sleep(1)
        exit()
    gradeCounter = gradeCounter + 1
    time.sleep(.5)

#accepted results
time.sleep(.5)
print("\n""Your grades are eligible for acceptance into Archbishop MacDonald.")
time.sleep(1)
exit()
