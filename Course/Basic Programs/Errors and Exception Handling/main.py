from ast import main


def greet(name):
    print(f'Good Morning: {name}')

if __name__ == "__main__":

    n = input('Enter your name: ')
    greet(n)