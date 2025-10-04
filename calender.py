# # Ask user for day number and print day name
# def print_day_of_week():
#     day_num = int(input("Enter day number (1-7): "))
#     days = {
#         1: "Monday",
#         2: "Tuesday",
#         3: "Wednesday",
#         4: "Thursday",
#         5: "Friday",
#         6: "Saturday",
#         7: "Sunday"
#     }
#     print(days.get(day_num, "Invalid day number"))
# # 
# print_day_of_week()
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
            return False
        case _:
            return "Invalid day"
print(is_weekend("Saturday"))