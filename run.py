import gspread
from collections import Counter


days = ("Monday", "Tuseday", "Wensday", "Thursday", "Fryday")

yes_or_no = {}

stock = {"laptops": 150, "phones": 75, "TV:s": 100, "Coustom_PC:s": 225,\
"coffe_machines": 150, "frezzers": 100}


def get_week_days():

    print("\n✭  Welcome to the solo salary application ! ✭  \n")
    print("Enter either yes or no as an awnser... \n")
    for i in days:
        """loop trow all the days in the days variabel"""   
        """removes spaces , transform to lowercase to not raise error""" 
        while True:
            print(f"Did you work on {i} ? \n")
            answer = input("\n").strip().lower()
            if not answer.isalpha() or answer is ["yes", "no"]:
                print(f"Value Error : {answer} , please follow the instructions\
                     above and insert the correct input")
                print(" ! __________________________ ! \n")    
                print(f"    Did you work on {i} ? \n ")
                print(" ! __________________________ ! \n")
            if answer.isalpha() or answer is ["yes", "no"]:
                break
        yes_or_no[i] = answer
   
    
def sales_comision():
   
    print("Lets see what youv sold this week")
    for Y in stock.keys():
        print(f"did you sell one or more {Y}")
        awnser2 = input("\n").strip().lower()
        if awnser2.isalpha() or awnser2 is ["yes"]:
            print("how many ?")
            num_items = int(input())
        else:
            continue     


get_week_days()


sales_comision()        



""" calling  the function for input and validation\
     for what days the user have worked"""

work_week = Counter(yes_or_no.values())
"""checking the amount of yes values from the user\
     input stored in the yes_or_no variabel"""


days_worked = work_week["yes"]
"""extrecting the nummber of "yes":es and storeing it in a variabel"""

print(f"You have worked for a total of {days_worked} days this week! \n")
"telling the user on how many days of the week they have worked"


payment = work_week["yes"] * 200
"""multeplying the days worked with the dayly salary"""


print(f"You have earned a total of {payment}£  this week \n")
"""infroming the user on how much they have earned this week""" 

  