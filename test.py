def init_board():
    """Draw the board and show game info"""
    width = 11
    height = 11

    print("\nGame board. Type 'row,column' to select move. For example, '0,0' selects top left move.\n\n", end="  ")
    for x in range(width):
        print("{0:6d}".format(x), end='')
    print('\r\n')
    for i in range(height):
        print("{0:3d}  ".format(i), end='')
        for j in range(width):
            print('_'.center(6), end='')
        print('\n')
        
init_board()