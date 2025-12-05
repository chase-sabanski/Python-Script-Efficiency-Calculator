import sys
import time as t
import itertools
import pyinputplus as pyip

def main():
    print(("#") * 35)
    print("UPLOAD SCRIPT EFFICIENCY CALCULATOR")
    print(("#") * 35)

    def spinner_animation(duration):
        spinner = itertools.cycle(['-', '\\', '|', '/']) # Sequence of characters for the spinner
        start_time = t.time()

        while t.time() - start_time < duration:
            sys.stdout.write('\r' + next(spinner)) # Write the next frame and carriage return
            sys.stdout.flush() # Flush the output buffer
            t.sleep(0.1) # Pause briefly
        
        # Clear the animation line and print a final message
        sys.stdout.write('\rComplete.   \n') # Add spaces to clear the line completely
        sys.stdout.flush()

    while True:

        # input validation loop that only accepts non-negative integers
        while True:
            try:
                ticket_count = input("Please enter the amount of tickets created using the python upload script: ")
                int_input = int(ticket_count)

                if int_input < 0:
                    print("Please enter a non-negative integer.\n")
                    continue
                elif int_input > 1000000000:
                    print("Nice try, but it's extremely unlikely that many tickets have been created. Please enter an integer smaller than 1,000,000,000.\n")
                    continue
                break

            except ValueError:
                print(f"'{ticket_count}' is invalid input. Please enter a whole number.")

        # Manual time to create tickets is calculated by:
        # ...multipling the input by 10 min (generous estimate of how long it takes to create a ticket) then,
        # ...dividing the input by 60 to get total hours then,
        # ...dividing the input by 8 to get total workdays then,
        # ...rounding up at each calculation to avoid large decimals from being printed
        minutes = round(int_input * 10)
        hours = round(minutes / 60)
        days = round(hours / 8)
        work_weeks = round(days / 5)
        years = round(days / 260) # this represents a work year, not a whole calendar year
        analysts = 5 # edit this variable depending on the current size of the team
        team_effort = round(days / analysts)

        print(f"\nCalculating for {int_input:,d} tickets...")
        spinner_animation(3)

        print(f"""
        Amount of labor saved in...
         > Minute(s): {minutes:,d}
         > Hour(s): {hours:,d}
         > Day(s): {days:,d}
         > Work week(s): {work_weeks:,d}
         > Year(s): {years:,d}
        """)

        print(f"\nCalculating amount of labor for a team of {analysts} analysts...")
        spinner_animation(3)

        # stylistic choice so that each new line starts with a number
        print(f"""
        It would take a team of
        {analysts} experienced analysts approximately
        {team_effort:,d} days to create
        {int_input:,d} tickets manually if that's all they did everyday for
        8 hours a day.
        """)

        # prompt that allows the user to break the while loop if they type "n" in the terminal
        prompt = "Run again? (Y/N): "
        response = pyip.inputYesNo(prompt, yesVal="y", noVal="n")
        if response == "n":
            print("\nExiting...\n",)
            break
        else:
            print()

if __name__=="__main__":
    main()
