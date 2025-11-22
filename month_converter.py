"""A simple month converter program.
Converts short month names (e.g., "jan") into full month names ("January")."""

# Dictionary that stores short month names and their full names
months = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}

def convert_month(short_name):
    short_name = short_name.lower()
     # Return full month name or error message if invalid
    return months.get(short_name, "Invalid abbreviation!")

# Main Program
user_input = input("Enter short month name (e.g, Jan): ")

print("Full month name is: ", convert_month(user_input))