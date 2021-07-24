import random
import time

money = 100
bet = 50


def roulette_wheel():
    roulette_number = random.randint(0, 36)
    colors = ["black", "red"]
    roulette_color = random.choice(colors)
    return [roulette_number, roulette_color]


def selection(cash):
    print("""\t1)Number\t2)Color\t3)Odd/Even\n\t4)Quarters\n\t\t\t\t8)Bet\t9)End""")
    print(f"Cash: {cash}")
    user_choice = input("> ")
    return int(user_choice)


def gamble_num(bet_amount, cash, number):
    user_bet = input("Number bet(s): ")
    all_bets = user_bet.split(' ')
    print(f"RN: {number}")
    for num in all_bets:
        if int(num) == number:
            print(f"WINNER {num}.")
            cash = cash + (int(bet_amount) * 36)
        elif int(num) > 36 or int(num) < 0:
            print(f"INVALID {num}")
        else:
            print(f"LOST {num}")
            cash = cash - bet_amount
    return cash


def gamble_color(bet_amount, cash, color):
    user_color = input("Color bet: ").lower()
    all_colors = user_color.split(' ')
    print(f"Landed on {color}!")
    for col in all_colors:
        if col == color:
            print("Success")
            cash += bet_amount
        else:
            print("failed")
            cash -= bet_amount
    return cash


def gamble_oe(bet_amount, cash, number):
    user_oe = input("Odd/Even bet: ").lower()
    all_oe = user_oe.split(' ')
    print(f"Landed on {number}!")
    if number % 2:
        even = False
        for oe in all_oe:
            if oe == "odd" and even is False:
                cash += bet_amount
            elif oe == "even" and even is False:
                cash -= bet_amount
    elif number / 2:
        even = True
        for oe in all_oe:
            if oe == "even" and even is True:
                cash += bet_amount
            elif oe == "odd" and even is True:
                cash -= bet_amount
    return cash


def gamble_quarters(bet_amount, cash, number):
    user_quarter = input("1: 1-12\n"
                         "2: 13-24\n"
                         "3: 25-36\n"
                         ">")
    all_quarters = user_quarter.split(' ')
    print(f"Landed on {number}!")
    for quarter in all_quarters:
        if number in range(0, 12) and int(quarter) == 1:
            print(f"{number} is in first quarter")
            cash = cash + (bet_amount * 3)
        elif number in range(13, 24) and int(quarter) == 2:
            print(f"{number} is in second quarter")
            cash = cash + (bet_amount * 3)
        elif number in range(25, 36) and int(quarter) == 3:
            print(f"{number} is in third quarter")
            cash = cash + (bet_amount * 3)
        elif int(quarter) > 3 or int(quarter) < 1:
            print("Invalid quarter selection")
        else:
            print("Wrong Quarter")
            cash -= bet_amount
    return cash


def gamble_bet():
    change_bet = input("New bet: ")
    return int(change_bet)


running = True

while running:
    wheel = roulette_wheel()
    menu_option = selection(money)
    # user selects option
    if menu_option == 1:
        money = gamble_num(bet, money, wheel[0])
        print(f"remaining money: {money}")

    elif menu_option == 2:
        money = gamble_color(bet, money, wheel[1])
        print(f"remaining money: {money}")

    elif menu_option == 3:
        money = gamble_oe(bet, money, wheel[0])

    elif menu_option == 4:
        money = gamble_quarters(bet, money, wheel[0])

    elif menu_option == 8:
        print(f"Old bet is {bet}")
        bet = gamble_bet()
        print(f"New bet is {bet}")

    elif menu_option == 9:
        print("Thanks for playing!")
        exit()

    if money <= 0:
        print("You ran out of money")
        running = False

exit()
