from datetime import datetime

def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def main():
    name = input("What is your name? ")
    greeting = get_greeting()
    print(f"{greeting}, {name}! Welcome!")

if __name__ == "__main__":
    main()