import gspread

days = ("Monday" , "Tuseday", "Wensday", "Thursday", "Fryday")

yes_or_no = {}

def get_week_days():
    print("Welcome to the solo salary application ! \n")
    print("Enter either yes or no as an awnser... \n")

    for i in days:
        print(f"Did you work on {i} ? \n \n ")
        answer = input().strip().lower()
        if not answer.isalpha() or answer not in ["yes","no"]:
            print("pleas enter the corecct choice")
        yes_or_no[i] = answer
        
get_week_days()
print(yes_or_no)



