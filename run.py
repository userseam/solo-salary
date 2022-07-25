import gspread

print("Welcome to the solo salary application \n")

def week_days():
    """ 
    This will be used to loop throw all the 5 days of the week and add them to a list
    """
    
    
    days = ["Monday" , "Tuseday" , "Wensday", "Thursday" , "Fryday"]
    for i in days:
        input(f"Did you work on  {i} ? \n")
    
    
       

week_days()