
from process import process_data
from display import display_result
# Main function - displays text to be on the initial terminal screen 
# Getting the source and the destination places from the user 
# Passing the inputs to 'api_call' function
def main():
    print("WELCOME TO EXPLORE THE COUNTRIES AROUND THE WORLD!")
    print("Let me know where you want to go , I will help you with selecting the right mode of transportation and the currency you need to have !")
    source=input("Where are you now?: ")
    destination=input("Where do you want to go?: ")
    result=process_data(source,destination)
    display_result(result)

if __name__ == "__main__":
    main()