import math
import pyinputplus as pyip

def main():
    print(("#") * 35)
    print("PYTHON SCRIPT EFFICIENCY CALCULATOR")
    print(("#") * 35)

    while True:

        # input validation loop that only accepts non-negative integers
        while True:
            try:
                ticket_count = input("How many tickets have been created via CSV: ")
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
        # ...rounding up
        manual_time_workdays = math.ceil((((int_input * 10) / 60) / 8))

        print(f"""
        Time saved:
        Minute(s): {(int_input * 10)}
        Hour(s): {(int_input * 10) / 60}
        Day(s): {manual_time_workdays}
        Work week(s): {(manual_time_workdays / 5)}
        Year(s): {((((int_input * 10) / 60) / 8) / 260)}
        """)

        print(f"""
        It would take a team of 5 experienced analysts approximately {round(((manual_time_workdays / 5) / 5))} weeks 
        to create {int_input} tickets manually if that's all they did everyday for 8 hours a day.
        """)

        # loop that allows the user to keep running the program until they type "n" in the terminal
        prompt = "Run again? (Y/N):\n"
        response = pyip.inputYesNo(prompt, yesVal="y", noVal="n")
        if response == "n":
            print("Exiting...")
            break

if __name__=="__main__":
    main()
