def print_menue():
    """
    Prints the menue to the user
    :return: None
    """
    print()  # Newline
    print('==============================================')
    print('Was möchten Sie mit dieser Applikation machen?')
    print('Wählen Sie \'f\' für Fibonacci-Reihe ausgeben')
    print('Wählen Sie \'e\' für Kleines Einmaleins')
    print('Wählen Sie \'g\' für Berechnung Gerade / Ungerade')
    print('Wählen Sie \'x\' um das Programm zu beenden!')


def fibonacci():
    """
    Prints the value from the Fibonacci series at position x.
    :return: None
    """
    print('Which position of the Fibonacci-List do you want to know?')
    position = int(input(''))
    number1 = 0
    number2 = 1
    counter = 3
    while counter <= position:
        next_number = number1 + number2
        number1 = number2
        number2 = next_number
        counter += 1

    print(number2)


def multiplication_table():
    """
    Prints the multiplication table for the number x.
    :return:
    """
    print('Which number do you want to learn?')
    number = int(input(''))
    for counter in range(0, 11):
        print(number * counter)


def even_or_odd():
    """
    Prints if the value is even or odd
    :return:
    """
    print('Enter a number to check for odd/even?')
    number = int(input('Give a number:\n'))
    if number % 2 == 0:
        print(f'Number {number} is even.')
    else:
        print(f'Number {number} is odd.')


def talk_to_user():
    """
    Talks to the user to determine what he wants.

    :return: None
    """

    print('Lieber Benutzer, herzlich willkommen zu diesem Programm')

    # Show Menue
    print_menue()
    selection = input('>> ')

    while selection != 'x':
        if selection == 'f':  # Fibonacci
            fibonacci()
        elif selection == 'e':  # Kleines Einmaleins
            multiplication_table()
        elif selection == 'g':  # Odd or Even
            even_or_odd()
        else:  # Wrong input
            print('Befehl nicht verstanden, bitte erneut eingeben.')

        print_menue()
        selection = input('>> ')


if __name__ == '__main__':
    talk_to_user()