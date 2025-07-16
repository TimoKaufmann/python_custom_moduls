from greetings import say_hello
from math_utils import add

if __name__ == "__main__":
    print("Willkommen zu deiner eigenen Modul-Anwendung!")

    print(say_hello("Timo"))

    result = add(5, 7)
    print(f"5 + 7 = {result}")
