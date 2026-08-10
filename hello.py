import datetime

import config

def say_hello(name):
    now = datetime.datetime.now()
    print(f"Goodbye, {name}from{comfig.APP_NAME}!")
    print(f"Today is{now.strftime('%Y-%m-%d')}.")

def say_hello(name):
    print(f"Hello,{name}!")

def greet_user():
    name = input("Please enter your name: ")
    say_hello(name)

if __name__ == "__main__" :
    greet_user()
    