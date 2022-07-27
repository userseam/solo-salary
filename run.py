import gspread
from collections import Counter


days = ("Monday", "Tuseday", "Wensday", "Thursday", "Fryday")
yes_or_no = {}


def get_week_days():
    print("Welcome to the solo salary application ! \n")
    print("Enter either yes or no as an awnser... \n")

    for i in days:
        """loop trow all the days in the days variabel"""   
        print(f"Did you work on {i} ? \n")
        answer = input("\n").strip().lower()
        """removes spaces , transform to lowercase to not raise error""" 
        if not answer.isalpha() or answer not in ["yes", "no"]:
            
            print(f"Value Error : {answer} , please follow the instructions above or you will have to start over")
            break
            """
            if the wrong user input is wrong , print message and validates that
            the user input was in a str format and matching the expected awnser
            if not , the user would be notefied and can try agian
            
            """
        yes_or_no[i] = answer
get_week_days()
""" calling  the function for input and validation for what days the user have worked"""


work_week = Counter(yes_or_no.values())
"""checking the amount of yes values from the user input stored in the yes_or_no variabel"""

days_worked = work_week["yes"]
"""extrecting the nummber of "yes":es and storeing it in a variabel"""

print(f"You have worked for a total of {days_worked} this week! \n")
"telling the user on how many days of the week they have worked"

payment = work_week["yes"] * 200
"""multeplying the days worked with the dayly salary"""


print(f"You have earned a total of {payment}£  this week \n")
"""infroming the user on how much they have earned this week""" 
