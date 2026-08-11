
from process import process_data

"""Method to make sure the user inputs a non empty string for source and destination"""
def get_nonempty_input(prompt):
    """Keep asking until the user types something other than blank/whitespace."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This can't be empty. Please enter a value.")

""" Main function - displays text to be on the initial terminal screen 
    Getting the source and the destination places from the user 
    Passing the inputs to 'process_data' function """
def main():    
        print("WELCOME TO EXPLORE THE PLACES AROUND THE WORLD!")
        print("Let me know your source and destination.")
        print("I will help you with:")
        print("1. distance between the source and the destination")
        print("2. efficient mode of transportation")
        print("3. currency you may need")
        print("4. language(s) you should know")
        print("5. calling code(s) of the destination")
        print("----------------------------------------------------")
        while True:
            print("Do you want to " )
            print("1. Enter the source and the destination?")
            print("2. Exit?")
            choice=input("Enter your choice 1 or 2: ")
            if choice=="1":
                source=get_nonempty_input("Source: ")
                destination=get_nonempty_input("Destination: ")
                process_data(source,destination)
            elif choice =="2": 
                print("Goodbye!")
                break
            else:
                print("ENTER EITHER 1 OR 2 PLEASE ...")
if __name__ == "__main__":
 try:
    main()
 except KeyboardInterrupt:
    print("\nGoodbye! (interrupted)")