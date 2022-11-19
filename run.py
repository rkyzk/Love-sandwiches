import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input from the user 
    """
    print("Enter sales data (For example, '35, 40, 41, 35, 46, 30')")
    data = input("Your input: ")
    print(f"You enetered: {data}")
    validation = input("Enter 'v' to validate, or 'r' to re-enter: ")
    list = []
    if validation != 'v' and validation != 'r':
        print("Invalid entry.")
        continue
    if validation == 'r':
        continue

    list = data.split(', ')
    if not len(list) == 6:
        print("Enter 6 values.")    
        continue

    for num in list:
        if not num.isdigit():
            print("Enter only numbers.")        
            
    list = [int(n) for n in list]
    print("The data have been stored.")
    

    
        