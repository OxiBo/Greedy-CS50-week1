#a program that calculates the minimum number of coins required to give a user change

def main():
    import cs50

    print("O hai!", end="")
    #prompt user to provide a non-negative value for change
    while True:
        print("How much change is owed? ", end="")
        change = cs50.get_float()
        if change>0:
            break

    change = round(change,2)*100
    coins = 0

    if change >= 25:
        coins = (change - change%25)/25
        change = change%25
    if change >= 10:
        coins = coins + (change - change%10)/10
        change = change%10
    if change >= 5:
        coins = coins + (change-change%5)/5
        change = change%5
    if change >= 1:
        coins = coins + change - change%1

    print("{:.0f}".format(coins)) # {:.0f} specifier is used to print number of coins as an integer
    exit(0)

if __name__ == "__main__":
    main()