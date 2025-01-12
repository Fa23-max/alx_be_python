FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Factor to convert Celsius to Fahrenheit

def convert_to_CELSIUS(FAHRENHEIT):
  """Converts a temperature in Fahrenheit to Celsius and returns the result."""
  celsius = (FAHRENHEIT - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_FAHRENHEIT(CELSIUS):
  """Converts a temperature in Celsius to Fahrenheit and returns the result."""
  FAHRENHEIT = (CELSIUS * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return FAHRENHEIT

def main():
  """Prompts the user for temperature and unit, performs conversion, and displays the result."""
  while True:
    try:
      temperature = float(input("Enter temperature: "))
      unit = input("Enter unit (C or F): ").upper().strip()
      break
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

  if unit == 'C':
    converted_temperature = convert_to_FAHRENHEIT(temperature)
    print(f"{temperature}°C is equivalent to {converted_temperature:.2f}°F")
  elif unit == 'F':
    converted_temperature = convert_to_CELSIUS(temperature)
    print(f"{temperature}°F is equivalent to {converted_temperature:.2f}°C")
  else:
    print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
  main()