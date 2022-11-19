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

def validate_data(values):
    """
    Inside the try statement, converts the data to integers.
    Also checks if 6 values have been enetered. 
    """
    try:
        values = [int(n) for n in values]
    except ValueError as e:
        print(f"All values must be numeric.")
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 numeric values must be entered.  You provided {len(values)} value(s)."
            )
    except ValueError as e:
        print(f"Invalid entry: {e}.  Please try again")
        
def get_sales_data():
    """
    Get sales figures input from the user
    Check if the input contains 6 integers, and store the data.
    """
    
    print("Enter sales data (For example, '35,40,41,35,46,30')")
    data = input("Your input: ")
    list = data.split(',')
    print(f"You entered {list}")
    validate_data(list)

get_sales_data()

