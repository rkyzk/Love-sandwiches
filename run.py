import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Check if the input contains 6 integers, and store the data.
    """
    while True:
        print("Enter sales data (For example, '35,40,41,35,46,30')\n")
        data = input("Your input: ")
        list = data.split(',')
        print(f"You entered {list}")
        sales_data = validate_data(list)
        if validate_data(list):
            print("The data has been stored")
            break 
    return sales_data 

def validate_data(values):
    """
    Inside the try statement, converts the data to integers.
    Also checks if 6 values have been enetered. 
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 numeric values must be entered.  You provided {len(values)} value(s)."
            )
        values = [int(n) for n in values]
        return values
    except ValueError as e:
        print(f"Invalid entry: {e}.  Please try again")

def update_sales_worksheet(data):
    """
    Add new data to sales worksheet
    """ 
    print("Updating the sales worksheet...")
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('Sales worksheet has been updated successfully.\n')

def calculate_surplus_data():
    """
    Calculate surplus by sales - stock 
    """
    print("calculating surplus data")
    stock = SHEET.worksheet("stock").get_all_values()
    pprint(stock)
    stock_row = stock[-1]
    pprint(stock_row)

def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    print(data)
    update_sales_worksheet(data)
    calculate_surplus_data()

# print('Welcome to Love Sandwiches data automation')
# main()
calculate_surplus_data()