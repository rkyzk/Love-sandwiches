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

def calculate_surplus_data(sales_data):
    """
    Calculate surplus by stock - sales 
    """
    print("calculating surplus data")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = [int(n) for n in stock[-1]]

    surplus_data = []
    for stock, sales in zip(stock_row, sales_data):
        surplus_data.append(stock - sales)
        
    return surplus_data

def update_worksheet(data, worksheet):
    """
    Update a worksheet
    """
    print(f"Updating {worksheet} data worksheet.\n")
    wsheet_to_update = SHEET.worksheet(worksheet)
    wsheet_to_update.append_row(data)
    print(f"{worksheet} worksheet has been updated.\n")

def get_last_5_entries_sales():
    """
    Collects columns of data from the last 5 entris for each
    sandwich in sale as a list of lists.
    """
    sales = SHEET.worksheet("sales")
    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns

def calculate_stock_data(data):
    """
    Calculate the average qty sold in the last 5 days and add 10%
    """
    print("Calculating stock recommendation...")
    new_stock_data = []
    for column in data:
        int_column = [int(num) for num in column]
        stock = round(sum(int_column) / len(int_column) * 1.1)
        new_stock_data.append(stock)

    return new_stock_data

def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    update_worksheet(data, "sales")
    surplus_data = calculate_surplus_data(data)
    update_worksheet(surplus_data, "surplus")
    quantity_sold = get_last_5_entries_sales()
    stock_data = calculate_stock_data(quantity_sold)
    update_worksheet(stock_data, "stock")

print('Welcome to Love Sandwiches data automation')
main()


