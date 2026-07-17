
from process import process_data
from display import display_result
# Main function - displays text to be on the initial terminal screen 
# Getting the source and the destination places from the user 
# Passing the inputs to 'api_call' function
def main():
    while True:
        print("WELCOME TO EXPLORE THE PLACES AROUND THE WORLD!")
        print("Let me know your source and destination.")
        print("I will help you with the,")
        print("1. distance between the places")
        print("2. the mode of transporatation")
        print("3. currency you may need")
        print("4. language(s) you should know")
        print("5. calling code(s) of the destination")
        print("6. timezone of the place")
        print("----------------------------------------------------")
        source=input("Source: ")
        destination=input("Destination: ")
        process_data(source,destination)
        
if __name__ == "__main__":
    main()