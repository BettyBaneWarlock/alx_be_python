from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted date and time
    print("Current date and time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Get the current date
    current_date = datetime.now()
    # Prompt the user to enter a number of days to add
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=number_of_days)
    # Format the future date as YYYY-MM-DD
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the future date
    print("Future date:", formatted_future_date)

# Main function to run the script
if __name__ == "__main__":
    # Display the current date and time
    display_current_datetime()
    # Calculate and display the future date
    calculate_future_date()
