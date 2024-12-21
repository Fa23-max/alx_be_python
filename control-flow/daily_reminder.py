task_description = input("Enter your task:")
priority = (input("Priority (high/medium/low):")).lower()
task_time_bound = (input("Is it time-bound? (yes/no):")).lower()

if(len(task_description) < 1):
  print("Input Task Description")
else:
  match priority:
    case "high":
      if task_time_bound.find("yes") != -1:
        print(f"Reminder: {task_description} is a high priority task that requires immediate attention today!")
      elif task_time_bound.find("no") != -1:
        print(f"Reminder: {task_description} is a high priority. Consider completing it when you have free time.")
      else:
        print("Input Time bound")
    case "medium":
      if task_time_bound.find("yes") != -1:
        print(f"Reminder: {task_description} is a medium priority task that requires immediate attention today!")
      elif task_time_bound.find("no") != -1:
        print(f"Reminder: {task_description} is a medium priority. Consider completing it when you have free time.")
      else:
        print("Input Time bound")
    case "low":
      if task_time_bound.find("yes") != -1:
        print(f"Note: {task_description} is a low priority task. Consider completing it when you have free time.")
      elif task_time_bound.find("no") != -1:
        print(f"Note: {task_description} is a low priority task. Consider completing it when you have free time.")
      else:
        print("Input Time bound")
    case _:
      print("Input Task Priority")