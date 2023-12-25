# This is a project developed by devhorla a.k.a Horlalaycon @ Github
import calendar
import time


print("Welcome, this calendar displays full year and the months or just a month\n")
# welcome statement
# this is a calendar that display the year or month based on which the user want to check
#
purpose = input("what do you want to check (y = year or m = month or t = time)\n")
#
# if the purpose is equal to (y/m or Y/M/ or year/month) the operation will be executed
# else the operation will continue to loop until it is true
#
if purpose == "y" or purpose == "m" or purpose == "t" or purpose == "time" or purpose == "year" or purpose == "month" or purpose == "time":
    # if purpose is equal to either (y/m or Y/M/ or year/month) the operation will run
    #
    if purpose == "y" or purpose == "year":
        cal_year = int(input("Enter the Year:\n"))
        print(calendar.calendar(cal_year, 5))
        # time
        current_time = time.ctime()
        print("the current date & time is: " + current_time)
    # else if purpose is equal to m
    #
    elif purpose == "m" or purpose == "month":
        cal_month = int(input("Enter The month:\n"))
        cal_year = int(input("Enter the Year:\n"))
        print(calendar.month(cal_year, cal_month, 5))
        # time
        current_time = time.ctime()
        print("the current date & time is: " + current_time)
    # time
    elif purpose == "t" or purpose == "time":
        current_time = time.ctime()
        print("the current date & time is: " + current_time)
#

else:
    # if the operation is not equal to either (y/m or Y/M or year/month)
    # the operation will loop until the condition is met
    #
    while purpose != "y" or purpose != "m" or purpose != "t" or purpose != "time" or purpose != "year" or purpose != "month":
        purpose = input("you have to input y or year, m or month, t or time !!!)\n")
        if purpose == "y" or purpose == "year":
            cal_year = int(input("Enter the Year:\n"))
            print(calendar.calendar(cal_year, 5))
            # time
            current_time = time.ctime()
            print("the date & time is: " + current_time)
            break
        elif purpose == "m" or purpose == "month":
            cal_month = int(input("Enter The month:\n"))
            cal_year = int(input("Enter the Year:\n"))
            print(calendar.month(cal_year, cal_month, 5))
            # time
            current_time = time.ctime()
            print("the current date & time is: " + current_time)
            break
        #
        elif purpose == "t" or purpose == "time":
            current_time = time.ctime()
            print("the current date & time is: " + current_time)
            break
