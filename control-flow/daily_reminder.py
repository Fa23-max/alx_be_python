task_description = input("Enter your task:")
priority = (input("Priority (high/medium/low):")).lower()
time_bound = (input("Is it time-bound? (yes/no):")).lower()

if(len(task_description) < 1):
  print("Input Task Description")
else:
  match priority:
    case "high":
      if time_bound == "yes":
        print(f"Reminder: {task_description} is a high priority task that requires immediate attention today!")
      elif time_bound == "no":
        print(f"Reminder: {task_description} is a high priority. Consider completing it when you have free time.")
      else:
        print("Input Time bound")
    case "medium":
      if time_bound == "yes":
        print(f"Reminder: {task_description} is a medium priority task that requires immediate attention today!")
      elif time_bound == "no":
        print(f"Reminder: {task_description} is a medium priority. Consider completing it when you have free time.")
      else:
        print("Input Time bound")
    case "low":
      if time_bound == "yes":
        print(f"Note: {task_description} is a low priority task. Consider completing it when you have free time.")
      elif time_bound == "no":
        print(f"Note: {task_description} is a low priority task. Consider completing it when you have free time.")
      else:
        print("Input Time bound")
    case _:
      print("Input Task Priority")