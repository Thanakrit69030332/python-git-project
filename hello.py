import config

def say_hello(name):
    print(f"Hello, {name}from{comfig.APP_NAME}!")

def say_hello(name):
    print(f"Hello,{name}!")

def greet_user():
    name = input("Please enter your name: ")
    say_hello(name)

if __name__ == "__main__" :
    greet_user()
    