def calculate_gross_pay(hours_worked, hourly_rate):
    standard_hours = 40
    overtime_rate = 1.5

    if hours_worked > standard_hours:
        regular_pay = standard_hours * hourly_rate
        overtime_hours = hours_worked - standard_hours
        overtime_pay = overtime_hours * (hourly_rate * overtime_rate)
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours_worked * hourly_rate

    return total_pay

def main():
    hours_worked = float(input("Enter the number of hours worked this week: "))
    hourly_rate = float(input("Enter your hourly rate: "))

    if hours_worked < 0 or hourly_rate < 0:
        print("Hours worked and hourly rate must be non-negative values.")
        return

    gross_pay = calculate_gross_pay(hours_worked, hourly_rate)
    print(f"Your gross pay for the week is: ${gross_pay:.2f}")


if __name__ == "__main__":
    main()