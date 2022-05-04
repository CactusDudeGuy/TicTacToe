import random

win = 0  # 0 = game ongoing, 1 = game won, 2 = game lost, 3 = game tied
score = 0
x = 10


def value_reset():
    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    tl = 0
    tm = 0
    tr = 0
    ml = 0
    mm = 0
    mr = 0
    bl = 0
    bm = 0
    br = 0


top_left = ['Top Left', 'Top left', 'top Left', 'top left', 'tl']
top_middle = ['Top Middle', 'Top middle', 'top Middle', 'top middle', 'tm']
top_right = ['Top Right', 'Top right', 'top Right', 'top right', 'tr']
middle_left = ['Middle Left', 'Middle left', 'middle Left', 'middle left', 'ml']
middle_middle = ['Middle Middle', 'Middle middle', 'middle Middle', 'middle middle', 'mm']
middle_right = ['Middle Right', 'Middle right', 'middle Right', 'middle right', 'mr']
bottom_left = ['Bottom Left', 'Bottom left', 'bottom Left', 'bottom left', 'bl']
bottom_middle = ['Bottom Middle', 'Bottom middle', 'bottom Middle', 'bottom middle', 'bm']
bottom_right = ['Bottom Right', 'Bottom right', 'bottom Right', 'bottom right', 'br']
opponent_choice_list = ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'bl', 'bm', 'br']
yes = ['Yes', 'yes', 'Y', 'y']
no = ['No', 'no', 'N', 'n']


# 0 = blank, 1 = x, 2 = triangle


def line_1(symbol):
    if symbol == 0:
        return '        |'
    elif symbol == 1:
        return '   \ /  |'
    elif symbol == 2:
        return '   /\   |'


def line_2(symbol):
    if symbol == 0:
        return '        |'
    elif symbol == 1:
        return '    x   |'
    elif symbol == 2:
        return '  /  \  |'


def line_3(symbol):
    if symbol == 0:
        return '________|'
    elif symbol == 1:
        return '___/_\__|'
    elif symbol == 2:
        return '_/____\_|'


def opponent_move_maker():
    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    global opponent_choice
    opponent_choice = random.choice(opponent_choice_list)
    if opponent_choice in top_left and tl == 0:
        tl = 2
        print_board()
    elif opponent_choice in top_middle and tm == 0:
        tm = 2
        print_board()
    elif opponent_choice in top_right and tr == 0:
        tr = 2
        print_board()
    elif opponent_choice in middle_left and ml == 0:
        ml = 2
        print_board()
    elif opponent_choice in middle_middle and mm == 0:
        mm = 2
        print_board()
    elif opponent_choice in middle_right and mr == 0:
        mr = 2
        print_board()
    elif opponent_choice in bottom_left and bl == 0:
        bl = 2
        print_board()
    elif opponent_choice in bottom_middle and bm == 0:
        bm = 2
        print_board()
    elif opponent_choice in bottom_right and br == 0:
        br = 2
        print_board()
    else:
        opponent_move_maker()
    win_checked = win_checker()
    if win_checked == 1 or win_checked == 2 or win_checked == 3:
        return


def move_maker():
    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    position = input('Where do you want to go: ')
    if position in top_left and tl == 0:
        tl = 1
        print_board()
        opponent_move_maker()
    elif position in top_middle and tm == 0:
        tm = 1
        print_board()
        opponent_move_maker()
    elif position in top_right and tr == 0:
        tr = 1
        print_board()
        opponent_move_maker()
    elif position in middle_left and ml == 0:
        ml = 1
        print_board()
        opponent_move_maker()
    elif position in middle_middle and mm == 0:
        mm = 1
        print_board()
        opponent_move_maker()
    elif position in middle_right and mr == 0:
        mr = 1
        print_board()
        opponent_move_maker()
    elif position in bottom_left and bl == 0:
        bl = 1
        print_board()
        opponent_move_maker()
    elif position in bottom_middle and bm == 0:
        bm = 1
        print_board()
        opponent_move_maker()

    elif position in bottom_right and br == 0:
        br = 1
        print_board()
        opponent_move_maker()

    else:
        print('Not valid answer, please check spelling and grammar.')
        move_maker()
    win_checked = win_checker()
    if win_checked == 1 or win_checked == 2 or win_checked == 3:
        return


def print_board():
    print(line_1(tl) + line_1(tm) + line_1(tr))
    print(line_2(tl) + line_2(tm) + line_2(tr))
    print(line_3(tl) + line_3(tm) + line_3(tr))
    print(line_1(ml) + line_1(mm) + line_1(mr))
    print(line_2(ml) + line_2(mm) + line_2(mr))
    print(line_3(ml) + line_3(mm) + line_3(mr))
    print(line_1(bl) + line_1(bm) + line_1(br))
    print(line_2(bl) + line_2(bm) + line_2(br))
    print(line_3(bl) + line_3(bm) + line_3(br))
    print('\n\n\n')


def win_checker():
    global win
    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    if tl == 1 and tm == 1 and tr == 1 or ml == 1 and mm == 1 and mr == 1 or bl == 1 and bm == 1 and br == 1 or tl == 1 and mm == 1 and br == 1 or tr == 1 and mm == 1 and bl == 1 or tl == 1 and ml == 1 and bl == 1 or tm == 1 and mm == 1 and bm or tr == 1 and mr == 1 and br == 1:  # This checks if player has won
        win = 1
        return win
    elif tl == 2 and tm == 2 and tr == 2 or ml == 2 and mm == 2 and mr == 2 or bl == 2 and bm == 2 and br == 2 or tl == 2 and mm == 2 and br == 2 or tr == 2 and mm == 2 and bl == 2 or tl == 2 and ml == 2 and bl == 2 or tm == 2 and mm == 2 and bm or tr == 2 and mr == 2 and br == 2:  # This checks if opponent has won
        win = 2
        return win
    elif tl != 0 and tm != 0 and tr != 0 and ml != 0 and mm != 0 and mr != 0 and bl != 0 and bm != 0 and br != 0:  # This checks if Board is full
        win = 3
        return win


value_reset()
while win == 0:
    move_maker()
    if win == 3:
        print('You tied \n')
        print(f'Your score is {score}')
        play_again = input('Do you want to play again? ')
        if play_again in no:
            print('Game Over')
            print(f'Your score was {score}')
            break
        elif play_again in yes:
            print('Continuing')
            win = 0
            value_reset()
    if win == 2:
        print('You lost \n')
        print(f'Your score is {score}')
        play_again = input('Do you want to play again? ')
        if play_again in no:
            print('Game Over')
            print(f'Your score was {score}')
            break
        elif play_again in yes:
            print('Continuing')
            print('Score resetting')
            win = 0
            score = 0
            value_reset()
    if win == 1:
        print('You won \n')
        score = score + 1
        print(f'your score is {score}')
        play_again = input('Do you want to play again? ')
        if play_again in no:
            print('Game Over')
            print(f'Your score was {score}')
            break
        elif play_again in yes:
            print('Continuing')
            win = 0
            value_reset()
