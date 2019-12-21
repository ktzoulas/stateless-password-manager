"""
Password evaluation and char check
"""
def evaluate_pass(password):
    """
    TODO pass evaluation
    """

    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
               'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    capitals = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A',
                'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    # symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}',
    # ':', '"', '|', '<', '>', '?', '[', ']', ';', "'", ',', '.', '/']
    # nsymbols = ['!', '@', '#', '$', '%','^', '&', '*', '(', ')']

    letters_quantity = 0
    capitals_quantity = 0
    numbers_quantity = 0
    symbols_quantity = 0

    for i in password:
        if letters.__contains__(i):
            letters_quantity += 1
        elif capitals.__contains__(i):
            capitals_quantity += 1
        elif numbers.__contains__(i):
            numbers_quantity += 1
        else:
            symbols_quantity += 1

    quantity = [letters_quantity, capitals_quantity, numbers_quantity, symbols_quantity]
    msgs = ['letter', 'Capital letter', 'number', 'symbol']

    msg = []
    valid = True
    for i in range(0, 4):
        if quantity[i] == 0:
            valid = False
            msg.append(('The password must contain at least one '+msgs[i]))

    if valid:
        msg = 'Good job'

    return msg


print(evaluate_pass(''))
