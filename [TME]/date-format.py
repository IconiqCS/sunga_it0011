#it will ask  the user to enter a date in this format mm/dd/yyyy
print("=============PLEASE ENTER YOUR BIRTHDATE=============" "\n")

print("------------------------------------------------------")
date_input = input("Enter the date (mm/dd/yyyy): ")
print("------------------------------------------------------" "\n")

#it will split the input string into parts (month, day, year)
date_parts = date_input.split("/")

#it will convert the parts into separate variables
month = int(date_parts[0])  #convert month to an integer
day = int(date_parts[1])    #convert day to an integer
year = int(date_parts[2])   #convert year to an integer

#create a list of month names, where index 1 corresponds to "January", etc.
months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#get the month name using the month number
month_name = months[month]

print("=====================OUTPUT STAGE=====================" "\n")

print("------------------------------------------------------")
print("You entered the following: " + month_name + " " + str(day) + ", " + str(year))#formatted data output
print("------------------------------------------------------")