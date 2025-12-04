import pyinputplus as pyip

def main():
    print(("#") * 35)
    print("PYTHON SCRIPT EFFICIENCY CALCULATOR")
    print(("#") * 35)

    while True:

        # input validation loop that only accepts non-negative integers
        while True:
            try:
                ticket_count = input("Please enter the amount of tickets created using the python upload script: ")
                int_input = int(ticket_count)

                if int_input < 0:
                    print("Please enter a non-negative integer.")
                    continue
                break

            except ValueError:
                print(f"'{ticket_count}' is invalid input. Please enter a whole number.")

        # Manual time to create tickets is calculated by:
        # ...multipling the input by 10 min (generous estimate of how long it takes to create a ticket) then,
        # ...dividing the input by 60 to get total hours then,
        # ...dividing the input by 8 to get total workdays then,
        # ...rounding up at each calculation
        minutes = round(int_input * 10)
        hours = round(minutes / 60)
        days = round(hours / 8)
        work_weeks = round(days / 5)
        years = round(days / 260) # this represents a work year, not a whole calendar year
        team_effort = round(days / 5)

        print(f"""
        Time saved:
        Minute(s): {minutes}
        Hour(s): {hours}
        Day(s): {days}
        Work week(s): {work_weeks}
        Year(s): {years}
        """)

        # stylistic choice so that each new line starts with a number
        print(f"""
        It would take a team of
        5 experienced analysts approximately
        {team_effort} days to create
        {ticket_count} tickets manually if that's all they did everyday for
        8 hours a day.
        """)

        # loop that allows the user to keep running the program until they type "n" in the terminal
        prompt = "Run again? (Y/N):\n"
        response = pyip.inputYesNo(prompt, yesVal="y", noVal="n")
        if response == "n":
            print("Exiting...")
            break

if __name__=="__main__":
    main()
