
from api import api_call

def main():
    print("WELCOME TO EXPLORE THE COUNTRIES AROUND THE WORLD!")
    print("Let me know where do you want to go , I will help you with selecting the right mode of transportation and the currency you need to have !")
    source=input("Where are you now?: ")
    destination=input("Where do you want to go?: ")
    result=api_call(source,destination)