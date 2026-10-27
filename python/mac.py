#allows delays :)
#the delays do absolutely nothing, but i'm keeping them because they look visually pleasing.
import time

#set up variables
gradeTotal = 0
gradeCounter = 0

#intro
print("Hello, welcome to the Archbishop MacDonald eligibility determinator.")
time.sleep(1)
print("This program will calculate your grades to see if they're high enough." "\n")
time.sleep(1)

#grade inputs
math = input("Please enter your math grade: ")
social = input("Please enter your social studies grade: ")
science = input("Please enter your science grade: ")
english = input("Please enter your english grade: ")
religion = input("Please enter your religion grade: ")

classes = [
    math,
    social,
    science,
    english,
    religion
]

#gives info.
print("\n" "Calculating grades... ")
print("A minimum of 75% or above in all inputted grades is required.""\n")
time.sleep(1)

#converts inputs to int
math = int(math); social = int(social); science = int(science); english = int(english); religion = int(religion)

#input list + names
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

#checks each grade, determines if they meet criteria
#exits program is grade is less than 75
for i in range(5):
    print(str(classes[gradeCounter + 10]) + " = " + str(classes[gradeCounter]) + "%")
    time.sleep(.5)
    if classes[gradeCounter] >= 75:
        print("Congratulations, your " + str(classes[gradeCounter + 5]) + " grade is high enough!")
    else:
        accepted = 0
        print("Sorry, your " + str(classes[gradeCounter + 5]) + " grade is too low.")
        
        #rejected results
        time.sleep(1.5)
        print("\n""You are not eligible for acceptance into Archbishop MacDonald.")
        exit()
    gradeCounter = gradeCounter + 1
    time.sleep(.5)

time.sleep(.5)

#accepted results
print("\n""Your grades are eligible for acceptance into Archbishop MacDonald.")
exit()
