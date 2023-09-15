import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET= 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')

        print()


def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number.')

    return amount

def get_number_of_lines():
    while True:
        lines = input('Enter number of lines to bet on (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines.')
        else:
            print('Please enter a number.')

    return lines

def get_bet():
    while True:
        amount = input('What would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Please enter a number.')

    return amount

def main():
    balance = deposit()

    while balance > 0:
        lines = get_number_of_lines()
        while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > balance:
                print(f'You do not have enough to bet that amount, your current balance is: ${balance}')
            else:
                break

        print(f'Your are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)

        # Check the outcome of each line
        winnings = 0
        for line in range(lines):
            symbols = [slots[i][line] for i in range(COLS)]
            # Customize the win logic based on your requirements
            # Here, I'm assuming you win if all symbols in a line are the same
            if all(symbol == symbols[0] for symbol in symbols):
                winnings += bet * symbol_count[symbols[0]]

        if winnings > 0:
            print(f'Congratulations! You won ${winnings}!')
            balance += winnings
        else:
            print('Sorry, you did not win anything.')

        # Update the balance
        balance -= total_bet
        print(f'Your new balance is: ${balance}')

    print('Game over. You have run out of money.')

main()

