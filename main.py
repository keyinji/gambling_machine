MAX_LINES = 3

MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("What would you like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        amount_of_lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?"
        )
        if amount_of_lines.isdigit():
            amount_of_lines = int(amount_of_lines)
            if amount_of_lines > 0:
                break
            else:
                print("Enter a valide number of lines")
        else:
            print("Please enter a number.")
    return amount_of_lines


def get_bet():
    while True:
        amount = input("What would you like to bet: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.")
    return amount
    

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total = bet * lines

    print(f"You are betting ${bet} on {lines}. Total bet: ${total}")


main()
