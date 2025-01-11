from datetime import datetime, timedelta

def display_current_datetime():
  """
  Gets the current date and time and prints it in a readable format.
  """
  current_date = datetime.now()
  print(f"Current Date and Time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
  """
  Prompts the user for days to add, calculates the future date, and prints it.
  """
  while True:
    try:
      number_of_days = int(input("Enter the number of days to add: "))
      break
    except ValueError:
      print("Please enter a valid integer number of days.")

  future_date = datetime.now() + timedelta(days=number_of_days)
  print(f"Future Date (after {number_of_days} days): {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
  display_current_datetime()
  calculate_future_date()